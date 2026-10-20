"""Каталог «Что мы умеем и знаем» одним .md-файлом — для Context проекта в Claude Desktop.

python katalog_md.py  →  Рабочий стол\\Новая папка (2)\\Файлы для проектов Claude\\Что мы умеем и знаем.md
"""
import json
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
import katalog as k  # noqa: E402

# 20.10: она перенесла папку в «Новая папка (2)» (рабочий стол — её метки порядка, назад не двигать)
OUT = Path(r"C:\Users\User\Desktop\Новая папка (2)\Файлы для проектов Claude\Что мы умеем и знаем.md")
ZNAK = {"da": "✅", "zhdet": "⏳", "net": "❌"}


def main():
    cfg = json.loads((k.HERE / "sobytiya.json").read_text(encoding="utf-8"))
    skills = k.read_skills()
    noted = k.read_noted()
    cnt = {s: sum(1 for i in noted if i["status"] == s) for s in ZNAK}
    L = [f"# Что мы умеем и знаем — на {datetime.now():%d.%m.%Y %H:%M}", "",
         f"Скиллов {len(skills)}. Принятого к сведению {len(noted)}: ✅ применяем {cnt['da']} · "
         f"⏳ ждёт своего дела {cnt['zhdet']} · ❌ отказались {cnt['net']}.",
         "Подробности каждого пункта — в скилле из строки «где»; поиск — скилл znaniya («что мы знаем про …»).", "",
         "## Что умеем (скиллы)", ""]
    groups = dict(cfg["gruppy_skillov"])
    rest = [n for n in skills if n not in {x for g in groups.values() for x in g}]
    if rest:
        groups["Прочие скиллы"] = rest
    for g, names in groups.items():
        L.append(f"### {g}")
        for n in names:
            if n in skills:
                s = skills[n]
                L.append(f"- **{n}** — {s['desc']}" + (f" _Фразы: {s['trig']}_" if s["trig"] else ""))
        L.append("")
    L += ["## Что знаем (принятое из новостей, книг, курсов) — по делам, когда поднимать", ""]
    used = set()
    for ev in cfg["sobytiya"] + [{"nazvanie": "Прочее", "skilly": [], "when": None}]:
        its = [i for i in noted if (i["when"] in ev["when"] if ev["when"] else i["when"] not in used)]
        if ev["when"]:
            used.update(ev["when"])
        if not its:
            continue
        sk = f" (скиллы: {', '.join(ev['skilly'])})" if ev["skilly"] else ""
        L.append(f"### {ev['nazvanie']}{sk}")
        for i in sorted(its, key=lambda x: "da zhdet net".split().index(x["status"])):
            L.append(f"- {ZNAK[i['status']]} **{i['title']}** — {i['what']}" + (f" · где: {i['where']}" if i["where"] else ""))
        L.append("")
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"готово: {OUT} ({OUT.stat().st_size // 1024} КБ)")


if __name__ == "__main__":
    main()
