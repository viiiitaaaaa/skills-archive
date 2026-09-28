"""Раскладка файлов по папкам по правилам «шаблон имени → папка».
По умолчанию вхолостую (показывает, сколько куда). Реальный перенос — с --apply.

python sort_by_rules.py <папка-источник> [<ещё папка> ...] --rules rules.local.json [--apply]

Правила (JSON): {"root": "G:/Мой диск", "trash": "_Можно удалить (дубли и мусор)",
                 "journal": "_журнал разбора диска.csv", "unsorted": "_Разобрать",
                 "rules": [["регулярка по имени", "папка относительно root"], ...]}
Первое совпавшее правило побеждает, регистр не важен. Что не подошло ни одному — в unsorted/<расширение>.
Скрипт не затирает одноимённые файлы (« (2)»), копии с тем же именем и размером кладёт в trash/Копии…,
пустые файлы (0 байт, кроме ~$) — в trash/Пустые…, каждое действие пишет в журнал откуда → куда."""
import argparse, csv, datetime, json, os, re, shutil
from collections import Counter

ap = argparse.ArgumentParser()
ap.add_argument("sources", nargs="+")
ap.add_argument("--rules", required=True)
ap.add_argument("--apply", action="store_true")
a = ap.parse_args()
cfg = json.load(open(a.rules, encoding="utf-8"))
R = cfg["root"].rstrip("/\\")
TR = os.path.join(R, cfg.get("trash", "_Можно удалить (дубли и мусор)"))
RULES = [(re.compile(p, re.I), os.path.join(R, d)) for p, d in cfg["rules"]]
LOG, stat = [], Counter()


def mv(src, d):
    name = os.path.basename(src.rstrip("/\\"))
    dst = os.path.join(d, name)
    if os.path.isfile(src) and os.path.isfile(dst) and os.path.getsize(src) == os.path.getsize(dst) and not d.startswith(TR):
        return mv(src, os.path.join(TR, "Копии (уже есть в папке назначения)"))
    b, e = os.path.splitext(dst); i = 2
    while os.path.exists(dst):
        dst = f"{b} ({i}){e}"; i += 1
    stat[os.path.relpath(d, R)] += 1
    LOG.append((src, dst))
    if a.apply:
        os.makedirs(d, exist_ok=True)
        shutil.move(src, dst)


for base in a.sources:
    for n in sorted(os.listdir(base)):
        p = os.path.join(base, n)
        if n == "desktop.ini":
            continue
        if os.path.isfile(p) and os.path.getsize(p) == 0 and not n.startswith("~$"):
            mv(p, os.path.join(TR, "Пустые (недокачанные) копии")); continue
        for rx, d in RULES:
            if rx.search(n):
                mv(p, d); break
        else:
            ext = os.path.splitext(n)[1].lower().lstrip(".") or "папки"
            mv(p, os.path.join(R, cfg.get("unsorted", "_Разобрать"), ext))

for k, v in stat.most_common():
    print(f"{v:5}  {k}")
print(f"{'ПЕРЕНЕСЕНО' if a.apply else 'ВХОЛОСТУЮ, будет перенесено'}: {len(LOG)}")
if a.apply and LOG:
    j = os.path.join(R, cfg.get("journal", f"_журнал разбора диска {datetime.date.today()}.csv"))
    with open(j, "a", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, delimiter=";")
        for s, d in LOG:
            w.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), os.path.relpath(s, R) if s.startswith(R) else s, os.path.relpath(d, R)])
    print("журнал:", j)
