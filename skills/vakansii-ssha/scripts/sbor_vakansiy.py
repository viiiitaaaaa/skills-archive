# -*- coding: utf-8 -*-
"""Сбор удалённых вакансий из открытых API: Himalayas, Remotive, RemoteOK, Jobicy, Arbeitnow.
Фильтр: роль близка к нашему опыту + зарплата от 75 000 $ в год
(берём из полей API, а если их нет — вытаскиваем из текста вакансии).
Итог: vakansii_sbor_<дата>.json
"""
import json, re, io, sys, time, urllib.request, datetime

sys.stdout.reconfigure(encoding="utf-8")

MIN_USD = 75000
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# роль должна быть из нашего профиля: e-commerce, маркетплейсы, закупка,
# рост и лидогенерация, реклама, ИИ-автоматизация, операционка
ROLE_WORDS = [
    "ecommerce", "e commerce", "marketplace", "amazon", "shopify", "dropship",
    "growth", "demand generation", "lead generation", "performance marketing",
    "paid media", "paid social", "media buyer", "lifecycle marketing",
    "ai automation", "automation", "ai operations", "no code", "nocode",
    "sourcing", "procurement", "merchandis", "category manager", "product research",
    "operations manager", "business operations", "revenue operations", "revops",
    "digital marketing", "brand manager", "ai trainer", "seo",
    "marketing manager", "marketing director", "head of marketing", "head of growth",
    "market research", "supply chain", "retail", "dtc", "d2c",
]
BAD_WORDS = [
    "nurse", "driver", "teacher", "lawyer", "attorney", "accountant", "recruiter",
    "software engineer", "backend", "front end", "frontend", "full stack", "fullstack",
    "devops", "data engineer", "security engineer", "ios developer", "android developer",
    "game ", "ux ", "ui ", "graphic designer", "controller", "physician", "therapist",
    "developer", "architect", "engineer", "customer success", "account manager",
    "sales development", "business development", "channel", "partner manager",
    "alliance", "clinical", "insurance", "security",
    # производство, стройка, медицина и прочее не наше — The Muse их приносит много
    "propulsion", "machining", "mechanical", "superintendent", "sewer", "technician",
    "shift supervisor", "labor relations", "equity research", "appointment setter",
    "data center", "dangerous goods", "lpn", "rn ", "pharmac", "welder", "machinist",
    "electrical", "structural", "quality inspector", "warehouse associate", "picker",
    "account executive", "account representative", "sales associate", "cashier",
    "trainer", "program manager", "delivery lead", "field ", "installer",
]

# «от 120 000 $», «$120k–$150k», «120,000 - 150,000 USD»
RE_RANGE = re.compile(
    r"\$\s?(\d{2,3})[\s,.]?(\d{3})?\s?(k|K)?\s?(?:-|–|—|to)\s?\$?\s?(\d{2,3})[\s,.]?(\d{3})?\s?(k|K)?")
RE_ONE = re.compile(r"\$\s?(\d{2,3})[\s,.](\d{3})(?!\d)|\$\s?(\d{2,3})\s?(k|K)\b")


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            print(f"    попытка {i+1}: {e}")
            time.sleep(3)
    return None


def clean(html):
    if not html:
        return ""
    t = re.sub(r"(?s)<(script|style).*?</\1>", " ", str(html))
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&#39;", "'"), ("&rsquo;", "'"),
                 ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">"), ("&#8211;", "–")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def role_ok(title, extra=""):
    t = (title + " " + extra).lower().replace("-", " ").replace("/", " ")
    if any(b in title.lower().replace("-", " ") for b in BAD_WORDS):
        return False
    return any(w in t for w in ROLE_WORDS)


def epoch_date(v):
    if isinstance(v, (int, float)) and v > 1_000_000_000:
        return datetime.date.fromtimestamp(v).isoformat()
    return str(v or "")[:10]


CUR_OK = ("", "USD", "EUR", "GBP", "CAD", "AUD", "CHF")


def to_year(v, period="", currency=""):
    """Годовая сумма в долларах. Валюты вне списка не берём — цифра обманет."""
    if not v:
        return 0
    if (currency or "").upper() not in CUR_OK:
        return 0
    try:
        v = float(v)
    except Exception:
        return 0
    p = (period or "").lower()
    if "hour" in p or v < 500:
        v *= 2000
    elif "month" in p or v < 15000:
        v *= 12
    return int(v) if v <= 400000 else 0


