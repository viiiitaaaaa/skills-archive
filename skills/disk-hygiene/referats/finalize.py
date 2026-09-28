"""Финал рефератов: сохранить не-учебное (keep), положить рефераты, удалить остальное (на G: — в корзину Диска).
python finalize.py "<учебная папка>" <work> [--later "подпапка/курс" ...] [--apply]
- <work>/manifest.json: {"titles", "files", "keep": {"отн. путь": "куда (путь от корня диска)"}}
- <work>/out/*.docx — готовые рефераты (md2docx.py)
- --later: курсы «на потом» — не удаляются, выносятся в «Курсы — на потом (исходники)» вместе с <work>/tr.
Без --apply только показывает. Проверяет, что все файлы папки есть в манифесте, иначе останавливается."""
import argparse, csv, datetime, json, os, shutil

ap = argparse.ArgumentParser()
ap.add_argument("folder"); ap.add_argument("work")
ap.add_argument("--later", nargs="*", default=[]); ap.add_argument("--apply", action="store_true")
a = ap.parse_args()
B, W = a.folder, a.work
root = os.path.dirname(B)
m = json.load(open(os.path.join(W, "manifest.json"), encoding="utf-8"))
known = set(m.get("keep", {}))
for v in m["files"].values(): known.update(v)
allf = {os.path.relpath(os.path.join(r, f), B) for r, _, fs in os.walk(B) for f in fs if f != "desktop.ini"}
lost = [x for x in allf - known if not any(x.startswith(l.replace("/", os.sep)) for l in a.later)]
if lost:
    raise SystemExit(f"СТОП: {len(lost)} файлов нет в манифесте, их не прочитали: {sorted(lost)[:10]}")

LOG = []
for rel, dest in m.get("keep", {}).items():
    src = os.path.join(B, rel); d = os.path.join(root, dest)
    if os.path.exists(src):
        LOG.append((rel, dest))
        if a.apply:
            os.makedirs(d, exist_ok=True); shutil.move(src, os.path.join(d, os.path.basename(src)))
LATER = "Курсы — на потом (исходники)"
for sub in a.later:
    src = os.path.join(B, sub)
    if os.path.exists(src):
        LOG.append((sub, LATER))
        if a.apply:
            os.makedirs(os.path.join(B, LATER), exist_ok=True)
            shutil.move(src, os.path.join(B, LATER, os.path.basename(sub.rstrip("/\\"))))
refs = sorted(os.listdir(os.path.join(W, "out")))
if a.apply:
    for f in refs: shutil.copy(os.path.join(W, "out", f), os.path.join(B, f))
keep = set(refs) | {"desktop.ini", LATER}
for n in os.listdir(B):
    if n in keep: continue
    LOG.append((n, "удалено"))
    if a.apply:
        p = os.path.join(B, n)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
print(f"рефератов: {len(refs)}; сохранить отдельно: {len(m.get('keep', {}))}; удалить объектов: {sum(1 for x in LOG if x[1]=='удалено')}")
if a.apply:
    with open(os.path.join(root, "_журнал разбора диска.csv"), "a", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, delimiter=";")
        for s, d in LOG: w.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), os.path.basename(B) + "/" + s, d])
    print("осталось в папке:", sorted(os.listdir(B)))
else:
    print("ВХОЛОСТУЮ. Запустите с --apply.")
