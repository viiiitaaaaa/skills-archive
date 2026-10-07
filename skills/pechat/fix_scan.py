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
    # линии края листа: строки/столбцы у краёв (8%), почти сплошь тёмные
    dark = out < 128
    h, w = out.shape
    bh, bw = int(h * 0.08), int(w * 0.08)
    for y in [*range(bh), *range(h - bh, h)]:
        if dark[y].mean() > 0.4:
            out[max(y - 4, 0): y + 5] = 255
    for x in [*range(bw), *range(w - bw, w)]:
        if dark[:, x].mean() > 0.4:
            out[:, max(x - 4, 0): x + 5] = 255
    return Image.fromarray(out.astype(np.uint8))


def fix(img, dpi=300, rot180=False):
    g = ImageOps.grayscale(img)
    if rot180:
        g = g.rotate(180)
    a = np.asarray(g)
    k = 4
    small = a[::k, ::k] < 160
    small = clean_border(small)
    ang = find_angle(small)
    g = g.rotate(ang, resample=Image.BICUBIC, fillcolor=255, expand=False)
    a = np.asarray(g).copy()
    hh, ww = (a.shape[0] // k) * k, (a.shape[1] // k) * k
    raw = (a[:hh, :ww].reshape(hh // k, k, ww // k, k).min(axis=(1, 3)) < 170)
    small = clean_border(raw.copy())
    # закрасить белым только выкинутое у краёв (тени, полосы, загнутые углы); текст не трогаем
    junk = ndi.binary_dilation(raw & ~small, iterations=3) & ~ndi.binary_dilation(small, iterations=1)
    big = np.zeros(a.shape, bool)
    big[:hh, :ww] = np.kron(junk, np.ones((k, k), bool))
    a[big] = 255
    ys, xs = np.nonzero(small)
    W, H = round(A4_MM[0] / 25.4 * dpi), round(A4_MM[1] / 25.4 * dpi)
    page = Image.new("L", (W, H), 255)
    if len(xs) == 0:
        return page, ang
    pad = 40
    x0, x1 = max(xs.min() * k - pad, 0), min(xs.max() * k + pad, a.shape[1])
    y0, y1 = max(ys.min() * k - pad, 0), min(ys.max() * k + pad, a.shape[0])
    crop = Image.fromarray(a[y0:y1, x0:x1])
    m = int(dpi * 0.2)
    s = min(1.0, (W - 2 * m) / crop.width, (H - 2 * m) / crop.height)
    if s < 1:
        crop = crop.resize((int(crop.width * s), int(crop.height * s)), Image.LANCZOS)
        y0 = int(y0 * s)
    x = (W - crop.width) // 2
    y = min(max(y0, m), H - crop.height - m)
    page.paste(crop, (x, y))
    return page, ang


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
    print(f"{a.out}: наклон {ang:+.2f}°")
