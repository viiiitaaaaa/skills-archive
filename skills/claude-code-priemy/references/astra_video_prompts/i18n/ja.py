# -*- coding: utf-8 -*-
"""Japanese translation table for README.md."""

TOC_TITLE = "目次"

SWITCHER = (
    '<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · '
    '<strong>日本語</strong> · <a href="README.ko.md">한국어</a> · '
    '<a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>'
)

NOTICE = (
    "> 📄 **これは README.md の日本語訳です。** プロンプトはすべて、作者が公開した"
    "原文のまま一字一句そのまま収録しており、翻訳していません。翻訳しているのは目次・"
    "説明・統計・投稿ルールなどの編集的な文章のみです。差異がある場合は"
    "[英語版](README.md)を正とします。"
)

REPLACE = [
    ("**Author:**", "**作者：**"),
    ("**Source:**", "**出典：**"),
    ("**Published:**", "**公開日：**"),
    ("**Tools:**", "**使用ツール：**"),
    ("**Reused by:**", "**再利用：**"),
    ("**Works with:**", "**対応：**"),
    ("**Chinese relay:**", "**中国語での二次投稿：**"),
    ("**Note:**", "**備考：**"),
    ("**Rules:**", "**ルール：**"),
    ("**Are you one of them?**", "**あなたもその一人ですか？**"),
    ("🎬 **[Watch the full video →](", "🎬 **[本編を見る →]("),
    ("[source repo](", "[ソースリポジトリ]("),
    ("[sizzle reel](", "[ダイジェスト映像]("),
    ("[full reply](", "[返信の全文]("),
    (" and following posts", " および以降の投稿"),
]

SKIP = {
    "# Awesome Astra Video Prompts",
    "[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)",
}

