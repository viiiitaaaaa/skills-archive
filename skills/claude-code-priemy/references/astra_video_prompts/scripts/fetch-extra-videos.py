#!/usr/bin/env python3
"""Download source clips that are NOT hosted on X.

`fetch-source-videos.py` handles the X posts via the syndication endpoint.
This script covers the other two shapes we found:

  1. Project READMEs that embed a video as a GitHub user-attachment
     (`https://github.com/user-attachments/assets/<id>`). These are plain
     MP4s, publicly readable, and can be fetched with a Range request, so
     they resume cleanly if the connection drops.
  2. YouTube demos (`yt-dlp`). Needs a JS runtime for YouTube's player API
     (`--js-runtimes node:<path>`) and working access to `*.googlevideo.com`.

Writes `<raw_dir>/manifest.json` in the same shape
`build-webp-previews.py` consumes, so the two fetchers can feed one build.

Usage: fetch-extra-videos.py [raw_dir]
"""
import json, os, subprocess, sys, time

RAW = sys.argv[1] if len(sys.argv) > 1 else r"C:\tmp\astra_raw_extra"
os.makedirs(RAW, exist_ok=True)

UA = "Mozilla/5.0"

# --- GitHub user-attachment MP4s -------------------------------------------
# (slug, asset_id, note, link_used_in_readme)
GITHUB = [
    ("shotcraft-gallery-intro", "cba2df8a-4b2e-4247-bace-d0b1dea9c2bd",
     "video-shotcraft README > Showcase (38s gallery intro)", None),
    ("shotcraft-ink-press", "4cf5af51-98f3-4af2-8ab2-7267f470513d",
     "video-shotcraft README > Ink Press promo template (36s)", None),
    ("montage-launch-film", "e7257684-72e1-47a3-a9e6-0c94b801dc8f",
     "simplexlabs/montage README demo video", None),
]

# --- YouTube demos ----------------------------------------------------------
# (slug, video_id, note)   -- link_used_in_readme is the watch URL
YOUTUBE = [
    ("astra-made-this-video", "dT5-x3u5nCg",
     "Nate Herk - idea -> uploadable YouTube video (main source)"),
    ("event-sizzle-reel", "QhmhUgccaS0",
     "Nate Herk - 1min sizzle reel from 152GB of event footage"),
]


def asset_url(asset_id):
    return f"https://github.com/user-attachments/assets/{asset_id}"


def curl_download(url, dest, expected=None, tries=8):
    """Resume until the file reaches the server's advertised length."""
    for i in range(tries):
        cmd = ["curl", "-sL", "-m", "240", "-C", "-",
               "-H", f"User-Agent: {UA}",
               "-H", "Accept: video/mp4,video/*,*/*",
               url, "-o", dest]
        subprocess.run(cmd, check=False)
        size = os.path.getsize(dest) if os.path.exists(dest) else 0
        print(f"    try {i+1}: {size/1048576:.2f} MB"
              + (f" / {expected/1048576:.2f} MB" if expected else ""))
        if expected and size >= expected:
            return size
        if not expected and size:
            return size
        time.sleep(2)
    return os.path.getsize(dest) if os.path.exists(dest) else 0


def remote_size(url):
    out = subprocess.run(
        ["curl", "-sL", "-m", "60", "-H", f"User-Agent: {UA}",
         "-H", "Range: bytes=0-0", "-D", "-", url, "-o",
         os.devnull], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.lower().startswith("content-range"):
            return int(line.rsplit("/", 1)[-1])
    return None


def duration_s(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of",
                              "default=nw=1:nk=1", path],
                             capture_output=True, text=True).stdout.strip()
        return round(float(out), 2)
    except Exception:
        return 0.0


manifest = []
manifest_path = os.path.join(RAW, "manifest.json")
if os.path.exists(manifest_path):          # merge, so a second run is additive
    manifest = json.load(open(manifest_path, encoding="utf-8"))
have = {m["slug"] for m in manifest}


def record(slug, local, dur, source):
    global manifest
    manifest = [m for m in manifest if m["slug"] != slug]
    manifest.append({"slug": slug, "local": local,
                     "duration_s": dur, "source": source})


for slug, asset_id, note, _link in GITHUB:
    url = asset_url(asset_id)
    dest = os.path.join(RAW, slug + ".mp4")
    total = remote_size(url)
    print(f"[git] {slug}  ({note})")
    size = curl_download(url, dest, expected=total)
    if not total or size < total:
        print(f"  [WARN] {slug}: got {size} B, expected {total} B — truncated")
        continue
    record(slug, os.path.basename(dest), duration_s(dest), url)
    print(f"  [ok] {slug:<24} {size/1048576:>6.2f} MB")

for slug, vid, note in YOUTUBE:
    url = f"https://www.youtube.com/watch?v={vid}"
    dest = os.path.join(RAW, slug + ".mp4")
    print(f"[yt ] {slug}  ({note})")
    # 360p video-only track: previews are silent, and it keeps the download small
    r = subprocess.run(
        ["yt-dlp", "--js-runtimes", f"node:{os.environ.get('NODE_BIN','node')}",
         "-f", "134", "--no-playlist", "-o", dest, url],
        capture_output=True, text=True)
    if not os.path.exists(dest) or os.path.getsize(dest) < 100_000:
        print(f"  [SKIP] {slug}: {r.stdout.strip().splitlines()[-1:] }")
        continue
    record(slug, os.path.basename(dest), duration_s(dest), url)
    print(f"  [ok] {slug:<24} {os.path.getsize(dest)/1048576:>6.2f} MB")

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print(f"\nmanifest: {len(manifest)} entries -> {manifest_path}")
