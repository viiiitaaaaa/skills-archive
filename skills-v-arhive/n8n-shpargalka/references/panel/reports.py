"""Отчёты панели в файлы: CSV и Excel без сторонних библиотек.

n8n присылает готовые строки на POST /api/report, панель складывает их в
data/reports/<имя>-<дата>.csv и .xlsx и отдаёт ссылки на скачивание.
Excel собирается вручную (это zip с XML внутри), чтобы не ставить openpyxl.
"""
from __future__ import annotations

import csv
import io
import re
import zipfile
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

SAFE = re.compile(r"[^a-z0-9\-]+")


def safe_name(name: str) -> str:
    name = SAFE.sub("-", str(name).lower()).strip("-")
    return name or "report"


def _col_letter(i: int) -> str:
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def _xlsx_bytes(columns: list[str], rows: list[dict], sheet: str = "Отчёт") -> bytes:
    def cell(ref: str, v) -> str:
        if v is None or v == "":
            return ""
        if isinstance(v, bool):
            return f'<c r="{ref}" t="b"><v>{int(v)}</v></c>'
        if isinstance(v, (int, float)):
            return f'<c r="{ref}"><v>{v}</v></c>'
        if isinstance(v, (list, tuple)):
            v = ", ".join(str(x) for x in v)
        text = escape(str(v))
        return f'<c r="{ref}" t="inlineStr"><is><t xml:space="preserve">{text}</t></is></c>'

    lines = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
             '<cols>' + "".join(f'<col min="{i+1}" max="{i+1}" width="{28 if i else 40}" customWidth="1"/>'
                                for i in range(len(columns))) + '</cols>',
             '<sheetData>']
    lines.append('<row r="1">' + "".join(cell(f"{_col_letter(i)}1", c) for i, c in enumerate(columns)) + '</row>')
    for r_i, row in enumerate(rows, start=2):
        lines.append(f'<row r="{r_i}">' + "".join(
            cell(f"{_col_letter(c_i)}{r_i}", row.get(c)) for c_i, c in enumerate(columns)) + '</row>')
    lines.append('</sheetData>')
    if columns:
        lines.append(f'<autoFilter ref="A1:{_col_letter(len(columns)-1)}{max(1, len(rows)+1)}"/>')
    lines.append('</worksheet>')
    sheet_xml = "\n".join(lines)

    wb = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
          f'<sheets><sheet name="{escape(sheet)}" sheetId="1" r:id="rId1"/></sheets></workbook>')
    wb_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
               '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
               '</Relationships>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '</Relationships>')
    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
             '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
             '</Types>')
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", wb)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)
    return buf.getvalue()


def _csv_bytes(columns: list[str], rows: list[dict]) -> bytes:
    out = io.StringIO()
    w = csv.writer(out, delimiter=";", lineterminator="\r\n")   # «;» — так Excel в русской/польской локали открывает без мастера импорта
    w.writerow(columns)
    for r in rows:
        w.writerow(["" if r.get(c) is None else
                    (", ".join(map(str, r[c])) if isinstance(r.get(c), (list, tuple)) else r[c]) for c in columns])
    return ("﻿" + out.getvalue()).encode("utf-8")


def write_report(folder: Path, name: str, rows: list[dict], columns: list[str] | None = None,
                 stamp: datetime | None = None) -> dict:
    """Пишет CSV и XLSX, возвращает имена файлов и число строк."""
    folder.mkdir(parents=True, exist_ok=True)
    stamp = stamp or datetime.now()
    base = f"{safe_name(name)}-{stamp:%Y-%m-%d}"
    if not columns:
        columns = []
        for r in rows:
            for k in r:
                if k not in columns:
                    columns.append(k)
    (folder / f"{base}.csv").write_bytes(_csv_bytes(columns, rows))
    (folder / f"{base}.xlsx").write_bytes(_xlsx_bytes(columns, rows))
    return {"base": base, "csv": f"{base}.csv", "xlsx": f"{base}.xlsx", "rows": len(rows)}


def list_reports(folder: Path, limit: int = 30) -> list[dict]:
    if not folder.exists():
        return []
    files = sorted(folder.glob("*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    out = []
    for p in files:
        csv_p = p.with_suffix(".csv")
        out.append({"name": p.stem, "xlsx": p.name, "csv": csv_p.name if csv_p.exists() else None,
                    "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
                    "size_kb": round(p.stat().st_size / 1024, 1)})
    return out
