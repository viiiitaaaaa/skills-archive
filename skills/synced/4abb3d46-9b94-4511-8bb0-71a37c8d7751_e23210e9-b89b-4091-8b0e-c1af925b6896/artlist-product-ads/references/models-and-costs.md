# Models and Costs

Prices verified against a live Artlist account. Treat them as a starting point, not gospel — the catalog changes. Always confirm the price the queue response echoes back before reporting it to the user.

## Video — image-to-video

| Model | ID | Settings | Price |
|---|---|---|---|
| **Kling 1.6 Standard I2V** | 1007 | 5s, 720p, 9:16 | **300** |
| Seedance 2.0 Mini I2V | 2467 | 5s, 480p, 9:16 | 350 |
| Kling 1.6 Pro T2V | 1010 | 5s, 720p | 500 |
| Kling 1.6 Standard T2V | 1009 | 10s, 720p, 9:16 | 600 |
| Seedance 2.0 Mini | 2465 | 15s with audio | 2475 |

**Default to Kling 1.6 Standard I2V (1007).** It is both the cheapest and the highest resolution of the budget tier — 720p is its floor, so there is nothing to gain by asking for lower. Its `duration` accepts only 5 or 10.

Counter-intuitive traps in this table: 480p models can cost *more* than 720p ones, and `generate_audio: true` on Seedance multiplies the price several times over while producing audio you will discard anyway. Longer duration scales the price roughly linearly, so a 15-second clip is never the economical way to get 15 seconds — three 5-second clips cost less and cut better.

## Images — image-to-image

| Model | ID | Settings | Price |
|---|---|---|---|
| **Nano Banana 2 I2I** | 2249 | 512px, 9:16 | **60** per image |

`num_images` accepts 1–5 and multiplies the price linearly. Its `aspect_ratio` list includes 9:16 but defaults to 16:9. `resolution` options run 512px / 1k / 2k / 4k, defaulting to 2k — always set 512px for drafts.

Accepts up to 14 reference images. Use a second reference when the model keeps getting a structural detail wrong.

## Voice-over

Verified working: **ElevenLabs Multilingual v2, `modelId` 2061** (model group 311). Eleven v3 (2070, group 206) also exists. Cost scales with text length — about **2 credits** for three words, **7–11** for a full 9–12 word line.

Call `get_model_config` with both `modelId` and a `voiceId`; passing the voice alone is rejected.

Settings that matter:

- `accent` — **defaults to British.** Set `American` explicitly for US audiences.
- `voice_stability` — 0 to 1. About 0.7 for calm and even; lower for livelier delivery.
- `language` — defaults to English.
- `voiceEffect` — leave at NONE.

`list_voices` accepts a `gender` filter. Present voices by name and character traits; never expose IDs. Preview URLs are not fetchable from the sandbox, so audition by generating one short line rather than promising to listen for the user.

**Lines run shorter than the 2.2 words/second estimate** — a 10-word advertising line lands around 3.8s, not 4.5s. Since Kling's floor is 5s, the picture always outruns the voice by several seconds across a five-shot cut. That gap is useful: it gives the hook time to land before the first word and lets the slogan hold after the last. Don't buy longer clips to fill it, and don't pad the script.

## Negative prompts

Kling 1.6 accepts `negative_prompt`, and it is the cheapest insurance in the pipeline. A working set for hands-and-product work:

```
distorted fingers, extra fingers, extra hands, warped hand, melting beads,
changing bracelet structure, text, logos, fast motion
```

Add per-shot terms as needed — `spilling drink`, `lifting arm`, `watch interface, icons, numbers on screen`.

## Budget arithmetic

A 7-shot ad at draft quality:

| Item | Count | Each | Total |
|---|---|---|---|
| Scene stills | 7 | 60 | 420 |
| Clips | 7 | 300 | 2100 |
| Voice lines | 7 | ~10 | 70 |
| **Total** | | | **~2600** |

Budget another 200–400 for revisions and re-rolls. Quote the user this total before starting stage 2, not after.

That revision figure is optimistic in practice. A real five-shot job ran ~2900 on the plan above and ~11,600 in total, because two shots went through five or six rounds each. Most of that overrun came from re-animating clips whose *stills* were the problem — a 300-credit fix for a 60-credit fault. When a user rejects a clip, ask what they dislike before regenerating anything: if the answer describes the frame rather than the movement, the still is the thing to rebuild.

## Upload constraint

The sandbox cannot reach Artlist's S3 upload endpoints — a presigned PUT returns 403. To get a local file into Artlist as a reference, use `upload_widget` and have the user upload from their browser, then `get_recent_uploads` to retrieve the asset ID.

Results already inside Artlist need no upload: reference them with `input: { generationId, outputIndex }`. Prefer this — it is free, instant, and avoids a round trip through the user.

Going the other way, Artlist's CDN is also unreachable from the sandbox, so finished clips must be downloaded by the user and re-uploaded into the conversation before assembly.
