"""Операционная панель ARTMELLIO — тонкий слой над n8n.

Что делает:
  * показывает сценарии из registry.json и их состояние (включён / последний
    запуск / результат) — состояние читается напрямую из базы n8n (SQLite,
    только чтение);
  * запускает сценарий кнопкой — дёргает вебхук n8n `panel/<...>`;
  * ведёт журнал действий сотрудника в journal.jsonl (кто, что, когда, чем
    кончилось).

Только стандартная библиотека Python: ничего ставить не нужно.

    python panel/server.py            # http://localhost:8787

Из n8n в панель стучаться по 127.0.0.1, не по localhost: n8n резолвит
localhost в IPv6, а сервер слушает только IPv4.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import sys
import threading
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from reports import list_reports, safe_name, write_report  # noqa: E402
REGISTRY = HERE / "registry.json"
INDEX = HERE / "index.html"
JOURNAL = HERE / "journal.jsonl"
NOTIFICATIONS = HERE / "notifications.jsonl"   # сюда n8n шлёт события (новый заказ и т.п.)

N8N_URL = os.environ.get("N8N_URL", "http://localhost:5678").rstrip("/")
N8N_DB = Path(os.environ.get("N8N_DB", Path.home() / ".n8n" / "database.sqlite"))
PORT = int(os.environ.get("PANEL_PORT", "8787"))
OPERATOR = os.environ.get("PANEL_OPERATOR", os.environ.get("USERNAME", "оператор"))
RUN_TIMEOUT = 1500  # секунд ждём ответа воркфлоу (проверка поставщиков через Dsers идёт 10–15 минут)

REPO = HERE.parent
WISHLIST_FILE = REPO / "data" / "wishlist-ids.json"
REPORTS = REPO / "data" / "reports"          # сюда n8n складывает отчёты через POST /api/report
WISHLIST_SCRIPT = REPO / "scripts" / "content-prep" / "wishlist_to_collection.py"
# Откуда разрешаем звать панель из браузера (закладка «Коллекция» на витрине).
STORE_ORIGINS = {"https://www.artmellio.com", "https://artmellio.com", "https://kmfmxn-r4.myshopify.com"}
# Вкладка Comfy Cloud один раз присылает ключи для работы без браузера (см. scripts/comfy/comfy_cloud.py).
COMFY_ORIGIN = "https://cloud.comfy.org"
COMFY_CREDS = Path(r"C:\Users\User\Desktop\Новая папка (4)\comfy cloud.txt")

_journal_lock = threading.Lock()


# ---------------------------------------------------------------- реестр ---

def load_registry() -> list[dict]:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return data["scenarios"]


# ------------------------------------------------------------- база n8n ---

def db() -> sqlite3.Connection | None:
    if not N8N_DB.exists():
        return None
    con = sqlite3.connect(f"file:{N8N_DB}?mode=ro", uri=True, timeout=5)
    con.row_factory = sqlite3.Row
    return con


def workflow_state(con: sqlite3.Connection | None, wf_id: str) -> dict:
    """Включён ли воркфлоу, последний запуск, счётчики."""
    out = {"known": False, "active": False, "last": None, "runs_total": 0, "errors_7d": 0}
    if con is None:
        return out
    row = con.execute("select active from workflow_entity where id = ?", (wf_id,)).fetchone()
    if row is None:
        return out
    out["known"] = True
    out["active"] = bool(row["active"])
    last = con.execute(
        "select id, status, mode, startedAt, stoppedAt from execution_entity "
        "where workflowId = ? and deletedAt is null order by id desc limit 1",
        (wf_id,),
    ).fetchone()
    if last:
        out["last"] = dict(last)
    out["runs_total"] = con.execute(
        "select count(*) from execution_entity where workflowId = ? and deletedAt is null", (wf_id,)
    ).fetchone()[0]
    week_ago = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    out["errors_7d"] = con.execute(
        "select count(*) from execution_entity where workflowId = ? and deletedAt is null "
        "and status in ('error','crashed') and startedAt >= ?",
        (wf_id, week_ago),
    ).fetchone()[0]
    return out


def executions(con: sqlite3.Connection | None, wf_id: str, limit: int = 20) -> list[dict]:
    if con is None:
        return []
    rows = con.execute(
        "select id, status, mode, startedAt, stoppedAt from execution_entity "
        "where workflowId = ? and deletedAt is null order by id desc limit ?",
        (wf_id, limit),
    ).fetchall()
    return [dict(r) for r in rows]


# ----------------------------------------------------------------- n8n ---

def n8n_alive() -> bool:
    try:
        with urllib.request.urlopen(f"{N8N_URL}/healthz", timeout=3) as r:
            return r.status == 200
    except Exception:
        return False


def run_webhook(path: str, payload: dict) -> tuple[bool, object]:
    """POST на продакшн-вебхук n8n. Возвращает (успех, ответ-или-текст ошибки)."""
    req = urllib.request.Request(
        f"{N8N_URL}/webhook/{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=RUN_TIMEOUT) as r:
            body = r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        text = e.read().decode("utf-8", "replace")
        if e.code == 404:
            return False, ("Сценарий выключен в n8n или у него нет кнопки запуска. "
                           "Включите воркфлоу в n8n и попробуйте снова.")
        return False, f"n8n ответил ошибкой {e.code}: {text[:500]}"
    except urllib.error.URLError as e:
        return False, f"Не удалось достучаться до n8n: {e.reason}. Запущен ли он? (.\\n8n\\start-n8n.ps1)"
    except TimeoutError:
        return False, f"Сценарий не ответил за {RUN_TIMEOUT} с. Проверьте историю запусков в n8n."
    try:
        return True, json.loads(body)
    except ValueError:
        return True, body


# -------------------------------------------------------------- журнал ---

def journal_append(entry: dict) -> None:
    entry = {"ts": datetime.now().isoformat(timespec="seconds"), **entry}
    with _journal_lock:
        with JOURNAL.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _tail(path: Path, limit: int) -> list[dict]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for line in lines[-limit:]:
        try:
            out.append(json.loads(line))
        except ValueError:
            continue
    return list(reversed(out))


def journal_tail(limit: int = 50) -> list[dict]:
    return _tail(JOURNAL, limit)


def notify_append(entry: dict) -> None:
    entry = {"ts": datetime.now().isoformat(timespec="seconds"), **entry}
    with _journal_lock:
        with NOTIFICATIONS.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def notifications_tail(limit: int = 20) -> list[dict]:
    return _tail(NOTIFICATIONS, limit)


# ------------------------------------------------------------- сборка ---

def state() -> dict:
    con = db()
    try:
        scenarios = []
        for s in load_registry():
            st = workflow_state(con, s["workflow_id"])
            public = {k: v for k, v in s.items() if k not in ("workflow_id", "run")}
            public["can_run"] = bool(s.get("run"))
            public.update(st)
            scenarios.append(public)
    finally:
        if con is not None:
            con.close()
    alive = n8n_alive()
    return {
        "n8n": {"alive": alive, "url": N8N_URL, "db_found": N8N_DB.exists()},
        "operator": OPERATOR,
        "now": datetime.now().isoformat(timespec="seconds"),
        "scenarios": scenarios,
        "journal": journal_tail(),
        "notifications": notifications_tail(),
        "reports": list_reports(REPORTS),
    }


# ------------------------------------------------------------- сервер ---

class Handler(BaseHTTPRequestHandler):
    server_version = "ArtmellioPanel/0.1"

    def log_message(self, fmt, *args):  # тише в консоли
        if "/api/" in (args[0] if args else ""):
            return
        super().log_message(fmt, *args)

    def _cors(self) -> None:
        origin = self.headers.get("Origin", "")
        if origin in STORE_ORIGINS or (origin == COMFY_ORIGIN and self.path == "/api/comfy-token"):
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            # Chrome: с https-страницы на localhost нужен явный ответ про частную сеть
            self.send_header("Access-Control-Allow-Private-Network", "true")

    def _json(self, code: int, obj: object) -> None:
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        path, _, query = self.path.partition("?")
        if path == "/" or path == "/index.html":
            body = INDEX.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path == "/api/state":
            return self._json(200, state())
        if path == "/api/reports":
            return self._json(200, {"reports": list_reports(REPORTS)})
        if path.startswith("/reports/"):
            name = path[len("/reports/"):]
            target = (REPORTS / name).resolve()
            if not name or "/" in name or "\\" in name or not target.is_file() or target.parent != REPORTS.resolve():
                return self._json(404, {"error": "нет такого отчёта"})
            ctype = ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                     if target.suffix == ".xlsx" else "text/csv; charset=utf-8")
            body = target.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Disposition", f'attachment; filename="{target.name}"')
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path == "/api/executions":
            params = dict(p.split("=", 1) for p in query.split("&") if "=" in p)
            sid = params.get("scenario", "")
            s = next((x for x in load_registry() if x["id"] == sid), None)
            if s is None:
                return self._json(404, {"error": "Нет такого сценария"})
            con = db()
            try:
                return self._json(200, {"executions": executions(con, s["workflow_id"])})
            finally:
                if con is not None:
                    con.close()
        self._json(404, {"error": "not found"})

    def _read_body(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        try:
            data = json.loads(raw.decode("utf-8", "replace")) if raw else {}
        except ValueError:
            return {}
        return data if isinstance(data, dict) else {"text": str(data)}

    def do_POST(self):
        if self.path == "/api/notify":
            # Сюда стучится n8n (и только он — сервер слушает 127.0.0.1).
            data = self._read_body()
            title = str(data.get("title") or "Событие").strip()[:200]
            text = str(data.get("text") or "").strip()[:1000]
            kind = str(data.get("kind") or "info")[:30]
            notify_append({"kind": kind, "title": title, "text": text})
            return self._json(200, {"ok": True})
        if self.path == "/api/comfy-token":
            # Со вкладки cloud.comfy.org: {"api_key": "...", "refresh_token": "..."} -> файл вне репозитория.
            data = self._read_body()
            key, rt = str(data.get("api_key") or "").strip(), str(data.get("refresh_token") or "").strip()
            if len(key) < 20 or len(rt) < 20:
                return self._json(400, {"ok": False, "error": "нужны api_key и refresh_token"})
            COMFY_CREDS.write_text(f"{key}\n{rt}\n", encoding="utf-8")
            journal_append({"who": OPERATOR, "scenario": "comfy-token", "action": "save", "ok": True,
                            "result": "ключи Comfy Cloud сохранены"})
            return self._json(200, {"ok": True, "saved": str(COMFY_CREDS)})
        if self.path == "/api/report":
            # n8n присылает готовые строки отчёта -> CSV и Excel в data/reports.
            # Тело: {"name": "catalog-gaps", "rows": [{...}, ...], "columns": [...]?, "title": "..."}
            data = self._read_body()
            rows = data.get("rows")
            if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
                return self._json(400, {"ok": False, "error": "rows должен быть списком объектов"})
            name = safe_name(data.get("name") or "report")
            columns = data.get("columns") if isinstance(data.get("columns"), list) else None
            info = write_report(REPORTS, name, rows, columns)
            base = f"http://localhost:{PORT}/reports/"
            notify_append({"kind": "report", "title": str(data.get("title") or f"Отчёт {name}"),
                           "text": f"{info['rows']} строк · {info['xlsx']}"})
            return self._json(200, {"ok": True, "rows": info["rows"], "file": info["xlsx"],
                                    "xlsx_url": base + info["xlsx"], "csv_url": base + info["csv"],
                                    "folder": str(REPORTS)})
        if self.path == "/api/wishlist-collection":
            # Закладка на витрине шлёт список избранного -> собираем коллекцию
            # тем же скриптом, что и руками: scripts/content-prep/wishlist_to_collection.py
            data = self._read_body()
            handles = [str(h).strip() for h in (data.get("handles") or []) if str(h).strip()]
            if not handles:
                return self._json(400, {"ok": False, "error": "Избранное пустое — нечего собирать."})
            WISHLIST_FILE.write_text(json.dumps(handles, ensure_ascii=False, indent=0), encoding="utf-8")
            try:
                proc = subprocess.run(
                    [sys.executable, str(WISHLIST_SCRIPT), str(WISHLIST_FILE)],
                    cwd=str(REPO), capture_output=True, text=True, encoding="utf-8", errors="replace",
                    timeout=300,
                )
                out = (proc.stdout or "") + (proc.stderr or "")
            except subprocess.TimeoutExpired:
                out = "скрипт не уложился в 5 минут"
                proc = None
            m = re.search(r"итог: (/collections/[^\s]+) — (\d+) товаров", out)
            ok = bool(m) and proc is not None and proc.returncode == 0
            entry = {"who": OPERATOR, "scenario": "wishlist-collection", "action": "run", "ok": ok,
                     "result": (m.group(0) if m else out[-500:])}
            journal_append(entry)
            if ok:
                notify_append({"kind": "collection", "title": f"Коллекция собрана: {m.group(1)}",
                               "text": f"{m.group(2)} товаров, из избранного ({len(handles)} шт.)"})
                return self._json(200, {"ok": True, "url": "https://www.artmellio.com" + m.group(1),
                                        "count": int(m.group(2)), "output": out})
            return self._json(502, {"ok": False, "error": "Скрипт не собрал коллекцию. Вывод:\n" + out[-1500:]})
        if not self.path.startswith("/api/run/"):
            return self._json(404, {"error": "not found"})
        sid = self.path[len("/api/run/"):]
        s = next((x for x in load_registry() if x["id"] == sid), None)
        if s is None:
            return self._json(404, {"error": "Нет такого сценария"})
        if not s.get("run"):
            return self._json(400, {"error": "Этот сценарий запускается только по событию, кнопки у него нет."})
        if not n8n_alive():
            msg = "n8n не запущен. Запустите .\\n8n\\start-n8n.ps1 и обновите страницу."
            journal_append({"who": OPERATOR, "scenario": sid, "action": "run", "ok": False, "result": msg})
            return self._json(503, {"error": msg})

        ok, result = run_webhook(s["run"]["path"], {"source": "panel", "operator": OPERATOR})
        journal_append({
            "who": OPERATOR, "scenario": sid, "action": "run", "ok": ok,
            "result": result if ok else str(result),
        })
        if ok:
            return self._json(200, {"ok": True, "result": result})
        return self._json(502, {"ok": False, "error": str(result)})


def main() -> None:
    if not REGISTRY.exists():
        sys.exit(f"нет реестра сценариев: {REGISTRY}")
    print(f"панель: http://localhost:{PORT}   n8n: {N8N_URL}   база n8n: {N8N_DB}")
    if not N8N_DB.exists():
        print("ВНИМАНИЕ: база n8n не найдена — статусы будут пустыми")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
