"""Скачивает текст уроков (Summary + Transcript) курсов academy.claude.com в папку out/academy/<course>/NN_<lesson>.md"""
import re, html, sys, pathlib, urllib.request, time

OUT = pathlib.Path(sys.argv[1])
COURSES = sys.argv[2:]
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    for _ in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode("utf8", "replace")
        except Exception as e:
            err = e
            time.sleep(2)
    raise err


def text(t):
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<(br|/p|/h\d|/li|/pre|/div)[^>]*>", "\n", t)
    t = re.sub(r"<h(\d)[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", t)
    t = re.sub(r"<li[^>]*>", "\n- ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


for c in COURSES:
    d = OUT / c
    d.mkdir(parents=True, exist_ok=True)
    page = get(f"https://academy.claude.com/courses/{c}")
    (d / "00_course.md").write_text(text(page), encoding="utf8")
    lessons = []
    for m in re.findall(rf'/courses/{re.escape(c)}/([a-z0-9-]+)', page):
        if m not in lessons and m != "complete":
            lessons.append(m)
    print(c, len(lessons), flush=True)
    for i, l in enumerate(lessons, 1):
        try:
            t = text(get(f"https://academy.claude.com/courses/{c}/{l}"))
            # отрезаем навигацию до заголовка урока
            (d / f"{i:02d}_{l}.md").write_text(t, encoding="utf8")
        except Exception as e:
            print("  fail", l, e, flush=True)
