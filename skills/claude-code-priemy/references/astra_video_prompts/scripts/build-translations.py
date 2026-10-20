#!/usr/bin/env python3
"""Generate the localized READMEs from README.md.

Only editorial prose is translated. Every fenced code block — i.e. every
quoted prompt — is copied through byte-for-byte, because the repo's first
rule is that a prompt is quoted verbatim in the language it was published in.

How it works
------------
README.md is split into segments: fenced code (never touched), blank lines,
and "prose" runs (maximal runs of consecutive non-blank lines outside code).
Each prose run is looked up in the language module's BLOCKS dict; if it is
not there, the module's REPLACE pairs are applied to it instead (that is how
`**Author:**` and friends get localized without a dict entry per author).

Two tokens may appear in a translation:

    @@TOC@@        replaced by a table of contents built from the translated
                   H2 headings (so its anchors always match the headings)
    @@A3@@         replaced by the anchor of the `### 3` heading (the
                   FeatureReveal link in Quick Start points at it)

Run:
    python scripts/build-translations.py
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
FENCE = re.compile(r"^\s*```")
SWITCH_OPEN = "<!-- lang-switcher -->"
SWITCH_CLOSE = "<!-- /lang-switcher -->"

LANGS = [
    ("zh-CN", "中文"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("es", "Español"),
    ("fr", "Français"),
]

LINK_LABELS = {
    "en": "English",
    "zh-CN": "中文",
    "ja": "日本語",
    "ko": "한국어",
    "es": "Español",
    "fr": "Français",
}


def split_segments(text):
    """-> list of (kind, lines). kind in {'raw', 'prose', 'blank'}."""
    segs = []
    buf = []
    in_code = False

    def flush():
        if buf:
            segs.append(("prose", list(buf)))
            buf.clear()

    for ln in text.split("\n"):
        if FENCE.match(ln):
            flush()
            in_code = not in_code
            segs.append(("raw", [ln]))
            continue
        if in_code:
            segs.append(("raw", [ln]))
            continue
        if ln.strip() == "":
            flush()
            segs.append(("blank", [ln]))
            continue
        buf.append(ln)
    flush()
    return segs


def slug(heading):
    """GitHub's heading-anchor algorithm, near enough."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def is_plumbing(body):
    """Pure markup: badges, preview links, bare HTML tags, rules."""
    s = body.strip()
    if s in ("---", "***"):
        return True
    if s.startswith(("![", "[![", "<a href", "<img", "<table", "<p>", "<div")):
        return True
    if re.fullmatch(r"</?[a-zA-Z][^>]*>", s):
        return True
    return False


def load(lang):
    spec = importlib.util.spec_from_file_location(
        f"i18n_{lang}", I18N / f"{lang}.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def apply_replace(body, pairs):
    for src, dst in pairs:
        if src in body:
            body = body.replace(src, dst)
    return body


def build(lang, mod, segs, report):
    blocks = mod.BLOCKS
    replace = getattr(mod, "REPLACE", [])
    skip = getattr(mod, "SKIP", set())

    out = []
    for kind, lines in segs:
        if kind != "prose":
            out.append("\n".join(lines))
            continue
        body = "\n".join(lines)
        if body in blocks:
            out.append(blocks[body])
            continue
        if body in skip:
            out.append(body)
            continue
        if is_plumbing(body):
            out.append(body)
            continue
        new_body = apply_replace(body, replace)
        if new_body == body and re.search(r"[A-Za-z]{3,}", body):
            report.append((lang, body))
        out.append(new_body)

    text = "\n".join(out)

    # table of contents, built from the translated H2 headings
    h2 = re.findall(r"^## (.+)$", text, flags=re.M)
    toc = "\n".join(
        f"- [{h}](#{slug(h)})" for h in h2 if h != mod.TOC_TITLE
    )
    text = text.replace("@@TOC@@", toc)

    # anchor of the FeatureReveal heading
    m = re.search(r"^### 3[:：].*$", text, flags=re.M)
    if m:
        text = text.replace("@@A3@@", slug(m.group(0)[4:]))

    # language switcher + translator's note, right after the hero block
    switcher = SWITCH_OPEN + "\n" + mod.SWITCHER + "\n" + SWITCH_CLOSE
    text = re.sub(
        re.escape(SWITCH_OPEN) + r".*?" + re.escape(SWITCH_CLOSE) + r"\n*",
        "",
        text,
        flags=re.S,
    )
    block = switcher + "\n\n" + mod.NOTICE
    idx = text.find("</div>")
    if idx == -1:
        raise SystemExit("no </div> hero block found")
    end = text.index("\n", idx) + 1
    text = text[:end] + "\n" + block + "\n" + text[end:]
    return text


def main():
    src = (ROOT / "README.md").read_text(encoding="utf-8")
    # any switcher already in the source is stripped before we start
    src = re.sub(
        re.escape(SWITCH_OPEN) + r".*?" + re.escape(SWITCH_CLOSE) + r"\n*",
        "",
        src,
        flags=re.S,
    )
    report = []
    segs = split_segments(src)
    wanted = sys.argv[1:] or [code for code, _ in LANGS]
    for lang, _label in LANGS:
        if lang not in wanted:
            continue
        mod = load(lang)
        out = build(lang, mod, segs, report)
        # switcher for this language
        dest = ROOT / f"README.{lang}.md"
        dest.write_text(out, encoding="utf-8")
        print(f"{dest.name:<22} {len(out):>7} bytes")

    if report:
        print(f"\n{len(report)} unit(s) left untranslated:\n", file=sys.stderr)
        for lang, body in report:
            first = body.split("\n")[0][:90]
            print(f"  [{lang}] {first}", file=sys.stderr)
    else:
        print("\nall prose units covered")


if __name__ == "__main__":
    main()