# рядом с числом не должно быть этих слов — тогда это не зарплата, а выручка/бюджет/раунд
NOT_SALARY = ("arr", "revenue", "funding", "raised", "valuation", "gmv", "budget",
              "pipeline", "quota", "deal", "saved", "spend", "investment", "mrr",
              "portfolio", "assets", "grant", "loan", "sales of", "ad spend")
SALARY_HINT = ("salary", "compensation", "base pay", "pay range", "per year", "annually",
               "annual", "ote", "/yr", "per annum", "we offer", "range for this",
               "total comp", "earn")


def salary_from_text(text):
    """Годовая вилка из текста. Возвращает (сумма, точно ли это зарплата).
    «Точно» — рядом стоят слова про оплату; иначе цифру надо проверить глазами."""
    sure = plain = 0

    def take(v, pos):
        nonlocal sure, plain
        if not (40000 <= v <= 400000):
            return
        c = text[max(0, pos - 120):pos + 120].lower()
        if any(b in c for b in NOT_SALARY):
            return
        if any(h in c for h in SALARY_HINT):
            sure = max(sure, v)
        else:
            plain = max(plain, v)

    for m in RE_RANGE.finditer(text):
        for base, thou, kk in ((m.group(1), m.group(2), m.group(3)),
                               (m.group(4), m.group(5), m.group(6))):
            if not base:
                continue
            v = int(base) * 1000 + int(thou) if thou else int(base) * (1000 if kk else 1)
            take(v, m.start())
    for m in RE_ONE.finditer(text):
        v = int(m.group(1)) * 1000 + int(m.group(2)) if m.group(1) else int(m.group(3)) * 1000
        take(v, m.start())
    return (sure, True) if sure else (plain, False)


def add(out, src, title, company, where, sal, raw, posted, url, text, locs=None, sure=True):
    if sal < MIN_USD:
        return
    w = (where or "Worldwide").lower()
    out.append({
        "source": src,
        "title": title,
        "company": company,
        "where": where or "Worldwide",
        "russia_ok": (not locs) and ("worldwide" in w or "anywhere" in w or "russia" in w
                                     or "emea" in w or not w.strip()),
        "salary_year_usd": sal,
        "salary_raw": raw,
        "salary_sure": sure,
        "posted": posted,
        "url": url,
        "text": text[:7000],
    })


out = []

# ---------- 1. Himalayas (общий список + по разделам) ----------
print("Himalayas...")
seen_urls = set()
cats = ["", "Marketing", "Sales", "Operations", "Business", "Data", "Customer-Success",
        "Product", "Finance", "Project-Management", "E-commerce", "Growth-Marketing",
        "Digital-Marketing", "Supply-Chain", "Procurement", "Performance-Marketing",
        "Business-Operations", "Brand-Marketing", "Marketing-Manager", "Analytics"]
for cat in cats:
    for offset in (0, 100, 200):
        q = f"https://himalayas.app/jobs/api?limit=100&offset={offset}"
        if cat:
            q += f"&category={cat}"
        d = get(q)
        if not d or not d.get("jobs"):
            break
        for j in d["jobs"]:
            u = j.get("applicationLink") or j.get("guid", "")
            if u in seen_urls:
                continue
            seen_urls.add(u)
            title = j.get("title", "")
            if not role_ok(title, " ".join(j.get("categories") or [])):
                continue
            text = clean(j.get("description", ""))
            sal = to_year(j.get("maxSalary") or j.get("minSalary"), j.get("salaryPeriod"), j.get("currency") or "")
            sure = sal > 0
            if sal < MIN_USD:
                sal, sure = salary_from_text(text)
            locs = j.get("locationRestrictions") or []
            add(out, "himalayas", title, j.get("companyName", ""),
                ", ".join(locs) if locs else "Worldwide", sal,
                f"{j.get('minSalary') or ''}–{j.get('maxSalary') or ''} {j.get('currency') or 'USD'}",
                epoch_date(j.get("pubDate")), u, text, sure=sure,
                locs=[x for x in locs if x.lower() not in ("worldwide", "anywhere", "russia")])
    print(f"  раздел {cat or 'все'}: подходящих всего {len(out)}")

