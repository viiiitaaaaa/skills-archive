"""Поиск «что мы знаем про …» по всем нашим знаниям сразу.

python poisk.py "доставка в США" [--n 15] [--vse]
Где ищет: все .md скиллов (уроки, книги, курсы, приёмы), память Claude, принятое к сведению (notes.json).
--vse — ещё и разобранные, но не принятые новости (biz/tool/soft), с меньшим весом.
Выдаёт куски с путём к файлу и строкой — открыть и прочитать целиком перед ответом.
"""
import json
import re
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\User\.claude\skills")
MEMORY = Path(r"C:\Users\User\.claude\projects\C--Users-User\memory")
NOTES = Path(r"C:\Users\User\tg_monitor\notes.json")
STOP = {"что", "мы", "про", "как", "для", "наш", "наши", "это", "и", "в", "на", "по", "с", "о", "об", "знаем", "умеем"}


def norm(s):
    return s.lower().replace("ё", "е")


def stems(q):
    out = []
    for w in re.findall(r"[\w\-]+", norm(q)):
        if w in STOP or len(w) < 2:
            continue
        out.append(w[:max(4, len(w) - 2)] if len(w) >= 6 else w)
    return out


def md_chunks():
    # принятое.md — копия notes.json, его ищем по заметкам
    files = [f for f in SKILLS.rglob("*.md") if "synced" not in f.parts and f.name != "принятое.md"]
    files += list(MEMORY.glob("*.md"))
    for f in files:
        try:
            lines = f.read_text(encoding="utf-8-sig").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        kind = "память" if MEMORY in f.parents else f"скилл {f.relative_to(SKILLS).parts[0]}"
        start, head, buf = 1, "", []
        for i, l in enumerate(lines, 1):
            if l.startswith("#") and buf:
                yield kind, f"{f}:{start}", head, "\n".join(buf), 1.0
                start, buf = i, []
            if l.startswith("#"):
                head = l.strip("# ").strip()
            buf.append(l)
        if buf:
            yield kind, f"{f}:{start}", head, "\n".join(buf), 1.0


def note_chunks(vse):
    notes = json.loads(NOTES.read_text(encoding="utf-8"))
    for k, v in notes.items():
        if v.get("noted"):
            w, kind = 1.2, "принято"
        elif vse and v.get("cat") in ("biz", "tool", "soft"):
            w, kind = 0.5, "новость"
        else:
            continue
        summ = v.get("summary", "")
        summ = " ".join(summ) if isinstance(summ, list) else str(summ)
        text = f'{v.get("headline", "")}\n{summ}\nДля нас: {v.get("for_us", "")}\nПринято: {v.get("noted", "")}'
        yield kind, f"https://t.me/{k}", v.get("noted_title") or v.get("headline", ""), text, w


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    n = int(a[a.index("--n") + 1]) if "--n" in a else 15
    vse = "--vse" in a
    q = " ".join(x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] != "--n"))
    st = stems(q)
    if not st:
        print("пустой запрос")
        return
    hits = []
    for kind, where, head, text, w in list(md_chunks()) + list(note_chunks(vse)):
        t, h = norm(text), norm(head)
        found = [s for s in st if s in t]
        if not found:
            continue
        score = (len(set(found)) / len(st)) * 10 + sum(2 for s in st if s in h) + min(t.count(st[0]), 5) * 0.2
        hits.append((score * w, kind, where, head, text, found))
    hits.sort(key=lambda x: -x[0])
    full = [x for x in hits if len(set(x[5])) == len(set(st))]
    print(f"запрос: {q} | найдено кусков: {len(hits)}, со всеми словами: {len(full)}\n")
    for score, kind, where, head, text, found in hits[:n]:
        t = text.replace("\n", " ")
        p = norm(t).find(found[0])
        snip = t[max(0, p - 120):p + 280].strip()
        print(f"[{kind}] {head[:90]}\n  {where}\n  …{snip}…\n")


if __name__ == "__main__":
    main()
