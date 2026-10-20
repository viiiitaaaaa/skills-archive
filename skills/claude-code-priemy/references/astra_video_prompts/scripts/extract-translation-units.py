#!/usr/bin/env python3
"""List every translatable unit in README.md.

Units are maximal runs of consecutive non-blank lines outside fenced code
blocks. Fenced code blocks (i.e. every quoted prompt) are never emitted —
the prompt is quoted verbatim in every translation, by repo rule.

Usage:
    python scripts/extract-translation-units.py README.md
"""
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^\s*```")


def split_units(text):
    """Yield (kind, line_no, body). kind is 'code' or 'prose'."""
    lines = text.split("\n")
    in_code = False
    buf = []
    start = 1

    def flush():
        nonlocal buf
        if buf:
            body = "\n".join(buf)
            buf = []
            return body
        return None

    for i, ln in enumerate(lines, start=1):
        if FENCE.match(ln):
            in_code = not in_code
            if in_code:
                body = flush()
                if body:
                    yield ("prose", start, body)
            continue
        if in_code:
            continue
        if ln.strip() == "":
            body = flush()
            if body:
                yield ("prose", start, body)
            continue
        if not buf:
            start = i
        buf.append(ln)
    body = flush()
    if body:
        yield ("prose", start, body)


def translatable(body):
    """A unit needs translation if it carries prose we authored."""
    if body.strip() in ("---", "***"):
        return False
    # strip media/html/link plumbing, then see if prose is left
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"(https?://\S+|shields\.io\S*)", "", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", "", s)
    return len(s) >= 2


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
    text = src.read_text(encoding="utf-8")
    n = 0
    skipped = 0
    for kind, line_no, body in split_units(text):
        if kind == "code":
            continue
        if not translatable(body):
            skipped += 1
            continue
        n += 1
        print(f"### [{n}] L{line_no}")
        print(body)
        print()
    print(f"# {n} translatable units, {skipped} skipped", file=sys.stderr)


if __name__ == "__main__":
    main()
