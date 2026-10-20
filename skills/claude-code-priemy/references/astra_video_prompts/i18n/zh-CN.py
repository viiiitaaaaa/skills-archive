# -*- coding: utf-8 -*-
"""Simplified Chinese translation table for README.md.

Keys are the exact source units from README.md. Values are the translation.
Anything not listed here is either a fenced code block (never touched) or
gets the REPLACE treatment below.
"""

TOC_TITLE = "目录"

SWITCHER = (
    '<p><a href="README.md">English</a> · <strong>中文</strong> · '
    '<a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · '
    '<a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>'
)

NOTICE = (
    "> 📄 **这是 README.md 的中文译本。** 所有提示词均按作者发布时的原始语言"
    "逐字保留、不作翻译；目录、说明、统计、投稿规则等编辑性文字为译本。"
    "两者若有出入，以[英文原版](README.md)为准。"
)

REPLACE = [
    ("**Author:**", "**作者：**"),
    ("**Source:**", "**来源：**"),
    ("**Published:**", "**发布时间：**"),
    ("**Tools:**", "**工具：**"),
    ("**Reused by:**", "**被复用：**"),
    ("**Works with:**", "**适用：**"),
    ("**Chinese relay:**", "**中文转发：**"),
    ("**Note:**", "**备注：**"),
    ("**Rules:**", "**规则：**"),
    ("**Are you one of them?**", "**你是其中一员？**"),
    ("🎬 **[Watch the full video →](", "🎬 **[观看完整视频 →]("),
    ("[source repo](", "[源码仓库]("),
    ("[sizzle reel](", "[花絮混剪]("),
    ("[full reply](", "[完整回复]("),
    (" and following posts", " 及后续帖子"),
]

SKIP = {
    "# Awesome Astra Video Prompts",
    "[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)",
}

