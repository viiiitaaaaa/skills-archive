r"""Слово «учиться»: что делаем сейчас + что из собранного подходит.

python kontekst.py            -> печатает паспорт дел и кандидатов по источникам
python kontekst.py --out f.md -> то же в файл
Ничего не пишет в скиллы — только читает. Поиск берём из znaniya\poisk.py (не дублируем).
"""
import io
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HOME = Path.home()
ZN = HOME / ".claude" / "skills" / "znaniya"
sys.path.insert(0, str(ZN))
import poisk  # noqa: E402  (наш общий поиск)

PY = sys.executable
STOP = set("это для при как что или надо нужно сделать скилл вкладка потом через если только можно после перед уже ещё "
           "свои свой новый новые пульт главная мой бот дела своя она сам сама".split())


def run(args):
    r = subprocess.run([PY, *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    return r.stdout.strip()


def tabs():
    return [l.strip() for l in run([str(HOME / "pult" / "razdat.py"), "list"]).splitlines() if re.match(r"\s+tm\w+ — ", l)]


def dela():
    out = []
    for l in run([str(HOME / "pult" / "razdat.py"), "dela"]).splitlines():
        if " | " in l:
            out.append(l.split(" | ", 1)[1][:160])
    return out


def табло():
    return run([str(HOME / ".claude" / "agent_status.py"), "list"])[:600]


def свежие_планы(days=3, n=5):
    res = []
    for p in HOME.glob("*/PLAN.md"):
        if time.time() - p.stat().st_mtime < days * 86400:
            heads = [l.strip("# ").strip() for l in p.read_text("utf-8", "replace").splitlines() if l.startswith("#")][:4]
            res.append((p.stat().st_mtime, p.parent.name, heads))
    return [f"{d}: {', '.join(h)}" for _, d, h in sorted(res, reverse=True)[:n]]


def темы(табы, планы, k=6):
    """Запросы = названия вкладок (без служебных слов) + заголовки свежих планов. Без частотной каши."""
    q = []
    for t in табы:
        name = t.split(" — ", 2)[-1].strip()
        if name and name not in q and "учиться" not in name.lower():
            q.append(name)
    for p in планы:
        head = p.split(": ", 1)[0]
        q.append(head)
    return q[:k]


def источник(kind, where):
    w = where.lower()
    if kind == "принято":
        return "новости: принято"
    if kind == "новость":
        return "новости"
    if "zapas" in w:
        return "запас"
    if "kursy-konspekty" in w:
        return "курсы"
    if "pravo-istochniki" in w:
        return "право"
    if "knowledge-library" in w or "knigi" in w or "iz_knig" in w or "kak-uchitsya" in w:
        return "книги"
    return "прочие скиллы/память"


def кандидаты(запросы, топ=5):
    """По каждому запросу — лучшие куски по оценке poisk (доля слов + слова в заголовке), по источникам."""
    out = {}
    chunks = [c for c in list(poisk.md_chunks()) + list(poisk.note_chunks(False)) if "backup" not in c[1].lower()]
    for q in запросы:
        st = poisk.stems(q)
        if not st:
            continue
        scored = []
        for kind, where, head, text, w in chunks:
            t, h = poisk.norm(text), poisk.norm(head)
            found = {s_ for s_ in st if s_ in t}
            if len(found) < max(1, (len(st) + 1) // 2):
                continue
            sc = (len(found) / len(st)) * 10 + sum(2 for s_ in st if s_ in h)
            scored.append((sc * w, источник(kind, where), where, head[:80]))
        per = {}
        for sc, src, where, head in sorted(scored, reverse=True):
            if len(per.setdefault(src, [])) < топ:
                per[src].append((where, head, q))
        for src, items in per.items():
            for where, head, qq in items:
                out.setdefault(src, {}).setdefault(where, (head, qq, 1))
    return out


def журнал(темы_):
    f = HOME / "zhurnal" / "data" / "lenta.json"
    if not f.exists():
        return []
    d = json.loads(f.read_text("utf-8"))
    items = d.values() if isinstance(d, dict) else d
    res = []
    for it in items:
        s = poisk.norm(json.dumps(it, ensure_ascii=False))
        if it.get("zachem") and it["zachem"] != "мимо" and any(st_ and st_[0] in s for st_ in (poisk.stems(t) for t in темы_)):
            res.append(f'{it.get("title", it.get("id", "?"))[:70]} — {str(it["zachem"])[:90]}')
    return res[:6]


def main():
    tb, dl, pl = tabs(), dela(), свежие_планы()
    ts = темы(tb, pl)
    lines = ["# Что делаем сейчас", "## Вкладки пульта", *tb, "## Табло", табло() or "пусто",
             "## Свежие PLAN.md", *pl, "## Мои дела (открытые)", *[d[:110] for d in dl[:12]],
             "", f"## Запросы (по вкладкам и планам): {' | '.join(ts)}", "", "# Кандидаты из собранного (путь:строка — раздел — по какой теме)"]
    cand = кандидаты(ts)
    for src in ["книги", "новости: принято", "запас", "курсы", "право", "прочие скиллы/память"]:
        items = cand.get(src, {})
        lines.append(f"## {src}: {len(items)}")
        for where, (head, t, w) in list(items.items())[:10]:
            lines.append(f"- {head} | {where} | «{t}»")
    zh = журнал(ts)
    lines += [f"## 📓 журнал: {len(zh)}", *[f"- {z}" for z in zh]]
    text = "\n".join(lines)
    if "--out" in sys.argv:
        Path(sys.argv[sys.argv.index("--out") + 1]).write_text(text, "utf-8")
    print(text)


if __name__ == "__main__":
    main()
