"""Какие папки компьютера Google Drive (DriveFS) на самом деле синхронизирует и куда.
python drive_sync_roots.py"""
import datetime, glob, os, sqlite3

D = os.path.join(os.environ["LOCALAPPDATA"], "Google", "DriveFS")
db = os.path.join(D, "root_preference_sqlite.db")
if not os.path.exists(db):
    raise SystemExit("Google Drive для компьютера не найден")
c = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
cols = [r[1] for r in c.execute("pragma table_info(roots)")]
rows = list(c.execute("select * from roots"))
if not rows:
    print("Ни одна папка компьютера не синхронизируется (работает только G:\\Мой диск).")
for r in rows:
    d = dict(zip(cols, r))
    path = next((v for v in r if isinstance(v, str) and ":\\" in v), "?")
    print(f"Синхронизируется: {path}  → раздел «Компьютеры» Google Диска (не «Мой диск»)")
for m in glob.glob(os.path.join(D, "*", "mirror_sqlite.db")):
    mc = sqlite3.connect(f"file:{m}?mode=ro", uri=True)
    for r in mc.execute("select * from mirror_item"):
        # корневая запись: 5-й столбец (родитель) = -1, дальше имя и время создания в мс
        if len(r) > 7 and r[4] == -1 and isinstance(r[7], int):
            print(f"   корень «{r[5]}», подключён {datetime.datetime.fromtimestamp(r[7]/1000):%d.%m.%Y %H:%M}")
print("\nВсё остальное на C: (в т.ч. Загрузки) НЕ синхронизируется: перетаскивание на G: делает копию.")
