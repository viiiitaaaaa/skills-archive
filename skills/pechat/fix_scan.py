"""Выравнивание скана: убрать наклон, тёмные края и тени, поставить ровно на лист A4.

python fix_scan.py <вход.png> <выход.png> [--rot180] [--dpi 300]
Угол наклона ищется по строкам текста (до ±5°). Тёмные полосы и пятна, касающиеся
края скана (тень края листа, загнутый угол), закрашиваются белым.
"""
import argparse
import numpy as np
from PIL import Image, ImageOps
from scipy import ndimage as ndi

A4_MM = (210, 297)


def find_angle(mask_small):
    def score(a):
        r = ndi.rotate(mask_small, a, reshape=False, order=0)
        return np.var(r.sum(axis=1))
    best = max(np.arange(-5, 5.01, 0.25), key=score)
    return max(np.arange(best - 0.3, best + 0.31, 0.05), key=score)


def clean_border(mask):
    """Убрать тёмные компоненты, касающиеся края, и длинные линии у краёв."""
    lab, n = ndi.label(ndi.binary_dilation(mask, iterations=2))
    if n:
        edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
        if edge:
            mask = mask & ~np.isin(lab, list(edge))
    h, w = mask.shape
    bw, bh = int(w * 0.07), int(h * 0.05)
    for sl in (np.s_[:, :bw], np.s_[:, w - bw:]):
        sub = mask[sl]
        sub[:, sub.mean(axis=0) > 0.2] = False
    for sl in (np.s_[:bh, :], np.s_[h - bh:, :]):
        sub = mask[sl]
        sub[sub.mean(axis=1) > 0.2, :] = False
    return mask


def clean_bg(page, white=175, black=95):
    """Выбелить фон: просвет текста с другой стороны, тени от заломов, неровная серость.
    Фон оценивается крупным «максимум-фильтром» (текст пропадает, остаётся бумага), делим на него,
    затем уровни: светлее white -> белое, темнее black -> чёрное."""
    a = np.asarray(page, dtype=np.float32)
    k = 8
    sm = a[::k, ::k]
    bg = ndi.gaussian_filter(ndi.grey_closing(sm, size=(9, 9)), 3)
    bg = np.kron(bg, np.ones((k, k), np.float32))[: a.shape[0], : a.shape[1]]
    pad = np.full(a.shape, 255, np.float32)
    pad[: bg.shape[0], : bg.shape[1]] = bg
    norm = np.clip(a / np.maximum(pad, 1) * 255, 0, 255)
    out = np.clip((norm - black) / (white - black) * 255, 0, 255)
    return Image.fromarray(out.astype(np.uint8))


EDGE = 0.015  # белим только кромку скана шириной 1,5% — там тень края листа, текста там нет


def fix(img, dpi=300, rot180=False):
    """Ничего из содержимого не обрезается и не стирается: только поворот, кромка скана и укладка на A4."""
    g = ImageOps.grayscale(img)
    if rot180:
        g = g.rotate(180)
    a = np.array(g)
    h, w = a.shape
    eh, ew = int(h * EDGE), int(w * EDGE)
    a[:eh], a[h - eh:], a[:, :ew], a[:, w - ew:] = 255, 255, 255, 255
    g = Image.fromarray(a)
    k = 4
    ang = find_angle(clean_border(a[::k, ::k] < 160))
    g = g.rotate(ang, resample=Image.BICUBIC, fillcolor=255, expand=True)
    a = np.asarray(g)
    hh, ww = (a.shape[0] // k) * k, (a.shape[1] // k) * k
    ink = a[:hh, :ww].reshape(hh // k, k, ww // k, k).min(axis=(1, 3)) < 200
    ink = ndi.binary_opening(ink, iterations=1) | (a[:hh:k, :ww:k] < 120)  # без одиночных точек пыли
    ys, xs = np.nonzero(ink)
    W, H = round(A4_MM[0] / 25.4 * dpi), round(A4_MM[1] / 25.4 * dpi)
    page = Image.new("L", (W, H), 255)
    if len(xs) == 0:
        return page, ang
    pad = 30
    x0, x1 = max(xs.min() * k - pad, 0), min(xs.max() * k + k + pad, a.shape[1])
    y0, y1 = max(ys.min() * k - pad, 0), min(ys.max() * k + k + pad, a.shape[0])
    crop = Image.fromarray(a[y0:y1, x0:x1])
    m = int(dpi * 0.15)
    s = min(1.0, (W - 2 * m) / crop.width, (H - 2 * m) / crop.height)
    if s < 1:
        crop = crop.resize((int(crop.width * s), int(crop.height * s)), Image.LANCZOS)
    x = (W - crop.width) // 2
    y = min(max(int(y0 * s), m), H - crop.height - m)
    page.paste(crop, (x, y))
    return page, ang


def ink_check(src, page, rot180=False):
    """Доля тёмных пикселей (текст), сохранившихся после обработки; должна быть ≥ 0.97."""
    a = np.asarray(ImageOps.grayscale(src))
    b = np.asarray(page)
    return (b < 110).sum() / max((a < 110).sum(), 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--rot180", action="store_true")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--white", type=int, default=175, help="светлее этого — в белое (ниже = агрессивнее)")
    ap.add_argument("--no-clean", action="store_true")
    a = ap.parse_args()
    page, ang = fix(Image.open(a.inp), a.dpi, a.rot180)
    if not a.no_clean:
        page = clean_bg(page, a.white)
    page.save(a.out)
    r = ink_check(Image.open(a.inp), page)
    print(f"{a.out}: наклон {ang:+.2f}°, текст сохранён {r:.0%}" + ("" if r >= 0.97 else "  ⚠ ПРОВЕРИТЬ — возможна потеря"))
