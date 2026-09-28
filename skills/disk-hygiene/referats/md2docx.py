import re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

INLINE = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`)")


def add_runs(p, text):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            p.add_run(part[2:-2]).bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1])
            r.font.name = "Consolas"
        else:
            p.add_run(part)


def toc(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    for tag, txt in (("begin", None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ("separate", None), (None, "Оглавление обновится при открытии (F9)"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag); r._r.append(el)
        elif txt.startswith("TOC"):
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = txt; r._r.append(el)
        else:
            r2 = p.add_run(txt); r = p.add_run()


def convert(md_path, out_path):
    lines = open(md_path, encoding="utf-8").read().splitlines()
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    for s in doc.sections:
        s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.8)
    first_h1 = True
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if ln.startswith("```"):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            p = doc.add_paragraph(); r = p.add_run("\n".join(buf)); r.font.name = "Consolas"; r.font.size = Pt(9)
            i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m:
            lvl = len(m.group(1)); txt = m.group(2).strip()
            if lvl == 1:
                h = doc.add_heading(txt, 0)
                if first_h1:
                    first_h1 = False
                    pass
            else:
                doc.add_heading(txt, min(lvl - 1, 3))
            i += 1; continue
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                if not re.match(r"^\s*\|?\s*:?-{2,}", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            n = max(len(r) for r in rows)
            t = doc.add_table(rows=len(rows), cols=n); t.style = "Table Grid"
            for ri, row in enumerate(rows):
                for ci in range(n):
                    cell = t.cell(ri, ci); cell.text = ""
                    add_runs(cell.paragraphs[0], row[ci] if ci < len(row) else "")
                    if ri == 0:
                        for r in cell.paragraphs[0].runs: r.bold = True
            doc.add_paragraph()
            continue
        m = re.match(r"^(\s*)([-*•]|\d+[.)])\s+(.*)", ln)
        if m:
            indent = len(m.group(1)) // 2
            style = "List Number" if m.group(2)[0].isdigit() else "List Bullet"
            if indent >= 1:
                style += " 2"
            try:
                p = doc.add_paragraph(style=style)
            except KeyError:
                p = doc.add_paragraph(style="List Bullet")
            add_runs(p, m.group(3)); i += 1; continue
        if ln.startswith(">"):
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(1); add_runs(p, ln.lstrip("> ")); p.runs and setattr(p.runs[0], "italic", True)
            i += 1; continue
        if re.match(r"^-{3,}$|^\*{3,}$", ln):
            i += 1; continue
        # абзац: склеиваем подряд идущие строки
        buf = [ln]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\s*[-*•]\s|\s*\d+[.)]\s|\||```|>)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        add_runs(doc.add_paragraph(), " ".join(buf))
    # статичное оглавление (видно и в Google Диске): все ## после титула
    heads=[re.sub(r"\*\*","",l[3:].strip()) for l in lines if l.startswith("## ")]
    if heads:
        body=doc.element.body
        els=[]
        h=doc.add_heading("Оглавление",1); els.append(h._p)
        for n,t in enumerate(heads,1):
            p=doc.add_paragraph(f"{n}. {t}"); p.paragraph_format.space_after=Pt(0); els.append(p._p)
        for e in els: body.remove(e)
        for k,e in enumerate(els): body.insert(1+k,e)
    doc.save(out_path)


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
