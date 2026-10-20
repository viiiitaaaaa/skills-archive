#!/usr/bin/env python3
"""Download source videos for the awesome-astra-video-prompts README.

Uses the public, login-free syndication endpoint to resolve mp4 variants,
then picks the best variant with width <= 1280 and downloads it.

Outputs:
  <raw_dir>/<slug>.mp4
  <raw_dir>/manifest.json   (slug, id, handle, post url, duration, source mp4)
"""
import json, os, ssl, sys, time, urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

RAW = sys.argv[1] if len(sys.argv) > 1 else "/tmp/astra_raw"
os.makedirs(RAW, exist_ok=True)

ENTRIES = [
    ("parkour-previz",      "2096096560690209130"),  # Kashiko_AIart
    ("adcar-tv",            "2096258259459964963"),  # d4m1n
    ("witch-first-flight",  "2095873015007592679"),  # Mayz1169
    ("t-cells",             "2095659170661904804"),  # DeryaTR_
    ("atomik-launch",       "2096555742597988400"),  # makwanatejas170
    ("game-cm",             "2096813471463882947"),  # guuchacha149182
    ("changelog-video",     "2096844989900914865"),  # leon7hao
    ("brandnewstudy-promo", "2096835902047932521"),  # NickYang130
    ("ios-app-launch",      "2096311328600113222"),  # stoufax
    ("seedance-handoff",    "2096871096759030114"),  # Naonekozamurai
    ("sprint-control",      "2094182215894831283"),  # Kashiko_AIart
    ("side-scroll-chase",   "2093692302745383041"),  # Kashiko_AIart
    ("camera-comps-30",     "2093575541916061984"),  # Kashiko_AIart
    ("chanbara",            "2096533732547264921"),  # Kashiko_AIart
    ("physics-motion",      "2096830622341976467"),  # paojiaofty
]

UA = {"User-Agent": "Mozilla/5.0"}


def fetch_json(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return json.load(urllib.request.urlopen(req, timeout=40))
        except Exception as e:  # transient proxy 502s happen
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def variant_width(src):
    try:
        return int(src.split("/")[-2].split("x")[0])
    except Exception:
        return 0


def download(url, dest, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as f:
                while True:
                    chunk = r.read(1 << 16)
                    if not chunk:
                        break
                    f.write(chunk)
            return os.path.getsize(dest)
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


manifest = []
for slug, tid in ENTRIES:
    d = fetch_json(f"https://cdn.syndication.twimg.com/tweet-result?id={tid}&token=a")
    handle = (d.get("user") or {}).get("screen_name", "?")
    post = f"https://x.com/{handle}/status/{tid}"
    v = d.get("video")
    if not v:
        print(f"[skip] {slug}: no video")
        continue

    cands = [x for x in v.get("variants", []) if x.get("type") == "video/mp4"]
    if not cands:
        print(f"[skip] {slug}: no mp4 variant")
        continue
    capped = [c for c in cands if variant_width(c["src"]) <= 1280] or cands
    capped.sort(key=lambda c: variant_width(c["src"]))
    pick = capped[-1]

    dest = os.path.join(RAW, slug + ".mp4")
    size = download(pick["src"], dest)
    dur = round((v.get("durationMs") or 0) / 1000, 1)
    poster = v.get("poster", "")
    print(f"[ok] {slug:<20} @{handle:<17} {dur:>6}s  {size/1048576:>6.2f}MB  {variant_width(pick['src'])}w")

    manifest.append({
        "slug": slug, "id": tid, "handle": handle, "post": post,
        "duration_s": dur, "poster": poster, "local": os.path.basename(dest),
    })

with open(os.path.join(RAW, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print(f"\ndone: {len(manifest)}/{len(ENTRIES)} downloaded -> {RAW}")