BLOCKS = {
    # ── LuxReal house CTA (rendered at the top of README.md) ─────────────
    "**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**":
        "**本项目由 LuxReal 维护** —— AI 短剧流水线：输入剧本，产出场景与角色一致、全流程可编辑的成片。**[免费试用 →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**",
    # ── hero ──────────────────────────────────────────────────────────────
    "**Real prompts for making video with GPT-6 Astra and coding agents.**":
        "**用 GPT-6 Astra 与编程智能体做视频的真实提示词合集。**",

    "Astra doesn't output video. It writes code and drives tools —\n"
    "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg":
        "Astra 不直接输出视频。它写代码、驱动工具 ——\n"
        "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg",

    # ── notices ───────────────────────────────────────────────────────────
    "> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.":
        "> ⚠️ **版权声明**：所有提示词均收集自公开的社区帖子，用于学习研究，并标注原作者。"
        "若你认为任何内容侵犯了你的权益，请[提交 issue](../../issues/new)，我们会尽快移除。",

    "> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.":
        "> 🎬 **关于预览动图**：`media/` 下的动画片段是各作者**公开发布的演示视频**的短小、"
        "低分辨率摘录，仅作为提示词旁的参考，并始终链回原帖。它们是摘录，而非完整视频的再分发。"
        "如果你是作者并希望移除自己的片段，请[提交 issue](../../issues/new?template=correction.yml)，"
        "我们会无条件删除。",

    # ── contents ──────────────────────────────────────────────────────────
    "## Table of Contents": "## 目录",
    "- [What is this?](#what-is-this)\n- [Quick Start](#quick-start)\n- [Statistics](#statistics)\n- [Featured Prompts](#featured-prompts)\n- [Product Launch & Marketing](#product-launch--marketing)\n- [Motion Previz → Generative](#motion-previz--generative)\n- [End-to-End Production](#end-to-end-production)\n- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)\n- [Adjacent: Blender & Others](#adjacent-blender--others)\n- [Skills & Tooling](#skills--tooling)\n- [What the Community Learned](#what-the-community-learned)\n- [Completeness Table](#completeness-table)\n- [Watch List](#watch-list)\n- [How to Contribute](#how-to-contribute)\n- [License & Acknowledgements](#license--acknowledgements)":
        "@@TOC@@",

    # ── what is this ──────────────────────────────────────────────────────
    "## What is this?": "## 这是什么？",

    "Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:":
        "Astra 并不原生渲染视频。**它写代码、编排插件、操作电脑。** 成片来自：",

    "- **Remotion / HyperFrames** — programmatic motion graphics\n"
    "- **Remotion motion previz → Seedance** and other generative models\n"
    "- **Blender previs** → render or generate\n"
    "- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly":
        "- **Remotion / HyperFrames** —— 程序化动态图形\n"
        "- **Remotion 运动预演 → Seedance** 及其他生成模型\n"
        "- **Blender 预演** → 渲染或生成\n"
        "- **HeyGen / ElevenLabs / ffmpeg** —— 旁白与合成",

    "That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.":
        "因此，给它写提示词与写一句「文生视频咒语」有本质区别。你是在下达一份构建指令，"
        "而不是描述一张画面。",

    "**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.":
        "**本仓库把这些提示词逐字收录，并标注出处。** 付费包与私有 skill 只留占位符 —— "
        "从未公开的内容，我们绝不复原。",

    # ── quick start ───────────────────────────────────────────────────────
    "## Quick Start": "## 快速开始",

    "Then paste any prompt below into Astra, Claude Code, or Codex.":
        "然后把下面任意一条提示词粘贴到 Astra、Claude Code 或 Codex 里。",

    "**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.":
        "**第一次来？** 从 [FeatureReveal](#@@A3@@) 开始 —— 它是最短的一条，"
        "也最能说明为什么帧号很重要。",

    # ── statistics ────────────────────────────────────────────────────────
    "## Statistics": "## 统计",

    "| | |\n|---|---|\n| **Entries** | 24 |\n| **Full text available** | 17 |\n| **Languages** | EN · JA · ZH |\n| **Preview clips** | 18 (animated WebP, `media/`) |\n| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |\n| **Last updated** | 2026-09-10 |":
        "| | |\n|---|---|\n| **条目数** | 24 |\n| **全文可得** | 17 |\n"
        "| **语言** | EN · JA · ZH |\n| **预览片段** | 18（动画 WebP，见 `media/`） |\n"
        "| **译本** | 中文 · 日本語 · 한국어 · Español · Français |\n"
        "| **最后更新** | 2026-09-10 |",

    "`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only":
        "`full` —— 与发布时一致完整 · `partial` —— 只有一部分 · "
        "`spec-only` —— 描述了方法，措辞从未公开 · `unpublished` —— 已知存在，仅有占位符",

    # ── featured ──────────────────────────────────────────────────────────
    "## Featured Prompts": "## 精选提示词",
    "#### 📖 Description": "#### 📖 说明",
    "#### 📝 Prompt": "#### 📝 提示词",
    "#### 📌 Details": "#### 📌 详情",

    "### 1: High-Speed Parkour Motion Previz": "### 1：高速跑酷运动预演",

    "The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the \"camera must not pass through the character\" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.":
        "目前公开的最完整的 Astra × Remotion 提示词（约 223 赞 / 149 收藏）。它的价值不在题材，"
        "而在于**交付物清单、物理接触校验，以及「摄影机绝不能穿过角色」这条约束**。"
        "后来被 [@Naonekozamurai](https://x.com/Naonekozamurai) 逐字复用，"
        "并经 Topview MCP 送入 Seedance 2.5。",

    "<details>\n<summary>Key constraints, summarized (unofficial)</summary>":
        "<details>\n<summary>关键约束（非官方整理）</summary>",

    "- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only\n"
    "- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL\n"
    "- Character: one \"i-shaped\" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing\n"
    "- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state\n"
    "- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification\n"
    "</details>":
        "- 15 秒 / 横屏 / SD / 30fps / 无声 / 无外部素材 —— 只用简单的实体形状\n"
        "- TypeScript + Remotion + `useCurrentFrame()` + 共享 3D 坐标系 + WebGL\n"
        "- 角色：一个「i 字形」替身（球形头 + 胶囊躯干）；用前倾、起跳前压缩、落地下沉来传达动作\n"
        "- **硬约束**：摄影机绝不能直接穿过角色；每个落地点都要有支撑面；同一帧必须永远得到同一状态\n"
        "- **交付物**：MP4 + 可编辑源码 + 镜头 JSON + 重渲染步骤 + ffprobe/ffmpeg 校验\n"
        "</details>",

    "### 2: AdCar TV — In-Repo One-Shot Launch Video":
        "### 2：AdCar TV —— 在产品仓库里一次成片",

    "Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.":
        "在**已有的产品仓库**里运行 —— Astra 把项目自带的 3D 查看器、音乐和引擎音效直接导入了 "
        "Remotion。当你手上已有素材时，这就是该照抄的模式：别从空文件夹开始。",

    "> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.":
        "> 作者备注：ffmpeg 主要用于把配音和音乐贴上去；Astra 把仓库里已有的 3D 直接拉进了 Remotion。",

    "### 3: FeatureReveal — Frame-Exact Composition Contract":
        "### 3：FeatureReveal —— 帧精确的合成契约",

    "The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.":
        "这里最短的一条，也是做 SaaS 更新日志视频最好的起步骨架。每个动画都是**一个帧区间**，"
        "而不是含糊的描述 —— 这正是它可被构建、而非靠猜的原因。",

    "### 4: Witch's First Flight — 15s Generated Shot Script":
        "### 4：女巫的初次飞行 —— 15 秒生成镜头脚本",

    "**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *\"I used it to create the prompt for this animation.\"* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.":
        "**这是产出，不是输入** —— 一份 Astra *写出来*、交给视频模型的镜头脚本。作者说得很明确："
        "*「我拿它来生成这段动画的提示词。」* 把它当作「好的生成镜头脚本长什么样」的范本来读："
        "逐秒的节拍、角色一致性锁定，以及一长串负面清单。",

    "### 5: T Cells — One Sentence, Five Minutes": "### 5：T 细胞 —— 一句话，五分钟",

    "The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.":
        "转发最多的一个例子。用户提示词字面上只有一行。**这证明：极短的说明 + 已装好的 skill，"
        "胜过一大段提示词** —— 整套工具链是 Astra 自己选的。",

    "The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):":
        "Astra 选择的编排方式（作者事后描述 —— 不是原始提示词，但可作为 skill 流程使用）：",

    "### 6: Six-Part Control Template + Shot JSON Contract":
        "### 6：六段式控制模板 + 镜头 JSON 契约",

    "A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.":
        "一套适用于任何 Astra 任务的六段式可复用结构，外加一份可以交给生成器的 JSON 镜头契约。"
        "**Authority** 和 **Verification** 两段是大多数人会漏掉的 —— 而正是它们让智能体既不追问过多，"
        "也不交付残次品。",

    "Six-part control template:": "六段式控制模板：",
    "Shot JSON contract:": "镜头 JSON 契约：",
    "60-second short:": "60 秒短片：",

    # ── product launch ────────────────────────────────────────────────────
    "## Product Launch & Marketing": "## 产品发布与营销",

    "### Atomik — 33-Second Launch Film": "### Atomik —— 33 秒发布片",

    "> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.":
        "> 用自制 `motion-flavor` skill 一次成片的发布视频，该 skill 同时支持 HyperFrames 和 "
        "Remotion。聊天里那句提示词从未公开；公开的是可复现的工程实现。",

    "X post, verbatim:": "X 帖子原文：",

    "Spec from the repo — useful as an acceptance contract for an agent:":
        "来自仓库的规格说明 —— 可作为交给智能体的验收契约：",

    "**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames":
        "**作者：** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | "
        "**来源：** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · "
        "[源码仓库](https://github.com/Tejashmakwana/astra-atomik-launch-video) | "
        "**发布时间：** 2026-09 | **工具：** Astra, Remotion, HyperFrames",

    "### video-shotcraft — Cinematic Product Video Skill":
        "### video-shotcraft —— 电影感产品视频 skill",

    "> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.":
        "> 157 张镜头配方卡 + Remotion 实现 + 成片模板。skill 本体是一份长文档；"
        "下面这些是用户侧的调用方式。",

    "Install:": "安装：",
    "Invocations (from the official README):": "调用示例（摘自官方 README）：",

    "<details>\n<summary>Skill frontmatter (determines when the agent activates it)</summary>":
        "<details>\n<summary>Skill frontmatter（决定智能体何时激活它）</summary>",

    "Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).":
        "三种互斥模式：直接套用 Ink Press 模板 · 全自动创作（按 `references/pipeline.md` "
        "一路做到成片，中途不询问）· 协作式（逐步确认需求 / 视觉方向 / 镜头清单）。",

    "Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic \"promo skin\".\n</details>":
        "硬性约束：真实页面必须使用截图，绝不能手绘假的 UI；字体和颜色必须映射自产品的设计 "
        "token，而不是套一层通用的「宣传皮肤」。\n</details>",

    "**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex":
        "**作者：** Vincentwei1021 | "
        "**来源：** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | "
        "**工具：** Remotion, Astra, Claude Code, Codex",

    "### Montage — Agent-Native Launch Video Scaffold":
        "### Montage —— 为智能体而生的发布片脚手架",

    "> A Remotion fork built for agents, aimed at product launch films.":
        "> 一个为智能体打造的 Remotion 分支，目标场景是产品发布片。",

    "What the README tells you to say to the agent:":
        "它的 README 让你对智能体这样说：",

    "The AGENTS.md rules worth stealing:": "AGENTS.md 里值得抄走的规则：",

    "**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion":
        "**作者：** simplexlabs | **来源：** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | "
        "**工具：** Remotion",

    "### Remotion Official Skill Invocations": "### Remotion 官方 skill 调用方式",

    "> The official slash commands. Most community prompts assume these are installed.":
        "> 官方的斜杠命令。社区里大多数提示词都默认它们已经装好。",

    "Bootstrap for a coding agent on a fresh project:":
        "在全新项目上给编程智能体的初始化指令：",

    "Invocations:": "调用示例：",

    "Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.":
        "可用 skill：`remotion-best-practices`（路由）、`remotion-create`、`remotion-markup`、"
        "`remotion-studio`、`remotion-render`、`remotion-maps`、`remotion-captions`、"
        "`remotion-saas`、`remotion-interactivity`、`remotion-docs`、`remotion-upgrade`、"
        "`remotion-multimedia`。",

    "**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion":
        "**作者：** Remotion | **来源：** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | "
        "**工具：** Remotion",

    "### Short Briefs That Still Worked": "### 依然管用的极简指令",

    "> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.":
        "> 极简指令。用来看「最少能少到什么程度」很有参考价值 —— 但不要当契约用。",

    "**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)":
        "**作者：** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | "
        "**来源：** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",

    "**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker":
        "**作者：** [@leon7hao](https://x.com/leon7hao) | "
        "**来源：** [x.com](https://x.com/leon7hao/status/2096844989900914865) | "
        "**备注：** GPT-6-Astra medium，未安装 skill —— 作者反馈效果明显偏弱",

    "Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)":
        "只发了成果、没发提示词的："
        "[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)"
        "（BrandNewStudy 营销视频，一次成片）· "
        "[@stoufax](https://x.com/stoufax/status/2096311328600113222)"
        "（iOS 应用发布，Remotion + ElevenLabs）· "
        "[@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)"
        "（`/goal` + fal 配音 + Remotion 插件，90 秒走查）",

    "**@NickYang130 — BrandNewStudy marketing video, one-shot**":
        "**@NickYang130 —— BrandNewStudy 营销视频，一次成片**",

    "**@stoufax — iOS app launch, Remotion + ElevenLabs**":
        "**@stoufax —— iOS 应用发布，Remotion + ElevenLabs**",

    # ── previz ────────────────────────────────────────────────────────────
    "## Motion Previz → Generative": "## 运动预演 → 生成",

    "> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.":
        "> 这一族不是在为视频模型描述画面。它先让 Astra 用 Remotion 渲染出一段 **control MP4**，"
        "再把它交给 Seedance 之类的模型作为运动参考。在日本圈子里，这正越来越成为主流的第二环。",

    "### Seedance Handoff Instruction": "### Seedance 交接指令",

    "> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.":
        "> 当你把 Remotion 渲染结果喂给生成模型时，该怎么说。如果不明确授权它修正，"
        "模型会忠实地复制你那个占位替身的所有缺陷。",

    "<details>\n<summary>English (unofficial)</summary>":
        "<details>\n<summary>英文（非官方）</summary>",

    "**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)":
        "**作者：** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | "
        "**来源：** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | "
        "**发布时间：** 2026-09 | **工具：** Remotion → Seedance 2.5（经 Topview MCP）",

    "### Ultra-High-Speed Sprint Control MP4": "### 超高速疾走 control MP4",

    "> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.":
        "> 注意那条防作弊条款：铺一条真正长长的路并真实地向前推进，而不是循环一张背景。"
        "而且**人物与网格必须使用同一套 3D 坐标系和相机投影** —— 不允许用只是缩放 2D 素材的假相机。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**来源：** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | "
        "**工具：** Astra, Remotion",

    "### Side-Scrolling Chase, with a Frame Table": "### 横版追逐，附帧表",

    "> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.":
        "> 全集里帧精度最高的一条：每个跑酷动作都分配了明确的帧区间，并写清了半开区间的语义。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**来源：** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | "
        "**工具：** Astra, Remotion",

    "### 30 Camera Compositions — Reference Sheet Generator":
        "### 30 种相机构图 —— 参考图生成器",

    "> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.":
        "> 生成一份可浏览的相机构图目录，之后跟视频模型对话时就能按 ID 直接引用。",

    "> ⚠️ The post continues past the output requirements; only what's visible is quoted.":
        "> ⚠️ 原帖在输出要求之后还有内容；这里只引用可见的部分。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**来源：** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | "
        "**工具：** Astra, Remotion, HTML/CSS/SVG",

    "> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.":
        "> 同一位作者还公开了一套 *chanbara*（剑戟）流程 —— "
        "[x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— "
        "但只有方法，没有提示词：1）只标相机与角色位置的最小镜头表，2）特效样张表，"
        "3）用提示词控制的精细动作。",

    # ── end to end ────────────────────────────────────────────────────────
    "## End-to-End Production": "## 端到端制作",

    "### Idea → Uploadable YouTube Video": "### 从想法 → 可直接上传的 YouTube 视频",

    "> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.":
        "> 约 50 分钟，API 成本大约 60 美元。真正吃重的是那句「不接受草稿」。",

    "Same author, sizzle reel from 152GB of event footage:":
        "同一位作者，用 152GB 活动素材做的花絮混剪：",

    "> ⚠️ Transcribed from the video's narration — no official paste block exists.":
        "> ⚠️ 由视频旁白转写而来 —— 官方没有提供可直接复制的文本块。",

    "**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames":
        "**作者：** Nate Herk | "
        "**来源：** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · "
        "[花絮混剪](https://www.youtube.com/watch?v=QhmhUgccaS0) | "
        "**工具：** Astra, HeyGen, ElevenLabs, HyperFrames",

    "### Narration-First Diagram Explainer": "### 旁白优先的图解视频",

    "> No generated footage at all. Record first, then build the picture to measured narration cues.":
        "> 完全不用生成视频素材。先录音，再按量好的旁白节点把画面做出来。",

    "Workflow:": "流程：",
    "Published short instructions:": "公开的短指令：",

    "> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.":
        "> ⚠️ 作者的 10 条 Master Prompts 在付费包里，从未公开发布。这里只收录公开的那点骨架。",

    "**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion":
        "**作者：** Foma ([@foma_on_x](https://x.com/foma_on_x)) | "
        "**来源：** [x.com](https://x.com/foma_on_x/status/2096845194788217049) 及后续帖子 | "
        "**工具：** Astra, Remotion",

    # ── meta ──────────────────────────────────────────────────────────────
    "## Meta: Prompts That Write Prompts": "## 元提示词：写提示词的提示词",

    "### Director / Animation Supervisor Template": "### 导演 / 动画总监模板",

    "> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.":
        "> 产出一条可直接生产的提示词，*外加*一条负面提示词和三种兜底调整 —— 最后这项是大多数模板会漏掉的。",

    "**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra":
        "**作者：** The AI Average | "
        "**来源：** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | "
        "**工具：** GPT-6 Astra",

    # ── adjacent ──────────────────────────────────────────────────────────
    "## Adjacent: Blender & Others": "## 邻近领域：Blender 及其他",

    "### Blender 8-Second Product Turntable": "### Blender 8 秒产品转台",

    "> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.":
        "> 注意「先渲静帧再做整段」这一步 —— 这是发现相机轨迹走歪最省成本的办法。",

    "**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra":
        "**作者：** Kingy.ai | "
        "**来源：** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | "
        "**工具：** Blender, Astra",

    "### Known but Unpublished": "### 已知但未公开",

    "> Confirmed to exist, no public primary source. **Listed, never reconstructed.**":
        "> 确认存在，但没有公开的一手来源。**只登记，绝不复原。**",

    "| What | Who | Status |\n|---|---|---|\n"
    "| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |\n"
    "| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |\n"
    "| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |\n"
    "| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |\n"
    "| \"Remotion 制作 8 本の裏側\" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |\n"
    "| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |":
        "| 什么 | 谁 | 状态 |\n|---|---|---|\n"
        "| 物理 / 软体运动 skill —— 丢掉 Remotion/HyperFrames 的淡入卡片，改用物理质感与软体力，4K60 "
        "| [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | 已预告，skill 未发布 |\n"
        "| Higgsfield + Blender 预演 + Seedance 2.5 剑戟流程 | 仅有二手媒体报道 | 非一手来源 |\n"
        "| `motion-flavor` skill 源码 | [@makwanatejas170](https://x.com/makwanatejas170) | 未单独发布 |\n"
        "| 面向图解视频的 10 条 Master Prompts | [@foma_on_x](https://x.com/foma_on_x) | 付费包 |\n"
        "| 《Remotion 制作 8 本の裏側》长文笔记 | [@chikaidev](https://x.com/chikaidev) | 尚未转写 |\n"
        "| 回复中声称的 5 条运动提示词 | [@dawoodkhan254](https://x.com/dawoodkhan254) | 只是声称，从未贴出 |",

    "**The physics / soft-body motion demo itself is public** (the skill is not):":
        "**物理 / 软体运动的演示视频本身是公开的**（skill 不是）：",

    # ── tooling ───────────────────────────────────────────────────────────
    "## Skills & Tooling": "## Skill 与工具",

    "Everyone here is feeding Astra the same base layer. We link, we don't vendor.":
        "这里每个人都在给 Astra 喂同一层底座。我们只给链接，不代为分发。",

    "| Tool | Install / Link | What it's for |\n|---|---|---|\n"
    "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |\n"
    "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |\n"
    "| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |\n"
    "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |\n"
    "| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |\n"
    "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |\n"
    "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |":
        "| 工具 | 安装 / 链接 | 用途 |\n|---|---|---|\n"
        "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | 几乎所有案例底下的那一层 |\n"
        "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) "
        "| 粘进 `SKILL.md` / `AGENTS.md` —— 不是给用户用的任务提示词 |\n"
        "| **Remotion Studio WebMCP** | 4.0.518+ | 智能体直接读取选区/时间线/几何信息，不用靠点截图 |\n"
        "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 张镜头配方卡 + 模板 |\n"
        "| **Montage** | [github](https://github.com/simplexlabs/montage) | 面向智能体的 Remotion 分支，做发布片 |\n"
        "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) "
        "| 可复现的发布片源码 |\n"
        "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | 更广的社区清单 |",

    # ── learned ───────────────────────────────────────────────────────────
    "## What the Community Learned": "## 社区学到了什么",

    "Patterns that show up across every thread above:":
        "上面每一条线索里反复出现的规律：",

    "**Install the skills first, then talk.** Without skills, a changelog video came out \"noticeably short of it\". With skills installed, one-shots became common.":
        "**先把 skill 装好，再开口。** 不装 skill 时，一条更新日志视频做出来「明显差口气」；"
        "装好之后，一次成片就成了常态。",

    "**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.":
        "**要交付物，不要感觉。** 本集最强的一条（かし子的）结尾就是：MP4 + 可编辑源码 + "
        "镜头 JSON + 重渲染步骤 + ffprobe 校验。",

    "**Align the timeline to narration, not \"make it faster overall.\"** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*":
        "**把时间轴对齐到旁白，而不是「整体再快一点」。** Foma 的解法是点明那个瞬间："
        "*当旁白说到结果时，画面必须已经在那里了。*",

    "**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.":
        "**在产品仓库里跑，胜过空文件夹。** AdCar、Atomik 和那条游戏 CM 都把已有素材拉了进来。",

    "**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.":
        "**Remotion 做预演、生成模型出成片**，正在成为日本圈子的标准第二环。",

    "**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.":
        "**Astra 最强的地方是编排和重构** —— [@paojiaofty](https://x.com/paojiaofty) "
        "宁可直接推翻整个框架，也不接受淡入卡片式的做法。",

    "**People are starting to demand disclosure on \"one-shot\" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.":
        "**大家开始在「一次成片」这个说法上要求公开信息：** 空仓库还是已有项目？"
        "哪个推理档位？重试了几次？skill 事先装了吗？值得设成必填字段。",

    # ── completeness ──────────────────────────────────────────────────────
    "## Completeness Table": "## 完整度表",

    "| ID | Type | Author | Full text? |\n|---|---|---|---|\n"
    "| AdCar TV | product launch | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
    "| Atomik | product launch | [@makwanatejas170](https://x.com/makwanatejas170) | spec yes, chat prompt no |\n"
    "| video-shotcraft | product promo skill | Vincentwei1021 | invocations yes, skill body long |\n"
    "| Montage | launch scaffold | simplexlabs | AGENTS.md rules |\n"
    "| FeatureReveal | feature video | OpenReplay | ✅ |\n"
    "| Remotion official | invocations | Remotion | ✅ (very short) |\n"
    "| Parkour previz | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
    "| Sprint control MP4 | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
    "| Side-scroll chase | motion previz | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
    "| 30 camera comps | reference sheet | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
    "| Seedance handoff | handoff | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
    "| T cells | explainer | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (one line) |\n"
    "| Nate YouTube | channel video | Nate Herk | transcribed |\n"
    "| Foma explainer | diagram video | [@foma_on_x](https://x.com/foma_on_x) | short instructions only |\n"
    "| Witch's flight | generated shot script | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
    "| Six-part + JSON | meta | Elser AI | ✅ |\n"
    "| Director template | meta | The AI Average | ✅ |\n"
    "| Blender turntable | 3D product | Kingy.ai | ✅ |\n"
    "| Physics motion skill | skill | [@paojiaofty](https://x.com/paojiaofty) | unpublished |":
        "| ID | 类型 | 作者 | 有全文？ |\n|---|---|---|---|\n"
        "| AdCar TV | 产品发布 | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
        "| Atomik | 产品发布 | [@makwanatejas170](https://x.com/makwanatejas170) | 规格有，聊天提示词无 |\n"
        "| video-shotcraft | 产品宣传 skill | Vincentwei1021 | 调用有，skill 本体很长 |\n"
        "| Montage | 发布片脚手架 | simplexlabs | AGENTS.md 规则 |\n"
        "| FeatureReveal | 功能视频 | OpenReplay | ✅ |\n"
        "| Remotion 官方 | 调用示例 | Remotion | ✅（极短） |\n"
        "| 跑酷预演 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 疾走 control MP4 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 横版追逐 | 运动预演 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 30 种相机构图 | 参考图 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
        "| Seedance 交接 | 交接指令 | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
        "| T 细胞 | 科普视频 | [@DeryaTR_](https://x.com/DeryaTR_) | ✅（一行） |\n"
        "| Nate 的 YouTube | 频道视频 | Nate Herk | 转写 |\n"
        "| Foma 图解 | 图解视频 | [@foma_on_x](https://x.com/foma_on_x) | 仅有短指令 |\n"
        "| 女巫首飞 | 生成镜头脚本 | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
        "| 六段式 + JSON | 元提示词 | Elser AI | ✅ |\n"
        "| 导演模板 | 元提示词 | The AI Average | ✅ |\n"
        "| Blender 转台 | 3D 产品 | Kingy.ai | ✅ |\n"
        "| 物理运动 skill | skill | [@paojiaofty](https://x.com/paojiaofty) | 未公开 |",

    # ── watch list ────────────────────────────────────────────────────────
    "## Watch List": "## 关注名单",

    "A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.":
        "一个 GitHub Action 每 6 小时检查这些账号，一旦发现看起来像视频提示词的帖子就自动开 Issue。",

    "| Account | Why |\n|---|---|\n"
    "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |\n"
    "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |\n"
    "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
    "| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |\n"
    "| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |\n"
    "| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |\n"
    "| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |\n"
    "| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |":
        "| 账号 | 原因 |\n|---|---|\n"
        "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | 最长的 Remotion 运动预演提示词出处 |\n"
        "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion 预演 → Seedance，实操派 |\n"
        "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
        "| [@paojiaofty](https://x.com/paojiaofty) | 已预告的物理运动 skill |\n"
        "| [@foma_on_x](https://x.com/foma_on_x) | 图解视频工作流 |\n"
        "| [@DeryaTR_](https://x.com/DeryaTR_) | 一行式需求 |\n"
        "| [@d4m1n](https://x.com/d4m1n) | 在仓库内一次成片 |\n"
        "| [@TROOVY](https://x.com/TROOVY) | 专业动态设计工作室视角 |",

    "[Suggest an account →](../../issues/new?template=watch-account.yml)":
        "[推荐要关注的账号 →](../../issues/new?template=watch-account.yml)",

    # ── contribute ────────────────────────────────────────────────────────
    "## How to Contribute": "## 如何投稿",

    "**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.":
        "**[→ 提交一条提示词](../../issues/new?template=new-prompt.yml)** —— 粘贴内容、附上来源链接即可，"
        "不需要会 git。",

    "Every entry needs three things:": "每个条目都需要三样东西：",

    "| Field | Why |\n|---|---|\n"
    "| **Author** | Name or handle, written the way they write it |\n"
    "| **Source** | Direct link to the post, thread, blog, or video |\n"
    "| **Published** | Date, so readers can judge how current it is |":
        "| 字段 | 为什么 |\n|---|---|\n"
        "| **作者** | 名字或 ID，按他们自己写的方式写 |\n"
        "| **来源** | 指向原帖、串、博客或视频的直接链接 |\n"
        "| **发布时间** | 日期，方便读者判断时效性 |",

    "- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.\n"
    "- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.\n"
    "- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.\n"
    "- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.":
        "- **逐字引用。** 不要整理、不要改写、不要「优化」。\n"
        "- **保留原始语言。** 可以在 `<details>` 块里附上译文并标注为非官方 —— 但绝不能替换原文。\n"
        "- **绝不编造缺失的部分。** 如果截图只截到半条提示词，就标 `partial`，只引用可见的部分。\n"
        "- **官方文档只给链接，不要复制。** 它们的 API 会变，这里放一份过期的副本只会误导人。",

    "See [CONTRIBUTING.md](CONTRIBUTING.md).": "详见 [CONTRIBUTING.md](CONTRIBUTING.md)。",

    # ── license ───────────────────────────────────────────────────────────
    "## License & Acknowledgements": "## 许可与致谢",

    "Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).":
        "仓库结构、编辑说明与脚本：[CC BY 4.0](LICENSE)。",

    "**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.":
        "**提示词的版权仍归各作者所有。** 此处引用均标注了出处并附原链接，用于参考与研究。",

    "Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.":
        "感谢所有公开构建智能体驱动视频的人 —— [かし子](https://x.com/Kashiko_AIart)、"
        "[なお](https://x.com/Naonekozamurai)、[Dan](https://x.com/d4m1n)、"
        "[Tejas](https://x.com/makwanatejas170)、[Foma](https://x.com/foma_on_x)、"
        "[Derya Unutmaz](https://x.com/DeryaTR_)、[Kiki](https://x.com/Mayz1169)、"
        "Nate Herk、OpenReplay、Elser AI、The AI Average、Kingy.ai、Vincentwei1021、"
        "simplexlabs，以及 Remotion 团队。",

    "**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.":
        "**你是其中一员吗？**[提交 issue](../../issues/new?template=correction.yml) 即可更正署名、"
        "补上你的完整提示词，或要求移除你的作品。我们会无条件处理。",


    "⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.":
        "如果这份清单对你有用，⭐ **给仓库点个 Star** —— 别人就是这样找到它的。",
}
