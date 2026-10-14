"""Каталог «Что мы умеем и что знаем» — одна страница без входа в Claude.

python katalog.py          — собрать C:\\Users\\User\\tg_monitor\\katalog_umeniy.html
python katalog.py --send   — собрать и отправить файлом в бот «Дела»
python katalog.py --list   — статусы принятого текстом (для проверки)

Источники: SKILL.md всех скиллов (описание и фразы), notes.json (принятое к сведению: noted/when),
sobytiya.json (группы скиллов и события), statusy.json (ручные статусы: {"канал/номер": "da|zhdet|net"}).
"""
import html
import json
import os
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
import urllib.request
import uuid
from datetime import datetime
from pathlib import Path

import yaml

HERE = Path(__file__).parent
SKILLS = Path(r"C:\Users\User\.claude\skills")
NOTES = Path(r"C:\Users\User\tg_monitor\notes.json")
OUT = Path(r"C:\Users\User\tg_monitor\katalog_umeniy.html")

STATUS = {"da": ("✅", "применено"), "zhdet": ("⏳", "ждёт своего события"), "net": ("❌", "отказались")}
LATER = re.compile(r"рано|вернуться|позже|при запуске", re.I)
DA = re.compile(r"\.py|скрипт|CLAUDE\.md", re.I)


def read_skills():
    out = {}
    for d in sorted(SKILLS.iterdir()):
        f = d / "SKILL.md"
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8-sig")
        m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
        desc = ""
        if m:
            try:
                desc = (yaml.safe_load(m.group(1)) or {}).get("description", "") or ""
            except yaml.YAMLError:
                desc = ""
        if not desc:  # описания нет — берём первую строку текста
            body = text[m.end():] if m else text
            desc = next((l.strip("# ").strip() for l in body.splitlines() if l.strip()), "")
        trig = ""
        t = re.search(r"Триггеры?:\s*(.+)$", desc, re.S)
        if t:
            trig = t.group(1).strip().rstrip(".")
            desc = desc[:t.start()].strip()
        short = re.split(r"(?<=[.!?])\s|\s—\s(?=Используй)|Используй", desc)[0].strip()
        out[d.name] = {"desc": short, "trig": trig.replace('"', "")}
    return out


def status_of(key, v, manual):
    if key in manual:
        return manual[key]
    # ✅ — правило «Всегда» действует, инструмент поставлен или по уроку сделан скрипт
    if v.get("when", "").startswith("Всегда") or v.get("installed") or DA.search(v.get("applied") or ""):
        return "da"
    # ❌ — отказались совсем: не ставили и знание в скилл не забирали
    if v.get("declined") and not v.get("applied") and not LATER.search(v["declined"]):
        return "net"
    # ⏳ — записано в скилл, поднимаю, когда начнём дело этого события
    return "zhdet"


