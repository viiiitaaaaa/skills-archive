"""Печать файла на принтер одной командой.

python print_file.py <файл> [--printer ИМЯ] [--pages 1,3-4] [--copies N]
python print_file.py --list            # показать принтеры

PDF и картинки печатаются напрямую; .html/.htm/.txt/.md — сначала
переводятся в PDF через Chrome без окна. Страница вписывается в лист по центру.
"""
import argparse, os, subprocess, sys, tempfile

DEFAULT_PRINTER = "RICOH SP 221SNw"  # лазерный A4; системный по умолчанию Xprinter — это этикетки
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
IMG = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tif", ".tiff", ".webp"}
VIA_CHROME = {".html", ".htm", ".txt", ".md", ".svg"}


def parse_pages(spec, total):
    if not spec:
        return list(range(total))
    out = []
    for part in spec.split(","):
        a, _, b = part.strip().partition("-")
        out += range(int(a) - 1, int(b or a))
    return [p for p in out if 0 <= p < total]


def to_pdf_via_chrome(path):
    pdf = os.path.join(tempfile.mkdtemp(), "page.pdf")
    url = "file:///" + os.path.abspath(path).replace("\\", "/")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", url], check=True, timeout=120,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return pdf


def images(path, pages):
    from PIL import Image
    ext = os.path.splitext(path)[1].lower()
    if ext in IMG:
        yield Image.open(path).convert("RGB")
        return
    import pymupdf
    doc = pymupdf.open(path)
    for i in parse_pages(pages, len(doc)):
        pix = doc[i].get_pixmap(dpi=300)
        yield Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--printer", default=DEFAULT_PRINTER)
    ap.add_argument("--pages")
    ap.add_argument("--copies", type=int, default=1)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    import win32print, win32ui
    from PIL import ImageWin
    if a.list or not a.file:
        for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS, None, 4):
            print(p["pPrinterName"])
        return

    src = a.file
    ext = os.path.splitext(src)[1].lower()
    if ext in VIA_CHROME:
        src = to_pdf_via_chrome(src)
    elif ext != ".pdf" and ext not in IMG:
        sys.exit(f"Не умею печатать {ext}: нужен PDF, картинка или html/txt")

    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(a.printer)
    pw, ph = hdc.GetDeviceCaps(8), hdc.GetDeviceCaps(10)
    hdc.StartDoc(os.path.basename(a.file))
    n = 0
    for _ in range(a.copies):
        for img in images(src, a.pages):
            s = min(pw / img.width, ph / img.height)
            w, h = int(img.width * s), int(img.height * s)
            x, y = (pw - w) // 2, (ph - h) // 2
            hdc.StartPage()
            ImageWin.Dib(img).draw(hdc.GetHandleOutput(), (x, y, x + w, y + h))
            hdc.EndPage()
            n += 1
    hdc.EndDoc()
    hdc.DeleteDC()
    print(f"Отправлено на «{a.printer}»: {n} стр.")


if __name__ == "__main__":
    main()
