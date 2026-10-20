#!/usr/bin/env python3
"""Build small looping animated-WebP previews from the downloaded source videos.

Each preview is a short excerpt (a few seconds) so it reads as a *reference
clip* pointing back at the original post — not a redistribution of the full
video. Output goes to <repo>/media/<slug>.webp.

Usage: build-webp-previews.py [raw_dir] [out_dir] [ffmpeg_exe]
"""
import json, os, subprocess, sys

RAW = sys.argv[1] if len(sys.argv) > 1 else r"C:\tmp\astra_raw"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")
FF = sys.argv[3] if len(sys.argv) > 3 else "ffmpeg"

WIDTH = 440           # matches the `width="440"` used in the README markup
FPS = 13
QUALITY = 62          # libwebp quality (0-100, higher = better/larger)

# Per-slug (start_seconds, duration_seconds). Defaults suit ~15s clips.
DEFAULT_TRIM = (1.0, 3.5)
TRIM = {
    "t-cells":            (40.0, 4.0),   # 342s explainer — mid-section, denser motion
    "camera-comps-30":    (6.0, 4.0),    # 37.5s grid walkthrough
    "side-scroll-chase":  (3.0, 4.0),    # 23.7s side-scroller
    "adcar-tv":           (2.0, 4.0),    # 44.2s launch film
    "atomik-launch":      (5.0, 4.0),    # 33s launch film
    "game-cm":            (3.0, 4.0),    # 30s game CM
    "brandnewstudy-promo": (4.0, 4.0),
    "sprint-control":     (1.0, 3.5),    # 10s only
    "ios-app-launch":     (2.0, 4.0),
    # --- non-X sources (see fetch-extra-videos.py) ---
    "shotcraft-gallery-intro": (21.5, 4.0),  # 38s: shot cards orbit / cascade
    "shotcraft-ink-press":     (9.0, 4.0),   # 36s: headline -> rotating paper stack
    "montage-launch-film":     (33.0, 4.0),  # 52s: check-marks fill the window grid
}

os.makedirs(OUT, exist_ok=True)

with open(os.path.join(RAW, "manifest.json"), encoding="utf-8") as f:
    manifest = json.load(f)

report = []
for m in manifest:
    slug = m["slug"]
    src = os.path.join(RAW, m["local"])
    dst = os.path.join(OUT, slug + ".webp")
    start, dur = TRIM.get(slug, DEFAULT_TRIM)

    # never read past the end of a short clip
    dur = min(dur, max(m["duration_s"] - start, 1.0))
    if m["duration_s"] < start + dur:
        start = max(m["duration_s"] - dur - 0.2, 0)

    vf = f"fps={FPS},scale={WIDTH}:-2:flags=lanczos"
    cmd = [FF, "-hide_banner", "-loglevel", "error", "-y",
           "-ss", str(start), "-t", str(dur), "-i", src,
           "-vf", vf, "-c:v", "libwebp_anim", "-lossless", "0",
           "-q:v", str(QUALITY), "-loop", "0", "-an", dst]
    subprocess.run(cmd, check=True)
    kb = os.path.getsize(dst) / 1024
    report.append((slug, kb, start, dur))
    print(f"[ok] {slug:<22} {kb:>7.0f} KB   trim {start:g}s +{dur:g}s")

total = sum(r[1] for r in report) / 1024
print(f"\n{len(report)} previews, total {total:.1f} MB -> {OUT}")
