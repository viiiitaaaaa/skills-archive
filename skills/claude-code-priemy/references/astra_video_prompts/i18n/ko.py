# -*- coding: utf-8 -*-
"""Korean translation table for README.md."""

TOC_TITLE = "목차"

SWITCHER = (
    '<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · '
    '<a href="README.ja.md">日本語</a> · <strong>한국어</strong> · '
    '<a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>'
)

NOTICE = (
    "> 📄 **이 문서는 README.md의 한국어 번역입니다.** 모든 프롬프트는 작성자가 공개한 "
    "원문 그대로, 한 글자도 바꾸지 않고 실었으며 번역하지 않았습니다. 번역한 것은 목차·설명·"
    "통계·기여 규칙 등 편집 문장뿐입니다. 내용이 다를 경우 [영어 원문](README.md)을 기준으로 합니다."
)

REPLACE = [
    ("**Author:**", "**작성자:**"),
    ("**Source:**", "**출처:**"),
    ("**Published:**", "**게시일:**"),
    ("**Tools:**", "**도구:**"),
    ("**Reused by:**", "**재사용:**"),
    ("**Works with:**", "**호환:**"),
    ("**Chinese relay:**", "**중국어 재게시:**"),
    ("**Note:**", "**비고:**"),
    ("**Rules:**", "**규칙:**"),
    ("**Are you one of them?**", "**여러분도 그중 한 명인가요?**"),
    ("🎬 **[Watch the full video →](", "🎬 **[전체 영상 보기 →]("),
    ("[source repo](", "[소스 저장소]("),
    ("[sizzle reel](", "[하이라이트 영상]("),
    ("[full reply](", "[전체 답글]("),
    (" and following posts", " 및 이후 게시물"),
]

SKIP = {
    "# Awesome Astra Video Prompts",
    "[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)",
}