def read_study():
    """Изучение ссылок поста (видео, курсы, статьи, GitHub): tg_monitor\\study_*\\res_*.json и out_*.json."""
    st = {}
    # папки по дате (study_0710 < study_1210): более свежая запись о той же ссылке заменяет старую
    files = sorted(list(NOTES.parent.glob("study_*/res_*.json")) + list(NOTES.parent.glob("study_*/out_*.json")),
                   key=lambda p: (p.parent.name[-4:], p.name))
    for f in files:
        try:
            rows = json.loads(f.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        for r in rows if isinstance(rows, list) else []:
            if not isinstance(r, dict) or not r.get("post"):
                continue
            s = str(r.get("status") or r.get("verdict") or "")
            kind = ("ok" if s.startswith(("изучено", "пропущено", "🟢", "🟡", "🔴")) else
                    "part" if s.startswith("частично") else "fail")
            st.setdefault(r["post"], {})[norm_link(r.get("link", ""))] = (kind, r.get("link", ""), s, r.get("result", ""))
    return {p: list(v.values()) for p, v in st.items()}


def norm_link(l):
    return re.sub(r"^https?://(www\.)?|[?#].*$|/$", "", l or "").lower()


def study_line(rows):
    if not rows:
        return ""
    ok = sum(1 for r in rows if r[0] == "ok")
    part = sum(1 for r in rows if r[0] == "part")
    fail = len(rows) - ok - part
    tail = (f", частично {part}" if part else "") + (f", ⚠️ не открылось {fail}" if fail else "")
    vid = " (есть видео/курс)" if any(re.search(r"youtu|course|playlist|academy", r[1]) for r in rows) else ""
    return f"📖 Материалы по ссылкам: изучено {ok} из {len(rows)}{tail}{vid}"


def read_noted():
    notes = json.loads(NOTES.read_text(encoding="utf-8"))
    study = read_study()
    mf = HERE / "statusy.json"
    manual = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
    items = []
    for k, v in notes.items():
        if not v.get("noted"):
            continue
        items.append({
            "key": k, "when": v.get("when", "Прочее"), "title": v.get("noted_title") or v.get("headline", k),
            "what": v.get("noted", ""), "where": v.get("applied") or v.get("installed") or v.get("declined") or "",
            "status": status_of(k, v, manual), "study": study_line(study.get(k)), "link": f"https://t.me/{k}" if not k.startswith("c/") else f"https://t.me/{k}",
        })
    return items


def read_sliv():
    """Курсы канала slivaker_it, отмеченные полезными при разборе (cat == course)."""
    import sqlite3
    notes = json.loads(NOTES.read_text(encoding="utf-8"))
    db = sqlite3.connect(NOTES.parent / "tg_monitor.db")
    out = []
    for k, v in notes.items():
        if not k.startswith("slivaker_it/") or v.get("cat") != "course":
            continue
        r = db.execute("select post_date, text from posts where channel='slivaker_it' and post_id=?",
                       (int(k.split("/")[1]),)).fetchone()
        date, text = (r[0][:10], r[1] or "") if r else ("", "")
        head = text.split("Размер:")[0]
        title = v.get("headline") or re.sub(r"^\s*Курс\s*:\s*", "", " ".join(head.split())) or k
        size = re.search(r"Размер:\s*([^\n]+)", text)
        price = re.search(r"Цена:\s*([^\n]+)", text)
        out.append({"key": k, "date": date, "title": title, "for_us": v.get("for_us", ""),
                    "size": size.group(1).strip() if size else "", "price": price.group(1).strip() if price else ""})
    return sorted(out, key=lambda x: x["date"], reverse=True)


def gaps_block(study):
    rows = []
    for post, items in study.items():
        for kind, link, status, result in items:
            if kind != "ok":
                rows.append((kind, post, link, status, result))
    rows.sort(key=lambda x: (x[0] != "fail", x[1]))
    lis = "".join(
        f'<li class="it {"zhdet" if k == "fail" else ""}"><span class="ic">{"⚠️" if k == "fail" else "◐"}</span><div>'
        f'<a href="https://t.me/{esc(p)}">{esc(p)}</a> · <a href="{esc(l)}">ссылка</a>'
        f'<div class="what">{esc(s)}</div><div class="where">{esc(res)}</div></div></li>' for k, p, l, s, res in rows)
    return len(rows), lis


def esc(s):
    return html.escape(str(s or ""))


def build():
    cfg = json.loads((HERE / "sobytiya.json").read_text(encoding="utf-8"))
    skills = read_skills()
    noted = read_noted()
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    cnt = {s: sum(1 for i in noted if i["status"] == s) for s in STATUS}
    n_study = sum(1 for i in noted if i["study"])

    # 1. Что умеем
    grouped = set(n for g in cfg["gruppy_skillov"].values() for n in g)
    groups = dict(cfg["gruppy_skillov"])
    rest = [n for n in skills if n not in grouped]
    if rest:
        groups["Прочие скиллы"] = rest
    sk_html = []
    for g, names in groups.items():
        cards = []
        for n in names:
            if n not in skills:
                continue
            s = skills[n]
            trig = f'<p class="trig">Скажите: {esc(s["trig"])}</p>' if s["trig"] else ""
            cards.append(f'<div class="card" data-s="{esc((n + s["desc"] + s["trig"]).lower())}">'
                         f'<h4>{esc(n)}</h4><p>{esc(s["desc"])}</p>{trig}</div>')
        sk_html.append(f'<h3>{esc(g)}</h3><div class="grid">{"".join(cards)}</div>')

    # 2. Что знаем — по событиям
    ev_html = []
    used = set()
    for ev in cfg["sobytiya"]:
        its = [i for i in noted if i["when"] in ev["when"]]
        used.update(ev["when"])
        ev_html.append(event_block(ev["nazvanie"], ev["skilly"], its))
    other = [i for i in noted if i["when"] not in used]
    if other:
        ev_html.append(event_block("Прочее", [], other))

    n_gaps, gaps = gaps_block(read_study())
    sliv = read_sliv()
    sliv_html = "".join(
        f'<li class="it" data-s="{esc((c["title"] + c["for_us"]).lower())}"><span class="ic">◻️</span><div>'
        f'<a href="https://t.me/{esc(c["key"])}">{esc(c["title"])}</a> <span class="muted">· {esc(c["date"])}'
        f'{" · " + esc(c["size"]) if c["size"] else ""}{" · цена автора " + esc(c["price"]) if c["price"] else ""}</span>'
        f'<div class="what">{esc(c["for_us"])}</div></div></li>' for c in sliv)
    page = TEMPLATE.format(
        n_gaps=n_gaps, gaps=gaps, n_sliv=len(sliv), sliv=sliv_html,
        now=now, n_study=n_study, n_sk=len(skills), n_no=len(noted), da=cnt["da"], zhdet=cnt["zhdet"], net=cnt["net"],
        skills="".join(sk_html), events="".join(ev_html))
    OUT.write_text(page, encoding="utf-8")
    print(f"каталог: {OUT} — скиллов {len(skills)}, принятого {len(noted)} "
          f"(✅ {cnt['da']} / ⏳ {cnt['zhdet']} / ❌ {cnt['net']}), с изученными материалами {n_study}")
    return noted


def event_block(name, skilly, its):
    order = {"zhdet": 0, "da": 1, "net": 2}
    rows = []
    for i in sorted(its, key=lambda x: order[x["status"]]):
        ic, lab = STATUS[i["status"]]
        where = f'<div class="where">{esc(i["where"])}</div>' if i["where"] and i["where"] != i["what"] else ""
        if i["study"]:
            where += f'<div class="where">{esc(i["study"])}</div>'
        rows.append(f'<li class="it {i["status"]}" data-s="{esc((i["title"] + i["what"]).lower())}">'
                    f'<span class="ic" title="{lab}">{ic}</span><div><a href="{esc(i["link"])}">{esc(i["title"])}</a>'
                    f'<div class="what">{esc(i["what"])}</div>{where}</div></li>')
    z = sum(1 for i in its if i["status"] == "zhdet")
    sk = ", ".join(skilly)
    return (f'<details class="ev"{" open" if z else ""}><summary><b>{esc(name)}</b> '
            f'<span class="muted">· {len(its)} пунктов, ждут {z}</span></summary>'
            f'<p class="muted">Скиллы: {esc(sk) or "—"}</p><ul>{"".join(rows)}</ul></details>')


def token():
    t, c = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("OWNER_ID")
    if not (t and c):
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            t = t or winreg.QueryValueEx(k, "TELEGRAM_BOT_TOKEN")[0]
            c = c or winreg.QueryValueEx(k, "OWNER_ID")[0]
    return t, c


def send(path, caption):
    t, chat = token()
    b = uuid.uuid4().hex
    body = (f'--{b}\r\nContent-Disposition: form-data; name="chat_id"\r\n\r\n{chat}\r\n'
            f'--{b}\r\nContent-Disposition: form-data; name="caption"\r\n\r\n{caption}\r\n'
            f'--{b}\r\nContent-Disposition: form-data; name="document"; filename="{path.name}"\r\n'
            f'Content-Type: text/html\r\n\r\n').encode() + path.read_bytes() + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{t}/sendDocument", data=body,
                                 headers={"Content-Type": f"multipart/form-data; boundary={b}"})
    res = json.load(urllib.request.urlopen(req, timeout=120))
    print("в бот:", "отправлено" if res.get("ok") else res)


