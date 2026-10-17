# Табло задач агентов (её просьба 13.10.2026: «нигде не вижу, на какой стадии обработка»).
# Каждая задача — файл ~/.claude/agent_status/<id>.json; statusline.py показывает их второй строкой.
# Прогресс считается сам по числу готовых файлов (glob), либо задаётся вручную (--done).
#
#   python agent_status.py set knigi13-hermes --title "Книги 13.10" --who Hermes --stage "пересказ" \
#          --total 136 --glob "C:\Users\User\knigi_kupleno\txt13\pereskaz\*.md"
#   python agent_status.py set knigi13-claude --who Claude --stage "ждёт Hermes"      # обновить только стадию
#   python agent_status.py done knigi13-hermes        # готово (строка «✅» висит ещё 30 мин)
#   python agent_status.py rm knigi13-hermes | list
#   python agent_status.py log knigi13-claude        # журнал шагов: когда какая стадия и сколько заняла
# Журнал (поле "log", последние 50 смен стадии) — приём «Traces» из Langflow (Хабр, 14.10.2026):
# видно, на каком шаге задача застряла и какой шаг самый долгий; пульт получает его в `json`.
import argparse
import glob as globmod
import json
import os
import sys
import time
from pathlib import Path

DIR = Path.home() / ".claude" / "agent_status"
KEEP_DONE = 30 * 60   # сколько показывать завершённую задачу
STALE = 20 * 60       # нет новых файлов дольше — «⚠ стоит?»


def load():
    out = []
    for f in sorted(DIR.glob("*.json")):
        try:
            out.append(json.loads(f.read_text("utf-8")))
        except Exception:
            pass
    return out


def progress(t):
    """(готово, всего, время последнего готового файла)"""
    if t.get("glob"):
        files = globmod.glob(t["glob"])
        last = max((Path(f).stat().st_mtime for f in files), default=None)
        return len(files), t.get("total"), last
    return t.get("done"), t.get("total"), t.get("updated")


