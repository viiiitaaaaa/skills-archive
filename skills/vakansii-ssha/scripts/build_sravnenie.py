# -*- coding: utf-8 -*-
"""Собирает страницу «Вакансии и наш опыт» из sravnenie_dannye.json
плюс данные (зарплата, страна, ссылка) из двух сборов вакансий."""
import json, io, html, sys, datetime

sys.stdout.reconfigure(encoding="utf-8")

D = json.load(io.open("sravnenie_dannye.json", encoding="utf-8"))
staryy = json.load(io.open("vakansii_30.json", encoding="utf-8"))
novyy = json.load(io.open("vakansii_sbor_2026-10-14.json", encoding="utf-8"))

ANYWHERE = ("anywhere", "любой точки мира", "нерезидента: да", "worldwide", "глобально")


def po_kompanii(name, title=""):
    """Ищем вакансию по компании, а если у компании их несколько — ещё и по названию."""
    n, t = name.lower(), title.lower()[:14]
    for j in staryy:
        if j.get("company", "").lower().startswith(n[:12]) and t[:8] in j.get("title", "").lower():
            w = j.get("where", "")
            return {
                "salary": j.get("salary_year_usd") or 0,
                "where": w,
                "url": j.get("url", ""),
                "posted": j.get("posted", ""),
                "ru": any(a in w.lower() for a in ANYWHERE),
                "src": "сбор 14.10 (LinkedIn/Himalayas)",
            }
    for j in novyy:
        if j.get("company", "").lower().startswith(n[:12]) and t[:8] in j.get("title", "").lower():
            return {
                "salary": j.get("salary_year_usd") or 0,
                "where": j.get("where", ""),
                "url": j.get("url", ""),
                "posted": j.get("posted", ""),
                "ru": bool(j.get("russia_ok")),
                "src": j.get("source", ""),
            }
    return None


SHTATY = ("usa", "united states", "u.s.", ", ca", ", ny", ", tx", ", ar", ", ga", ", va",
          ", md", ", il", ", ma", ", wa", ", pa", ", dc", ", co", ", mo", ", nc", ", fl",
          "california", "new york", "texas", "arkansas", "georgia", "virginia", "chicago",
          "san francisco", "san jose", "seattle", "boston", "austin", "denver", "miami")


def eto_ssha(where):
    w = (where or "").lower()
    return any(k in w for k in SHTATY)


rows = []
for v in D["vakansii"]:
    meta = po_kompanii(v["company"], v["title"])
    if not meta:
        print("не нашла данные:", v["company"])
        continue
    m, p, g = len(v["match"]), len(v["partial"]), len(v["gap"])
    score = round(100 * (m + 0.5 * p) / max(1, m + p + g))
    usa = eto_ssha(meta["where"])
    # группы: 0 — США, 1 — остальные страны, 2 — те, что можно вести из России (в самый конец)
    gruppa = 0 if usa else (2 if meta["ru"] else 1)
    rows.append({**v, **meta, "score": score, "usa": usa, "gruppa": gruppa})

rows.sort(key=lambda r: (r["gruppa"], -r["score"], -r["salary"]))
print(f"вакансий в таблице: {len(rows)}; США: {sum(1 for r in rows if r['usa'])}; "
      f"можно из России: {sum(1 for r in rows if r['ru'])}")

e = html.escape


def spisok(items, cls):
    if not items:
        return '<p class="pusto">—</p>'
    return f'<ul class="{cls}">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


def stolbtsy(v):
    return f"""<div class="tri">
      <div class="col da"><h4><span class="zn">✓</span>Совпадает<span class="cnt">{len(v['match'])}</span></h4>{spisok(v['match'],'da')}</div>
      <div class="col chast"><h4><span class="zn">≈</span>Частично<span class="cnt">{len(v['partial'])}</span></h4>{spisok(v['partial'],'chast')}</div>
      <div class="col net"><h4><span class="zn">✕</span>Не совпадает<span class="cnt">{len(v['gap'])}</span></h4>{spisok(v['gap'],'net')}</div>
    </div>"""