TEMPLATE = """<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Что мы умеем</title>
<style>
:root{{--bg:#faf9f6;--card:#fff;--tx:#1d1d1b;--mu:#6b6a65;--ln:#e4e2dc;--ac:#2f5d50;--wait:#fff6dc;}}
@media (prefers-color-scheme:dark){{:root{{--bg:#161615;--card:#1f1f1d;--tx:#ecebe6;--mu:#9c9a93;--ln:#33322f;--ac:#8cc4b0;--wait:#2b2716;}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:20px 16px 60px}}h1{{margin:0 0 4px;font-size:26px}}
h2{{margin:36px 0 8px;font-size:21px}}h3{{margin:22px 0 8px;font-size:16px;color:var(--ac)}}
.muted{{color:var(--mu);font-size:13px}}a{{color:var(--ac)}}
.stats{{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}}.stats div{{background:var(--card);border:1px solid var(--ln);border-radius:10px;padding:8px 14px}}
.stats b{{font-size:20px;display:block}}
#q{{width:100%;padding:11px 14px;font-size:16px;border:1px solid var(--ln);border-radius:10px;background:var(--card);color:var(--tx);position:sticky;top:8px;z-index:2}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}}
.card{{background:var(--card);border:1px solid var(--ln);border-radius:10px;padding:10px 12px}}
.card h4{{margin:0 0 4px;font-size:15px}}.card p{{margin:0;font-size:13.5px}}.card .trig{{margin-top:6px;color:var(--mu);font-size:12.5px}}
.ev{{background:var(--card);border:1px solid var(--ln);border-radius:10px;padding:10px 14px;margin:10px 0}}
.ev summary{{cursor:pointer;font-size:15.5px}}.ev ul{{list-style:none;padding:0;margin:6px 0 0}}
.it{{display:flex;gap:10px;padding:8px 6px;border-top:1px solid var(--ln)}}.it.zhdet{{background:var(--wait);border-radius:6px}}
.it .ic{{flex:none}}.what{{font-size:13.5px}}.where{{font-size:12.5px;color:var(--mu);word-break:break-word}}
.hide{{display:none!important}}
</style></head><body><main>
<h1>Что мы умеем и что знаем</h1>
<div class="muted">Обновлено {now}. Файл открывается в любом браузере, вход в Claude не нужен.</div>
<div class="stats"><div><b>{n_sk}</b>скиллов</div><div><b>{n_no}</b>принято к сведению</div>
<div><b>✅ {da}</b>применено</div><div><b>⏳ {zhdet}</b>ждут события</div><div><b>❌ {net}</b>отказались</div><div><b>📖 {n_study}</b>с изученными ссылками, видео, курсами</div></div>
<details class="ev" open><summary><b>⚠️ Не удалось изучить полностью — {n_gaps}</b>
<span class="muted">· важно: что не открылось и почему</span></summary>
<p class="muted">⚠️ — не открылось совсем; ◐ — частично (причина в строке). Остальные ссылки, видео и курсы из принятого изучены.</p>
<ul>{gaps}</ul></details>
<input id="q" placeholder="Поиск: реклама, доставка, сайт, 1688…" oninput="f(this.value)">
<h2>Что умеем — скиллы</h2>
<p class="muted">Скилл — готовая инструкция для Claude по одной теме. Чтобы вызвать, напишите одну из фраз «Скажите: …».</p>
{skills}
<h2>Что знаем — по событиям</h2>
<p class="muted">Всё, что вы принимали к сведению из новостей. Когда начинаем дело из списка, Claude поднимает пункты ⏳ этого события.
Книги и курсы — в скиллах knowledge-library и kursy-konspekty (поиск: «что мы знаем про …»).</p>
{events}
<h2>Курсы Сливакера — отмечены полезными, не изучены ({n_sliv})</h2>
<p class="muted">Канал slivaker_it выкладывает чужие платные курсы бесплатно, без разрешения авторов, поэтому Claude их не скачивает
и не проходит. Если курс куплен у автора или лежит у вас законно, скажите, где файлы, и Claude пройдёт его и разложит по скиллам.
Строка «цена автора» — сколько курс стоит официально.</p>
<details class="ev"><summary><b>Список курсов</b></summary><ul>{sliv}</ul></details>
</main><script>
function f(v){{v=v.toLowerCase().trim();
document.querySelectorAll('[data-s]').forEach(e=>e.classList.toggle('hide',v&&!e.dataset.s.includes(v)));
document.querySelectorAll('.ev').forEach(d=>{{if(v)d.open=true;d.classList.toggle('hide',v&&!d.querySelector('.it:not(.hide)'));}});
document.querySelectorAll('.grid').forEach(g=>{{const h=g.previousElementSibling;const e=v&&!g.querySelector('.card:not(.hide)');g.classList.toggle('hide',e);h.classList.toggle('hide',e);}});}}
</script></body></html>"""


if __name__ == "__main__":
    noted = build()
    if "--list" in sys.argv:
        for i in noted:
            print(STATUS[i["status"]][0], i["key"], "|", i["when"], "|", i["title"][:70], "|", i["what"][:90])
    if "--send" in sys.argv:
        send(OUT, "📚 Что мы умеем и что знаем — каталог. Открыть в браузере, вход в Claude не нужен.")
