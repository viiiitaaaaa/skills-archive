<div align="center">

# Awesome Astra Video Prompts

**Real prompts for making video with GPT-6 Astra and coding agents.**

Astra doesn't output video. It writes code and drives tools —
Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Prompts](https://img.shields.io/badge/prompts-24-blue)
![Full text](https://img.shields.io/badge/full%20text-17-success)
![Previews](https://img.shields.io/badge/previews-18-blueviolet)

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="38"></picture></a>

**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**

</div>

<!-- lang-switcher -->
<p><strong>English</strong> · <a href="README.zh-CN.md">中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>
<!-- /lang-switcher -->

> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.

> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.

---

## Table of Contents

- [What is this?](#what-is-this)
- [Quick Start](#quick-start)
- [Statistics](#statistics)
- [Featured Prompts](#featured-prompts)
- [Product Launch & Marketing](#product-launch--marketing)
- [Motion Previz → Generative](#motion-previz--generative)
- [End-to-End Production](#end-to-end-production)
- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)
- [Adjacent: Blender & Others](#adjacent-blender--others)
- [Skills & Tooling](#skills--tooling)
- [What the Community Learned](#what-the-community-learned)
- [Completeness Table](#completeness-table)
- [Watch List](#watch-list)
- [How to Contribute](#how-to-contribute)
- [License & Acknowledgements](#license--acknowledgements)

---

## What is this?

Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:

- **Remotion / HyperFrames** — programmatic motion graphics
- **Remotion motion previz → Seedance** and other generative models
- **Blender previs** → render or generate
- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly

That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.

**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.

---

## Quick Start

```bash
# Official Remotion Agent Skills — the base layer under almost every case here
npx -y skills@latest add remotion-dev/skills -g -y

# Cinematic product video shot library
npx skills add Vincentwei1021/video-shotcraft
```

Then paste any prompt below into Astra, Claude Code, or Codex.

**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.

---

## Statistics

| | |
|---|---|
| **Entries** | 24 |
| **Full text available** | 17 |
| **Languages** | EN · JA · ZH |
| **Preview clips** | 18 (animated WebP, `media/`) |
| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |
| **Last updated** | 2026-09-10 |

`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only

---

## Featured Prompts

### 1: High-Speed Parkour Motion Previz

![JA](https://img.shields.io/badge/lang-JA-red) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2096096560690209130"><img src="media/parkour-previz.webp" width="440" alt="High-Speed Parkour Motion Previz — Remotion motion previz demo"></a>

🎬 **[Watch the full video →](https://x.com/Kashiko_AIart/status/2096096560690209130)**

#### 📖 Description

The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the "camera must not pass through the character" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.

#### 📝 Prompt

```
Remotionを使い、高低差と多彩なカメラワークを備えた、高速パルクールのモーションコンテを実装・レンダーしてください。計画や静止画だけで終わらず、実際に動くMP4を完成させてください。

【制作条件】
題材は「遊園地のアトラクションを渡り歩く高速パルクール」。題材の指定があれば、その舞台へ置き換えてください。
尺・画面指定がなければ、15秒、横長、SD程度、30fps、無音を初期値とします。軽量で動きを確認しやすい解像度を選んでください。
外部素材がなくても、単純な立体形状で制作を完結できる構成にしてください。

【必須技術】
TypeScriptとRemotionを使用し、useCurrentFrame()を時間の基準として、人物、背景、動く足場、カメラの状態を決定してください。
背景と人物は共通の3D座標系に置き、WebGLで奥行きと遮蔽を描画します。RemotionでプレビューとMP4のレンダーを行ってください。

コース形状、人物の移動経路、姿勢、動く足場、カメラ、描画処理を分離し、後から動作とカメラを編集できる構成にしてください。同じフレーム番号からは常に同じ状態が得られるようにします。

【人物の形と動き】
人物は1体。球形の頭と縦長のカプセル状の胴体からなる、単純な「i型」にしてください。頭と胴体は少し離し、背景から見分けやすい色にします。

四肢や衣装を作り込まず、位置移動、前傾、左右の傾き、軽い上下動、踏み切り前の圧縮、着地時の沈み込みで動作を伝えてください。
走行では短周期の接地感を入れ、加速、跳躍、着地、再加速をつなぎます。
宙返りは身体の向きが空間内で実際に回転するようにし、移動軌道と回転を別々に制御してください。

【コースとアクション】
遊具を、実際に通過・接地できる一続きの立体コースとして配置してください。

基本の流れ：
・ジェットコースターの上りレールを高速で駆け上がる
・曲線レールを急降下する
・レール間の隙間を横宙返りで越える
・ひねり跳躍で動く観覧車のゴンドラ屋根へ飛び移る
・ゴンドラから外周の足場へ跳び、観覧車上部のアーチを走る
・一段低いメリーゴーランドの屋根へ前宙で降りる
・着地ロールから起き上がり、方向転換する
・振り子アトラクションの動く平台へ飛び乗る
・平台からさらに低い屋根へ後宙で降りる
・障害物を跳び越え、曲がる水路沿いを走る
・水路を宙返りで越え、そのまま出口へ疾走する

尺に応じて動作を整理し、各動作の踏み切り、空中移動、接地が読み取れる時間を確保してください。

移動する足場は独立して動かし、接地中の人物は足場の移動へ追従させます。離れた瞬間から人物自身の跳躍軌道へ移行してください。
高さ、距離、足場の幅、回転速度は、接触が成立し、映像でも読める値を設計してください。

背景には支柱、隣接する遊具、屋根、水路、地面などを配置し、人物の移動距離とカメラの視差が分かるようにします。形状は簡素でも、遊具の種類を識別できる輪郭を持たせてください。

【カメラ演出】
次の構図を、アクションの意味に合わせて組み合わせてください。

・真後ろから、進行方向へ伸びるレール越しに追走
・やや斜め後ろから、高低差と次の足場を見せる追走
・横から並走し、跳躍距離や身体の回転を見せる構図
・着地点側に先回りし、こちらへ飛び込んでくる人物を正面で迎える構図
・高所で周囲の地形と落差を見せる広い構図
・次の足場を見る意図を伝える、短い頭部のアップ
・踏み切りや着地の接触を伝える、短い接地部のアップ

正面の迎えでは、カメラを着地点側の一定位置に構える区間を設けてください。人物とカメラの距離が実際に縮まり、人物が画面内で大きくなるようにします。

空中の回転や遊具間の移動では、全身と着地点が読める画角を確保してください。接地部のアップは接触成立後に入れ、次の移動へ素早くつなぎます。

カメラ位置、注視点、画角は連続した軌道でつないでください。背後から正面へ移る際は、人物の周囲を弧を描いて回り込みます。人物を挟んだ2地点を単純に直線補間して、カメラが人物を突き抜けることのない設計にしてください。

構図の名称だけを増やすのではなく、実際の進行方向に対するカメラ位置と、完成映像の見え方に変化を作ってください。

【見た目と速度感】
人物と遊具の形状が読みやすい、簡素な色と照明で仕上げてください。
高速感は、大きな位置変化、短い踏み切り、着地直後の再加速、前景の通過、カメラへの接近で表現します。
映像面は人物と環境で構成し、説明文や制作メモは別資料へまとめてください。

【検証と提出】
レンダー前に、以下を確認・修正してください。
・着地点に支持面があり、接地中の人物が足場へ追従する
・意図しない床抜け、支柱や遊具へのめり込みがない
・人物とカメラの位置、姿勢、画角に不連続や非数値がない
・広い構図では人物全体が画面内に収まる
・頭部と接地部のアップが対象を正しく捉える
・背後、斜め後方、側方、正面の構図が実際に成立する
・正面の迎えで人物がカメラへ接近する

MP4をレンダーした後、ffprobeで尺、解像度、fps、フレーム数、音声の有無を確認し、ffmpegで最後までデコードしてください。
完成動画から各動作とカメラ移行の代表フレームを取り出して目視確認し、可能なら通常速度でも通し再生してください。数値検査と映像の見やすさは別々に検証します。

提出物：
1. 完成したモーションコンテMP4
2. 編集可能なRemotion／TypeScriptソース
3. 動作区間、開始・終了フレーム、カメラ、出力仕様を記載したJSON
4. 再レンダー手順
5. 実施した検証と未確認事項の短い記録

最後に、完成MP4をすぐ開けるリンクを提示してください。
```

<details>
<summary>Key constraints, summarized (unofficial)</summary>

- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only
- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL
- Character: one "i-shaped" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing
- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state
- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification
</details>

#### 📌 Details

- **Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart))
- **Source:** [x.com/Kashiko_AIart/status/2096096560690209130](https://x.com/Kashiko_AIart/status/2096096560690209130)
- **Reused by:** [@Naonekozamurai](https://x.com/Naonekozamurai/status/2096871096759030114)
- **Published:** 2026-09-05
- **Tools:** GPT-6 Astra, Remotion, TypeScript, WebGL

---

### 2: AdCar TV — In-Repo One-Shot Launch Video

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/d4m1n/status/2096258259459964963"><img src="media/adcar-tv.webp" width="440" alt="AdCar TV — 44s one-shot launch video"></a>

🎬 **[Watch the full video →](https://x.com/d4m1n/status/2096258259459964963)**

#### 📖 Description

Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.

#### 📝 Prompt

```
can we create an overall video presenting the concept of AdCar TV?

make an intro video of 30-60s showing nice visuals (maybe the 3d of the car)?
and really cool car animations / branded stuff, showing off the site etc.
Use ffmpeg, remotion and qwen 3 tts for voice, and install whatever makes sense,
and come up with a cool artboard first and then make the video.
there is some music and car sounds in the codebase already.
```

> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.

#### 📌 Details

- **Author:** Dan ⚡️ ([@d4m1n](https://x.com/d4m1n))
- **Source:** [x.com/d4m1n/status/2096258259459964963](https://x.com/d4m1n/status/2096258259459964963)
- **Published:** 2026-09-05
- **Tools:** GPT-6 Astra, Remotion, ffmpeg, local Qwen 3 TTS

---

### 3: FeatureReveal — Frame-Exact Composition Contract

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Description

The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.

#### 📝 Prompt

```
Create a Remotion composition called FeatureReveal.

- 15 seconds at 30fps (450 frames), 1920x1080.
- Dark background (#0d1117).
- A headline "Ship changelogs as video" fades in over frames 0-30,
  holds, then fades out over frames 420-450.
- Three feature rows below the headline, each sliding up from 40px
  with a spring, staggered: row 1 enters at frame 60, row 2 at 90,
  row 3 at 120.
- Register FeatureReveal in Root.tsx with the correct
  durationInFrames and fps.
```

#### 📌 Details

- **Author:** OpenReplay Team
- **Source:** [blog.openreplay.com/making-videos-claude-code-remotion](https://blog.openreplay.com/making-videos-claude-code-remotion/)
- **Published:** 2026-06-04
- **Works with:** Claude Code, Codex, Astra
- **Tools:** Remotion

---

### 4: Witch's First Flight — 15s Generated Shot Script

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Mayz1169/status/2095873015007592679"><img src="media/witch-first-flight.webp" width="440" alt="Witch's First Flight — 15s generated shot"></a>

🎬 **[Watch the full video →](https://x.com/Mayz1169/status/2095873015007592679)**

#### 📖 Description

**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *"I used it to create the prompt for this animation."* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.

#### 📝 Prompt

```
Create a 15-second horizontal 16:9 high-energy fairy-tale animation about a young witch's completely uncontrolled first flight. The entire sequence must stay in fast continuous motion from the first second to the final frame. Bright morning sunlight, rich cheerful colors, whimsical storybook architecture, hand-painted textures and expressive animated acting. Lighthearted magical adventure with playful chase comedy. No dark magic, horror or gloomy atmosphere.

CHARACTER:
A small apprentice witch with a round expressive face, large curious eyes and tousled chestnut hair. She wears a slightly oversized deep-blue pointed hat with a golden star buckle, a short violet cape, a cream blouse, a blue pleated skirt, striped stockings and brown ankle boots. Her old wooden broom has a crooked handle, golden bindings and a slightly messy straw tail. Preserve her face, outfit, hat and broom design consistently throughout the video. Her hat must remain on her head, although she may need to grab it during the dive.

0–1.5s:
Inside the sunlit upper room of a magical academy tower, the apprentice secretly climbs onto the broom while her teacher is facing away. The moment she settles onto it, the broom violently activates with a bright golden spark. It rockets forward before she is ready, dragging her across the room and blasting straight through an open tower window within the first second. Papers, feathers and tiny magical particles spiral behind her. Her eyes widen and she desperately wraps both arms around the broom.

1.5–4s:
The camera rushes alongside her as the broom shoots around the enormous magical academy. She swerves uncontrollably between colorful pointed towers, a giant clock face and suspended stone walkways. She narrowly misses walls and decorative flags. A flock of mail-delivering owls suddenly crosses her path. The broom rolls sideways through the flock while the startled owls scatter in every direction, loose envelopes fluttering through the air. Her expression is pure panic, but the sequence remains playful rather than dangerous.

4–6s:
Without slowing down, the broom turns almost vertically and launches above the towers into soft white clouds. The camera follows from a dramatic low angle as sunlight shines through the cloud mist. At the highest point the broom instantly flips forward and dives toward the valley. Her pointed hat begins lifting from her head, so she grabs it with one hand while clinging to the broom with the other, screaming as her cape and hair stream violently backward.

6–10s:
The dive flows directly into a fast flight through the lively magical town below the academy. The broom skims just above colorful tiled rooftops and twists between narrow streets. She narrowly avoids smoking chimneys, flapping laundry, hanging wooden shop signs and a surprised flying magical postman. The postman spins harmlessly in the air as letters scatter behind him. Use dynamic chase-camera movement, quick side tracking, close passes by foreground objects and strong depth, while keeping the witch's face and broom clearly readable.

10–12.5s:
She bursts over a crowded open-air market, flying above fruit stands and a bright candy shop. The wind trail from the broom sends ribbons, paper wrappers, flower petals and a few lightweight pieces of fruit swirling upward in a colorful spiral. Townspeople and tiny magical creatures look up in astonishment. She ducks beneath a striped market banner, rises over a candy-shop sign and begins pulling the broom handle into a straighter direction.

12.5–15s:
For one brief moment the broom becomes steady. Still racing above the final rooftops, she slowly lifts her head. Her frightened expression changes into a surprised, delighted smile as she begins to enjoy the speed. Before she can celebrate, the broom gives another powerful golden spark and accelerates even faster. She leans forward, laughing and struggling to steer as they blast out of the town and over a green valley toward a magnificent floating castle in the distant sunlit cloud sea. End in the middle of this acceleration with the camera chasing closely behind her, clearly suggesting that the uncontrolled adventure continues.

The story must feel like one flowing pursuit, with each action naturally leading into the next. Keep the broom, witch, environment and camera constantly moving. Use energetic banking turns, dives, rapid elevation changes and near misses, but never show a serious collision or injury. Her emotional progression must remain clear: secret excitement, sudden panic, frantic struggle, then growing exhilaration.

Bright fairy-tale morning lighting, saturated blues, violets, warm golds, fresh greens and candy-colored town details. Soft storybook clouds, sparkling magical trails, fluttering fabric and lively environmental reactions. Fluid animation, clean character silhouette, stable facial features, consistent hands and limbs, coherent broom movement and readable action staging.

No stopping, no landing, no successful mastery of the broom, no final hero pose, no freeze frame, no fade to black, no ending card, no captions, no logos, no dialogue text, no dark fantasy, no night scene, no broken anatomy, no disappearing hat, no duplicated broom and no sudden character or costume changes.
```

#### 📌 Details

- **Author:** Kiki / Mayz ([@Mayz1169](https://x.com/Mayz1169))
- **Source:** [x.com/Mayz1169/status/2095873015007592679](https://x.com/Mayz1169/status/2095873015007592679) · [full reply](https://x.com/Mayz1169/status/2095873204351070296)
- **Published:** 2026-09
- **Tools:** GPT-6 Astra (as prompt writer) → video model

---

### 5: T Cells — One Sentence, Five Minutes

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/DeryaTR_/status/2095659170661904804"><img src="media/t-cells.webp" width="440" alt="T Cells — 5-minute explainer, one-line brief"></a>

🎬 **[Watch the full video →](https://x.com/DeryaTR_/status/2095659170661904804)**

#### 📖 Description

The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.

#### 📝 Prompt

```
Create a 5 minute educational video about T cells.
```

The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):

```
Use the Remotion plugin for video generation.
Use Imagegen for visuals.
You may use HeyGen for narration.
Assemble the entire educational video one-shot,
including what to say and how to explain it.
```

#### 📌 Details

- **Author:** Derya Unutmaz, MD ([@DeryaTR_](https://x.com/DeryaTR_))
- **Source:** [x.com/DeryaTR_/status/2095659170661904804](https://x.com/DeryaTR_/status/2095659170661904804)
- **Chinese relay:** [@LinearUncle](https://x.com/LinearUncle/status/2095719251277701516)
- **Published:** 2026-09-03
- **Tools:** GPT-6 Astra, Remotion plugin, Imagegen, HeyGen

---

### 6: Six-Part Control Template + Shot JSON Contract

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Description

A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.

#### 📝 Prompt

Six-part control template:

```
Outcome:
Create [specific deliverable] for [audience and use].

Source of truth:
Use [documents/URLs/data].
Treat [file/version] as authoritative.
Mark any unresolved conflict instead of inventing an answer.

Constraints:
Follow [length, tone, technical, legal or creative rules].

Authority:
Make routine, reversible decisions without asking.
Ask only when missing information would materially change the outcome.

Output contract:
Return [sections/schema/file type], in [order], with [citations/fields].

Verification:
Before finishing, check [acceptance criteria] and repair failures.
```

Shot JSON contract:

```
Return valid JSON with project_summary and shots. Each shot must contain id,
story_purpose, framing, subject_action, camera, duration_seconds,
continuity_constraints and audio_cue. Total duration must equal 45 seconds.
```

60-second short:

```
Turn the premise below into a 60-second anime short. Preserve the theme and
character rules. Use 8–10 shots, one primary location and no crowd. Each shot
must change story information. Return logline, beat sheet, dialogue, shot table
and continuity checklist. Remove any beat that cannot be shown or heard.
```

#### 📌 Details

- **Author:** Elser AI
- **Source:** [elser.ai/blog/gpt-6-astra-prompt-guide](https://www.elser.ai/blog/gpt-6-astra-prompt-guide)
- **Published:** 2026-09
- **Tools:** GPT-6 Astra

---

## Product Launch & Marketing

### Atomik — 33-Second Launch Film

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/makwanatejas170/status/2096555742597988400"><img src="media/atomik-launch.webp" width="440" alt="Atomik — 33s launch film"></a>

🎬 **[Watch the full video →](https://x.com/makwanatejas170/status/2096555742597988400)**

> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.

X post, verbatim:

```
GPT-6 Astra one-shot this launch video for @atomikgrowth
with New motion-flavor skill that i made
works on both @HyperFrames_ & @Remotion
```

Spec from the repo — useful as an acceptance contract for an agent:

```
Build a 33-second launch film in Remotion + React + TypeScript + CSS/SVG.
1920×1080, 60 fps, 1980 frames, H.264/AAC.
Rocket, layouts, cursor, typography and transitions must be rendered from code.
Portfolio imagery and soundtrack are bundled local media.
Do not hide a finished-video layer inside the composition.
No AI API call is required to render.
Output: out/final-render.mp4
```

**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames

---

### video-shotcraft — Cinematic Product Video Skill

![ZH](https://img.shields.io/badge/lang-ZH-yellow) ![full](https://img.shields.io/badge/invocations-full-success)

<a href="https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd"><img src="media/shotcraft-gallery-intro.webp" width="440" alt="video-shotcraft — 38s gallery intro, produced with the skill"></a>

🎬 **[Watch the full video →](https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd)**

<a href="https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d"><img src="media/shotcraft-ink-press.webp" width="440" alt="Ink Press — the 36s promo template shipped with the skill"></a>

🎬 **[Watch the full video →](https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d)**

> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.

Install:

```
帮我安装这个 skill：https://github.com/Vincentwei1021/video-shotcraft
```
```bash
npx skills add Vincentwei1021/video-shotcraft
```

Invocations (from the official README):

```
用 video-shotcraft 给我的桌面产品做一支宣传片。
用 deck-deal-flyin 和 row-embed 两张镜头卡展示这个功能。
参考 spotlight-hero-card，为这个页面设计一个产品特写镜头。
```
```
用 video-shotcraft 的 Ink Press 模板给我的产品做一支宣传片。
```

<details>
<summary>Skill frontmatter (determines when the agent activates it)</summary>

```yaml
name: video-shotcraft
description: Create cinematic product videos from shot recipe cards, a validated
template, and code/audio assets (Remotion + real page screenshots + 2.5D camera
moves + beat-synced cuts + sound design). Use when the user asks to turn a
frontend project or webpage into a product video, says "use video-shotcraft to
make a video/promo", names the Ink Press template or asks to reproduce its
effect, or wants a single shot card's motion.
```

Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).

Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic "promo skin".
</details>

**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex

---

### Montage — Agent-Native Launch Video Scaffold

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> A Remotion fork built for agents, aimed at product launch films.

What the README tells you to say to the agent:

```
Create a master sequence in a new folder and start creating.
Copy any of the examples to get started.
Reference AGENTS.md and leverage all animations possible.
Replace background primitives and the logo with our branding.
```

The AGENTS.md rules worth stealing:

```
Do NOT one-shot all sections at once without viewing them.
Build one section → register it → render key frames → verify → next section.
Every frame should have something animating.
Never use flat backgroundColor — always layer vignette + grain + corner glow.
Do NOT default to useLetterPopIn for every text entrance.
Use SF Pro Display. Never use Geist or Inter.
After every change: render stills at entrance / mid / settled, inspect, then MP4.
```

**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion

<a href="https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f"><img src="media/montage-launch-film.webp" width="440" alt="Montage — launch film rendered by the agent"></a>

🎬 **[Watch the full video →](https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f)**

---

### Remotion Official Skill Invocations

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> The official slash commands. Most community prompts assume these are installed.

Bootstrap for a coding agent on a fresh project:

```
Ensure Node.js is installed.
Install Remotion Skills:
npx -y skills@latest add remotion-dev/skills -g -y
Then use them to create a video.
```

Invocations:

```
/remotion-create Make a promo video for a record store
/remotion-markup Create an animated title card using Inter
/remotion-maps Animate a route from Los Angeles to New York and make the camera follow it
/remotion-render
/remotion-studio
```

Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.

**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion

---

### Short Briefs That Still Worked

![Mixed](https://img.shields.io/badge/lang-mixed-lightgrey) ![partial](https://img.shields.io/badge/text-partial-orange)

> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.

```
游戏做好了，用 remotion 做个好看的 CM
```
**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)

<a href="https://x.com/guuchacha149182/status/2096813471463882947"><img src="media/game-cm.webp" width="440" alt="Game CM — one-prompt Remotion promo"></a>

🎬 **[Watch the full video →](https://x.com/guuchacha149182/status/2096813471463882947)**

```
根据最近的 changelog 比较亮眼的功能做个视频。
```
**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker

<a href="https://x.com/leon7hao/status/2096844989900914865"><img src="media/changelog-video.webp" width="440" alt="Changelog video — no skill installed, weaker result"></a>

🎬 **[Watch the full video →](https://x.com/leon7hao/status/2096844989900914865)**

Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)

**@NickYang130 — BrandNewStudy marketing video, one-shot**

<a href="https://x.com/NickYang130/status/2096835902047932521"><img src="media/brandnewstudy-promo.webp" width="440" alt="BrandNewStudy marketing video, one-shot"></a>

🎬 **[Watch the full video →](https://x.com/NickYang130/status/2096835902047932521)**

**@stoufax — iOS app launch, Remotion + ElevenLabs**

<a href="https://x.com/stoufax/status/2096311328600113222"><img src="media/ios-app-launch.webp" width="440" alt="iOS app launch — Remotion + ElevenLabs"></a>

🎬 **[Watch the full video →](https://x.com/stoufax/status/2096311328600113222)**

---

## Motion Previz → Generative

> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.

### Seedance Handoff Instruction

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Naonekozamurai/status/2096871096759030114"><img src="media/seedance-handoff.webp" width="440" alt="Remotion previz control MP4 handed to Seedance 2.5"></a>

🎬 **[Watch the full video →](https://x.com/Naonekozamurai/status/2096871096759030114)**

> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.

```
Remotionで作成した動画はあくまで動きを参照するだけの動画。
参照動画で不自然な挙動や不自然な女の子の体勢は、動画化の際にどんどん修正して良い。
動画では、前後のつながり、動画としてのかっこよさを重視してほしい。
```

<details>
<summary>English (unofficial)</summary>

```
The video made with Remotion is purely a reference for movement.
Any unnatural behavior or unnatural poses of the girl in the reference video
may be freely corrected during video generation.
In the video, prioritize continuity between shots and how good it looks as a video.
```
</details>

**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)

---

### Ultra-High-Speed Sprint Control MP4

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2094182215894831283"><img src="media/sprint-control.webp" width="440" alt="Ultra-high-speed sprint control MP4"></a>

🎬 **[Watch the full video →](https://x.com/Kashiko_AIart/status/2094182215894831283)**

> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.

```
Remotionで超高速疾走モーションコンテを作ってください。フレーム単位で実際に動く3Dドローン追従型のcontrol MP4を出力。
固定された一つの3Dワールドとして構築し、床グリッド、左右の壁線、一定間隔のゲート、空間中の光跡を配置する。背景をループさせるのではなく、十分に長い一本道を実際に前進させる。
キャラクターは疾走するキャラクターをやや斜め後ろから追従する。
人物とグリッドは必ず同じ3D座標系とカメラ投影を使用してください。2D素材を拡大縮小するだけの疑似カメラにはしないでください。

【人物proxy】
全員、次の2要素だけで表現する。
1. 円形の頭
2. 傾きや回転が可能な一本の縦長胴体

【疾走速度】
見かけだけの速度表現ではなく、root座標を毎フレーム実際に前進させる。

【敵と接触frame】
敵は接触frameを決定してコース上へ固定配置する。
キャラクターは流れるような体術で3体を進行軸の外へ弾き、そのまま走り抜ける。
カメラは接触の前後だけ、短いイージングで別アングルへ移行し、接触後は必ず後方追従へ戻す。

【クリーンcontrol画面】
映像内には人物proxy、空間、接触アクセントだけを表示する。
```

**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion

---

### Side-Scrolling Chase, with a Frame Table

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2093692302745383041"><img src="media/side-scroll-chase.webp" width="440" alt="Side-scrolling chase with a frame table"></a>

🎬 **[Watch the full video →](https://x.com/Kashiko_AIart/status/2093692302745383041)**

> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.

```
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion

---

### 30 Camera Compositions — Reference Sheet Generator

![JA](https://img.shields.io/badge/lang-JA-red) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/Kashiko_AIart/status/2093575541916061984"><img src="media/camera-comps-30.webp" width="440" alt="30 camera compositions reference sheet"></a>

🎬 **[Watch the full video →](https://x.com/Kashiko_AIart/status/2093575541916061984)**

> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.

```
RemotionとHTML、CSS、SVGを使って、動画生成AIへカメラ構図と連続したカメラ移動を伝えるための「カメラ構図一覧」と「モーションコンテ」を作ってください。

30種類の重複しないカメラ構図を、HTML画面上の6列×5行グリッドに並べてください。

各パネルには以下を表示します。
・ID：A〜Z、AA〜AD
・構図名
・16:9の構図サムネイル

被写体は、位置、向き、傾きだけが分かるシンプルなi字人形を2体使います。人物Aはシアン、人物Bはオレンジにして、二人の位置関係を判別しやすくしてください。背景、ステージ、客席、家具なども単純なSVG図形で表現してください。

全景、ツーショット、各人物の寄り、肩越し、横顔、俯瞰、あおり、主観、前景越し、背面、周回など、重複しない30種類を作ってください。
```

> ⚠️ The post continues past the output requirements; only what's visible is quoted.

**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG

> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.

<a href="https://x.com/Kashiko_AIart/status/2096533732547264921"><img src="media/chanbara.webp" width="440" alt="Chanbara sword-fight motion previz"></a>

🎬 **[Watch the full video →](https://x.com/Kashiko_AIart/status/2096533732547264921)**

---

## End-to-End Production

### Idea → Uploadable YouTube Video

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.

```
I need you to take me from idea to finished YouTube video.
I want you to create me an engaging and professional video about GPT-6 Astra.
You need to use Nate Herk's voice clone and HeyGen avatar.

Start the video off by telling everyone that this is not Nate
and that you orchestrated the entire video.
You planned it out. You researched it. You grabbed all the B-roll.
You grabbed the screenshots, you edited everything,
and you produced a finished video, which is what they're watching right now.

I want this to feel professional, like it was edited by a human using HyperFrames.
Do not give me a draft or a WIP.
Give me a finished working version that I can post on my YouTube channel.
```

Same author, sizzle reel from 152GB of event footage:

```
Create me a sizzle reel recap that's a minute long from this event.
```

> ⚠️ Transcribed from the video's narration — no official paste block exists.

**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames

---

### Narration-First Diagram Explainer

![EN](https://img.shields.io/badge/lang-EN-blue) ![spec-only](https://img.shields.io/badge/text-spec--only-lightgrey)

> No generated footage at all. Record first, then build the picture to measured narration cues.

Workflow:

```
1. write and record the explanation
2. mark the moments where the picture needs to change
3. ask Astra to build those moments with shapes, labels and motion in Remotion
4. add captions timed to the recording
5. render and watch with sound
```

Published short instructions:

```
Use this image for the scene, plan the framing around the measured narration cues,
keep important details visible and stop the movement while the viewer reads the label
```

```
Bring the result on screen when the recording names it,
shorten the entrance animation and preserve the time needed to read the final state
```

> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.

**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion

---

## Meta: Prompts That Write Prompts

### Director / Animation Supervisor Template

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.

```
Act as a film director, animation supervisor and prompt engineer.

Develop a complete prompt for a [DURATION]-second animated sequence.

Story:
[Describe what happens.]

Define:
Character appearance
Environment
Opening composition
Camera movement
Character actions
Timing and pacing
Lighting
Color palette
Emotional tone
Final shot

Maintain visual and narrative continuity throughout the sequence.
Every movement should connect naturally to the next.

Return:
1. The final production-ready prompt
2. A shot-by-shot breakdown
3. A negative prompt identifying unwanted outcomes
4. Three adjustments I can make if the first generation is inconsistent
```

**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra

---

## Adjacent: Blender & Others

### Blender 8-Second Product Turntable

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.

```
Make an eight-second product animation from the starter at 1920 × 1080, 24 fps,
frames 1–192.
Move the camera from a right-front elevated view to a left-front view,
easing at the beginning and end.
Keep the product stationary, the cyan indicator visible, and the lighting deliberate.
Preserve the enclosure dimensions.
Render frames 1, 96, and 192 before the full sequence.
Save animation_v001.blend.
```

**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra

---

### Known but Unpublished

> Confirmed to exist, no public primary source. **Listed, never reconstructed.**

| What | Who | Status |
|---|---|---|
| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |
| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |
| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |
| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |
| "Remotion 制作 8 本の裏側" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |
| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |

**The physics / soft-body motion demo itself is public** (the skill is not):

<a href="https://x.com/paojiaofty/status/2096830622341976467"><img src="media/physics-motion.webp" width="440" alt="Physics / soft-body motion — 4K60 direct output"></a>

🎬 **[Watch the full video →](https://x.com/paojiaofty/status/2096830622341976467)**

---

## Skills & Tooling

Everyone here is feeding Astra the same base layer. We link, we don't vendor.

| Tool | Install / Link | What it's for |
|---|---|---|
| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |
| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |
| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |
| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |
| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |
| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |
| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |

---

## What the Community Learned

Patterns that show up across every thread above:

**Install the skills first, then talk.** Without skills, a changelog video came out "noticeably short of it". With skills installed, one-shots became common.

**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.

**Align the timeline to narration, not "make it faster overall."** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*

**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.

**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.

**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.

**People are starting to demand disclosure on "one-shot" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.

---

## Completeness Table

| ID | Type | Author | Full text? |
|---|---|---|---|
| AdCar TV | product launch | [@d4m1n](https://x.com/d4m1n) | ✅ |
| Atomik | product launch | [@makwanatejas170](https://x.com/makwanatejas170) | spec yes, chat prompt no |
| video-shotcraft | product promo skill | Vincentwei1021 | invocations yes, skill body long |
| Montage | launch scaffold | simplexlabs | AGENTS.md rules |
| FeatureReveal | feature video | OpenReplay | ✅ |
| Remotion official | invocations | Remotion | ✅ (very short) |
| Parkour previz | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| Sprint control MP4 | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| Side-scroll chase | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 30 camera comps | reference sheet | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |
| Seedance handoff | handoff | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |
| T cells | explainer | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (one line) |
| Nate YouTube | channel video | Nate Herk | transcribed |
| Foma explainer | diagram video | [@foma_on_x](https://x.com/foma_on_x) | short instructions only |
| Witch's flight | generated shot script | [@Mayz1169](https://x.com/Mayz1169) | ✅ |
| Six-part + JSON | meta | Elser AI | ✅ |
| Director template | meta | The AI Average | ✅ |
| Blender turntable | 3D product | Kingy.ai | ✅ |
| Physics motion skill | skill | [@paojiaofty](https://x.com/paojiaofty) | unpublished |

---

## Watch List

A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.

| Account | Why |
|---|---|
| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |
| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |
| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |
| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |
| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |
| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |
| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |
| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |

[Suggest an account →](../../issues/new?template=watch-account.yml)

---

## How to Contribute

**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.

Every entry needs three things:

| Field | Why |
|---|---|
| **Author** | Name or handle, written the way they write it |
| **Source** | Direct link to the post, thread, blog, or video |
| **Published** | Date, so readers can judge how current it is |

**Rules:**

- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.
- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.
- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.
- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License & Acknowledgements

Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).

**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.

Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.

**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.

---

<div align="center">

⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="32"></picture></a>

[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)

</div>
