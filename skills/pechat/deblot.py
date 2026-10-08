"""Убрать с готовой страницы скана серые тени/кляксы и чёрные линии краёв листа.
Текст, печати, подписи, рамки таблиц не трогаются.
python deblot.py in.png out.png
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, dst = sys.argv[1], sys.argv[2]
a = np.asarray(Image.open(src).convert("L")).astype(np.float32)
H, W = a.shape
out = a.copy()

# 1) тени: область, где в среднем серо (<205), но почти нет чёрного (текста)
k = 4
sm = a[: H // k * k, : W // k * k].reshape(H // k, k, W // k, k).mean(axis=(1, 3))
mean = ndi.gaussian_filter(sm, 12)
blk = ndi.gaussian_filter((sm < 90).astype(np.float32), 12)
shadow_s = (mean < 205) & (blk < 0.10)
shadow_s = ndi.binary_opening(shadow_s, iterations=3)
# только крупные пятна, прилегающие к краю листа (печати и подписи внутри листа не трогаем)
lab_s, _ = ndi.label(shadow_s)
hs, ws = shadow_s.shape
keep_s = np.zeros_like(shadow_s)
for i, sl in enumerate(ndi.find_objects(lab_s), 1):
    m = lab_s[sl] == i
    ys, xs = sl
    at_edge = xs.start < ws * 0.12 or xs.stop > ws * 0.88 or ys.start < hs * 0.08 or ys.stop > hs * 0.92
    if m.sum() > 0.015 * hs * ws and at_edge:
        keep_s[sl] |= m
shadow_s = ndi.binary_dilation(keep_s, iterations=6)
shadow = np.kron(shadow_s, np.ones((k, k), bool))
shadow = np.pad(shadow, ((0, H - shadow.shape[0]), (0, W - shadow.shape[1])))
fine = ndi.gaussian_filter(a, 1.5)
keep = fine < 120                     # печатный текст внутри тени остаётся
out[shadow & ~keep] = 255
out[shadow & keep] = np.minimum(a[shadow & keep], 60)

# 2) прямые линии края листа: вертикальные у левого/правого края, горизонтальные у верха/низа
dark = out < 150
v = ndi.binary_closing(dark, structure=np.ones((25, 1)))
v = ndi.binary_opening(v, structure=np.ones((int(H * 0.08), 1)))
h = ndi.binary_closing(dark, structure=np.ones((1, 25)))
h = ndi.binary_opening(h, structure=np.ones((1, int(W * 0.25))))
bx, by = int(W * 0.10), int(H * 0.06)
vb = v.copy(); vb[:, bx:W - bx] = False
hb = h.copy(); hb[by:H - by, :] = False
# только тонкие линии (толщина <= 12 px): строки текста и рамки толще/иные
def thin_only(mask, vertical):
    """оставить только линии: толщина поперёк (медиана) <= 9 px; строка текста толще"""
    lab, _ = ndi.label(mask)
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        m = lab[sl] == i
        prof = m.sum(axis=1 if vertical else 0)
        prof = prof[prof > 0]
        if len(prof) == 0 or np.median(prof) > 9:
            mask[sl][m] = False
    return mask
vb = thin_only(vb, True); hb = thin_only(hb, False)
# не трогать рамки таблиц: вертикаль, которую пересекает длинная горизонталь внутри листа
h_in = ndi.binary_dilation(h, iterations=6)
lab, n = ndi.label(vb)
for i, sl in enumerate(ndi.find_objects(lab), 1):
    if (h_in[sl] & (lab[sl] == i)).sum() > 40:
        vb[sl][lab[sl] == i] = False
kill = ndi.binary_dilation(vb | hb, iterations=3) & (out < 230)
# где к линии вплотную подходит буква/штамп — линию в этом месте не трогаем
darkpix = out < 170
touch = ndi.binary_dilation(kill, iterations=4) & ~kill & darkpix
protect = ndi.binary_dilation(touch, iterations=8)
kill &= ~protect
out[kill] = 255

# 3) серая «крупа» (точки растра тени): мелкие и бледные пятнышки; точки и запятые текста тёмные — остаются
spk = out < 215
lab, n = ndi.label(spk)
if n:
    idx = np.arange(1, n + 1)
    area = ndi.sum(spk, lab, idx)
    mn = ndi.minimum(out, lab, idx)
    bad = np.zeros(n + 1, bool)
    bad[1:] = (area <= 40) & (mn > 95)
    out[bad[lab]] = 255

Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(dst)
print(f"{dst}: тень {shadow.mean():.1%}, линий {(vb | hb).sum()} px")
