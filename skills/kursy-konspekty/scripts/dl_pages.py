"""Скачивает список страниц (url -> текст) в папку. args: outdir url1 url2 ..."""
import re, html, sys, pathlib, urllib.request, ssl, time

OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}
ctx = ssl.create_default_context()


def get(url):
    err = None
    for _ in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60, context=ctx).read()
        except Exception as e:
            err = e; time.sleep(2)
    raise err


def text(t):
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<nav.*?</nav>", "", t, flags=re.S)
    t = re.sub(r"<(br|/p|/h\d|/li|/pre|/div|/tr)[^>]*>", "\n", t)
    t = re.sub(r"<h(\d)[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", t)
    t = re.sub(r"<li[^>]*>", "\n- ", t)
    t = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r"\2 (\1)", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


for i, url in enumerate(sys.argv[2:], 1):
    name = f"{i:02d}_" + re.sub(r"[^a-zA-Z0-9]+", "_", url.split("//", 1)[-1])[-70:]
    try:
        b = get(url)
        if url.lower().endswith(".pdf"):
            (OUT / (name + ".pdf")).write_bytes(b)
        elif url.endswith(".md") or "raw.githubusercontent" in url:
            (OUT / (name + ".md")).write_text(b.decode("utf8", "replace"), encoding="utf8")
        else:
            (OUT / (name + ".md")).write_text(url + "\n\n" + text(b.decode("utf8", "replace")), encoding="utf8")
        print("ok", url, flush=True)
    except Exception as e:
        print("FAIL", url, e, flush=True)
