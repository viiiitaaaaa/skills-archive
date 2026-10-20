#!/usr/bin/env python3
"""Insert animated-WebP previews + video links into README.md.

Safe to re-run: every rule is skipped when its slug already appears in the
target file, so patching a README that already has some previews only adds
the missing ones.

Usage: patch-readme-previews.py <README.md>
"""
import io, re, sys

PATH = sys.argv[1]

W = 440


def preview(slug, post, alt):
    return (
        f'<a href="{post}"><img src="media/{slug}.webp" width="{W}" alt="{alt}"></a>\n'
        f'\n'
        f'🎬 **[Watch the full video \u2192]({post})**'
    )


def row(*blocks):
    """Stack previews vertically.

    NOTE: do NOT wrap these in an HTML <table> — GitHub's markdown parser
    suppresses markdown inside raw HTML blocks, so the `[link](url)` caption
    would render as literal text. Stacking keeps each preview a normal block.
    """
    return "\n\n".join(blocks)


# (anchor substring, kind, payload)
#   kind 'after'   -> insert block after the anchor line
#   kind 'heading' -> find heading, then insert after the badge line that follows
RULES = [
    # ---- Featured ----
    ("### 1: High-Speed Parkour Motion Previz", "heading",
     preview("parkour-previz", "https://x.com/Kashiko_AIart/status/2096096560690209130",
             "High-Speed Parkour Motion Previz \u2014 Remotion motion previz demo")),
    ("### 2: AdCar TV \u2014 In-Repo One-Shot Launch Video", "heading",
     preview("adcar-tv", "https://x.com/d4m1n/status/2096258259459964963",
             "AdCar TV \u2014 44s one-shot launch video")),
    ("### 4: Witch's First Flight \u2014 15s Generated Shot Script", "heading",
     preview("witch-first-flight", "https://x.com/Mayz1169/status/2095873015007592679",
             "Witch's First Flight \u2014 15s generated shot")),
    ("### 5: T Cells \u2014 One Sentence, Five Minutes", "heading",
     preview("t-cells", "https://x.com/DeryaTR_/status/2095659170661904804",
             "T Cells \u2014 5-minute explainer, one-line brief")),

    # ---- Product Launch & Marketing ----
    ("### Atomik \u2014 33-Second Launch Film", "heading",
     preview("atomik-launch", "https://x.com/makwanatejas170/status/2096555742597988400",
             "Atomik \u2014 33s launch film")),

    # ---- Motion Previz -> Generative ----
    ("### Seedance Handoff Instruction", "heading",
     preview("seedance-handoff", "https://x.com/Naonekozamurai/status/2096871096759030114",
             "Remotion previz control MP4 handed to Seedance 2.5")),
    ("### Ultra-High-Speed Sprint Control MP4", "heading",
     preview("sprint-control", "https://x.com/Kashiko_AIart/status/2094182215894831283",
             "Ultra-high-speed sprint control MP4")),
    ("### Side-Scrolling Chase, with a Frame Table", "heading",
     preview("side-scroll-chase", "https://x.com/Kashiko_AIart/status/2093692302745383041",
             "Side-scrolling chase with a frame table")),
    ("### 30 Camera Compositions \u2014 Reference Sheet Generator", "heading",
     preview("camera-comps-30", "https://x.com/Kashiko_AIart/status/2093575541916061984",
             "30 camera compositions reference sheet")),

    # ---- Short briefs block: three clips inline ----
    ("**Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",
     "after",
     preview("game-cm", "https://x.com/guuchacha149182/status/2096813471463882947",
             "Game CM \u2014 one-prompt Remotion promo")),
    ("author reported the result was noticeably weaker", "after",
     preview("changelog-video", "https://x.com/leon7hao/status/2096844989900914865",
             "Changelog video \u2014 no skill installed, weaker result")),
    ("Results posted without the prompt:", "after",
     row("**@NickYang130 \u2014 BrandNewStudy marketing video, one-shot**",
         preview("brandnewstudy-promo", "https://x.com/NickYang130/status/2096835902047932521",
                 "BrandNewStudy marketing video, one-shot"),
         "**@stoufax \u2014 iOS app launch, Remotion + ElevenLabs**",
         preview("ios-app-launch", "https://x.com/stoufax/status/2096311328600113222",
                 "iOS app launch \u2014 Remotion + ElevenLabs"))),

    # ---- chanbara, mentioned as a footnote to the 30-camera entry ----
    ("3) fine motion controlled by prompt.", "after",
     preview("chanbara", "https://x.com/Kashiko_AIart/status/2096533732547264921",
             "Chanbara sword-fight motion previz")),

    # ---- Known but Unpublished: the physics-motion demo does exist on X ----
    ("| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |",
     "after",
     "**The physics / soft-body motion demo itself is public** (the skill is not):\n"
     "\n"
     + preview("physics-motion", "https://x.com/paojiaofty/status/2096830622341976467",
               "Physics / soft-body motion \u2014 4K60 direct output")),

    # ---- Non-X sources: project READMEs that embed the demo themselves ----
    ("### video-shotcraft \u2014 Cinematic Product Video Skill", "heading",
     row(preview("shotcraft-gallery-intro",
                 "https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd",
                 "video-shotcraft \u2014 38s gallery intro, produced with the skill"),
         preview("shotcraft-ink-press",
                 "https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d",
                 "Ink Press \u2014 the 36s promo template shipped with the skill"))),
    ("**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage]",
     "after",
     preview("montage-launch-film",
             "https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f",
             "Montage \u2014 launch film rendered by the agent")),
]

