# Contributing

This repo collects **prompts, verbatim, with credit**. That's it.

---

## Submit a prompt

**[→ Open an Issue](../../issues/new?template=new-prompt.yml)** — paste the prompt, link the source. No git required.

Or open a PR adding an entry to `README.md`.

---

## Required fields

Every entry needs these three. No exceptions.

| Field | Format |
|---|---|
| **Author** | Name or handle, written the way they write it. Link their profile. |
| **Source** | Direct link to the post, thread, blog post, or video. |
| **Published** | `YYYY-MM-DD`, or `YYYY-MM` if that's all you know. |

Plus, where known: **Tools** (Remotion, Seedance, HeyGen…) and **Language** of the prompt.

---

## Entry format

Copy an existing entry from `README.md`. Two shapes:

**Featured** — for prompts with full text and something to show:

```markdown
### N: Title

![Language](badge) ![full](badge)

#### 📖 Description
Two or three sentences. What it does, and what makes it worth keeping.

#### 📝 Prompt
​```
Verbatim, original language.
​```

#### 📌 Details
- **Author:** Name ([@handle](url))
- **Source:** [link](url)
- **Published:** YYYY-MM-DD
- **Tools:** …
```

**All Prompts** — condensed:

```markdown
### Title

![Language](badge) ![status](badge)

> One-line description.

​```
Prompt text
​```

**Author:** … | **Source:** [link](url) | **Published:** … | **Tools:** …
```

---

## Status labels

| Label | Meaning |
|---|---|
| `full` | Complete prompt as published |
| `partial` | Some of it — cropped screenshot, transcript, thread that stops |
| `pending` | Source identified, text not yet transcribed |
| `unpublished` | Known to exist, no public source. Listed only. |

---

## Preview clips

Where a source post has a published video, the entry carries a short animated
WebP preview from `media/`, wrapped in a link back to the original post:

```html
<a href="https://x.com/handle/status/123"><img src="media/slug.webp" width="440" alt="Short description"></a>

🎬 **[Watch the full video →](https://x.com/handle/status/123)**
```

Rules for previews:

- **Excerpt only.** 3–5 seconds, ~440px wide, under 500 KB. The preview sits
  beside the prompt as a reference — it is never the full video, and it always
  links back to the author's post.
- **Never rehost the full video.** Link to the original; don't vendor it.
  Same principle as "link official docs, don't copy them."
- **GitHub user-attachments count as an original.** Many project READMEs embed
  their demo as `github.com/user-attachments/assets/<id>` (a plain MP4). That is
  the author's own hosting — fetch it, excerpt it, link back to it. Do **not**
  copy it into `media/` wholesale.
- **Not every entry can have one.** Blogs, docs pages and text-only posts often
  publish no video at all. That is fine — leave those entries as they are.
- **Don't wrap previews in an HTML `<table>`.** GitHub's markdown parser
  suppresses markdown inside raw HTML blocks, so link captions would render as
  literal text. Stack them instead.
- **Authors can have theirs removed.** Same as prompts — open the correction
  issue and it goes, no argument.

Rebuild the set:

```bash
python scripts/fetch-source-videos.py <raw_dir>   # X posts (login-free syndication)
python scripts/fetch-extra-videos.py <raw_dir>    # GitHub-attachment / YouTube sources
python scripts/build-webp-previews.py <raw_dir> media <ffmpeg>
python scripts/patch-readme-previews.py README.md
```

---

## The rules that matter

**Quote verbatim.** Don't tidy, don't paraphrase, don't "improve" it. The exact wording is the point.

**Keep the original language.** A Japanese prompt stays Japanese. Add a translation *below* it in a `<details>` block, marked unofficial — never replace the original.

**Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible. A plausible reconstruction is worse than an honest gap, because readers can't tell the difference.

**Credit is not optional.** No author, no merge.

**Link official docs, don't copy them.** Their docs change; a copy here would go stale and mislead.

**One prompt per entry.** Easier to link, easier to correct.

---

## Translations

The README is published in English, Simplified Chinese, Japanese, Korean, Spanish and French:

| | |
|---|---|
| [English](README.md) | `README.md` |
| [中文](README.zh-CN.md) | `README.zh-CN.md` |
| [日本語](README.ja.md) | `README.ja.md` |
| [한국어](README.ko.md) | `README.ko.md` |
| [Español](README.es.md) | `README.es.md` |
| [Français](README.fr.md) | `README.fr.md` |

**Only the editorial text is translated** — headings, descriptions, statistics, contribution rules.
Every prompt stays in the language its author published it in, byte for byte. Translating a prompt
would break the first rule above, so the build enforces it: the generator copies each fenced code
block through untouched.

The translated files are **generated, not hand-edited**. Never edit `README.<lang>.md` directly —
your change will be overwritten. Edit the language table instead:

```bash
# 1. edit the table (keys are exact source units from README.md)
$EDITOR i18n/zh-CN.py

# 2. regenerate every README.<lang>.md
python scripts/build-translations.py

# or just one language
python scripts/build-translations.py ja
```

Adding a language means adding `i18n/<code>.py` at the same shape as the existing ones
(`SWITCHER`, `NOTICE`, `REPLACE`, `BLOCKS`, `TOC_TITLE`), plus one line in `LANGS` in
`scripts/build-translations.py`. The table of contents and every anchor are derived from the
translated headings at build time, so they can't drift.

To see which units still need a translation:

```bash
python scripts/extract-translation-units.py README.md
```

The build fails loudly on an untranslated unit rather than shipping a half-English page. If you
change README.md, re-run the build — a unit whose English text changed will show up as untranslated
and needs its key updated.

---

## If you're the author of something here

[Open an Issue](../../issues/new?template=correction.yml) to:

- Fix or expand your credit
- Add the full text of a `partial` entry
- Correct a mis-transcription
- Have your prompt removed

Actioned without argument, including removal. You don't owe us a reason.