# ---------- 2. Remotive ----------
print("Remotive...")
d = get("https://remotive.com/api/remote-jobs?limit=600")
for j in (d or {}).get("jobs", []):
    title = j.get("title", "")
    if not role_ok(title, j.get("category", "")):
        continue
    text = clean(j.get("description", ""))
    raw = j.get("salary") or ""
    sal, sure = salary_from_text(raw)
    if not sal:
        sal, sure = salary_from_text(text)
    where = j.get("candidate_required_location", "")
    add(out, "remotive", title, j.get("company_name", ""), where, sal, raw,
        (j.get("publication_date") or "")[:10], j.get("url", ""), text, sure=sure,
        locs=None if ("worldwide" in where.lower() or "anywhere" in where.lower()) else [where])
print(f"  подходящих всего {len(out)}")

# ---------- 3. RemoteOK ----------
print("RemoteOK...")
d = get("https://remoteok.com/api")
for j in (d[1:] if isinstance(d, list) else []):
    title = j.get("position", "")
    if not role_ok(title, " ".join(j.get("tags") or [])):
        continue
    text = clean(j.get("description", ""))
    sal = to_year(j.get("salary_max") or j.get("salary_min"))
    sure = sal > 0
    if not sal:
        sal, sure = salary_from_text(text)
    where = j.get("location") or "Worldwide"
    add(out, "remoteok", title, j.get("company", ""), where, sal,
        f"{j.get('salary_min') or ''}–{j.get('salary_max') or ''} USD",
        (j.get("date") or "")[:10], j.get("url") or j.get("apply_url", ""), text, sure=sure,
        locs=None if ("worldwide" in where.lower() or "anywhere" in where.lower()) else [where])
print(f"  подходящих всего {len(out)}")

# ---------- 4. Jobicy ----------
print("Jobicy...")
for ind in ["", "marketing", "sales", "data-science", "supporting", "management",
            "business", "seo", "copywriting", "hr", "finance", "product"]:
    q = "https://jobicy.com/api/v2/remote-jobs?count=50"
    if ind:
        q += f"&industry={ind}"
    d = get(q)
    for j in (d or {}).get("jobs", []):
        title = j.get("jobTitle", "")
        if not role_ok(title, str(j.get("jobIndustry") or "")):
            continue
        text = clean(j.get("jobDescription", "")) or clean(j.get("jobExcerpt", ""))
        sal = to_year(j.get("salaryMax") or j.get("salaryMin"), j.get("salaryPeriod"),
                      j.get("salaryCurrency") or "")
        sure = sal > 0
        if not sal:
            sal, sure = salary_from_text(text)
        where = j.get("jobGeo", "") or "Worldwide"
        add(out, "jobicy", title, j.get("companyName", ""), where, sal,
            f"{j.get('salaryMin') or ''}–{j.get('salaryMax') or ''} {j.get('salaryCurrency') or ''}",
            (j.get("pubDate") or "")[:10], j.get("url", ""), text, sure=sure,
            locs=None if ("worldwide" in where.lower() or "anywhere" in where.lower()) else [where])
print(f"  подходящих всего {len(out)}")

# ---------- 5. Arbeitnow (Европа), несколько страниц ----------
print("Arbeitnow...")
for page in range(1, 9):
    d = get(f"https://www.arbeitnow.com/api/job-board-api?page={page}")
    if not d or not d.get("data"):
        break
    for j in d["data"]:
        title = j.get("title", "")
        if not role_ok(title, " ".join(j.get("tags") or [])):
            continue
        text = clean(j.get("description", ""))
        sal, sure = salary_from_text(text)
        where = j.get("location", "") or "Europe"
        add(out, "arbeitnow", title, j.get("company_name", ""), where, sal, "из текста",
            (j.get("created_at") and epoch_date(j["created_at"])) or "", j.get("url", ""), text,
            sure=sure, locs=[where])
print(f"  подходящих всего {len(out)}")

# ---------- 6. Working Nomads ----------
print("Working Nomads...")
d = get("https://www.workingnomads.com/api/exposed_jobs/")
for j in (d if isinstance(d, list) else []):
    title = j.get("title", "")
    if not role_ok(title, str(j.get("category_name") or "") + " " + str(j.get("tags") or "")):
        continue
    text = clean(j.get("description", ""))
    sal, sure = salary_from_text(text)
    where = j.get("location", "") or "Worldwide"
    glob = any(x in where.lower() for x in ("global", "worldwide", "anywhere"))
    add(out, "workingnomads", title, j.get("company_name", ""), where, sal, "из текста",
        (j.get("pub_date") or "")[:10], j.get("url", ""), text,
        sure=sure, locs=None if glob else [where])
print(f"  подходящих всего {len(out)}")

