"""Извлекает текст из всех документов папки в <work>/src/<путь с "\\"→"__">.txt и пишет _stat.tsv.
python extract_text.py "<учебная папка>" <рабочая папка>
docx читается из XML целиком (все w:t) — python-docx теряет пункты нумерованных списков (+2…20% текста)."""
import html, json, os, re, sys, zipfile

B, W = sys.argv[1], sys.argv[2]
O = os.path.join(W, "src"); os.makedirs(O, exist_ok=True)
NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(p):
    from lxml import etree
    x = etree.fromstring(zipfile.ZipFile(p).read("word/document.xml"))
    out = []
    for para in x.iter(NS + "p"):
        t = "".join(n.text or "" for n in para.iter(NS + "t"))
        if t.strip(): out.append(t)
    return "\n".join(out)


def rtf_text(p):
    s = open(p, encoding="cp1251", errors="ignore").read()
    s = re.sub(r"\\u(-?\d+)\??", lambda m: chr(int(m.group(1)) % 65536), s)
    s = re.sub(r"\\'([0-9a-f]{2})", lambda m: bytes([int(m.group(1), 16)]).decode("cp1251"), s)
    s = re.sub(r"\{\\\*[^{}]*\}|\\[a-z]+-?\d* ?", " ", s)
    return re.sub(r"[{}]", "", s)


def txt(p):
    e = p.lower().rsplit(".", 1)[-1]
    if e == "docx": return docx_text(p)
    if e == "pdf":
        from pypdf import PdfReader
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
    if e in ("md", "txt", "csv"): return open(p, encoding="utf-8", errors="ignore").read()
    if e in ("html", "htm"):
        s = open(p, encoding="utf-8", errors="ignore").read()
        s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
        s = re.sub(r"<br\s*/?>|</p>|</h\d>|</li>|</div>", "\n", s)
        return html.unescape(re.sub(r"<[^>]+>", " ", s))
    if e == "rtf": return rtf_text(p)
    if e == "ipynb":
        j = json.load(open(p, encoding="utf-8"))
        return "\n\n".join(("## MD\n" if c["cell_type"] == "markdown" else "## CODE\n") + "".join(c["source"]) for c in j["cells"])
    if e == "drawio":
        s = open(p, encoding="utf-8", errors="ignore").read()
        return "\n".join(html.unescape(re.sub(r"<[^>]+>", " ", html.unescape(v))).strip() for v in re.findall(r'value="([^"]*)"', s) if v.strip())
    if e == "pptx":
        z = zipfile.ZipFile(p)
        return "\n".join(" ".join(re.findall(r"<a:t>([^<]*)</a:t>", z.read(n).decode("utf-8")))
                         for n in sorted(x for x in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml", x)))
    if e == "fb2":
        s = open(p, encoding="utf-8", errors="ignore").read()
        return html.unescape(re.sub(r"<[^>]+>", "\n", re.sub(r"(?is)<binary.*?</binary>", "", s)))
    if e == "xlsx":
        import openpyxl
        wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
        return "\n".join(" | ".join(str(x) for x in r if x is not None) for ws in wb.worksheets for r in ws.iter_rows(values_only=True) if any(r))
    if e in ("gdoc", "gsheet"):
        return "GDOC — читать коннектором Google Drive (read_file_content) по id"
    return None


stat = []
for root, _, fs in os.walk(B):
    for f in fs:
        p = os.path.join(root, f); rel = os.path.relpath(p, B)
        if f.endswith((".cs", ".csproj", ".sln", ".http")): continue
        try: t = txt(p)
        except Exception as ex: t = f"ОШИБКА {ex}"
        if t is None: continue
        t = re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", t)).strip()
        open(os.path.join(O, rel.replace(os.sep, "__") + ".txt"), "w", encoding="utf-8").write(t)
        stat.append((rel, len(t)))
open(os.path.join(O, "_stat.tsv"), "w", encoding="utf-8").write("\n".join(f"{a}\t{b}" for a, b in sorted(stat)))
print(len(stat), "файлов, символов:", sum(b for _, b in stat))
for a, b in stat:
    if b < 200: print("  мало текста:", a, b)
