# -*- coding: utf-8 -*-
"""docx → PDF без Word: python-docx → HTML (A4, поля, шрифт, выравнивание, отступы) → Chrome headless.
Запуск: python _docx_v_pdf.py <файл.docx> [<выход.pdf>]"""
import html, os, subprocess, sys, tempfile
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH as A
from docx.shared import Emu

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
mm = lambda emu: Emu(emu).mm if emu is not None else None


def para_css(p, default_size):
    pf = p.paragraph_format
    css = []
    al = p.alignment if p.alignment is not None else (p.style.paragraph_format.alignment)
    css.append({A.CENTER: "text-align:center", A.RIGHT: "text-align:right",
                A.JUSTIFY: "text-align:justify"}.get(al, "text-align:left"))
    for k, v in (("margin-left", pf.left_indent), ("margin-right", pf.right_indent), ("text-indent", pf.first_line_indent)):
        if v is not None:
            css.append(f"{k}:{mm(v):.1f}mm")
    css.append(f"margin-top:{(pf.space_before.pt if pf.space_before else 0):.1f}pt")
    css.append(f"margin-bottom:{(pf.space_after.pt if pf.space_after else 0):.1f}pt")
    ls = pf.line_spacing
    if isinstance(ls, float):
        css.append(f"line-height:{ls:.2f}")
    if pf.page_break_before:  # «с новой страницы» в Word — так же и в PDF (29.10.2026: приложение с подписью на второй лист)
        css.append("break-before:page")
    return ";".join(css)


def run_html(r, default_size):
    t = html.escape(r.text).replace("\t", "&emsp;&emsp;")
    st = []
    if r.font.size:
        st.append(f"font-size:{r.font.size.pt}pt")
    if r.bold: t = f"<b>{t}</b>"
    if r.italic: t = f"<i>{t}</i>"
    if r.underline: t = f"<u>{t}</u>"
    return f'<span style="{";".join(st)}">{t}</span>' if st else t


def convert(src, dst):
    d = docx.Document(src)
    s = d.sections[0]
    # Стиля «Normal» может не быть — тогда берём размер из первого куска текста с размером
    try:
        font = d.styles["Normal"].font; size = font.size.pt if font.size else None; name = font.name
    except KeyError:
        size = name = None
    rr = [r for p in d.paragraphs for r in p.runs]
    size = size or next((r.font.size.pt for r in rr if r.font.size), 12)
    name = name or next((r.font.name for r in rr if r.font.name), None) or "Times New Roman"
    body = []
    for p in d.paragraphs:
        inner = "".join(run_html(r, size) for r in p.runs) or "&nbsp;"
        body.append(f'<p style="{para_css(p, size)}">{inner}</p>')
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size:A4; margin:{mm(s.top_margin):.1f}mm {mm(s.right_margin):.1f}mm {mm(s.bottom_margin):.1f}mm {mm(s.left_margin):.1f}mm; }}
body {{ font-family:'{name}','Times New Roman',serif; font-size:{size}pt; line-height:1.15; margin:0; }}
p {{ margin:0; orphans:2; widows:2; }}
</style></head><body>{''.join(body)}</body></html>"""
    tmp = os.path.join(tempfile.gettempdir(), "docx2pdf_tmp.html")
    open(tmp, "w", encoding="utf-8").write(page)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={dst}", "file:///" + tmp.replace("\\", "/")], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    return dst


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
    print(convert(os.path.abspath(src), os.path.abspath(dst)))