# ---------- 7. Remotive: поиск по словам (так выдача каждый раз другая) ----------
print("Remotive по словам...")
for slovo in ["ecommerce", "shopify", "amazon", "growth", "automation", "operations",
              "sourcing", "procurement", "marketing", "analytics", "supply chain"]:
    d = get(f"https://remotive.com/api/remote-jobs?limit=100&search={slovo.replace(' ', '%20')}")
    for j in (d or {}).get("jobs", []):
        title = j.get("title", "")
        if not role_ok(title, j.get("category", "")):
            continue
        text = clean(j.get("description", ""))
        sal, sure = salary_from_text(j.get("salary") or "")
        if not sal:
            sal, sure = salary_from_text(text)
        where = j.get("candidate_required_location", "")
        add(out, "remotive", title, j.get("company_name", ""), where, sal, j.get("salary") or "",
            (j.get("publication_date") or "")[:10], j.get("url", ""), text, sure=sure,
            locs=None if ("worldwide" in where.lower() or "anywhere" in where.lower()) else [where])
print(f"  подходящих всего {len(out)}")

# ---------- 8. Jobicy по США ----------
print("Jobicy США...")
for ind in ["", "marketing", "sales", "business", "management", "data-science", "supporting"]:
    q = "https://jobicy.com/api/v2/remote-jobs?count=50&geo=usa"
    if ind:
        q += f"&industry={ind}"
    d = get(q)
    for j in (d or {}).get("jobs", []):
        title = j.get("jobTitle", "")
        if not role_ok(title, str(j.get("jobIndustry") or "")):
            continue
        text = clean(j.get("jobDescription", "")) or clean(j.get("jobExcerpt", ""))
        sal = to_year(j.get("salaryMax") or j.get("salaryMin"), j.get("salaryPeriod"),
                      j.get("salaryCurrency") or "")
        sure = sal > 0
        if not sal:
            sal, sure = salary_from_text(text)
        where = j.get("jobGeo", "") or "USA"
        add(out, "jobicy", title, j.get("companyName", ""), where, sal,
            f"{j.get('salaryMin') or ''}–{j.get('salaryMax') or ''} {j.get('salaryCurrency') or ''}",
            (j.get("pubDate") or "")[:10], j.get("url", ""), text, sure=sure, locs=[where])
print(f"  подходящих всего {len(out)}")

# ---------- 9. The Muse (США), только нужные разделы ----------
print("The Muse...")
razdely = ["Marketing", "Business%20Operations", "Data%20and%20Analytics", "Sales",
           "Product%20Management", "Project%20Management"]
for r in razdely:
    for page in range(1, 13):
        d = get(f"https://www.themuse.com/api/public/jobs?category={r}&page={page}")
        if not d or not d.get("results"):
            break
        for j in d["results"]:
            title = j.get("name", "")
            # у The Muse раздел слишком широкий — требуем совпадение в самом названии
            if not role_ok(title):
                continue
            text = clean(j.get("contents", ""))
            sal, sure = salary_from_text(text)
            mesta = [x.get("name", "") for x in (j.get("locations") or [])]
            where = ", ".join(mesta[:3]) or "USA"
            add(out, "themuse", title, (j.get("company") or {}).get("name", ""), where, sal,
                "из текста", (j.get("publication_date") or "")[:10],
                (j.get("refs") or {}).get("landing_page", ""), text, sure=sure, locs=mesta or ["USA"])
    print(f"  раздел {r.replace('%20',' ')}: подходящих всего {len(out)}")

# ---------- дубли и итог ----------
seen, uniq = set(), []
for j in out:
    k = (j["company"].lower().strip(), re.sub(r"\W+", "", j["title"].lower())[:40])
    if k in seen:
        continue
    seen.add(k)
    uniq.append(j)

uniq.sort(key=lambda x: -x["salary_year_usd"])
name = f"vakansii_sbor_{datetime.date.today()}.json"
io.open(name, "w", encoding="utf-8").write(json.dumps(uniq, ensure_ascii=False, indent=1))
print(f"\nГотово: {len(uniq)} вакансий (из них из России можно {sum(1 for j in uniq if j['russia_ok'])}) → {name}")
for j in uniq:
    flag = ("RU-ok" if j["russia_ok"] else "     ") + ("" if j["salary_sure"] else " ?")
    print(f"  {j['salary_year_usd']:>7} $ {flag} {j['title'][:52]:54} | {j['company'][:20]:22} | {j['where'][:26]}")