# (old, new, skip_if_already_present)
#   skip_if_already_present=None -> always apply (delta edits below)
SCALARS = [
    ("![Full text](https://img.shields.io/badge/full%20text-17-success)",
     "![Full text](https://img.shields.io/badge/full%20text-17-success)\n"
     "![Previews](https://img.shields.io/badge/previews-18-blueviolet)",
     "previews-"),

    ("| **Languages** | EN \u00b7 JA \u00b7 ZH |",
     "| **Languages** | EN \u00b7 JA \u00b7 ZH |\n"
     "| **Preview clips** | 18 (animated WebP, `media/`) |",
     "**Preview clips**"),

    # Note right after the copyright notice
    ("we will remove it promptly.",
     "we will remove it promptly.\n"
     "\n"
     "> \U0001f3ac **About the previews**: the animated clips under `media/` are short, "
     "low-resolution excerpts of each author's *published demo*, included only as a "
     "reference next to the prompt and always linked back to the original post. They are "
     "excerpts \u2014 not redistributions of the full videos. If you are the author and want "
     "yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed "
     "without argument.",
     "**About the previews**"),

    # --- running totals (keep in sync when a batch is added) ---
    ("previews-15-blueviolet", "previews-18-blueviolet", None),
    ("| **Preview clips** | 15 (animated WebP, `media/`) |",
     "| **Preview clips** | 18 (animated WebP, `media/`) |", None),
]

SLUG_RE = re.compile(r"media/([a-z0-9-]+)\.webp")


def main():
    with io.open(PATH, encoding="utf-8") as f:
        lines = f.read().split("\n")

    applied, skipped = [], []

    text = "\n".join(lines)
    for old, new, guard in SCALARS:
        if guard and guard in text:
            skipped.append(f"already present: {guard}")
            continue
        if old not in text:
            skipped.append(f"SCALAR missing: {old[:60]}")
            continue
        text = text.replace(old, new, 1)
        applied.append(f"scalar: {old[:50]}")
    lines = text.split("\n")

    for anchor, kind, payload in RULES:
        idx = next((i for i, l in enumerate(lines) if anchor in l), None)
        if idx is None:
            skipped.append(f"anchor not found: {anchor[:60]}")
            continue

        # guard: any slug this rule would insert already present -> skip
        already = [s for s in SLUG_RE.findall(payload) if f"media/{s}.webp" in text]
        if already:
            skipped.append(f"already applied ({','.join(already)}): {anchor[:45]}")
            continue

        if kind == "heading":
            insert_at = idx
            j = idx + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].lstrip().startswith("!["):
                insert_at = j
            lines[insert_at + 1:insert_at + 1] = ["", payload]
        else:
            lines[idx + 1:idx + 1] = ["", payload]
        applied.append(f"{kind}: {anchor[:55]}")

    with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print(f"applied {len(applied)}:")
    for a in applied:
        print("  +", a)
    if skipped:
        print(f"\nskipped {len(skipped)}:")
        for s in skipped:
            print("  -", s)


main()