BLOCKS = {
    # ── LuxReal house CTA (rendered at the top of README.md) ─────────────
    "**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**":
        "**LuxReal が運営・メンテナンスしています** —— AI ショートドラマのパイプライン。脚本を入れると、シーンと人物の一貫性を保ったまま全工程で編集できる映像が出てきます。**[無料で試す →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**",
    "**Real prompts for making video with GPT-6 Astra and coding agents.**":
        "**GPT-6 Astra とコーディングエージェントで動画を作るための、実際に使われたプロンプト集。**",

    "Astra doesn't output video. It writes code and drives tools —\n"
    "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg":
        "Astra は動画を直接出力しません。コードを書き、ツールを動かします ——\n"
        "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg",

    "> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.":
        "> ⚠️ **著作権について**：掲載しているプロンプトはすべて公開コミュニティ投稿から収集したもので、"
        "原作者を明記しています。権利を侵害していると思われる場合は"
        "[Issue を作成](../../issues/new)してください。速やかに削除します。",

    "> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.":
        "> 🎬 **プレビューについて**：`media/` 以下のアニメーションは、各作者が*公開したデモ動画*から"
        "切り出した短い低解像度の抜粋です。プロンプトの横に参考として置き、必ず元の投稿へリンクしています。"
        "あくまで抜粋であり、本編動画の再配布ではありません。作者本人で削除を希望される場合は"
        "[Issue を作成](../../issues/new?template=correction.yml)してください。異議なく削除します。",

    "## Table of Contents": "## 目次",
    "- [What is this?](#what-is-this)\n- [Quick Start](#quick-start)\n- [Statistics](#statistics)\n- [Featured Prompts](#featured-prompts)\n- [Product Launch & Marketing](#product-launch--marketing)\n- [Motion Previz → Generative](#motion-previz--generative)\n- [End-to-End Production](#end-to-end-production)\n- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)\n- [Adjacent: Blender & Others](#adjacent-blender--others)\n- [Skills & Tooling](#skills--tooling)\n- [What the Community Learned](#what-the-community-learned)\n- [Completeness Table](#completeness-table)\n- [Watch List](#watch-list)\n- [How to Contribute](#how-to-contribute)\n- [License & Acknowledgements](#license--acknowledgements)":
        "@@TOC@@",

    "## What is this?": "## これは何か",

    "Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:":
        "Astra は動画をネイティブにレンダリングしません。**コードを書き、プラグインを編成し、"
        "コンピュータを操作します。** 完成した動画は次のものから生まれます：",

    "- **Remotion / HyperFrames** — programmatic motion graphics\n"
    "- **Remotion motion previz → Seedance** and other generative models\n"
    "- **Blender previs** → render or generate\n"
    "- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly":
        "- **Remotion / HyperFrames** —— プログラムによるモーショングラフィックス\n"
        "- **Remotion のモーションコンテ → Seedance** などの生成モデル\n"
        "- **Blender プリビズ** → レンダリングまたは生成\n"
        "- **HeyGen / ElevenLabs / ffmpeg** —— ナレーションと合成",

    "That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.":
        "そのため、プロンプトの書き方は text-to-video のおまじないを書くのとは根本的に異なります。"
        "あなたが発行するのは絵の説明ではなく、ビルド命令です。",

    "**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.":
        "**このリポジトリは、それらのプロンプトを出典付きで一字一句そのまま収録します。** "
        "有料パックや非公開 skill はプレースホルダのみ —— 公開されなかったものを復元することは決してしません。",

    "## Quick Start": "## クイックスタート",

    "Then paste any prompt below into Astra, Claude Code, or Codex.":
        "あとは下記のプロンプトを好きなものを Astra、Claude Code、Codex に貼り付けるだけです。",

    "**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.":
        "**初めての方へ：** [FeatureReveal](#@@A3@@) から始めてください —— 最も短く、"
        "なぜフレーム番号が重要なのかが分かる一本です。",

    "## Statistics": "## 統計",

    "| | |\n|---|---|\n| **Entries** | 24 |\n| **Full text available** | 17 |\n| **Languages** | EN · JA · ZH |\n| **Preview clips** | 18 (animated WebP, `media/`) |\n| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |\n| **Last updated** | 2026-09-10 |":
        "| | |\n|---|---|\n| **収録数** | 24 |\n| **全文あり** | 17 |\n"
        "| **言語** | EN · JA · ZH |\n| **プレビュー** | 18（アニメーション WebP、`media/`） |\n"
        "| **翻訳** | 中文 · 日本語 · 한국어 · Español · Français |\n"
        "| **最終更新** | 2026-09-10 |",

    "`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only":
        "`full` —— 公開時のまま完全 · `partial` —— 一部のみ · "
        "`spec-only` —— 手法は説明されているが文言は非公開 · `unpublished` —— 存在は確認できるがプレースホルダのみ",

    "## Featured Prompts": "## 注目のプロンプト",
    "#### 📖 Description": "#### 📖 説明",
    "#### 📝 Prompt": "#### 📝 プロンプト",
    "#### 📌 Details": "#### 📌 詳細",

    "### 1: High-Speed Parkour Motion Previz": "### 1：高速パルクールのモーションコンテ",

    "The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the \"camera must not pass through the character\" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.":
        "これまでに公開された中で最も完成度の高い Astra × Remotion プロンプト（約223いいね / "
        "149ブックマーク）。価値は題材ではなく、**成果物チェックリスト、物理的な接触の検証、"
        "そして「カメラがキャラクターを突き抜けてはいけない」という制約**にあります。"
        "後に [@Naonekozamurai](https://x.com/Naonekozamurai) がそのまま再利用し、"
        "Topview MCP → Seedance 2.5 へ渡しています。",

    "<details>\n<summary>Key constraints, summarized (unofficial)</summary>":
        "<details>\n<summary>主要な制約（非公式の要約）</summary>",

    "- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only\n"
    "- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL\n"
    "- Character: one \"i-shaped\" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing\n"
    "- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state\n"
    "- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification\n"
    "</details>":
        "- 15秒 / 横長 / SD / 30fps / 無音 / 外部素材なし —— 単純な立体形状のみ\n"
        "- TypeScript + Remotion + `useCurrentFrame()` + 共通の3D座標系 + WebGL\n"
        "- キャラクター：「i字型」プロキシ1体（球の頭 + カプセル状の胴体）。前傾、踏切前の圧縮、"
        "着地時の沈み込みで動きを伝える\n"
        "- **ハード制約**：カメラはキャラクターを直線的に突き抜けてはいけない／着地点には必ず支持面が必要／"
        "同じフレーム番号は常に同じ状態を返す\n"
        "- **成果物**：MP4 + 編集可能なソース + ショットJSON + 再レンダリング手順 + "
        "ffprobe/ffmpeg による検証\n"
        "</details>",

    "### 2: AdCar TV — In-Repo One-Shot Launch Video":
        "### 2：AdCar TV —— 既存プロダクトリポジトリ内でのワンショット制作",

    "Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.":
        "**既存のプロダクトリポジトリ**の中で実行 —— Astra はプロジェクト自身の3Dビューア、音楽、"
        "エンジン音をそのまま Remotion に取り込みました。すでに素材があるときの定石です。"
        "空のフォルダから始めないこと。",

    "> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.":
        "> 作者の補足：ffmpeg は主に音声と音楽の貼り付けに使用。Astra はリポジトリ内の既存3Dを"
        "そのまま Remotion に読み込ませた。",

    "### 3: FeatureReveal — Frame-Exact Composition Contract":
        "### 3：FeatureReveal —— フレーム単位で正確なコンポジション契約",

    "The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.":
        "ここで最短のプロンプトであり、SaaS のチェンジログ動画を作る際の最良の出発点です。"
        "すべてのアニメーションが**フレーム範囲**として指定され、曖昧な記述がありません —— "
        "だからこそ推測ではなく実装できるのです。",

    "### 4: Witch's First Flight — 15s Generated Shot Script":
        "### 4：魔女の初飛行 —— 15秒の生成用ショットスクリプト",

    "**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *\"I used it to create the prompt for this animation.\"* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.":
        "**これは入力ではなく出力です** —— Astra が動画モデル向けに*書いた*ショットスクリプト。"
        "作者は明言しています：*「このアニメーションのプロンプトを作るために使いました。」* "
        "良い生成用ショットスクリプトの見本として読んでください：秒単位のビート、"
        "キャラクターの一貫性ロック、そして長いネガティブリスト。",

    "### 5: T Cells — One Sentence, Five Minutes": "### 5：T細胞 —— 一文で、5分",

    "The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.":
        "最も多く再共有された例。ユーザープロンプトは文字通り一行です。"
        "**非常に短い依頼 + すでに入っている skill が、長いプロンプトに勝つことを証明しています** —— "
        "ツールチェーン全体を Astra 自身が選びました。",

    "The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):":
        "Astra が選んだ編成（作者が後から説明したもので、元のプロンプトではありませんが、"
        "skill フローとして使えます）：",

    "### 6: Six-Part Control Template + Shot JSON Contract":
        "### 6：6部構成のコントロールテンプレート + ショットJSON契約",

    "A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.":
        "どんな Astra タスクにも使える再利用可能な6部構成と、生成器に渡せる JSON ショット契約。"
        "**Authority** と **Verification** のブロックは多くの人が省いてしまう部分ですが、"
        "まさにこれが、エージェントが余計に質問しすぎたり壊れたものを納品したりするのを防ぎます。",

    "Six-part control template:": "6部構成のコントロールテンプレート：",
    "Shot JSON contract:": "ショットJSON契約：",
    "60-second short:": "60秒のショート：",

    "## Product Launch & Marketing": "## 製品ローンチとマーケティング",

    "### Atomik — 33-Second Launch Film": "### Atomik —— 33秒のローンチフィルム",

    "> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.":
        "> 自作の `motion-flavor` skill を使ったワンショットのローンチ映像。この skill は "
        "HyperFrames と Remotion の両方で動きます。チャットのプロンプトは公開されておらず、"
        "再現可能な実装のほうが公開されています。",

    "X post, verbatim:": "X の投稿（原文）：",

    "Spec from the repo — useful as an acceptance contract for an agent:":
        "リポジトリの仕様 —— エージェントへの受け入れ契約として使えます：",

    "**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames":
        "**作者：** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | "
        "**出典：** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · "
        "[ソースリポジトリ](https://github.com/Tejashmakwana/astra-atomik-launch-video) | "
        "**公開日：** 2026-09 | **使用ツール：** Astra, Remotion, HyperFrames",

    "### video-shotcraft — Cinematic Product Video Skill":
        "### video-shotcraft —— シネマティックな製品動画 skill",

    "> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.":
        "> 157枚のショットレシピカード + Remotion 実装 + 完成映像テンプレート。"
        "skill 本体は長いドキュメントで、ここに載せているのはユーザー側の呼び出し方です。",

    "Install:": "インストール：",
    "Invocations (from the official README):": "呼び出し例（公式 README より）：",

    "<details>\n<summary>Skill frontmatter (determines when the agent activates it)</summary>":
        "<details>\n<summary>Skill の frontmatter（エージェントがいつ起動するかを決める）</summary>",

    "Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).":
        "3つの排他的なモード：Ink Press テンプレートをそのまま適用 · 自律制作"
        "（`references/pipeline.md` に従い、途中で確認せず完成カットまで）· 協働"
        "（ブリーフ / ビジュアルの方向性 / ショットリストを段階的に確認）。",

    "Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic \"promo skin\".\n</details>":
        "厳格な制約：実際のページは必ずスクリーンショットを使い、手描きの偽UIは禁止。"
        "書体と色は製品のデザイントークンからマッピングすること（汎用の「プロモスキン」ではない）。\n"
        "</details>",

    "**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex":
        "**作者：** Vincentwei1021 | "
        "**出典：** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | "
        "**使用ツール：** Remotion, Astra, Claude Code, Codex",

    "### Montage — Agent-Native Launch Video Scaffold":
        "### Montage —— エージェントネイティブなローンチ映像の土台",

    "> A Remotion fork built for agents, aimed at product launch films.":
        "> エージェントのために作られた Remotion フォーク。狙いは製品ローンチ映像。",

    "What the README tells you to say to the agent:":
        "README がエージェントにこう言えと指示している内容：",

    "The AGENTS.md rules worth stealing:": "AGENTS.md から盗む価値のあるルール：",

    "**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion":
        "**作者：** simplexlabs | **出典：** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | "
        "**使用ツール：** Remotion",

    "### Remotion Official Skill Invocations": "### Remotion 公式 skill の呼び出し",

    "> The official slash commands. Most community prompts assume these are installed.":
        "> 公式のスラッシュコマンド。コミュニティのプロンプトの多くは、これらが入っている前提で"
        "書かれています。",

    "Bootstrap for a coding agent on a fresh project:":
        "新規プロジェクトでコーディングエージェントに渡す立ち上げ手順：",

    "Invocations:": "呼び出し：",

    "Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.":
        "利用可能な skill：`remotion-best-practices`（ルーター）、`remotion-create`、"
        "`remotion-markup`、`remotion-studio`、`remotion-render`、`remotion-maps`、"
        "`remotion-captions`、`remotion-saas`、`remotion-interactivity`、`remotion-docs`、"
        "`remotion-upgrade`、`remotion-multimedia`。",

    "**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion":
        "**作者：** Remotion | **出典：** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | "
        "**使用ツール：** Remotion",

    "### Short Briefs That Still Worked": "### それでも通った極短プロンプト",

    "> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.":
        "> 最小限の依頼。どこまで少なくできるかの基準として有用ですが、契約書ではありません。",

    "**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)":
        "**作者：** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | "
        "**出典：** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",

    "**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker":
        "**作者：** [@leon7hao](https://x.com/leon7hao) | "
        "**出典：** [x.com](https://x.com/leon7hao/status/2096844989900914865) | "
        "**備考：** GPT-6-Astra medium、skill 未インストール —— 作者いわく出来は明らかに見劣りした",

    "Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)":
        "プロンプトなしで結果だけ投稿されたもの："
        "[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)"
        "（BrandNewStudy のマーケティング動画、ワンショット）· "
        "[@stoufax](https://x.com/stoufax/status/2096311328600113222)"
        "（iOS アプリのローンチ、Remotion + ElevenLabs）· "
        "[@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)"
        "（`/goal` + fal 音声 + Remotion プラグイン、90秒のウォークスルー）",

    "**@NickYang130 — BrandNewStudy marketing video, one-shot**":
        "**@NickYang130 —— BrandNewStudy のマーケティング動画、ワンショット**",

    "**@stoufax — iOS app launch, Remotion + ElevenLabs**":
        "**@stoufax —— iOS アプリのローンチ、Remotion + ElevenLabs**",

    "## Motion Previz → Generative": "## モーションコンテ → 生成",

    "> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.":
        "> この系統は、動画モデルに絵を説明するのではなく、まず Astra に Remotion で "
        "**control MP4** をレンダリングさせ、それを Seedance などにモーション参照として渡します。"
        "日本のシーンでは、ますます主流の第2の工程になりつつあります。",

    "### Seedance Handoff Instruction": "### Seedance への引き渡し指示",

    "> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.":
        "> Remotion のレンダリング結果を生成モデルに渡すときの言い方。修正の許可を明示しないと、"
        "モデルはプレースホルダの欠陥を忠実に再現してしまいます。",

    "<details>\n<summary>English (unofficial)</summary>":
        "<details>\n<summary>英語（非公式）</summary>",

    "**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)":
        "**作者：** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | "
        "**出典：** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | "
        "**公開日：** 2026-09 | **使用ツール：** Remotion → Seedance 2.5（Topview MCP 経由）",

    "### Ultra-High-Speed Sprint Control MP4": "### 超高速疾走 control MP4",

    "> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.":
        "> チート防止条項に注目：背景をループさせるのではなく、十分に長い一本道を作り、"
        "実際に前進させること。そして**人物とグリッドは必ず同じ3D座標系とカメラ投影を使う** —— "
        "2D素材を拡大縮小するだけの疑似カメラは禁止です。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**出典：** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | "
        "**使用ツール：** Astra, Remotion",

    "### Side-Scrolling Chase, with a Frame Table": "### 横スクロール追従、フレーム表付き",

    "> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.":
        "> 収録中で最もフレーム精度の高いプロンプト。すべてのパルクール動作に明示的なフレーム範囲が"
        "割り当てられ、半開区間の意味まで書き切っています。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**出典：** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | "
        "**使用ツール：** Astra, Remotion",

    "### 30 Camera Compositions — Reference Sheet Generator":
        "### 30種類のカメラ構図 —— リファレンスシート生成",

    "> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.":
        "> 動画モデルと話すときに ID で参照できる、閲覧可能なカメラ構図カタログを作ります。",

    "> ⚠️ The post continues past the output requirements; only what's visible is quoted.":
        "> ⚠️ 投稿は出力要件の先まで続きますが、ここでは見えている部分のみ引用しています。",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG":
        "**作者：** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**出典：** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | "
        "**使用ツール：** Astra, Remotion, HTML/CSS/SVG",

    "> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.":
        "> 同じ作者が *ちゃんばら* のワークフローも公開しています —— "
        "[x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— "
        "ただし方法のみでプロンプトは非公開：1) カメラと人物位置だけの最小ショットリスト、"
        "2) エフェクトのサンプルシート、3) プロンプトで制御する細かい動き。",

    "## End-to-End Production": "## エンドツーエンド制作",

    "### Idea → Uploadable YouTube Video": "### アイデア → そのまま公開できる YouTube 動画",

    "> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.":
        "> 約50分、API コストはおよそ60ドル。肝は「下書きは受け取らない」という一行です。",

    "Same author, sizzle reel from 152GB of event footage:":
        "同じ作者による、152GB のイベント素材から作ったダイジェスト：",

    "> ⚠️ Transcribed from the video's narration — no official paste block exists.":
        "> ⚠️ 動画のナレーションから文字起こししたものです —— 公式のコピペ用テキストは存在しません。",

    "**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames":
        "**作者：** Nate Herk | "
        "**出典：** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · "
        "[ダイジェスト映像](https://www.youtube.com/watch?v=QhmhUgccaS0) | "
        "**使用ツール：** Astra, HeyGen, ElevenLabs, HyperFrames",

    "### Narration-First Diagram Explainer": "### ナレーション先行の図解動画",

    "> No generated footage at all. Record first, then build the picture to measured narration cues.":
        "> 生成映像は一切なし。先に録音し、計測したナレーションのキューに合わせて絵を作ります。",

    "Workflow:": "ワークフロー：",
    "Published short instructions:": "公開されている短い指示：",

    "> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.":
        "> ⚠️ 作者の10本の Master Prompts は有料バンドルに含まれ、公開されていません。"
        "ここには公開された骨組みのみを掲載しています。",

    "**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion":
        "**作者：** Foma ([@foma_on_x](https://x.com/foma_on_x)) | "
        "**出典：** [x.com](https://x.com/foma_on_x/status/2096845194788217049) および以降の投稿 | "
        "**使用ツール：** Astra, Remotion",

    "## Meta: Prompts That Write Prompts": "## メタ：プロンプトを書くプロンプト",

    "### Director / Animation Supervisor Template": "### 監督 / アニメーションスーパーバイザーのテンプレート",

    "> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.":
        "> そのまま本番で使えるプロンプトに*加えて*、ネガティブプロンプトと3つの代替調整案を出します "
        "—— 最後の項目がほとんどのテンプレートに欠けています。",

    "**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra":
        "**作者：** The AI Average | "
        "**出典：** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | "
        "**使用ツール：** GPT-6 Astra",

    "## Adjacent: Blender & Others": "## 隣接領域：Blender ほか",

    "### Blender 8-Second Product Turntable": "### Blender 8秒の製品ターンテーブル",

    "> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.":
        "> 全編の前に静止画をレンダリングする手順に注目 —— カメラ軌道の失敗を最も安く検出する方法です。",

    "**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra":
        "**作者：** Kingy.ai | "
        "**出典：** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | "
        "**使用ツール：** Blender, Astra",

    "### Known but Unpublished": "### 存在は確認できるが未公開",

    "> Confirmed to exist, no public primary source. **Listed, never reconstructed.**":
        "> 存在は確認済み、公開された一次情報はなし。**掲載のみ、復元はしない。**",

    "| What | Who | Status |\n|---|---|---|\n"
    "| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |\n"
    "| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |\n"
    "| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |\n"
    "| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |\n"
    "| \"Remotion 制作 8 本の裏側\" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |\n"
    "| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |":
        "| 何が | 誰が | 状態 |\n|---|---|---|\n"
        "| 物理 / ソフトボディのモーション skill —— Remotion/HyperFrames のフェードインカードを捨て、"
        "物理的な手応えとソフトボディの力で見せる、4K60 "
        "| [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | 予告済み、skill は未公開 |\n"
        "| Higgsfield + Blender プリビズ + Seedance 2.5 のちゃんばらパイプライン | 二次報道のみ | 一次情報ではない |\n"
        "| `motion-flavor` skill のソース | [@makwanatejas170](https://x.com/makwanatejas170) | 単体では未公開 |\n"
        "| 図解動画用の10本の Master Prompts | [@foma_on_x](https://x.com/foma_on_x) | 有料バンドル |\n"
        "| 「Remotion 制作 8本の裏側」長文note | [@chikaidev](https://x.com/chikaidev) | 未文字起こし |\n"
        "| 返信で主張された5本のモーションプロンプト | [@dawoodkhan254](https://x.com/dawoodkhan254) | 主張のみ、未投稿 |",

    "**The physics / soft-body motion demo itself is public** (the skill is not):":
        "**物理 / ソフトボディのデモ映像自体は公開されています**（skill は非公開）：",

    "## Skills & Tooling": "## Skill とツール",

    "Everyone here is feeding Astra the same base layer. We link, we don't vendor.":
        "ここに集まる全員が、Astra に同じ土台を入れています。リンクは貼りますが、同梱はしません。",

    "| Tool | Install / Link | What it's for |\n|---|---|---|\n"
    "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |\n"
    "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |\n"
    "| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |\n"
    "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |\n"
    "| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |\n"
    "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |\n"
    "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |":
        "| ツール | インストール / リンク | 用途 |\n|---|---|---|\n"
        "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | ほぼすべての事例の下にある土台 |\n"
        "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) "
        "| `SKILL.md` / `AGENTS.md` に貼るもの —— ユーザーのタスク用プロンプトではない |\n"
        "| **Remotion Studio WebMCP** | 4.0.518+ | スクリーンショットをクリックせず、選択範囲・"
        "タイムライン・ジオメトリを直接読む |\n"
        "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157枚のショットレシピカード + テンプレート |\n"
        "| **Montage** | [github](https://github.com/simplexlabs/montage) | ローンチ映像向けのエージェントネイティブな Remotion フォーク |\n"
        "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) "
        "| 再現可能なローンチ映像のソース |\n"
        "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | より広範なコミュニティリスト |",

    "## What the Community Learned": "## コミュニティが学んだこと",

    "Patterns that show up across every thread above:":
        "上記すべてのスレッドに共通して現れるパターン：",

    "**Install the skills first, then talk.** Without skills, a changelog video came out \"noticeably short of it\". With skills installed, one-shots became common.":
        "**まず skill を入れ、それから話す。** skill なしでは、チェンジログ動画は"
        "「明らかに物足りない」出来でした。入れてからは、ワンショットが当たり前になりました。",

    "**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.":
        "**求めるのは成果物であって、雰囲気ではない。** ここで最強のプロンプト（かし子さんのもの）は、"
        "MP4 + 編集可能なソース + ショットJSON + 再レンダリング手順 + ffprobe による検証、で締めています。",

    "**Align the timeline to narration, not \"make it faster overall.\"** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*":
        "**「全体をもっと速く」ではなく、タイムラインをナレーションに合わせる。** Foma の解決策は"
        "その瞬間を名指しすることです：*ナレーションが結果を言うときには、絵はもうそこにある必要がある。*",

    "**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.":
        "**空のフォルダより、プロダクトリポジトリの中で走らせるほうが強い。** AdCar、Atomik、"
        "そしてゲームの CM も、いずれも既存の素材を引き込んでいます。",

    "**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.":
        "**Remotion をプリビズに、生成モデルを本番に**という流れが、日本のシーンでは標準の第2工程に"
        "なりつつあります。",

    "**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.":
        "**Astra が最も力を発揮するのは編成と再設計** —— [@paojiaofty](https://x.com/paojiaofty) は"
        "フェードインカードを受け入れるくらいなら、フレームワークごと捨て去りました。",

    "**People are starting to demand disclosure on \"one-shot\" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.":
        "**「ワンショット」という主張に対して、開示を求める動きが出ています：** 空のリポジトリか既存"
        "プロジェクトか？推論ティアは？何回リトライした？skill は事前に入っていた？"
        "必須項目にする価値があります。",

    "## Completeness Table": "## 完全性の一覧",

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
        "| ID | 種類 | 作者 | 全文あり？ |\n|---|---|---|---|\n"
        "| AdCar TV | 製品ローンチ | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
        "| Atomik | 製品ローンチ | [@makwanatejas170](https://x.com/makwanatejas170) | 仕様はあり、チャットのプロンプトはなし |\n"
        "| video-shotcraft | 製品プロモ skill | Vincentwei1021 | 呼び出しはあり、skill 本体は長い |\n"
        "| Montage | ローンチの土台 | simplexlabs | AGENTS.md のルール |\n"
        "| FeatureReveal | 機能紹介動画 | OpenReplay | ✅ |\n"
        "| Remotion 公式 | 呼び出し | Remotion | ✅（ごく短い） |\n"
        "| パルクールのコンテ | モーションコンテ | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 疾走 control MP4 | モーションコンテ | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 横スクロール追従 | モーションコンテ | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| カメラ構図30種 | リファレンス | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
        "| Seedance 引き渡し | 引き渡し | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
        "| T細胞 | 解説動画 | [@DeryaTR_](https://x.com/DeryaTR_) | ✅（一行） |\n"
        "| Nate の YouTube | チャンネル動画 | Nate Herk | 文字起こし |\n"
        "| Foma の図解 | 図解動画 | [@foma_on_x](https://x.com/foma_on_x) | 短い指示のみ |\n"
        "| 魔女の初飛行 | 生成用ショットスクリプト | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
        "| 6部構成 + JSON | メタ | Elser AI | ✅ |\n"
        "| 監督テンプレート | メタ | The AI Average | ✅ |\n"
        "| Blender ターンテーブル | 3D製品 | Kingy.ai | ✅ |\n"
        "| 物理モーション skill | skill | [@paojiaofty](https://x.com/paojiaofty) | 未公開 |",

    "## Watch List": "## ウォッチリスト",

    "A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.":
        "GitHub Action が6時間ごとにこれらのアカウントを確認し、動画プロンプトらしい投稿があれば "
        "Issue を立てます。",

    "| Account | Why |\n|---|---|\n"
    "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |\n"
    "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |\n"
    "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
    "| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |\n"
    "| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |\n"
    "| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |\n"
    "| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |\n"
    "| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |":
        "| アカウント | 理由 |\n|---|---|\n"
        "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | 最長の Remotion モーションコンテプロンプトの出所 |\n"
        "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion コンテ → Seedance、実践派 |\n"
        "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
        "| [@paojiaofty](https://x.com/paojiaofty) | 予告された物理モーション skill |\n"
        "| [@foma_on_x](https://x.com/foma_on_x) | 図解動画のワークフロー |\n"
        "| [@DeryaTR_](https://x.com/DeryaTR_) | 一行の依頼 |\n"
        "| [@d4m1n](https://x.com/d4m1n) | リポジトリ内でのワンショット |\n"
        "| [@TROOVY](https://x.com/TROOVY) | プロのモーションスタジオの視点 |",

    "[Suggest an account →](../../issues/new?template=watch-account.yml)":
        "[アカウントを提案する →](../../issues/new?template=watch-account.yml)",

    "## How to Contribute": "## 投稿方法",

    "**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.":
        "**[→ プロンプトを投稿する](../../issues/new?template=new-prompt.yml)** —— "
        "貼り付けて、出典をリンクするだけ。git は不要です。",

    "Every entry needs three things:": "各項目には3つ必要です：",

    "| Field | Why |\n|---|---|\n"
    "| **Author** | Name or handle, written the way they write it |\n"
    "| **Source** | Direct link to the post, thread, blog, or video |\n"
    "| **Published** | Date, so readers can judge how current it is |":
        "| 項目 | なぜ必要か |\n|---|---|\n"
        "| **作者** | 名前やハンドル。本人が書いている表記のまま |\n"
        "| **出典** | 投稿・スレッド・ブログ・動画への直接リンク |\n"
        "| **公開日** | どれだけ新しいかを読者が判断できるように |",

    "- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.\n"
    "- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.\n"
    "- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.\n"
    "- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.":
        "- **一字一句そのまま引用する。** 整えない、言い換えない、「改善」しない。\n"
        "- **原文の言語を保つ。** 訳文は `<details>` ブロックに入れ、非公式と明記すること —— "
        "原文を置き換えてはいけない。\n"
        "- **欠けている部分を創作しない。** スクリーンショットで半分しか写っていないなら、"
        "`partial` と明記し、見えている部分だけを引用する。\n"
        "- **公式ドキュメントはリンクする。コピーしない。** API は変わるので、"
        "古いコピーは誤解を招く。",

    "See [CONTRIBUTING.md](CONTRIBUTING.md).": "詳しくは [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。",

    "## License & Acknowledgements": "## ライセンスと謝辞",

    "Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).":
        "リポジトリの構成・編集メモ・スクリプト：[CC BY 4.0](LICENSE)。",

    "**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.":
        "**プロンプトの著作権は各作者に帰属します。** 出典と原文へのリンクを添えて、"
        "参照と研究のために引用しています。",

    "Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.":
        "エージェント駆動の動画制作をオープンに進めるすべての人に感謝します —— "
        "[かし子](https://x.com/Kashiko_AIart)、[なお](https://x.com/Naonekozamurai)、"
        "[Dan](https://x.com/d4m1n)、[Tejas](https://x.com/makwanatejas170)、"
        "[Foma](https://x.com/foma_on_x)、[Derya Unutmaz](https://x.com/DeryaTR_)、"
        "[Kiki](https://x.com/Mayz1169)、Nate Herk、OpenReplay、Elser AI、The AI Average、"
        "Kingy.ai、Vincentwei1021、simplexlabs、そして Remotion チーム。",

    "**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.":
        "**あなたもその一人ですか？**[Issue を作成](../../issues/new?template=correction.yml)すれば、"
        "クレジットの修正、プロンプト全文の追加、作品の削除ができます。異議なく対応します。",


    "⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.":
        "役に立ったら ⭐ **このリポジトリに Star を** —— 他の人がそれで見つけます。",
}