karty = []
for i, v in enumerate(rows, 1):
    if v["usa"]:
        ru = '<span class="metka ru">США</span>'
    elif v["ru"]:
        ru = '<span class="metka strana">можно вести из России</span>'
    else:
        ru = '<span class="metka strana">другая страна, нужен местный адрес</span>'
    ssylka = f'<a class="ssylka" href="{e(v["url"])}" target="_blank" rel="noopener">Открыть вакансию ↗</a>' if v["url"] else ""
    karty.append(f"""<article class="karta" data-ru="{int(v['ru'])}" data-usa="{int(v['usa'])}" data-score="{v['score']}">
      <header class="shapka">
        <div class="nomer">{i}</div>
        <div class="zagolovki">
          <h3>{e(v['title_ru'])}</h3>
          <p class="orig">{e(v['title'])} · {e(v['company'])}</p>
        </div>
        <div class="cifry">
          <div class="dengi">{v['salary']:,}</div><div class="dengi-pod">$ в год</div>
        </div>
      </header>
      <div class="metki">{ru}<span class="metka">{e(v['where'][:80])}</span><span class="metka tihaya">{e(v['src'])}</span></div>
      <div class="polosa" aria-hidden="true"><div class="zapoln" style="width:{v['score']}%"></div><span class="procent">{v['score']}% наш опыт</span></div>
      {stolbtsy(v)}
      <footer class="vyvod"><strong>Вывод:</strong> {e(v['vyvod'])} {ssylka}</footer>
    </article>""")

pr = D["profil"]
profil = f"""<section class="profil">
  <h2>Наш опыт — то, с чем сверяем</h2>
  {stolbtsy({'match': pr['est'], 'partial': pr['chastichno'], 'gap': pr['net']})}
</section>"""

vsego = len(rows)
ru_n = sum(1 for r in rows if r["usa"])
silno = sum(1 for r in rows if r["score"] >= 50)