BLOCKS = {
    # ── LuxReal house CTA (rendered at the top of README.md) ─────────────
    "**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**":
        "**LuxReal이 운영·유지보수합니다** —— AI 숏드라마 파이프라인. 대본을 넣으면 장면과 인물의 일관성을 유지한 채 전 과정을 편집할 수 있는 영상이 나옵니다. **[무료로 시작하기 →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**",
    "**Real prompts for making video with GPT-6 Astra and coding agents.**":
        "**GPT-6 Astra와 코딩 에이전트로 영상을 만드는, 실제로 쓰인 프롬프트 모음.**",

    "Astra doesn't output video. It writes code and drives tools —\n"
    "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg":
        "Astra는 영상을 직접 출력하지 않습니다. 코드를 쓰고 도구를 움직입니다 ——\n"
        "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg",

    "> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.":
        "> ⚠️ **저작권 안내**: 모든 프롬프트는 공개 커뮤니티 게시물에서 수집했으며, 학습 목적으로 "
        "사용하고 원작자를 명시했습니다. 권리를 침해한다고 판단되면 "
        "[이슈를 열어](../../issues/new) 주세요. 즉시 삭제하겠습니다.",

    "> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.":
        "> 🎬 **미리보기 안내**: `media/` 아래의 애니메이션 클립은 각 작성자가 *공개한 데모 영상*에서 "
        "잘라낸 짧고 저해상도인 발췌본입니다. 프롬프트 옆에 참고용으로 두었고, 항상 원문 게시물로 "
        "연결됩니다. 발췌본이며 원본 영상을 재배포하는 것이 아닙니다. 작성자 본인이 삭제를 원하시면 "
        "[이슈를 열어](../../issues/new?template=correction.yml) 주세요. 이견 없이 삭제합니다.",

    "## Table of Contents": "## 목차",
    "- [What is this?](#what-is-this)\n- [Quick Start](#quick-start)\n- [Statistics](#statistics)\n- [Featured Prompts](#featured-prompts)\n- [Product Launch & Marketing](#product-launch--marketing)\n- [Motion Previz → Generative](#motion-previz--generative)\n- [End-to-End Production](#end-to-end-production)\n- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)\n- [Adjacent: Blender & Others](#adjacent-blender--others)\n- [Skills & Tooling](#skills--tooling)\n- [What the Community Learned](#what-the-community-learned)\n- [Completeness Table](#completeness-table)\n- [Watch List](#watch-list)\n- [How to Contribute](#how-to-contribute)\n- [License & Acknowledgements](#license--acknowledgements)":
        "@@TOC@@",

    "## What is this?": "## 이것은 무엇인가",

    "Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:":
        "Astra는 영상을 네이티브로 렌더링하지 않습니다. **코드를 쓰고, 플러그인을 엮고, "
        "컴퓨터를 조작합니다.** 완성된 영상은 다음에서 나옵니다:",

    "- **Remotion / HyperFrames** — programmatic motion graphics\n"
    "- **Remotion motion previz → Seedance** and other generative models\n"
    "- **Blender previs** → render or generate\n"
    "- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly":
        "- **Remotion / HyperFrames** —— 프로그램 방식의 모션 그래픽\n"
        "- **Remotion 모션 프리비즈 → Seedance** 및 기타 생성 모델\n"
        "- **Blender 프리비즈** → 렌더링 또는 생성\n"
        "- **HeyGen / ElevenLabs / ffmpeg** —— 내레이션과 합성",

    "That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.":
        "그래서 프롬프트를 쓰는 일은 text-to-video 주문을 외는 것과 근본적으로 다릅니다. "
        "여러분이 내리는 것은 그림 설명이 아니라 빌드 명령입니다.",

    "**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.":
        "**이 저장소는 그 프롬프트들을 출처와 함께 한 글자도 바꾸지 않고 수록합니다.** "
        "유료 팩과 비공개 skill은 자리표시자만 남깁니다 —— 공개되지 않은 것을 복원하지는 않습니다.",

    "## Quick Start": "## 빠른 시작",

    "Then paste any prompt below into Astra, Claude Code, or Codex.":
        "그런 다음 아래 프롬프트 중 아무거나 Astra, Claude Code, Codex에 붙여 넣으면 됩니다.",

    "**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.":
        "**처음이신가요?** [FeatureReveal](#@@A3@@)부터 보세요 —— 가장 짧으면서, "
        "프레임 번호가 왜 중요한지 보여주는 예시입니다.",

    "## Statistics": "## 통계",

    "| | |\n|---|---|\n| **Entries** | 24 |\n| **Full text available** | 17 |\n| **Languages** | EN · JA · ZH |\n| **Preview clips** | 18 (animated WebP, `media/`) |\n| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |\n| **Last updated** | 2026-09-10 |":
        "| | |\n|---|---|\n| **항목 수** | 24 |\n| **전문 공개** | 17 |\n"
        "| **언어** | EN · JA · ZH |\n| **미리보기 클립** | 18 (애니메이션 WebP, `media/`) |\n"
        "| **번역** | 中文 · 日本語 · 한국어 · Español · Français |\n"
        "| **최종 갱신** | 2026-09-10 |",

    "`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only":
        "`full` —— 공개된 그대로 완전 · `partial` —— 일부만 · "
        "`spec-only` —— 방식만 설명, 문구는 비공개 · `unpublished` —— 존재는 확인되나 자리표시자만",

    "## Featured Prompts": "## 주목할 프롬프트",
    "#### 📖 Description": "#### 📖 설명",
    "#### 📝 Prompt": "#### 📝 프롬프트",
    "#### 📌 Details": "#### 📌 세부 정보",

    "### 1: High-Speed Parkour Motion Previz": "### 1: 고속 파쿠르 모션 프리비즈",

    "The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the \"camera must not pass through the character\" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.":
        "지금까지 공개된 것 중 가장 완성도 높은 Astra × Remotion 프롬프트(약 223 좋아요 / 149 북마크). "
        "가치는 소재가 아니라 **산출물 체크리스트, 물리적 접촉 검증, 그리고 '카메라가 캐릭터를 "
        "뚫고 지나가서는 안 된다'는 제약**에 있습니다. 이후 "
        "[@Naonekozamurai](https://x.com/Naonekozamurai)가 그대로 재사용해 "
        "Topview MCP → Seedance 2.5로 넘겼습니다.",

    "<details>\n<summary>Key constraints, summarized (unofficial)</summary>":
        "<details>\n<summary>핵심 제약 (비공식 요약)</summary>",

    "- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only\n"
    "- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL\n"
    "- Character: one \"i-shaped\" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing\n"
    "- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state\n"
    "- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification\n"
    "</details>":
        "- 15초 / 가로 / SD / 30fps / 무음 / 외부 소재 없음 —— 단순한 입체 도형만\n"
        "- TypeScript + Remotion + `useCurrentFrame()` + 공유 3D 좌표계 + WebGL\n"
        "- 캐릭터: 'i자형' 프록시 1개(구형 머리 + 캡슐형 몸통). 기울기, 도약 전 압축, "
        "착지 시 가라앉음으로 동작을 전달\n"
        "- **강한 제약**: 카메라는 캐릭터를 직선으로 뚫고 지나갈 수 없음 / 착지점에는 반드시 지지면이 "
        "있어야 함 / 같은 프레임은 항상 같은 상태를 반환해야 함\n"
        "- **산출물**: MP4 + 편집 가능한 소스 + 샷 JSON + 재렌더링 절차 + ffprobe/ffmpeg 검증\n"
        "</details>",

    "### 2: AdCar TV — In-Repo One-Shot Launch Video":
        "### 2: AdCar TV —— 기존 제품 저장소 안에서 원샷 제작",

    "Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.":
        "**이미 있는 제품 저장소** 안에서 실행 —— Astra는 프로젝트 자체의 3D 뷰어, 음악, 엔진 사운드를 "
        "그대로 Remotion으로 가져왔습니다. 소재가 이미 있을 때 베껴야 할 패턴입니다. "
        "빈 폴더에서 시작하지 마세요.",

    "> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.":
        "> 작성자 메모: ffmpeg는 주로 음성과 음악을 붙이는 데 사용했습니다. Astra는 저장소에 있던 "
        "3D를 Remotion으로 직접 끌어왔습니다.",

    "### 3: FeatureReveal — Frame-Exact Composition Contract":
        "### 3: FeatureReveal —— 프레임 단위로 정확한 합성 계약",

    "The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.":
        "여기서 가장 짧은 프롬프트이자, SaaS 체인지로그 영상을 만들 때 가장 좋은 출발 골격입니다. "
        "모든 애니메이션이 **프레임 범위**로 지정되어 있고 모호한 설명이 없습니다 —— "
        "그래서 추측이 아니라 구현이 가능합니다.",

    "### 4: Witch's First Flight — 15s Generated Shot Script":
        "### 4: 마녀의 첫 비행 —— 15초 생성용 샷 스크립트",

    "**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *\"I used it to create the prompt for this animation.\"* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.":
        "**이것은 입력이 아니라 출력입니다** —— Astra가 영상 모델을 위해 *써낸* 샷 스크립트입니다. "
        "작성자는 분명히 밝혔습니다: *\"이 애니메이션의 프롬프트를 만들기 위해 사용했습니다.\"* "
        "좋은 생성용 샷 스크립트가 어떤 모습인지 참고하세요: 초 단위 비트, 캐릭터 일관성 고정, "
        "그리고 긴 네거티브 목록.",

    "### 5: T Cells — One Sentence, Five Minutes": "### 5: T 세포 —— 한 문장, 5분",

    "The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.":
        "가장 많이 공유된 사례입니다. 사용자 프롬프트는 문자 그대로 한 줄입니다. "
        "**아주 짧은 요청 + 이미 설치된 skill이 긴 프롬프트를 이긴다는 것을 증명합니다** —— "
        "툴체인 전체를 Astra가 스스로 골랐습니다.",

    "The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):":
        "Astra가 선택한 오케스트레이션 (작성자가 나중에 설명한 것으로, 원래 프롬프트는 아니지만 "
        "skill 흐름으로 쓸 수 있습니다):",

    "### 6: Six-Part Control Template + Shot JSON Contract":
        "### 6: 6단계 제어 템플릿 + 샷 JSON 계약",

    "A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.":
        "어떤 Astra 작업에도 쓸 수 있는 재사용 가능한 6단계 구조와, 생성기에 넘길 수 있는 JSON 샷 "
        "계약입니다. **Authority**와 **Verification** 블록은 대부분의 사람이 빼먹는 부분인데, "
        "바로 이것이 에이전트가 과하게 캐묻거나 망가진 결과물을 내놓는 것을 막아줍니다.",

    "Six-part control template:": "6단계 제어 템플릿:",
    "Shot JSON contract:": "샷 JSON 계약:",
    "60-second short:": "60초 단편:",

    "## Product Launch & Marketing": "## 제품 출시와 마케팅",

    "### Atomik — 33-Second Launch Film": "### Atomik —— 33초 런치 필름",

    "> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.":
        "> 직접 만든 `motion-flavor` skill로 원샷에 만든 런치 영상입니다. 이 skill은 HyperFrames와 "
        "Remotion 양쪽에서 동작합니다. 채팅 프롬프트는 공개되지 않았고, 재현 가능한 구현이 "
        "공개되었습니다.",

    "X post, verbatim:": "X 게시물 원문:",

    "Spec from the repo — useful as an acceptance contract for an agent:":
        "저장소의 사양 —— 에이전트용 인수 계약으로 쓸 수 있습니다:",

    "**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames":
        "**작성자:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | "
        "**출처:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · "
        "[소스 저장소](https://github.com/Tejashmakwana/astra-atomik-launch-video) | "
        "**게시일:** 2026-09 | **도구:** Astra, Remotion, HyperFrames",

    "### video-shotcraft — Cinematic Product Video Skill":
        "### video-shotcraft —— 시네마틱 제품 영상 skill",

    "> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.":
        "> 157장의 샷 레시피 카드 + Remotion 구현 + 완성 영상 템플릿. skill 본체는 긴 문서이고, "
        "여기 실린 것은 사용자 쪽 호출 방식입니다.",

    "Install:": "설치:",
    "Invocations (from the official README):": "호출 예시 (공식 README에서):",

    "<details>\n<summary>Skill frontmatter (determines when the agent activates it)</summary>":
        "<details>\n<summary>Skill frontmatter (에이전트가 언제 활성화하는지 결정)</summary>",

    "Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).":
        "상호 배타적인 세 가지 모드: Ink Press 템플릿 바로 적용 · 자율 제작"
        "(`references/pipeline.md`를 따라 묻지 않고 완성 컷까지) · 협업"
        "(브리프 / 비주얼 방향 / 샷 리스트를 단계별로 확인).",

    "Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic \"promo skin\".\n</details>":
        "강한 제약: 실제 페이지는 반드시 스크린샷을 써야 하고 손으로 그린 가짜 UI는 금지. "
        "서체와 색상은 제품의 디자인 토큰에서 매핑해야 하며, 범용 '프로모 스킨'을 덮어쓰면 안 됩니다.\n"
        "</details>",

    "**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex":
        "**작성자:** Vincentwei1021 | "
        "**출처:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | "
        "**도구:** Remotion, Astra, Claude Code, Codex",

    "### Montage — Agent-Native Launch Video Scaffold":
        "### Montage —— 에이전트 네이티브 런치 영상 스캐폴드",

    "> A Remotion fork built for agents, aimed at product launch films.":
        "> 에이전트를 위해 만든 Remotion 포크. 겨냥한 것은 제품 런치 영상.",

    "What the README tells you to say to the agent:":
        "README가 에이전트에게 이렇게 말하라고 안내합니다:",

    "The AGENTS.md rules worth stealing:": "AGENTS.md에서 훔칠 만한 규칙:",

    "**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion":
        "**작성자:** simplexlabs | **출처:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | "
        "**도구:** Remotion",

    "### Remotion Official Skill Invocations": "### Remotion 공식 skill 호출",

    "> The official slash commands. Most community prompts assume these are installed.":
        "> 공식 슬래시 커맨드. 커뮤니티 프롬프트 대부분이 이것들이 설치되어 있다고 전제합니다.",

    "Bootstrap for a coding agent on a fresh project:":
        "새 프로젝트에서 코딩 에이전트를 부트스트랩하는 방법:",

    "Invocations:": "호출:",

    "Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.":
        "사용 가능한 skill: `remotion-best-practices`(라우터), `remotion-create`, "
        "`remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, "
        "`remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, "
        "`remotion-upgrade`, `remotion-multimedia`.",

    "**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion":
        "**작성자:** Remotion | **출처:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | "
        "**도구:** Remotion",

    "### Short Briefs That Still Worked": "### 그래도 통한 극단적으로 짧은 요청",

    "> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.":
        "> 최소한의 요청. 얼마나 적게 써도 되는지 기준으로는 유용하지만, 계약서는 아닙니다.",

    "**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)":
        "**작성자:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | "
        "**출처:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",

    "**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker":
        "**작성자:** [@leon7hao](https://x.com/leon7hao) | "
        "**출처:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | "
        "**비고:** GPT-6-Astra medium, skill 미설치 —— 작성자는 결과가 눈에 띄게 약했다고 밝혔습니다",

    "Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)":
        "프롬프트 없이 결과만 올린 사례: "
        "[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)"
        "(BrandNewStudy 마케팅 영상, 원샷) · "
        "[@stoufax](https://x.com/stoufax/status/2096311328600113222)"
        "(iOS 앱 출시, Remotion + ElevenLabs) · "
        "[@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)"
        "(`/goal` + fal 음성 + Remotion 플러그인, 90초 워크스루)",

    "**@NickYang130 — BrandNewStudy marketing video, one-shot**":
        "**@NickYang130 —— BrandNewStudy 마케팅 영상, 원샷**",

    "**@stoufax — iOS app launch, Remotion + ElevenLabs**":
        "**@stoufax —— iOS 앱 출시, Remotion + ElevenLabs**",

    "## Motion Previz → Generative": "## 모션 프리비즈 → 생성",

    "> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.":
        "> 이 계열은 영상 모델에게 그림을 설명하지 않습니다. 먼저 Astra가 Remotion으로 "
        "**control MP4**를 렌더링하게 하고, 그것을 Seedance 같은 모델에 모션 참조로 넘깁니다. "
        "일본 씬에서는 점점 주류가 되어 가는 두 번째 연결 고리입니다.",

    "### Seedance Handoff Instruction": "### Seedance 전달 지시",

    "> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.":
        "> Remotion 렌더 결과를 생성 모델에 넘길 때 뭐라고 말할지. 수정 허가를 명시하지 않으면 "
        "모델은 플레이스홀더의 결함을 충실히 재현합니다.",

    "<details>\n<summary>English (unofficial)</summary>":
        "<details>\n<summary>영어 (비공식)</summary>",

    "**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)":
        "**작성자:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | "
        "**출처:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | "
        "**게시일:** 2026-09 | **도구:** Remotion → Seedance 2.5 (Topview MCP 경유)",

    "### Ultra-High-Speed Sprint Control MP4": "### 초고속 질주 control MP4",

    "> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.":
        "> 반칙 방지 조항에 주목하세요: 배경을 루프시키는 대신, 충분히 긴 실제 길을 만들고 "
        "실제로 앞으로 나아가야 합니다. 그리고 **인물과 그리드는 반드시 같은 3D 좌표계와 "
        "카메라 투영을 써야 합니다** —— 2D 소재를 확대·축소하는 가짜 카메라는 안 됩니다.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion":
        "**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**출처:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | "
        "**도구:** Astra, Remotion",

    "### Side-Scrolling Chase, with a Frame Table": "### 횡스크롤 추격, 프레임 표 포함",

    "> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.":
        "> 수록된 것 중 프레임 정밀도가 가장 높은 프롬프트. 모든 파쿠르 동작에 명시적인 프레임 범위가 "
        "배정되어 있고, 반개구간(half-open) 의미까지 적혀 있습니다.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion":
        "**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**출처:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | "
        "**도구:** Astra, Remotion",

    "### 30 Camera Compositions — Reference Sheet Generator":
        "### 카메라 구도 30종 —— 레퍼런스 시트 생성기",

    "> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.":
        "> 훑어볼 수 있는 카메라 구도 카탈로그를 만듭니다. 이후 영상 모델과 대화할 때 ID로 "
        "바로 참조할 수 있습니다.",

    "> ⚠️ The post continues past the output requirements; only what's visible is quoted.":
        "> ⚠️ 게시물은 출력 요구사항 이후로도 이어지지만, 보이는 부분만 인용했습니다.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG":
        "**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**출처:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | "
        "**도구:** Astra, Remotion, HTML/CSS/SVG",

    "> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.":
        "> 같은 작성자가 *참바라*(검극) 워크플로도 공개했습니다 —— "
        "[x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— "
        "다만 방법만 있고 프롬프트는 없습니다: 1) 카메라와 캐릭터 위치만 표시한 최소 샷 리스트, "
        "2) 이펙트 샘플 시트, 3) 프롬프트로 제어하는 세밀한 동작.",

    "## End-to-End Production": "## 엔드투엔드 제작",

    "### Idea → Uploadable YouTube Video": "### 아이디어 → 바로 업로드 가능한 YouTube 영상",

    "> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.":
        "> 약 50분, API 비용은 대략 60달러. 핵심은 '초안은 받지 않는다'는 그 한 줄입니다.",

    "Same author, sizzle reel from 152GB of event footage:":
        "같은 작성자가 152GB 행사 영상으로 만든 하이라이트:",

    "> ⚠️ Transcribed from the video's narration — no official paste block exists.":
        "> ⚠️ 영상 내레이션을 받아쓴 것입니다 —— 공식 붙여넣기 텍스트는 없습니다.",

    "**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames":
        "**작성자:** Nate Herk | "
        "**출처:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · "
        "[하이라이트 영상](https://www.youtube.com/watch?v=QhmhUgccaS0) | "
        "**도구:** Astra, HeyGen, ElevenLabs, HyperFrames",

    "### Narration-First Diagram Explainer": "### 내레이션 우선 도해 영상",

    "> No generated footage at all. Record first, then build the picture to measured narration cues.":
        "> 생성 영상은 전혀 쓰지 않습니다. 먼저 녹음하고, 계측한 내레이션 큐에 맞춰 그림을 만듭니다.",

    "Workflow:": "워크플로:",
    "Published short instructions:": "공개된 짧은 지시:",

    "> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.":
        "> ⚠️ 작성자의 10가지 Master Prompts는 유료 번들에 포함되어 공개된 적이 없습니다. "
        "여기에는 공개된 뼈대만 실었습니다.",

    "**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion":
        "**작성자:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | "
        "**출처:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) 및 이후 게시물 | "
        "**도구:** Astra, Remotion",

    "## Meta: Prompts That Write Prompts": "## 메타: 프롬프트를 쓰는 프롬프트",

    "### Director / Animation Supervisor Template": "### 감독 / 애니메이션 슈퍼바이저 템플릿",

    "> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.":
        "> 바로 쓸 수 있는 프롬프트에*더해* 네거티브 프롬프트와 세 가지 대안 조정안을 내놓습니다 "
        "—— 마지막 항목이 대부분의 템플릿에 빠져 있습니다.",

    "**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra":
        "**작성자:** The AI Average | "
        "**출처:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | "
        "**도구:** GPT-6 Astra",

    "## Adjacent: Blender & Others": "## 인접 영역: Blender와 기타",

    "### Blender 8-Second Product Turntable": "### Blender 8초 제품 턴테이블",

    "> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.":
        "> 전체 시퀀스 전에 스틸을 렌더링하는 단계에 주목하세요 —— 카메라 경로가 잘못됐는지 "
        "가장 싸게 잡아내는 방법입니다.",

    "**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra":
        "**작성자:** Kingy.ai | "
        "**출처:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | "
        "**도구:** Blender, Astra",

    "### Known but Unpublished": "### 존재하지만 미공개",

    "> Confirmed to exist, no public primary source. **Listed, never reconstructed.**":
        "> 존재는 확인되었으나 공개된 1차 출처가 없습니다. **등재만 하고, 복원하지 않습니다.**",

    "| What | Who | Status |\n|---|---|---|\n"
    "| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |\n"
    "| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |\n"
    "| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |\n"
    "| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |\n"
    "| \"Remotion 制作 8 本の裏側\" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |\n"
    "| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |":
        "| 무엇 | 누가 | 상태 |\n|---|---|---|\n"
        "| 물리 / 소프트바디 모션 skill —— Remotion/HyperFrames의 페이드인 카드를 버리고 물리적 "
        "질감과 소프트바디 힘으로, 4K60 "
        "| [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | 예고됨, skill 미공개 |\n"
        "| Higgsfield + Blender 프리비즈 + Seedance 2.5 검극 파이프라인 | 2차 보도만 존재 | 1차 출처 아님 |\n"
        "| `motion-flavor` skill 소스 | [@makwanatejas170](https://x.com/makwanatejas170) | 별도 공개 안 됨 |\n"
        "| 도해 영상용 10가지 Master Prompts | [@foma_on_x](https://x.com/foma_on_x) | 유료 번들 |\n"
        "| 「Remotion 制作 8本の裏側」장문 노트 | [@chikaidev](https://x.com/chikaidev) | 아직 받아쓰지 않음 |\n"
        "| 답글에서 주장한 5가지 모션 프롬프트 | [@dawoodkhan254](https://x.com/dawoodkhan254) | 주장만, 게시 없음 |",

    "**The physics / soft-body motion demo itself is public** (the skill is not):":
        "**물리 / 소프트바디 모션 데모 자체는 공개되어 있습니다** (skill은 비공개):",

    "## Skills & Tooling": "## Skill과 도구",

    "Everyone here is feeding Astra the same base layer. We link, we don't vendor.":
        "여기 있는 모두가 Astra에 같은 토대를 넣고 있습니다. 링크만 걸고, 직접 배포하지는 않습니다.",

    "| Tool | Install / Link | What it's for |\n|---|---|---|\n"
    "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |\n"
    "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |\n"
    "| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |\n"
    "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |\n"
    "| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |\n"
    "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |\n"
    "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |":
        "| 도구 | 설치 / 링크 | 용도 |\n|---|---|---|\n"
        "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | 거의 모든 사례 밑에 깔린 토대 |\n"
        "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) "
        "| `SKILL.md` / `AGENTS.md`에 붙여넣는 것 —— 사용자 작업 프롬프트가 아님 |\n"
        "| **Remotion Studio WebMCP** | 4.0.518+ | 스크린샷을 클릭하는 대신 선택 영역·타임라인·"
        "지오메트리를 직접 읽음 |\n"
        "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 샷 레시피 카드 157장 + 템플릿 |\n"
        "| **Montage** | [github](https://github.com/simplexlabs/montage) | 런치 영상용 에이전트 네이티브 Remotion 포크 |\n"
        "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) "
        "| 재현 가능한 런치 영상 소스 |\n"
        "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | 더 넓은 커뮤니티 목록 |",

    "## What the Community Learned": "## 커뮤니티가 배운 것",

    "Patterns that show up across every thread above:":
        "위의 모든 스레드에서 반복해서 나타나는 패턴:",

    "**Install the skills first, then talk.** Without skills, a changelog video came out \"noticeably short of it\". With skills installed, one-shots became common.":
        "**먼저 skill을 설치하고, 그다음 말하세요.** skill 없이 만든 체인지로그 영상은 "
        "'눈에 띄게 아쉬운' 결과였습니다. 설치한 뒤에는 원샷이 흔해졌습니다.",

    "**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.":
        "**분위기가 아니라 산출물을 요구하세요.** 여기서 가장 강력한 프롬프트(かし子의 것)는 "
        "MP4 + 편집 가능한 소스 + 샷 JSON + 재렌더링 절차 + ffprobe 검증으로 끝납니다.",

    "**Align the timeline to narration, not \"make it faster overall.\"** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*":
        "**'전체적으로 더 빠르게'가 아니라 타임라인을 내레이션에 맞추세요.** Foma의 해법은 그 순간을 "
        "지목하는 것입니다: *내레이션이 결과를 말할 때 그림은 이미 거기 있어야 한다.*",

    "**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.":
        "**빈 폴더보다 제품 저장소 안에서 돌리는 편이 낫습니다.** AdCar, Atomik, 그리고 게임 CM 모두 "
        "이미 있는 소재를 끌어왔습니다.",

    "**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.":
        "**Remotion은 프리비즈로, 생성 모델은 최종 결과물로** —— 일본 씬에서 표준적인 두 번째 "
        "연결 고리가 되어 가고 있습니다.",

    "**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.":
        "**Astra가 가장 강한 지점은 오케스트레이션과 재설계** —— "
        "[@paojiaofty](https://x.com/paojiaofty)는 페이드인 카드를 받아들이느니 프레임워크를 "
        "통째로 버렸습니다.",

    "**People are starting to demand disclosure on \"one-shot\" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.":
        "**'원샷'이라는 주장에 정보 공개를 요구하는 움직임이 시작됐습니다:** 빈 저장소인가 기존 "
        "프로젝트인가? 추론 등급은? 몇 번 재시도했나? skill은 미리 설치했나? "
        "필수 항목으로 만들 만합니다.",

    "## Completeness Table": "## 완성도 표",

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
        "| ID | 유형 | 작성자 | 전문 있음? |\n|---|---|---|---|\n"
        "| AdCar TV | 제품 출시 | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
        "| Atomik | 제품 출시 | [@makwanatejas170](https://x.com/makwanatejas170) | 사양은 있음, 채팅 프롬프트는 없음 |\n"
        "| video-shotcraft | 제품 프로모 skill | Vincentwei1021 | 호출은 있음, skill 본체는 김 |\n"
        "| Montage | 런치 스캐폴드 | simplexlabs | AGENTS.md 규칙 |\n"
        "| FeatureReveal | 기능 영상 | OpenReplay | ✅ |\n"
        "| Remotion 공식 | 호출 | Remotion | ✅ (아주 짧음) |\n"
        "| 파쿠르 프리비즈 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 질주 control MP4 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 횡스크롤 추격 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 카메라 구도 30종 | 레퍼런스 시트 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
        "| Seedance 전달 | 전달 지시 | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
        "| T 세포 | 해설 영상 | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (한 줄) |\n"
        "| Nate의 YouTube | 채널 영상 | Nate Herk | 받아쓰기 |\n"
        "| Foma 도해 | 도해 영상 | [@foma_on_x](https://x.com/foma_on_x) | 짧은 지시만 |\n"
        "| 마녀의 첫 비행 | 생성용 샷 스크립트 | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
        "| 6단계 + JSON | 메타 | Elser AI | ✅ |\n"
        "| 감독 템플릿 | 메타 | The AI Average | ✅ |\n"
        "| Blender 턴테이블 | 3D 제품 | Kingy.ai | ✅ |\n"
        "| 물리 모션 skill | skill | [@paojiaofty](https://x.com/paojiaofty) | 미공개 |",

    "## Watch List": "## 관찰 목록",

    "A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.":
        "GitHub Action이 6시간마다 이 계정들을 확인하고, 영상 프롬프트로 보이는 글을 올리면 "
        "이슈를 생성합니다.",

    "| Account | Why |\n|---|---|\n"
    "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |\n"
    "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |\n"
    "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
    "| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |\n"
    "| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |\n"
    "| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |\n"
    "| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |\n"
    "| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |":
        "| 계정 | 이유 |\n|---|---|\n"
        "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | 가장 긴 Remotion 모션 프리비즈 프롬프트의 출처 |\n"
        "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion 프리비즈 → Seedance, 실전파 |\n"
        "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
        "| [@paojiaofty](https://x.com/paojiaofty) | 예고된 물리 모션 skill |\n"
        "| [@foma_on_x](https://x.com/foma_on_x) | 도해 영상 워크플로 |\n"
        "| [@DeryaTR_](https://x.com/DeryaTR_) | 한 줄 요청 |\n"
        "| [@d4m1n](https://x.com/d4m1n) | 저장소 안에서 원샷 |\n"
        "| [@TROOVY](https://x.com/TROOVY) | 프로 모션 스튜디오의 시선 |",

    "[Suggest an account →](../../issues/new?template=watch-account.yml)":
        "[계정 추천하기 →](../../issues/new?template=watch-account.yml)",

    "## How to Contribute": "## 기여 방법",

    "**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.":
        "**[→ 프롬프트 제출하기](../../issues/new?template=new-prompt.yml)** —— 붙여 넣고 출처를 "
        "링크하면 됩니다. git은 필요 없습니다.",

    "Every entry needs three things:": "모든 항목에는 세 가지가 필요합니다:",

    "| Field | Why |\n|---|---|\n"
    "| **Author** | Name or handle, written the way they write it |\n"
    "| **Source** | Direct link to the post, thread, blog, or video |\n"
    "| **Published** | Date, so readers can judge how current it is |":
        "| 항목 | 필요한 이유 |\n|---|---|\n"
        "| **작성자** | 이름 또는 핸들. 본인이 쓰는 표기 그대로 |\n"
        "| **출처** | 게시물·스레드·블로그·영상으로 가는 직접 링크 |\n"
        "| **게시일** | 얼마나 최신인지 독자가 판단할 수 있도록 |",

    "- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.\n"
    "- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.\n"
    "- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.\n"
    "- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.":
        "- **한 글자도 바꾸지 말고 인용하세요.** 정리하지 말고, 바꿔 쓰지 말고, '개선'하지 마세요.\n"
        "- **원문 언어를 유지하세요.** 번역은 `<details>` 블록에 비공식이라고 표시해 넣고, "
        "원문을 대체해서는 안 됩니다.\n"
        "- **빠진 부분을 지어내지 마세요.** 스크린샷이 프롬프트의 절반만 담았다면 `partial`로 "
        "표시하고 보이는 부분만 인용하세요.\n"
        "- **공식 문서는 링크만 하고 복사하지 마세요.** API는 바뀌므로 오래된 사본은 오해를 낳습니다.",

    "See [CONTRIBUTING.md](CONTRIBUTING.md).": "자세한 내용은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.",

    "## License & Acknowledgements": "## 라이선스와 감사의 말",

    "Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).":
        "저장소 구조, 편집 노트, 스크립트: [CC BY 4.0](LICENSE).",

    "**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.":
        "**프롬프트의 저작권은 각 작성자에게 있습니다.** 출처와 원문 링크를 함께 밝혀 참고와 연구 "
        "목적으로 인용했습니다.",

    "Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.":
        "에이전트 기반 영상 제작을 공개적으로 만들어 가는 모든 분께 감사합니다 —— "
        "[かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), "
        "[Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), "
        "[Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), "
        "[Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, "
        "Kingy.ai, Vincentwei1021, simplexlabs, 그리고 Remotion 팀.",

    "**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.":
        "**여러분도 그중 한 명인가요?** [이슈를 열면](../../issues/new?template=correction.yml) "
        "크레딧을 고치고, 프롬프트 전문을 추가하고, 작업물 삭제를 요청할 수 있습니다. "
        "이견 없이 처리합니다.",


    "⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.":
        "유용하다면 ⭐ **이 저장소에 Star를** —— 다른 사람들이 그것으로 찾습니다.",
}
