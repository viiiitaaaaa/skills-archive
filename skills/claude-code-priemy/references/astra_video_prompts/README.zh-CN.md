<div align="center">

# Awesome Astra Video Prompts

**用 GPT-6 Astra 与编程智能体做视频的真实提示词合集。**

Astra 不直接输出视频。它写代码、驱动工具 ——
Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Prompts](https://img.shields.io/badge/prompts-24-blue)
![Full text](https://img.shields.io/badge/full%20text-17-success)
![Previews](https://img.shields.io/badge/previews-18-blueviolet)

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="38"></picture></a>

**本项目由 LuxReal 维护** —— AI 短剧流水线：输入剧本，产出场景与角色一致、全流程可编辑的成片。**[免费试用 →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**

</div>

<!-- lang-switcher -->
<p><a href="README.md">English</a> · <strong>中文</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>
<!-- /lang-switcher -->

> 📄 **这是 README.md 的中文译本。** 所有提示词均按作者发布时的原始语言逐字保留、不作翻译；目录、说明、统计、投稿规则等编辑性文字为译本。两者若有出入，以[英文原版](README.md)为准。

> ⚠️ **版权声明**：所有提示词均收集自公开的社区帖子，用于学习研究，并标注原作者。若你认为任何内容侵犯了你的权益，请[提交 issue](../../issues/new)，我们会尽快移除。

> 🎬 **关于预览动图**：`media/` 下的动画片段是各作者**公开发布的演示视频**的短小、低分辨率摘录，仅作为提示词旁的参考，并始终链回原帖。它们是摘录，而非完整视频的再分发。如果你是作者并希望移除自己的片段，请[提交 issue](../../issues/new?template=correction.yml)，我们会无条件删除。

---

## 目录

- [这是什么？](#这是什么)
- [快速开始](#快速开始)
- [统计](#统计)
- [精选提示词](#精选提示词)
- [产品发布与营销](#产品发布与营销)
- [运动预演 → 生成](#运动预演--生成)
- [端到端制作](#端到端制作)
- [元提示词：写提示词的提示词](#元提示词写提示词的提示词)
- [邻近领域：Blender 及其他](#邻近领域blender-及其他)
- [Skill 与工具](#skill-与工具)
- [社区学到了什么](#社区学到了什么)
- [完整度表](#完整度表)
- [关注名单](#关注名单)
- [如何投稿](#如何投稿)
- [许可与致谢](#许可与致谢)

---

## 这是什么？

Astra 并不原生渲染视频。**它写代码、编排插件、操作电脑。** 成片来自：

- **Remotion / HyperFrames** —— 程序化动态图形
- **Remotion 运动预演 → Seedance** 及其他生成模型
- **Blender 预演** → 渲染或生成
- **HeyGen / ElevenLabs / ffmpeg** —— 旁白与合成

因此，给它写提示词与写一句「文生视频咒语」有本质区别。你是在下达一份构建指令，而不是描述一张画面。

**本仓库把这些提示词逐字收录，并标注出处。** 付费包与私有 skill 只留占位符 —— 从未公开的内容，我们绝不复原。

---

## 快速开始

```bash
# Official Remotion Agent Skills — the base layer under almost every case here
npx -y skills@latest add remotion-dev/skills -g -y

# Cinematic product video shot library
npx skills add Vincentwei1021/video-shotcraft
```

然后把下面任意一条提示词粘贴到 Astra、Claude Code 或 Codex 里。

**第一次来？** 从 [FeatureReveal](#3featurereveal--帧精确的合成契约) 开始 —— 它是最短的一条，也最能说明为什么帧号很重要。

---

## 统计

| | |
|---|---|
| **条目数** | 24 |
| **全文可得** | 17 |
| **语言** | EN · JA · ZH |
| **预览片段** | 18（动画 WebP，见 `media/`） |
| **译本** | 中文 · 日本語 · 한국어 · Español · Français |
| **最后更新** | 2026-09-10 |

`full` —— 与发布时一致完整 · `partial` —— 只有一部分 · `spec-only` —— 描述了方法，措辞从未公开 · `unpublished` —— 已知存在，仅有占位符

---

## 精选提示词

### 1：高速跑酷运动预演

![JA](https://img.shields.io/badge/lang-JA-red) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2096096560690209130"><img src="media/parkour-previz.webp" width="440" alt="High-Speed Parkour Motion Previz — Remotion motion previz demo"></a>

🎬 **[观看完整视频 →](https://x.com/Kashiko_AIart/status/2096096560690209130)**

#### 📖 说明

目前公开的最完整的 Astra × Remotion 提示词（约 223 赞 / 149 收藏）。它的价值不在题材，而在于**交付物清单、物理接触校验，以及「摄影机绝不能穿过角色」这条约束**。后来被 [@Naonekozamurai](https://x.com/Naonekozamurai) 逐字复用，并经 Topview MCP 送入 Seedance 2.5。

#### 📝 提示词

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
<summary>关键约束（非官方整理）</summary>

- 15 秒 / 横屏 / SD / 30fps / 无声 / 无外部素材 —— 只用简单的实体形状
- TypeScript + Remotion + `useCurrentFrame()` + 共享 3D 坐标系 + WebGL
- 角色：一个「i 字形」替身（球形头 + 胶囊躯干）；用前倾、起跳前压缩、落地下沉来传达动作
- **硬约束**：摄影机绝不能直接穿过角色；每个落地点都要有支撑面；同一帧必须永远得到同一状态
- **交付物**：MP4 + 可编辑源码 + 镜头 JSON + 重渲染步骤 + ffprobe/ffmpeg 校验
</details>

#### 📌 详情

- **作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart))
- **来源：** [x.com/Kashiko_AIart/status/2096096560690209130](https://x.com/Kashiko_AIart/status/2096096560690209130)
- **被复用：** [@Naonekozamurai](https://x.com/Naonekozamurai/status/2096871096759030114)
- **发布时间：** 2026-09-05
- **工具：** GPT-6 Astra, Remotion, TypeScript, WebGL

---

### 2：AdCar TV —— 在产品仓库里一次成片

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/d4m1n/status/2096258259459964963"><img src="media/adcar-tv.webp" width="440" alt="AdCar TV — 44s one-shot launch video"></a>

🎬 **[观看完整视频 →](https://x.com/d4m1n/status/2096258259459964963)**

#### 📖 说明

在**已有的产品仓库**里运行 —— Astra 把项目自带的 3D 查看器、音乐和引擎音效直接导入了 Remotion。当你手上已有素材时，这就是该照抄的模式：别从空文件夹开始。

#### 📝 提示词

```
can we create an overall video presenting the concept of AdCar TV?

make an intro video of 30-60s showing nice visuals (maybe the 3d of the car)?
and really cool car animations / branded stuff, showing off the site etc.
Use ffmpeg, remotion and qwen 3 tts for voice, and install whatever makes sense,
and come up with a cool artboard first and then make the video.
there is some music and car sounds in the codebase already.
```

> 作者备注：ffmpeg 主要用于把配音和音乐贴上去；Astra 把仓库里已有的 3D 直接拉进了 Remotion。

#### 📌 详情

- **作者：** Dan ⚡️ ([@d4m1n](https://x.com/d4m1n))
- **来源：** [x.com/d4m1n/status/2096258259459964963](https://x.com/d4m1n/status/2096258259459964963)
- **发布时间：** 2026-09-05
- **工具：** GPT-6 Astra, Remotion, ffmpeg, local Qwen 3 TTS

---

### 3：FeatureReveal —— 帧精确的合成契约

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 说明

这里最短的一条，也是做 SaaS 更新日志视频最好的起步骨架。每个动画都是**一个帧区间**，而不是含糊的描述 —— 这正是它可被构建、而非靠猜的原因。

#### 📝 提示词

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

#### 📌 详情

- **作者：** OpenReplay Team
- **来源：** [blog.openreplay.com/making-videos-claude-code-remotion](https://blog.openreplay.com/making-videos-claude-code-remotion/)
- **发布时间：** 2026-06-04
- **适用：** Claude Code, Codex, Astra
- **工具：** Remotion

---

### 4：女巫的初次飞行 —— 15 秒生成镜头脚本

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Mayz1169/status/2095873015007592679"><img src="media/witch-first-flight.webp" width="440" alt="Witch's First Flight — 15s generated shot"></a>

🎬 **[观看完整视频 →](https://x.com/Mayz1169/status/2095873015007592679)**

#### 📖 说明

**这是产出，不是输入** —— 一份 Astra *写出来*、交给视频模型的镜头脚本。作者说得很明确：*「我拿它来生成这段动画的提示词。」* 把它当作「好的生成镜头脚本长什么样」的范本来读：逐秒的节拍、角色一致性锁定，以及一长串负面清单。

#### 📝 提示词

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

#### 📌 详情

- **作者：** Kiki / Mayz ([@Mayz1169](https://x.com/Mayz1169))
- **来源：** [x.com/Mayz1169/status/2095873015007592679](https://x.com/Mayz1169/status/2095873015007592679) · [完整回复](https://x.com/Mayz1169/status/2095873204351070296)
- **发布时间：** 2026-09
- **工具：** GPT-6 Astra (as prompt writer) → video model

---

### 5：T 细胞 —— 一句话，五分钟

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/DeryaTR_/status/2095659170661904804"><img src="media/t-cells.webp" width="440" alt="T Cells — 5-minute explainer, one-line brief"></a>

🎬 **[观看完整视频 →](https://x.com/DeryaTR_/status/2095659170661904804)**

#### 📖 说明

转发最多的一个例子。用户提示词字面上只有一行。**这证明：极短的说明 + 已装好的 skill，胜过一大段提示词** —— 整套工具链是 Astra 自己选的。

#### 📝 提示词

```
Create a 5 minute educational video about T cells.
```

Astra 选择的编排方式（作者事后描述 —— 不是原始提示词，但可作为 skill 流程使用）：

```
Use the Remotion plugin for video generation.
Use Imagegen for visuals.
You may use HeyGen for narration.
Assemble the entire educational video one-shot,
including what to say and how to explain it.
```

#### 📌 详情

- **作者：** Derya Unutmaz, MD ([@DeryaTR_](https://x.com/DeryaTR_))
- **来源：** [x.com/DeryaTR_/status/2095659170661904804](https://x.com/DeryaTR_/status/2095659170661904804)
- **中文转发：** [@LinearUncle](https://x.com/LinearUncle/status/2095719251277701516)
- **发布时间：** 2026-09-03
- **工具：** GPT-6 Astra, Remotion plugin, Imagegen, HeyGen

---

### 6：六段式控制模板 + 镜头 JSON 契约

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 说明

一套适用于任何 Astra 任务的六段式可复用结构，外加一份可以交给生成器的 JSON 镜头契约。**Authority** 和 **Verification** 两段是大多数人会漏掉的 —— 而正是它们让智能体既不追问过多，也不交付残次品。

#### 📝 提示词

六段式控制模板：

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

镜头 JSON 契约：

```
Return valid JSON with project_summary and shots. Each shot must contain id,
story_purpose, framing, subject_action, camera, duration_seconds,
continuity_constraints and audio_cue. Total duration must equal 45 seconds.
```

60 秒短片：

```
Turn the premise below into a 60-second anime short. Preserve the theme and
character rules. Use 8–10 shots, one primary location and no crowd. Each shot
must change story information. Return logline, beat sheet, dialogue, shot table
and continuity checklist. Remove any beat that cannot be shown or heard.
```

#### 📌 详情

- **作者：** Elser AI
- **来源：** [elser.ai/blog/gpt-6-astra-prompt-guide](https://www.elser.ai/blog/gpt-6-astra-prompt-guide)
- **发布时间：** 2026-09
- **工具：** GPT-6 Astra

---

## 产品发布与营销

### Atomik —— 33 秒发布片

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/makwanatejas170/status/2096555742597988400"><img src="media/atomik-launch.webp" width="440" alt="Atomik — 33s launch film"></a>

🎬 **[观看完整视频 →](https://x.com/makwanatejas170/status/2096555742597988400)**

> 用自制 `motion-flavor` skill 一次成片的发布视频，该 skill 同时支持 HyperFrames 和 Remotion。聊天里那句提示词从未公开；公开的是可复现的工程实现。

X 帖子原文：

```
GPT-6 Astra one-shot this launch video for @atomikgrowth
with New motion-flavor skill that i made
works on both @HyperFrames_ & @Remotion
```

来自仓库的规格说明 —— 可作为交给智能体的验收契约：

```
Build a 33-second launch film in Remotion + React + TypeScript + CSS/SVG.
1920×1080, 60 fps, 1980 frames, H.264/AAC.
Rocket, layouts, cursor, typography and transitions must be rendered from code.
Portfolio imagery and soundtrack are bundled local media.
Do not hide a finished-video layer inside the composition.
No AI API call is required to render.
Output: out/final-render.mp4
```

**作者：** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **来源：** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [源码仓库](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **发布时间：** 2026-09 | **工具：** Astra, Remotion, HyperFrames

---

### video-shotcraft —— 电影感产品视频 skill

![ZH](https://img.shields.io/badge/lang-ZH-yellow) ![full](https://img.shields.io/badge/invocations-full-success)

<a href="https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd"><img src="media/shotcraft-gallery-intro.webp" width="440" alt="video-shotcraft — 38s gallery intro, produced with the skill"></a>

🎬 **[观看完整视频 →](https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd)**

<a href="https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d"><img src="media/shotcraft-ink-press.webp" width="440" alt="Ink Press — the 36s promo template shipped with the skill"></a>

🎬 **[观看完整视频 →](https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d)**

> 157 张镜头配方卡 + Remotion 实现 + 成片模板。skill 本体是一份长文档；下面这些是用户侧的调用方式。

安装：

```
帮我安装这个 skill：https://github.com/Vincentwei1021/video-shotcraft
```
```bash
npx skills add Vincentwei1021/video-shotcraft
```

调用示例（摘自官方 README）：

```
用 video-shotcraft 给我的桌面产品做一支宣传片。
用 deck-deal-flyin 和 row-embed 两张镜头卡展示这个功能。
参考 spotlight-hero-card，为这个页面设计一个产品特写镜头。
```
```
用 video-shotcraft 的 Ink Press 模板给我的产品做一支宣传片。
```

<details>
<summary>Skill frontmatter（决定智能体何时激活它）</summary>

```yaml
name: video-shotcraft
description: Create cinematic product videos from shot recipe cards, a validated
template, and code/audio assets (Remotion + real page screenshots + 2.5D camera
moves + beat-synced cuts + sound design). Use when the user asks to turn a
frontend project or webpage into a product video, says "use video-shotcraft to
make a video/promo", names the Ink Press template or asks to reproduce its
effect, or wants a single shot card's motion.
```

三种互斥模式：直接套用 Ink Press 模板 · 全自动创作（按 `references/pipeline.md` 一路做到成片，中途不询问）· 协作式（逐步确认需求 / 视觉方向 / 镜头清单）。

硬性约束：真实页面必须使用截图，绝不能手绘假的 UI；字体和颜色必须映射自产品的设计 token，而不是套一层通用的「宣传皮肤」。
</details>

**作者：** Vincentwei1021 | **来源：** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **工具：** Remotion, Astra, Claude Code, Codex

---

### Montage —— 为智能体而生的发布片脚手架

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 一个为智能体打造的 Remotion 分支，目标场景是产品发布片。

它的 README 让你对智能体这样说：

```
Create a master sequence in a new folder and start creating.
Copy any of the examples to get started.
Reference AGENTS.md and leverage all animations possible.
Replace background primitives and the logo with our branding.
```

AGENTS.md 里值得抄走的规则：

```
Do NOT one-shot all sections at once without viewing them.
Build one section → register it → render key frames → verify → next section.
Every frame should have something animating.
Never use flat backgroundColor — always layer vignette + grain + corner glow.
Do NOT default to useLetterPopIn for every text entrance.
Use SF Pro Display. Never use Geist or Inter.
After every change: render stills at entrance / mid / settled, inspect, then MP4.
```

**作者：** simplexlabs | **来源：** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **工具：** Remotion

<a href="https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f"><img src="media/montage-launch-film.webp" width="440" alt="Montage — launch film rendered by the agent"></a>

🎬 **[观看完整视频 →](https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f)**

---

### Remotion 官方 skill 调用方式

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 官方的斜杠命令。社区里大多数提示词都默认它们已经装好。

在全新项目上给编程智能体的初始化指令：

```
Ensure Node.js is installed.
Install Remotion Skills:
npx -y skills@latest add remotion-dev/skills -g -y
Then use them to create a video.
```

调用示例：

```
/remotion-create Make a promo video for a record store
/remotion-markup Create an animated title card using Inter
/remotion-maps Animate a route from Los Angeles to New York and make the camera follow it
/remotion-render
/remotion-studio
```

可用 skill：`remotion-best-practices`（路由）、`remotion-create`、`remotion-markup`、`remotion-studio`、`remotion-render`、`remotion-maps`、`remotion-captions`、`remotion-saas`、`remotion-interactivity`、`remotion-docs`、`remotion-upgrade`、`remotion-multimedia`。

**作者：** Remotion | **来源：** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **工具：** Remotion

---

### 依然管用的极简指令

![Mixed](https://img.shields.io/badge/lang-mixed-lightgrey) ![partial](https://img.shields.io/badge/text-partial-orange)

> 极简指令。用来看「最少能少到什么程度」很有参考价值 —— 但不要当契约用。

```
游戏做好了，用 remotion 做个好看的 CM
```
**作者：** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **来源：** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)

<a href="https://x.com/guuchacha149182/status/2096813471463882947"><img src="media/game-cm.webp" width="440" alt="Game CM — one-prompt Remotion promo"></a>

🎬 **[观看完整视频 →](https://x.com/guuchacha149182/status/2096813471463882947)**

```
根据最近的 changelog 比较亮眼的功能做个视频。
```
**作者：** [@leon7hao](https://x.com/leon7hao) | **来源：** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **备注：** GPT-6-Astra medium，未安装 skill —— 作者反馈效果明显偏弱

<a href="https://x.com/leon7hao/status/2096844989900914865"><img src="media/changelog-video.webp" width="440" alt="Changelog video — no skill installed, weaker result"></a>

🎬 **[观看完整视频 →](https://x.com/leon7hao/status/2096844989900914865)**

只发了成果、没发提示词的：[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)（BrandNewStudy 营销视频，一次成片）· [@stoufax](https://x.com/stoufax/status/2096311328600113222)（iOS 应用发布，Remotion + ElevenLabs）· [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)（`/goal` + fal 配音 + Remotion 插件，90 秒走查）

**@NickYang130 —— BrandNewStudy 营销视频，一次成片**

<a href="https://x.com/NickYang130/status/2096835902047932521"><img src="media/brandnewstudy-promo.webp" width="440" alt="BrandNewStudy marketing video, one-shot"></a>

🎬 **[观看完整视频 →](https://x.com/NickYang130/status/2096835902047932521)**

**@stoufax —— iOS 应用发布，Remotion + ElevenLabs**

<a href="https://x.com/stoufax/status/2096311328600113222"><img src="media/ios-app-launch.webp" width="440" alt="iOS app launch — Remotion + ElevenLabs"></a>

🎬 **[观看完整视频 →](https://x.com/stoufax/status/2096311328600113222)**

---

## 运动预演 → 生成

> 这一族不是在为视频模型描述画面。它先让 Astra 用 Remotion 渲染出一段 **control MP4**，再把它交给 Seedance 之类的模型作为运动参考。在日本圈子里，这正越来越成为主流的第二环。

### Seedance 交接指令

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Naonekozamurai/status/2096871096759030114"><img src="media/seedance-handoff.webp" width="440" alt="Remotion previz control MP4 handed to Seedance 2.5"></a>

🎬 **[观看完整视频 →](https://x.com/Naonekozamurai/status/2096871096759030114)**

> 当你把 Remotion 渲染结果喂给生成模型时，该怎么说。如果不明确授权它修正，模型会忠实地复制你那个占位替身的所有缺陷。

```
Remotionで作成した動画はあくまで動きを参照するだけの動画。
参照動画で不自然な挙動や不自然な女の子の体勢は、動画化の際にどんどん修正して良い。
動画では、前後のつながり、動画としてのかっこよさを重視してほしい。
```

<details>
<summary>英文（非官方）</summary>

```
The video made with Remotion is purely a reference for movement.
Any unnatural behavior or unnatural poses of the girl in the reference video
may be freely corrected during video generation.
In the video, prioritize continuity between shots and how good it looks as a video.
```
</details>

**作者：** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **来源：** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **发布时间：** 2026-09 | **工具：** Remotion → Seedance 2.5（经 Topview MCP）

---

### 超高速疾走 control MP4

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2094182215894831283"><img src="media/sprint-control.webp" width="440" alt="Ultra-high-speed sprint control MP4"></a>

🎬 **[观看完整视频 →](https://x.com/Kashiko_AIart/status/2094182215894831283)**

> 注意那条防作弊条款：铺一条真正长长的路并真实地向前推进，而不是循环一张背景。而且**人物与网格必须使用同一套 3D 坐标系和相机投影** —— 不允许用只是缩放 2D 素材的假相机。

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

**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **来源：** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **工具：** Astra, Remotion

---

### 横版追逐，附帧表

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2093692302745383041"><img src="media/side-scroll-chase.webp" width="440" alt="Side-scrolling chase with a frame table"></a>

🎬 **[观看完整视频 →](https://x.com/Kashiko_AIart/status/2093692302745383041)**

> 全集里帧精度最高的一条：每个跑酷动作都分配了明确的帧区间，并写清了半开区间的语义。

```
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **来源：** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **工具：** Astra, Remotion

---

### 30 种相机构图 —— 参考图生成器

![JA](https://img.shields.io/badge/lang-JA-red) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/Kashiko_AIart/status/2093575541916061984"><img src="media/camera-comps-30.webp" width="440" alt="30 camera compositions reference sheet"></a>

🎬 **[观看完整视频 →](https://x.com/Kashiko_AIart/status/2093575541916061984)**

> 生成一份可浏览的相机构图目录，之后跟视频模型对话时就能按 ID 直接引用。

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

> ⚠️ 原帖在输出要求之后还有内容；这里只引用可见的部分。

**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **来源：** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **工具：** Astra, Remotion, HTML/CSS/SVG

> 同一位作者还公开了一套 *chanbara*（剑戟）流程 —— [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— 但只有方法，没有提示词：1）只标相机与角色位置的最小镜头表，2）特效样张表，3）用提示词控制的精细动作。

<a href="https://x.com/Kashiko_AIart/status/2096533732547264921"><img src="media/chanbara.webp" width="440" alt="Chanbara sword-fight motion previz"></a>

🎬 **[观看完整视频 →](https://x.com/Kashiko_AIart/status/2096533732547264921)**

---

## 端到端制作

### 从想法 → 可直接上传的 YouTube 视频

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

> 约 50 分钟，API 成本大约 60 美元。真正吃重的是那句「不接受草稿」。

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

同一位作者，用 152GB 活动素材做的花絮混剪：

```
Create me a sizzle reel recap that's a minute long from this event.
```

> ⚠️ 由视频旁白转写而来 —— 官方没有提供可直接复制的文本块。

**作者：** Nate Herk | **来源：** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [花絮混剪](https://www.youtube.com/watch?v=QhmhUgccaS0) | **工具：** Astra, HeyGen, ElevenLabs, HyperFrames

---

### 旁白优先的图解视频

![EN](https://img.shields.io/badge/lang-EN-blue) ![spec-only](https://img.shields.io/badge/text-spec--only-lightgrey)

> 完全不用生成视频素材。先录音，再按量好的旁白节点把画面做出来。

流程：

```
1. write and record the explanation
2. mark the moments where the picture needs to change
3. ask Astra to build those moments with shapes, labels and motion in Remotion
4. add captions timed to the recording
5. render and watch with sound
```

公开的短指令：

```
Use this image for the scene, plan the framing around the measured narration cues,
keep important details visible and stop the movement while the viewer reads the label
```

```
Bring the result on screen when the recording names it,
shorten the entrance animation and preserve the time needed to read the final state
```

> ⚠️ 作者的 10 条 Master Prompts 在付费包里，从未公开发布。这里只收录公开的那点骨架。

**作者：** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **来源：** [x.com](https://x.com/foma_on_x/status/2096845194788217049) 及后续帖子 | **工具：** Astra, Remotion

---

## 元提示词：写提示词的提示词

### 导演 / 动画总监模板

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 产出一条可直接生产的提示词，*外加*一条负面提示词和三种兜底调整 —— 最后这项是大多数模板会漏掉的。

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

**作者：** The AI Average | **来源：** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **工具：** GPT-6 Astra

---

## 邻近领域：Blender 及其他

### Blender 8 秒产品转台

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 注意「先渲静帧再做整段」这一步 —— 这是发现相机轨迹走歪最省成本的办法。

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

**作者：** Kingy.ai | **来源：** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **工具：** Blender, Astra

---

### 已知但未公开

> 确认存在，但没有公开的一手来源。**只登记，绝不复原。**

| 什么 | 谁 | 状态 |
|---|---|---|
| 物理 / 软体运动 skill —— 丢掉 Remotion/HyperFrames 的淡入卡片，改用物理质感与软体力，4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | 已预告，skill 未发布 |
| Higgsfield + Blender 预演 + Seedance 2.5 剑戟流程 | 仅有二手媒体报道 | 非一手来源 |
| `motion-flavor` skill 源码 | [@makwanatejas170](https://x.com/makwanatejas170) | 未单独发布 |
| 面向图解视频的 10 条 Master Prompts | [@foma_on_x](https://x.com/foma_on_x) | 付费包 |
| 《Remotion 制作 8 本の裏側》长文笔记 | [@chikaidev](https://x.com/chikaidev) | 尚未转写 |
| 回复中声称的 5 条运动提示词 | [@dawoodkhan254](https://x.com/dawoodkhan254) | 只是声称，从未贴出 |

**物理 / 软体运动的演示视频本身是公开的**（skill 不是）：

<a href="https://x.com/paojiaofty/status/2096830622341976467"><img src="media/physics-motion.webp" width="440" alt="Physics / soft-body motion — 4K60 direct output"></a>

🎬 **[观看完整视频 →](https://x.com/paojiaofty/status/2096830622341976467)**

---

## Skill 与工具

这里每个人都在给 Astra 喂同一层底座。我们只给链接，不代为分发。

| 工具 | 安装 / 链接 | 用途 |
|---|---|---|
| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | 几乎所有案例底下的那一层 |
| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | 粘进 `SKILL.md` / `AGENTS.md` —— 不是给用户用的任务提示词 |
| **Remotion Studio WebMCP** | 4.0.518+ | 智能体直接读取选区/时间线/几何信息，不用靠点截图 |
| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 张镜头配方卡 + 模板 |
| **Montage** | [github](https://github.com/simplexlabs/montage) | 面向智能体的 Remotion 分支，做发布片 |
| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | 可复现的发布片源码 |
| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | 更广的社区清单 |

---

## 社区学到了什么

上面每一条线索里反复出现的规律：

**先把 skill 装好，再开口。** 不装 skill 时，一条更新日志视频做出来「明显差口气」；装好之后，一次成片就成了常态。

**要交付物，不要感觉。** 本集最强的一条（かし子的）结尾就是：MP4 + 可编辑源码 + 镜头 JSON + 重渲染步骤 + ffprobe 校验。

**把时间轴对齐到旁白，而不是「整体再快一点」。** Foma 的解法是点明那个瞬间：*当旁白说到结果时，画面必须已经在那里了。*

**在产品仓库里跑，胜过空文件夹。** AdCar、Atomik 和那条游戏 CM 都把已有素材拉了进来。

**Remotion 做预演、生成模型出成片**，正在成为日本圈子的标准第二环。

**Astra 最强的地方是编排和重构** —— [@paojiaofty](https://x.com/paojiaofty) 宁可直接推翻整个框架，也不接受淡入卡片式的做法。

**大家开始在「一次成片」这个说法上要求公开信息：** 空仓库还是已有项目？哪个推理档位？重试了几次？skill 事先装了吗？值得设成必填字段。

---

## 完整度表

| ID | 类型 | 作者 | 有全文？ |
|---|---|---|---|
| AdCar TV | 产品发布 | [@d4m1n](https://x.com/d4m1n) | ✅ |
| Atomik | 产品发布 | [@makwanatejas170](https://x.com/makwanatejas170) | 规格有，聊天提示词无 |
| video-shotcraft | 产品宣传 skill | Vincentwei1021 | 调用有，skill 本体很长 |
| Montage | 发布片脚手架 | simplexlabs | AGENTS.md 规则 |
| FeatureReveal | 功能视频 | OpenReplay | ✅ |
| Remotion 官方 | 调用示例 | Remotion | ✅（极短） |
| 跑酷预演 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 疾走 control MP4 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 横版追逐 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 30 种相机构图 | 参考图 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |
| Seedance 交接 | 交接指令 | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |
| T 细胞 | 科普视频 | [@DeryaTR_](https://x.com/DeryaTR_) | ✅（一行） |
| Nate 的 YouTube | 频道视频 | Nate Herk | 转写 |
| Foma 图解 | 图解视频 | [@foma_on_x](https://x.com/foma_on_x) | 仅有短指令 |
| 女巫首飞 | 生成镜头脚本 | [@Mayz1169](https://x.com/Mayz1169) | ✅ |
| 六段式 + JSON | 元提示词 | Elser AI | ✅ |
| 导演模板 | 元提示词 | The AI Average | ✅ |
| Blender 转台 | 3D 产品 | Kingy.ai | ✅ |
| 物理运动 skill | skill | [@paojiaofty](https://x.com/paojiaofty) | 未公开 |

---

## 关注名单

一个 GitHub Action 每 6 小时检查这些账号，一旦发现看起来像视频提示词的帖子就自动开 Issue。

| 账号 | 原因 |
|---|---|
| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | 最长的 Remotion 运动预演提示词出处 |
| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion 预演 → Seedance，实操派 |
| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |
| [@paojiaofty](https://x.com/paojiaofty) | 已预告的物理运动 skill |
| [@foma_on_x](https://x.com/foma_on_x) | 图解视频工作流 |
| [@DeryaTR_](https://x.com/DeryaTR_) | 一行式需求 |
| [@d4m1n](https://x.com/d4m1n) | 在仓库内一次成片 |
| [@TROOVY](https://x.com/TROOVY) | 专业动态设计工作室视角 |

[推荐要关注的账号 →](../../issues/new?template=watch-account.yml)

---

## 如何投稿

**[→ 提交一条提示词](../../issues/new?template=new-prompt.yml)** —— 粘贴内容、附上来源链接即可，不需要会 git。

每个条目都需要三样东西：

| 字段 | 为什么 |
|---|---|
| **作者** | 名字或 ID，按他们自己写的方式写 |
| **来源** | 指向原帖、串、博客或视频的直接链接 |
| **发布时间** | 日期，方便读者判断时效性 |

**规则：**

- **逐字引用。** 不要整理、不要改写、不要「优化」。
- **保留原始语言。** 可以在 `<details>` 块里附上译文并标注为非官方 —— 但绝不能替换原文。
- **绝不编造缺失的部分。** 如果截图只截到半条提示词，就标 `partial`，只引用可见的部分。
- **官方文档只给链接，不要复制。** 它们的 API 会变，这里放一份过期的副本只会误导人。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可与致谢

仓库结构、编辑说明与脚本：[CC BY 4.0](LICENSE)。

**提示词的版权仍归各作者所有。** 此处引用均标注了出处并附原链接，用于参考与研究。

感谢所有公开构建智能体驱动视频的人 —— [かし子](https://x.com/Kashiko_AIart)、[なお](https://x.com/Naonekozamurai)、[Dan](https://x.com/d4m1n)、[Tejas](https://x.com/makwanatejas170)、[Foma](https://x.com/foma_on_x)、[Derya Unutmaz](https://x.com/DeryaTR_)、[Kiki](https://x.com/Mayz1169)、Nate Herk、OpenReplay、Elser AI、The AI Average、Kingy.ai、Vincentwei1021、simplexlabs，以及 Remotion 团队。

**你是其中一员吗？**[提交 issue](../../issues/new?template=correction.yml) 即可更正署名、补上你的完整提示词，或要求移除你的作品。我们会无条件处理。

---

<div align="center">

如果这份清单对你有用，⭐ **给仓库点个 Star** —— 别人就是这样找到它的。

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="32"></picture></a>

[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)

</div>
