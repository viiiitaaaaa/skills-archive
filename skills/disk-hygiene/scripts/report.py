"""Отчёт по выгрузке WizTree: крупные папки, файлы, повторы, кэши, старые версии, нужные ревизии playwright.
python report.py <wiz.csv>"""
import csv, collections, json, os, sys
from pathlib import Path

BS = "\\"
U = os.path.expanduser("~")
L, A = os.environ.get("LOCALAPPDATA", ""), os.environ.get("APPDATA", "")


def load(path):
    rows = []
    with open(path, encoding="utf-8-sig", errors="ignore") as f:
        r = csv.reader(f); next(r); next(r)
        for row in r:
            try: rows.append((row[0], int(row[1])))
            except (ValueError, IndexError): pass
    return rows


def dir_size(p):
    p = Path(p)
    if not p.exists(): return None
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) if p.is_dir() else p.stat().st_size


def playwright_needed():
    """Ревизии браузеров, которые реально требуются установленным playwright/patchright."""
    need = set()
    for base in (U, A, L + BS + "Programs"):
        for bj in Path(base).rglob("browsers.json"):
            if "playwright" not in str(bj) and "patchright" not in str(bj): continue
            try:
                for b in json.load(open(bj, encoding="utf-8"))["browsers"]:
                    need.add(f"{b['name'].replace('-', '_')}-{b['revision']}")
            except Exception: pass
    return need


def main(csv_path):
    rows = load(csv_path)
    dirs = [x for x in rows if x[0].endswith(BS)]
    files = [x for x in rows if not x[0].endswith(BS)]
    drive = rows[0][0][:3] if rows else "C:" + BS

    def show(prefix, mn, n=20):
        out = [x for x in dirs if x[0].startswith(prefix) and x[0][len(prefix):].count(BS) == 1 and x[1] >= mn]
        if out: print("===", prefix)
        for p, s in sorted(out, key=lambda x: -x[1])[:n]: print(f"{s/1e9:7.2f} ГБ  {p}")

    for pre, mn in [(drive, 3e8), (drive + "Program Files" + BS, 5e8), (drive + "Program Files (x86)" + BS, 5e8),
                    (drive + "ProgramData" + BS, 5e8), (U + BS, 4e8), (L + BS, 6e8), (A + BS, 6e8), (drive + "Windows" + BS, 1e9)]:
        show(pre, mn)

    sys_prefix = tuple(drive + x for x in ("Windows", "Program Files", "ProgramData", "pagefile", "hiberfil", "swapfile"))
    print("\n=== 40 крупнейших файлов (кроме системных)")
    for p, s in sorted([x for x in files if not x[0].startswith(sys_prefix)], key=lambda x: -x[1])[:40]:
        print(f"{s/1e6:7.0f} МБ  {p}")
    for p, s in files:
        if p.lower() in (drive.lower() + "pagefile.sys", drive.lower() + "hiberfil.sys"):
            print(f"{s/1e9:7.2f} ГБ  {p}  (системный — трогает только она через настройки)")

    print("\n=== Повторы (имя+размер, от 10 МБ)")
    g = collections.defaultdict(list)
    for p, s in files:
        if s >= 1e7 and not p.startswith(sys_prefix): g[(os.path.basename(p), s)].append(p)
    dup = sorted([(k, v) for k, v in g.items() if len(v) > 1], key=lambda x: -x[0][1] * (len(x[1]) - 1))
    for (nm, s), v in dup[:25]:
        print(f"{s/1e6:6.0f} МБ x{len(v)}  {nm}  | " + " ; ".join(os.path.dirname(x)[-55:] for x in v))
    print(f"лишних копий: {sum(k[1]*(len(v)-1) for k, v in dup)/1e9:.2f} ГБ")

    print("\n=== Кэши и остатки (ключи для clean.ps1)")
    cand = {
        "capcut-cache": L + r"\CapCut\User Data\Cache", "npm-cache": L + r"\npm-cache", "pip-cache": L + r"\pip\cache",
        "temp": os.environ.get("TEMP", ""), "telegram-cache": A + r"\Telegram Desktop\tdata\user_data",
        "amd": drive + "AMD", "aliim-updates": A + r"\aliim\Update", "wechat-update": A + r"\Tencent\xwechat\update",
    }
    for k, p in cand.items():
        s = dir_size(p)
        if s: print(f"{s/1e9:6.2f} ГБ  {k:15} {p}")
    chrome = Path(L + r"\Google\Chrome\User Data")
    if chrome.exists():
        s = sum(f.stat().st_size for d in chrome.rglob("*") if d.is_dir() and d.name in ("Cache", "Code Cache", "GPUCache")
                for f in d.rglob("*") if f.is_file())
        print(f"{s/1e9:6.2f} ГБ  chrome-cache    {chrome}\\*\\Cache")

    print("\n=== Старые версии программ (рядом есть новее) — ключ old-versions")
    for base in (L + r"\CapCut\Apps", L + r"\Programs\Opera"):
        vs = sorted([d for d in Path(base).glob("*") if d.is_dir() and d.name[0].isdigit()],
                    key=lambda d: [int(x) for x in d.name.split(".") if x.isdigit()]) if Path(base).exists() else []
        for d in vs[:-1]:
            s = dir_size(d)
            if s and s > 1e7: print(f"{s/1e9:6.2f} ГБ  {d}")
    for d in list(Path(L).glob("*-updater")) + [Path(r"C:\Users\Public\Documents\PDD\FullUpdateFile")]:
        s = dir_size(d)
        if s and s > 1e7: print(f"{s/1e9:6.2f} ГБ  {d}")

    need = playwright_needed()
    pw = Path(L + r"\ms-playwright")
    if pw.exists():
        print("\n=== playwright: нужны скриптам:", ", ".join(sorted(need)) or "нет данных")
        for d in pw.glob("*-*"):
            flag = "нужна" if d.name in need or not d.name.startswith(("chromium", "webkit", "firefox")) else "НЕ используется"
            print(f"{dir_size(d)/1e9:6.2f} ГБ  {d.name:40} {flag}")


if __name__ == "__main__":
    main(sys.argv[1])