def fmt_min(sec):
    m = int(sec // 60)
    return f"{m // 60} ч {m % 60} мин" if m >= 60 else f"{max(m, 1)} мин"


def line(t):
    now = time.time()
    if t.get("finished"):
        if now - t["finished"] > KEEP_DONE:
            return None
        return f"✅ {t.get('title', '')} · {t.get('who', '')}: {t.get('stage', 'готово')}"
    done, total, last = progress(t)
    s = f"⚙ {t.get('title', '')} · {t.get('who', '')}: {t.get('stage', '')}"
    if total:
        done = done or 0
        s += f" {done} из {total} ({round(100 * done / total)}%)"
        base = t.get("base", 0)
        el = now - t.get("started", now)
        if done > base and el > 60 and done < total:
            s += f" · ещё ~{fmt_min(el / (done - base) * (total - done))}"
    elif done:
        s += f" {done}"
    if last and now - last > STALE and not (total and done >= total):
        s += f" · ⚠ без новых {fmt_min(now - last)}"
    return s


def trace(t):
    """Журнал шагов: время начала, стадия, сколько длилась (последняя — до сих пор или до «готово»)."""
    log = t.get("log") or []
    if not log:
        return "журнала нет (задача заведена до 14.10 или стадия не менялась)"
    out = [f"{t.get('title', t.get('id', ''))} · {t.get('who', '')}"]
    for i, e in enumerate(log):
        end = log[i + 1]["t"] if i + 1 < len(log) else (t.get("finished") or time.time())
        mark = "✅" if t.get("finished") and i == len(log) - 1 else "·"
        dur = "" if mark == "✅" else f" — {fmt_min(end - e['t'])}"
        n = f" [{e['done']}]" if e.get("done") is not None else ""
        out.append(f"{time.strftime('%H:%M', time.localtime(e['t']))} {mark} {e['stage']}{n}{dur}")
    return "\n".join(out)


def lines():
    return [l for l in (line(t) for t in load()) if l]


def env_user(name):
    """Переменная Windows (User) — у вкладок пульта её может не быть в окружении."""
    if os.environ.get(name):
        return os.environ[name]
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            return winreg.QueryValueEx(k, name)[0]
    except OSError:
        return None


def remind(t):
    """Её слово 16.10: задача готова — всегда напоминание ей в личку бота «Дела», в группу — никогда.
    Шлёт не сам: ставит в очередь pult/gotovo_tg.py — тот копит 90 с, шлёт пачкой и без повторов."""
    import subprocess
    cmd = [sys.executable, "C:/Users/User/pult/gotovo_tg.py", "add", "--key", f"st:{t.get('id')}",
           "--task", t.get("title") or t.get("id", ""), "--stage", t.get("stage", "")]
    if t.get("session"):
        cmd += ["--session", t["session"]]
    if t.get("files"):
        cmd += ["--file", t["files"][-1]]
    try:
        subprocess.run(cmd, timeout=20, capture_output=True)
    except Exception as e:
        print(f"напоминание в личку не встало в очередь: {type(e).__name__}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["set", "done", "rm", "list", "json", "log"])
    ap.add_argument("id", nargs="?")
    for k in ("title", "who", "stage", "glob"):
        ap.add_argument(f"--{k}")
    ap.add_argument("--total", type=int)
    ap.add_argument("--done", type=int, dest="done_n")
    # для «Карты» пульта: какой скилл взят и какой файл получился (можно по нескольку раз)
    ap.add_argument("--skill", action="append", default=[])
    ap.add_argument("--file", action="append", default=[])
    a = ap.parse_args()
    DIR.mkdir(exist_ok=True)
    if a.cmd == "list":
        print("\n".join(lines()) or "задач нет"); return
    if a.cmd == "json":   # для Пульта агентов (C:\Users\User\pult): прогресс по вкладкам
        out, now = [], time.time()
        for t in load():
            if t.get("finished") and now - t["finished"] > KEEP_DONE:
                continue
            done, total, _ = progress(t)
            eta = None
            base, el = t.get("base", 0), now - t.get("started", now)
            if total and done and done > base and el > 60 and done < total:
                eta = fmt_min(el / (done - base) * (total - done))
            out.append({**t, "done": done, "total": total, "eta": eta})
        print(json.dumps(out, ensure_ascii=False)); return
    f = DIR / f"{a.id}.json"
    t = json.loads(f.read_text("utf-8")) if f.exists() else {"id": a.id, "started": time.time()}
    if a.cmd == "log":
        print(trace(t)); return
    prev_stage = t.get("stage") if not t.get("finished") else None
    was_done = bool(t.get("finished"))   # повторный done той же задачи — без нового напоминания
    if os.environ.get("PULT_SESSION") and not t.get("session"):   # запущено из вкладки Пульта
        t["session"] = os.environ["PULT_SESSION"]
    if a.cmd == "rm":
        f.unlink(missing_ok=True); return
    if a.cmd == "done":
        t["finished"] = time.time()
        t["stage"] = a.stage or "готово"
    else:
        for k in ("title", "who", "stage", "glob", "total"):
            if getattr(a, k) is not None:
                t[k] = getattr(a, k)
        if a.done_n is not None:
            t["done"] = a.done_n
        t.pop("finished", None)
        if a.glob or "base" not in t:   # с какого числа файлов считаем скорость
            t["base"], _, _ = progress(t)
            t["base"] = t["base"] or 0
            t["started"] = time.time()
    for k, vals in (("skills", a.skill), ("files", a.file)):
        for v in vals:
            if v not in t.setdefault(k, []):
                t[k].append(v)
    t["updated"] = time.time()
    if t.get("stage") != prev_stage or a.cmd == "done":   # журнал шагов
        t.setdefault("log", []).append({"t": t["updated"], "stage": t.get("stage", ""), "done": t.get("done")})
        t["log"] = t["log"][-50:]
    f.write_text(json.dumps(t, ensure_ascii=False), "utf-8")
    if a.cmd == "done" and not was_done:
        remind(t)
    print(line(t) or "")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