HTML = f"""<title>Вакансии и наш опыт</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Public+Sans:wght@400;500;700&display=swap">
<style>
/* Раскладка: шапка с цифрами → наш профиль → карточки вакансий в три столбца сверки */
:root {{
  --bg:#f7f5f1; --panel:#fffefb; --fg:#1f1d1a; --tihiy:#6b6559; --ramka:#e2ddd3;
  --da:#2f6f4f; --da-fon:#e8f1ea; --chast:#8a6420; --chast-fon:#f6eedd; --net:#9b3d33; --net-fon:#f6e6e3;
  --akcent:#1f4f6f; --akcent-fon:#e4edf3;
  --display:"Fraunces", Georgia, serif; --text:"Public Sans", -apple-system, system-ui, sans-serif;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#17181a; --panel:#1f2124; --fg:#eceae5; --tihiy:#9a958b; --ramka:#33363a;
  --da:#79c49a; --da-fon:#1d2b24; --chast:#d8ab5c; --chast-fon:#2c2519; --net:#e08a7e; --net-fon:#2e1f1d;
  --akcent:#8fc3e0; --akcent-fon:#1b2730; color-scheme: dark;
}} }}
:root[data-theme="dark"] {{
  --bg:#17181a; --panel:#1f2124; --fg:#eceae5; --tihiy:#9a958b; --ramka:#33363a;
  --da:#79c49a; --da-fon:#1d2b24; --chast:#d8ab5c; --chast-fon:#2c2519; --net:#e08a7e; --net-fon:#2e1f1d;
  --akcent:#8fc3e0; --akcent-fon:#1b2730; color-scheme: dark;
}}
* {{ box-sizing:border-box }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--text); line-height:1.5; margin:0 }}
.obolochka {{ max-width:1180px; margin:0 auto;
  padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px));
  padding-block:32px 56px }}
h1 {{ font-family:var(--display); font-size:clamp(28px,5vw,44px); font-weight:700; margin:0 0 8px; text-wrap:balance; letter-spacing:-.01em }}
.podzag {{ color:var(--tihiy); max-width:62ch; margin:0 0 24px }}
.svodka {{ display:flex; flex-wrap:wrap; gap:12px; margin-bottom:28px }}
.plitka {{ background:var(--panel); border:1px solid var(--ramka); border-radius:10px; padding:12px 16px; min-width:0; flex:1 1 150px }}
.plitka b {{ display:block; font-family:var(--display); font-size:26px; font-variant-numeric:tabular-nums; line-height:1.1 }}
.plitka span {{ color:var(--tihiy); font-size:12.5px }}
h2 {{ font-family:var(--display); font-size:clamp(19px,2.6vw,24px); margin:0 0 14px }}
.profil {{ background:var(--akcent-fon); border:1px solid var(--ramka); border-radius:12px; padding:20px; margin-bottom:34px }}
.profil h2 {{ color:var(--akcent) }}
.filtry {{ display:flex; flex-wrap:wrap; gap:8px; margin:0 0 20px; align-items:center }}
.filtry button {{ font:inherit; font-size:13px; padding:7px 14px; border-radius:999px; cursor:pointer;
  border:1px solid var(--ramka); background:var(--panel); color:var(--fg) }}
.filtry button[aria-pressed="true"] {{ background:var(--fg); color:var(--bg); border-color:var(--fg) }}
.filtry button:focus-visible, .ssylka:focus-visible {{ outline:2px solid var(--akcent); outline-offset:2px }}
.karta {{ background:var(--panel); border:1px solid var(--ramka); border-radius:12px; padding:18px; margin-bottom:16px }}
.shapka {{ display:flex; gap:14px; align-items:flex-start; flex-wrap:wrap }}
.nomer {{ font-family:var(--display); font-size:15px; color:var(--tihiy); min-width:1.6em; font-variant-numeric:tabular-nums }}
.zagolovki {{ flex:1 1 240px; min-width:0 }}
.karta h3 {{ font-family:var(--display); font-size:19px; margin:0 0 2px; text-wrap:balance }}
.orig {{ margin:0; color:var(--tihiy); font-size:13px }}
.cifry {{ text-align:right; min-width:0 }}
.dengi {{ font-family:var(--display); font-size:24px; font-variant-numeric:tabular-nums; line-height:1 }}
.dengi-pod {{ color:var(--tihiy); font-size:11.5px }}
.metki {{ display:flex; flex-wrap:wrap; gap:6px; margin:12px 0 10px }}
.metka {{ font-size:11.5px; padding:3px 9px; border-radius:999px; border:1px solid var(--ramka); color:var(--tihiy) }}
.metka.ru {{ background:var(--da-fon); color:var(--da); border-color:transparent; font-weight:500 }}
.metka.strana {{ background:var(--net-fon); color:var(--net); border-color:transparent }}
.metka.tihaya {{ opacity:.7 }}
.polosa {{ position:relative; height:22px; background:var(--bg); border:1px solid var(--ramka); border-radius:999px; overflow:hidden; margin-bottom:16px }}
.zapoln {{ height:100%; background:var(--da-fon); border-right:2px solid var(--da) }}
.procent {{ position:absolute; inset:0; display:flex; align-items:center; padding-left:10px; font-size:11.5px; color:var(--fg) }}
.tri {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px }}
@media (max-width:760px) {{ .tri {{ grid-template-columns:1fr }} .cifry {{ text-align:left }} }}
.col {{ min-width:0; border-radius:10px; padding:12px 13px }}
.col.da {{ background:var(--da-fon) }} .col.chast {{ background:var(--chast-fon) }} .col.net {{ background:var(--net-fon) }}
.col h4 {{ display:flex; align-items:center; gap:7px; margin:0 0 8px; font-size:11.5px; text-transform:uppercase; letter-spacing:.07em }}
.col.da h4 {{ color:var(--da) }} .col.chast h4 {{ color:var(--chast) }} .col.net h4 {{ color:var(--net) }}
.zn {{ font-size:13px }}
.cnt {{ margin-left:auto; font-variant-numeric:tabular-nums; opacity:.65 }}
.col ul {{ margin:0; padding-left:17px; font-size:13.5px }}
.col li {{ margin-bottom:6px }}
.pusto {{ margin:0; color:var(--tihiy) }}
.vyvod {{ margin-top:14px; padding-top:12px; border-top:1px solid var(--ramka); font-size:13.5px; color:var(--fg) }}
.ssylka {{ color:var(--akcent); text-decoration:none; font-weight:500; white-space:nowrap }}
.ssylka:hover {{ text-decoration:underline }}
.snoska {{ color:var(--tihiy); font-size:12.5px; margin-top:28px; max-width:70ch }}
.popravka {{ background:var(--net-fon); border:1px solid var(--ramka); border-left:3px solid var(--net);
  border-radius:0 10px 10px 0; padding:14px 17px; margin-bottom:28px }}
.popravka h2 {{ color:var(--net); border:0; padding:0; margin:0 0 7px }}
.popravka p {{ margin:0 0 8px; font-size:13.5px; max-width:68ch }}
.popravka p:last-child {{ margin:0 }}
</style>

<div class="obolochka">
  <h1>Вакансии и наш опыт</h1>
  <p class="podzag">Вакансии с оплатой от 75 000 $ в год, сначала США. Страница открывается сразу
  на американских; вакансии других стран и те, что можно вести из России, идут последними.
  По каждой — три столбца:
  что из требований у нас уже есть, что есть частично и чего нет. Проценты считаются как
  совпадения плюс половина частичных.</p>

  <div class="popravka">
    <h2>Английский A2 (pre-intermediate) учтён</h2>
    <p>Почти в каждой из этих вакансий работа идёт на английском — переписка, созвоны, документы.
    Поэтому английский стоит в столбце «Не совпадает» у всех, и проценты это уже учитывают.</p>
    <p>Меньше всего он мешает там, где работа письменная и асинхронная, а не голосом на созвонах:
    Invisible Technologies, Zuora, Mozilla, Tremendous. Больше всего — там, где платят за тексты
    и переговоры: RevenueCat, NetBox Labs, Wpromote, Liminal, Ashby, Cloudinary. Дойдёте до B1 —
    список открывается почти целиком, потому что по делу вы в эти роли попадаете.</p>
  </div>

  <div class="svodka">
    <div class="plitka"><b>{vsego}</b><span>вакансий в сверке</span></div>
    <div class="plitka"><b>{ru_n}</b><span>в США</span></div>
    <div class="plitka"><b>{silno}</b><span>совпадение 50% и выше</span></div>
    <div class="plitka"><b>{max(r['salary'] for r in rows):,}</b><span>$ — верх вилки</span></div>
  </div>

  {profil}

  <div class="filtry">
    <button data-f="usa" aria-pressed="true">Только США</button>
    <button data-f="vse" aria-pressed="false">Все</button>
    <button data-f="silno" aria-pressed="false">Совпадение 50%+</button>
    <button data-f="ru" aria-pressed="false">Можно из России</button>
  </div>

  <div id="spisok">
  {''.join(karty)}
  </div>

  <p class="snoska">Собрано {datetime.date.today().strftime('%d.%m.%Y')} парсером по открытым API
  (Himalayas, Remotive, RemoteOK, Jobicy, Arbeitnow) плюс наш сбор от 14.10. Зарплата взята из полей
  вакансии, а где её нет — из текста объявления, поэтому вилку стоит проверить при отклике.
  «Нужна виза или местный адрес» значит, что в объявлении прямо указана страна проживания.</p>
</div>

<script>
const knopki = document.querySelectorAll('.filtry button');
const karty = document.querySelectorAll('.karta');
knopki.forEach(k => k.addEventListener('click', () => {{
  knopki.forEach(d => d.setAttribute('aria-pressed', String(d === k)));
  const f = k.dataset.f;
  karty.forEach(c => {{
    const ru = c.dataset.ru === '1';
    const usa = c.dataset.usa === '1';
    const s = Number(c.dataset.score);
    c.hidden = (f === 'ru' && !ru) || (f === 'usa' && !usa) || (f === 'silno' && s < 50);
  }});
}}));
// страница открывается на вакансиях США — так же, как нажата первая кнопка
karty.forEach(c => {{ c.hidden = c.dataset.usa !== '1'; }});
</script>
"""

io.open("sravnenie_vakansiy.html", "w", encoding="utf-8").write(HTML)
print("готово: sravnenie_vakansiy.html")
