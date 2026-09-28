"""Сверка двух мест (например C:\\Users\\User\\Downloads и G:\\Мой диск): какие файлы из первого есть во втором
(по имени+размеру, в любой подпапке), а каких нет нигде.
python compare_dirs.py <что проверяем> <где ищем> [--out список.txt]"""
import argparse, datetime, os

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst"); ap.add_argument("--out")
a = ap.parse_args()
idx = set()
for r, _, fs in os.walk(a.dst):
    for f in fs:
        try: idx.add((f, os.path.getsize(os.path.join(r, f))))
        except OSError: pass
have = miss = 0; total = msz = 0; rows = []
for r, _, fs in os.walk(a.src):
    for f in fs:
        p = os.path.join(r, f); s = os.path.getsize(p); total += s
        if (f, s) in idx: have += 1
        else:
            miss += 1; msz += s
            rows.append(f"{datetime.datetime.fromtimestamp(os.path.getmtime(p)):%d.%m.%Y}\t{s//1024} КБ\t{os.path.relpath(p, a.src)}")
print(f"В «{a.src}»: {have+miss} файлов, {total/1e9:.2f} ГБ")
print(f"  есть копия в «{a.dst}»: {have}")
print(f"  НЕТ копии: {miss} ({msz/1e9:.2f} ГБ) — при удалении пропадут навсегда")
if a.out:
    open(a.out, "w", encoding="utf-8").write("\n".join(sorted(rows)))
    print("список:", a.out)
