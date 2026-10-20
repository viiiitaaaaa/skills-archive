# -*- coding: utf-8 -*-
"""French translation table for README.md."""

TOC_TITLE = "Sommaire"

SWITCHER = (
    '<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · '
    '<a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · '
    '<a href="README.es.md">Español</a> · <strong>Français</strong></p>'
)

NOTICE = (
    "> 📄 **Ceci est la traduction française de README.md.** Tous les prompts sont reproduits "
    "mot pour mot dans la langue de publication de leur auteur ; ils ne sont pas traduits. Seul "
    "le texte éditorial est traduit : sommaire, descriptions, statistiques et règles de "
    "contribution. En cas d'écart, la [version anglaise](README.md) fait foi."
)

REPLACE = [
    ("**Author:**", "**Auteur :**"),
    ("**Source:**", "**Source :**"),
    ("**Published:**", "**Publié :**"),
    ("**Tools:**", "**Outils :**"),
    ("**Reused by:**", "**Réutilisé par :**"),
    ("**Works with:**", "**Compatible avec :**"),
    ("**Chinese relay:**", "**Relais en chinois :**"),
    ("**Note:**", "**Remarque :**"),
    ("**Rules:**", "**Règles :**"),
    ("**Are you one of them?**", "**Vous en faites partie ?**"),
    ("🎬 **[Watch the full video →](", "🎬 **[Voir la vidéo complète →]("),
    ("[source repo](", "[dépôt source]("),
    ("[sizzle reel](", "[montage rétrospectif]("),
    ("[full reply](", "[réponse complète]("),
    (" and following posts", " et publications suivantes"),
]

SKIP = {
    "# Awesome Astra Video Prompts",
    "[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)",
}

BLOCKS = {
    # ── LuxReal house CTA (rendered at the top of README.md) ─────────────
    "**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**":
        "**Maintenu par LuxReal** — le pipeline de short drama par IA : un script en entrée, un montage cohérent et entièrement éditable en sortie. **[Essayer gratuitement →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**",
    "**Real prompts for making video with GPT-6 Astra and coding agents.**":
        "**De vrais prompts pour faire de la vidéo avec GPT-6 Astra et des agents de codage.**",

    "Astra doesn't output video. It writes code and drives tools —\n"
    "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg":
        "Astra ne produit pas la vidéo. Il écrit du code et pilote des outils —\n"
        "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg",

    "> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.":
        "> ⚠️ **Mention de copyright** : tous les prompts sont collectés dans des publications "
        "publiques de la communauté à des fins pédagogiques, avec attribution à leurs auteurs "
        "originaux. Si vous estimez qu'un contenu porte atteinte à vos droits, "
        "[ouvrez une issue](../../issues/new) et nous le retirerons rapidement.",

    "> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.":
        "> 🎬 **À propos des aperçus** : les clips animés de `media/` sont de courts extraits en "
        "basse résolution de la *démo publiée* de chaque auteur. Ils sont placés à côté du prompt à "
        "titre de référence et renvoient toujours vers la publication d'origine. Ce sont des "
        "extraits, pas une redistribution des vidéos complètes. Si vous êtes l'auteur et souhaitez "
        "le retrait du vôtre, [ouvrez une issue](../../issues/new?template=correction.yml) ; il "
        "sera retiré sans discussion.",

    "## Table of Contents": "## Sommaire",
    "- [What is this?](#what-is-this)\n- [Quick Start](#quick-start)\n- [Statistics](#statistics)\n- [Featured Prompts](#featured-prompts)\n- [Product Launch & Marketing](#product-launch--marketing)\n- [Motion Previz → Generative](#motion-previz--generative)\n- [End-to-End Production](#end-to-end-production)\n- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)\n- [Adjacent: Blender & Others](#adjacent-blender--others)\n- [Skills & Tooling](#skills--tooling)\n- [What the Community Learned](#what-the-community-learned)\n- [Completeness Table](#completeness-table)\n- [Watch List](#watch-list)\n- [How to Contribute](#how-to-contribute)\n- [License & Acknowledgements](#license--acknowledgements)":
        "@@TOC@@",

    "## What is this?": "## Présentation",

    "Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:":
        "Astra ne fait pas de rendu vidéo nativement. **Il écrit du code, orchestre des plugins et "
        "pilote l'ordinateur.** La vidéo finale vient de :",

    "- **Remotion / HyperFrames** — programmatic motion graphics\n"
    "- **Remotion motion previz → Seedance** and other generative models\n"
    "- **Blender previs** → render or generate\n"
    "- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly":
        "- **Remotion / HyperFrames** —— du motion design programmatique\n"
        "- **Prévisualisation de mouvement Remotion → Seedance** et autres modèles génératifs\n"
        "- **Previs Blender** → rendu ou génération\n"
        "- **HeyGen / ElevenLabs / ffmpeg** —— narration et montage",

    "That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.":
        "C'est pourquoi lui écrire un prompt n'a rien à voir avec la formule magique d'un "
        "text-to-video. Vous émettez un ordre de fabrication, pas la description d'une image.",

    "**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.":
        "**Ce dépôt recueille ces prompts mot pour mot, avec attribution.** Les packs payants et les "
        "skills privés n'ont qu'un emplacement réservé : nous ne reconstituons jamais ce qui n'a pas "
        "été publié.",

    "## Quick Start": "## Démarrage rapide",

    "Then paste any prompt below into Astra, Claude Code, or Codex.":
        "Collez ensuite n'importe quel prompt ci-dessous dans Astra, Claude Code ou Codex.",

    "**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.":
        "**Première visite ?** Commencez par [FeatureReveal](#@@A3@@) —— le prompt le plus court, et "
        "celui qui montre le mieux pourquoi les numéros d'image comptent.",

    "## Statistics": "## Statistiques",

    "| | |\n|---|---|\n| **Entries** | 24 |\n| **Full text available** | 17 |\n| **Languages** | EN · JA · ZH |\n| **Preview clips** | 18 (animated WebP, `media/`) |\n| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |\n| **Last updated** | 2026-09-10 |":
        "| | |\n|---|---|\n| **Entrées** | 24 |\n| **Texte intégral** | 17 |\n"
        "| **Langues** | EN · JA · ZH |\n| **Clips d'aperçu** | 18 (WebP animé, `media/`) |\n"
        "| **Traductions** | 中文 · 日本語 · 한국어 · Español · Français |\n"
        "| **Dernière mise à jour** | 2026-09-10 |",

    "`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only":
        "`full` —— complet tel que publié · `partial` —— une partie seulement · "
        "`spec-only` —— approche décrite, formulation jamais publiée · "
        "`unpublished` —— existence connue, emplacement réservé uniquement",

    "## Featured Prompts": "## Prompts en vedette",
    "#### 📖 Description": "#### 📖 Description",
    "#### 📝 Prompt": "#### 📝 Prompt",
    "#### 📌 Details": "#### 📌 Détails",

    "### 1: High-Speed Parkour Motion Previz":
        "### 1: Previs de parkour à grande vitesse",

    "The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the \"camera must not pass through the character\" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.":
        "Le prompt Astra × Remotion le plus complet publié à ce jour (~223 j'aime / 149 signets). Sa "
        "valeur ne tient pas au sujet, mais à la **liste des livrables, à la validation des contacts "
        "physiques et à la contrainte « la caméra ne doit pas traverser le personnage »**. Réutilisé "
        "mot pour mot ensuite par [@Naonekozamurai](https://x.com/Naonekozamurai), puis passé par "
        "Topview MCP → Seedance 2.5.",

    "<details>\n<summary>Key constraints, summarized (unofficial)</summary>":
        "<details>\n<summary>Contraintes clés, résumées (non officiel)</summary>",

    "- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only\n"
    "- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL\n"
    "- Character: one \"i-shaped\" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing\n"
    "- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state\n"
    "- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification\n"
    "</details>":
        "- 15 s / paysage / SD / 30 fps / sans son / aucun élément externe —— uniquement des formes "
        "pleines simples\n"
        "- TypeScript + Remotion + `useCurrentFrame()` + repère 3D partagé + WebGL\n"
        "- Personnage : un seul proxy « en i » (tête sphérique + torse en capsule) ; le mouvement "
        "passe par l'inclinaison, la compression avant l'appel et l'enfoncement à la réception\n"
        "- **Contraintes dures** : la caméra ne doit jamais traverser le personnage en ligne droite ; "
        "chaque point de réception a besoin d'une surface d'appui ; une même image doit toujours "
        "donner le même état\n"
        "- **Livrables** : MP4 + source éditable + JSON de plans + étapes de re-rendu + vérification "
        "ffprobe/ffmpeg\n"
        "</details>",

    "### 2: AdCar TV — In-Repo One-Shot Launch Video":
        "### 2: AdCar TV —— vidéo de lancement en une passe, dans le dépôt",

    "Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.":
        "À exécuter dans un **dépôt produit déjà existant** : Astra a importé la visionneuse 3D, la "
        "musique et les sons de moteur du projet directement dans Remotion. C'est le schéma à "
        "reproduire quand vous avez déjà des éléments : ne partez pas d'un dossier vide.",

    "> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.":
        "> Note de l'auteur : ffmpeg a surtout servi à poser la voix et la musique ; Astra a tiré la "
        "3D déjà présente dans le dépôt directement vers Remotion.",

    "### 3: FeatureReveal — Frame-Exact Composition Contract":
        "### 3: FeatureReveal —— contrat de composition à l'image près",

    "The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.":
        "Le prompt le plus court de tous, et le meilleur squelette de départ pour une vidéo de "
        "changelog SaaS. Chaque animation est une **plage d'images**, pas une description vague : "
        "c'est ce qui la rend constructible au lieu d'être devinable.",

    "### 4: Witch's First Flight — 15s Generated Shot Script":
        "### 4: Le premier vol de la sorcière —— script de plans généré de 15 s",

    "**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *\"I used it to create the prompt for this animation.\"* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.":
        "**C'est une sortie, pas une entrée** —— un script de plans qu'Astra a *écrit* pour un modèle "
        "vidéo. L'auteur est explicite : *« Je m'en suis servi pour créer le prompt de cette "
        "animation. »* À étudier comme référence de ce à quoi ressemble un bon script de plans "
        "généré : des temps seconde par seconde, des verrous de cohérence du personnage et une "
        "longue liste de négatifs.",

    "### 5: T Cells — One Sentence, Five Minutes":
        "### 5: Lymphocytes T —— une phrase, cinq minutes",

    "The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.":
        "L'exemple le plus repartagé. Le prompt utilisateur tient littéralement en une ligne. "
        "**Cela prouve qu'une consigne très courte + des skills déjà installés battent un long "
        "prompt** : Astra a choisi toute la chaîne d'outils lui-même.",

    "The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):":
        "L'orchestration qu'Astra a choisie (décrite après coup par l'auteur —— ce n'est pas le "
        "prompt d'origine, mais c'est utilisable comme flux de skill) :",

    "### 6: Six-Part Control Template + Shot JSON Contract":
        "### 6: Gabarit de contrôle en six parties + contrat JSON de plans",

    "A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.":
        "Une structure réutilisable en six parties pour n'importe quelle tâche Astra, plus un contrat "
        "JSON de plans à remettre à un générateur. Les blocs **Authority** et **Verification** sont "
        "ceux que la plupart des gens oublient —— et c'est précisément ce qui empêche l'agent de trop "
        "poser de questions ou de livrer quelque chose de cassé.",

    "Six-part control template:": "Gabarit de contrôle en six parties :",
    "Shot JSON contract:": "Contrat JSON de plans :",
    "60-second short:": "Court de 60 secondes :",

    "## Product Launch & Marketing": "## Lancement de produit et marketing",

    "### Atomik — 33-Second Launch Film": "### Atomik —— film de lancement de 33 secondes",

    "> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.":
        "> Film de lancement réalisé en une passe avec un skill `motion-flavor` maison, qui fonctionne "
        "aussi bien sur HyperFrames que sur Remotion. Le prompt du chat n'a jamais été publié ; "
        "l'ingénierie reproductible, si.",

    "X post, verbatim:": "Publication X, mot pour mot :",

    "Spec from the repo — useful as an acceptance contract for an agent:":
        "Spécification tirée du dépôt —— utile comme contrat de recette pour un agent :",

    "**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames":
        "**Auteur :** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | "
        "**Source :** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · "
        "[dépôt source](https://github.com/Tejashmakwana/astra-atomik-launch-video) | "
        "**Publié :** 2026-09 | **Outils :** Astra, Remotion, HyperFrames",

    "### video-shotcraft — Cinematic Product Video Skill":
        "### video-shotcraft —— skill de vidéo produit cinématographique",

    "> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.":
        "> 157 fiches recettes de plans + implémentation Remotion + gabarits de vidéos finies. Le "
        "corps du skill est un long document ; ce qui figure ici, ce sont les invocations côté "
        "utilisateur.",

    "Install:": "Installation :",
    "Invocations (from the official README):": "Invocations (d'après le README officiel) :",

    "<details>\n<summary>Skill frontmatter (determines when the agent activates it)</summary>":
        "<details>\n<summary>Frontmatter du skill (détermine quand l'agent l'active)</summary>",

    "Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).":
        "Trois modes exclusifs : appliquer directement le gabarit Ink Press · création autonome "
        "(suivre `references/pipeline.md` jusqu'au montage final sans rien demander) · collaboratif "
        "(valider brief / direction visuelle / liste de plans étape par étape).",

    "Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic \"promo skin\".\n</details>":
        "Contraintes dures : les vraies pages doivent utiliser des captures d'écran, jamais une fausse "
        "interface dessinée à la main ; la typographie et la couleur doivent provenir des design "
        "tokens du produit, pas d'un « habillage promo » générique.\n</details>",

    "**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex":
        "**Auteur :** Vincentwei1021 | "
        "**Source :** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | "
        "**Outils :** Remotion, Astra, Claude Code, Codex",

    "### Montage — Agent-Native Launch Video Scaffold":
        "### Montage —— échafaudage de vidéo de lancement pensé pour les agents",

    "> A Remotion fork built for agents, aimed at product launch films.":
        "> Un fork de Remotion conçu pour les agents, destiné aux films de lancement de produit.",

    "What the README tells you to say to the agent:":
        "Ce que le README vous dit de dire à l'agent :",

    "The AGENTS.md rules worth stealing:": "Les règles d'AGENTS.md qui valent la peine d'être reprises :",

    "**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion":
        "**Auteur :** simplexlabs | **Source :** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | "
        "**Outils :** Remotion",

    "### Remotion Official Skill Invocations": "### Invocations officielles des skills Remotion",

    "> The official slash commands. Most community prompts assume these are installed.":
        "> Les commandes slash officielles. La plupart des prompts de la communauté partent du "
        "principe qu'elles sont installées.",

    "Bootstrap for a coding agent on a fresh project:":
        "Amorçage pour un agent de codage sur un projet neuf :",

    "Invocations:": "Invocations :",

    "Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.":
        "Skills disponibles : `remotion-best-practices` (routeur), `remotion-create`, "
        "`remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, "
        "`remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, "
        "`remotion-upgrade`, `remotion-multimedia`.",

    "**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion":
        "**Auteur :** Remotion | **Source :** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | "
        "**Outils :** Remotion",

    "### Short Briefs That Still Worked": "### Des consignes minimales qui ont quand même fonctionné",

    "> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.":
        "> Consignes minimales. Utiles comme repère du peu qu'on peut se permettre —— mais pas comme "
        "contrats.",

    "**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)":
        "**Auteur :** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | "
        "**Source :** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",

    "**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker":
        "**Auteur :** [@leon7hao](https://x.com/leon7hao) | "
        "**Source :** [x.com](https://x.com/leon7hao/status/2096844989900914865) | "
        "**Remarque :** GPT-6-Astra medium, aucun skill installé —— l'auteur rapporte un résultat "
        "nettement plus faible",

    "Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)":
        "Résultats publiés sans le prompt : "
        "[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)"
        " (vidéo marketing BrandNewStudy, en une passe) · "
        "[@stoufax](https://x.com/stoufax/status/2096311328600113222)"
        " (lancement d'app iOS, Remotion + ElevenLabs) · "
        "[@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)"
        " (`/goal` + voix fal + plugin Remotion, visite guidée de 90 s)",

    "**@NickYang130 — BrandNewStudy marketing video, one-shot**":
        "**@NickYang130 —— vidéo marketing BrandNewStudy, en une passe**",

    "**@stoufax — iOS app launch, Remotion + ElevenLabs**":
        "**@stoufax —— lancement d'app iOS, Remotion + ElevenLabs**",

    "## Motion Previz → Generative": "## Prévisualisation de mouvement → génératif",

    "> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.":
        "> Cette famille ne décrit pas des images pour un modèle vidéo. Elle fait d'abord rendre à "
        "Astra un **MP4 de contrôle** dans Remotion, puis le remet à Seedance ou équivalent comme "
        "référence de mouvement. C'est de plus en plus le deuxième maillon standard de la scène "
        "japonaise.",

    "### Seedance Handoff Instruction": "### Consigne de passage à Seedance",

    "> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.":
        "> Quoi dire quand vous confiez un rendu Remotion à un modèle génératif. Sans autorisation "
        "explicite de corriger, le modèle reproduit fidèlement les défauts de votre proxy.",

    "<details>\n<summary>English (unofficial)</summary>":
        "<details>\n<summary>Anglais (non officiel)</summary>",

    "**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)":
        "**Auteur :** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | "
        "**Source :** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | "
        "**Publié :** 2026-09 | **Outils :** Remotion → Seedance 2.5 (via Topview MCP)",

    "### Ultra-High-Speed Sprint Control MP4": "### Control MP4 de sprint ultra-rapide",

    "> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.":
        "> Notez la clause anti-triche : construire une vraie route bien longue et réellement avancer "
        "dessus, plutôt que de boucler un arrière-plan. Et **le personnage et la grille doivent "
        "partager le même repère 3D et la même projection caméra** —— pas de fausse caméra qui se "
        "contente de mettre à l'échelle des éléments 2D.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion":
        "**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Source :** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | "
        "**Outils :** Astra, Remotion",

    "### Side-Scrolling Chase, with a Frame Table":
        "### Poursuite en défilement latéral, avec table d'images",

    "> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.":
        "> Le prompt le plus précis image par image de toute la collection : chaque mouvement de "
        "parkour se voit attribuer une plage d'images explicite, avec la sémantique d'intervalle "
        "semi-ouvert écrite noir sur blanc.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion":
        "**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Source :** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | "
        "**Outils :** Astra, Remotion",

    "### 30 Camera Compositions — Reference Sheet Generator":
        "### 30 compositions de caméra —— générateur de planche de référence",

    "> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.":
        "> Construit un catalogue de compositions de caméra à parcourir, que vous pourrez ensuite "
        "citer par identifiant quand vous parlez à un modèle vidéo.",

    "> ⚠️ The post continues past the output requirements; only what's visible is quoted.":
        "> ⚠️ La publication continue au-delà des exigences de sortie ; seuls les éléments visibles "
        "sont cités.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG":
        "**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Source :** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | "
        "**Outils :** Astra, Remotion, HTML/CSS/SVG",

    "> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.":
        "> Le même auteur a aussi publié un flux *chanbara* (combat au sabre) —— "
        "[x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— mais seulement la "
        "méthode, pas le prompt : 1) une liste de plans minimale avec les positions de caméra et de "
        "personnages, 2) une planche d'échantillons d'effets, 3) le mouvement fin piloté par prompt.",

    "## End-to-End Production": "## Production de bout en bout",

    "### Idea → Uploadable YouTube Video": "### De l'idée → une vidéo YouTube prête à publier",

    "> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.":
        "> Environ 50 minutes, et à peu près 60 $ de coût d'API. La ligne qui porte tout, c'est le "
        "refus des brouillons.",

    "Same author, sizzle reel from 152GB of event footage:":
        "Le même auteur, montage rétrospectif à partir de 152 Go de rushes de l'événement :",

    "> ⚠️ Transcribed from the video's narration — no official paste block exists.":
        "> ⚠️ Transcrit depuis la narration de la vidéo —— il n'existe aucun bloc de texte officiel à "
        "copier.",

    "**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames":
        "**Auteur :** Nate Herk | "
        "**Source :** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · "
        "[montage rétrospectif](https://www.youtube.com/watch?v=QhmhUgccaS0) | "
        "**Outils :** Astra, HeyGen, ElevenLabs, HyperFrames",

    "### Narration-First Diagram Explainer": "### Explicatif en schémas, la narration d'abord",

    "> No generated footage at all. Record first, then build the picture to measured narration cues.":
        "> Aucune image générée. On enregistre d'abord, puis on construit l'image en suivant les "
        "repères mesurés de la narration.",

    "Workflow:": "Déroulé :",
    "Published short instructions:": "Consignes courtes publiées :",

    "> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.":
        "> ⚠️ Les 10 Master Prompts de l'auteur sont vendus dans un pack payant et n'ont jamais été "
        "publiés. Seul le squelette public figure ici.",

    "**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion":
        "**Auteur :** Foma ([@foma_on_x](https://x.com/foma_on_x)) | "
        "**Source :** [x.com](https://x.com/foma_on_x/status/2096845194788217049) et publications suivantes | "
        "**Outils :** Astra, Remotion",

    "## Meta: Prompts That Write Prompts": "## Méta : des prompts qui écrivent des prompts",

    "### Director / Animation Supervisor Template":
        "### Gabarit de réalisateur / superviseur d'animation",

    "> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.":
        "> Produit un prompt prêt à produire, *plus* un prompt négatif et trois ajustements de repli "
        "—— cette dernière partie manque dans la plupart des gabarits.",

    "**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra":
        "**Auteur :** The AI Average | "
        "**Source :** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | "
        "**Outils :** GPT-6 Astra",

    "## Adjacent: Blender & Others": "## Domaines voisins : Blender et autres",

    "### Blender 8-Second Product Turntable":
        "### Platine produit de 8 secondes sous Blender",

    "> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.":
        "> Notez l'étape « rendre des images fixes avant la séquence complète » —— le moyen le moins "
        "coûteux de repérer une trajectoire de caméra ratée.",

    "**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra":
        "**Auteur :** Kingy.ai | "
        "**Source :** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | "
        "**Outils :** Blender, Astra",

    "### Known but Unpublished": "### Connus mais non publiés",

    "> Confirmed to exist, no public primary source. **Listed, never reconstructed.**":
        "> Existence confirmée, aucune source primaire publique. **Répertoriés, jamais reconstitués.**",

    "| What | Who | Status |\n|---|---|---|\n"
    "| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |\n"
    "| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |\n"
    "| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |\n"
    "| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |\n"
    "| \"Remotion 制作 8 本の裏側\" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |\n"
    "| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |":
        "| Quoi | Qui | État |\n|---|---|---|\n"
        "| Skill de mouvement physique / soft-body —— abandonner les cartes en fondu de "
        "Remotion/HyperFrames au profit d'une sensation physique et de forces de corps mou, 4K60 "
        "| [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | annoncé, skill non publié |\n"
        "| Pipeline chanbara Higgsfield + previs Blender + Seedance 2.5 | presse de seconde main uniquement | pas une source primaire |\n"
        "| Code source du skill `motion-flavor` | [@makwanatejas170](https://x.com/makwanatejas170) | jamais publié séparément |\n"
        "| 10 Master Prompts pour explicatifs en schémas | [@foma_on_x](https://x.com/foma_on_x) | pack payant |\n"
        "| Note longue « Remotion 制作 8 本の裏側 » | [@chikaidev](https://x.com/chikaidev) | pas encore transcrite |\n"
        "| 5 prompts de mouvement annoncés en réponse | [@dawoodkhan254](https://x.com/dawoodkhan254) | annoncés, jamais publiés |",

    "**The physics / soft-body motion demo itself is public** (the skill is not):":
        "**La démo de mouvement physique / soft-body est publique, elle** (le skill, non) :",

    "## Skills & Tooling": "## Skills et outils",

    "Everyone here is feeding Astra the same base layer. We link, we don't vendor.":
        "Ici, tout le monde donne à Astra la même couche de base. On met des liens, on ne distribue pas.",

    "| Tool | Install / Link | What it's for |\n|---|---|---|\n"
    "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |\n"
    "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |\n"
    "| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |\n"
    "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |\n"
    "| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |\n"
    "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |\n"
    "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |":
        "| Outil | Installation / lien | À quoi ça sert |\n|---|---|---|\n"
        "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | La couche de base sous presque tous les cas |\n"
        "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) "
        "| À coller dans `SKILL.md` / `AGENTS.md` —— ce n'est pas un prompt de tâche utilisateur |\n"
        "| **Remotion Studio WebMCP** | 4.0.518+ | L'agent lit directement la sélection, la timeline et "
        "la géométrie au lieu de cliquer sur des captures |\n"
        "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 fiches recettes de plans + gabarits |\n"
        "| **Montage** | [github](https://github.com/simplexlabs/montage) | Fork Remotion natif pour agents, destiné aux films de lancement |\n"
        "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) "
        "| Source reproductible d'un film de lancement |\n"
        "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Liste communautaire plus large |",

    "## What the Community Learned": "## Ce que la communauté a appris",

    "Patterns that show up across every thread above:":
        "Des motifs qui reviennent dans tous les fils ci-dessus :",

    "**Install the skills first, then talk.** Without skills, a changelog video came out \"noticeably short of it\". With skills installed, one-shots became common.":
        "**Installez d'abord les skills, puis parlez.** Sans skills, une vidéo de changelog est sortie "
        "« nettement en dessous ». Une fois les skills installés, réussir en une passe est devenu la "
        "norme.",

    "**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.":
        "**Exigez des livrables, pas des impressions.** Le prompt le plus solide de tous (celui de "
        "かし子) se termine par : MP4 + source éditable + JSON de plans + étapes de re-rendu + "
        "vérification ffprobe.",

    "**Align the timeline to narration, not \"make it faster overall.\"** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*":
        "**Alignez la timeline sur la narration, pas sur « accélère tout ».** La solution de Foma "
        "consiste à nommer le moment : *l'image doit déjà être là quand la voix dit le résultat.*",

    "**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.":
        "**Travailler dans un dépôt produit vaut mieux qu'un dossier vide.** AdCar, Atomik et le CM du "
        "jeu ont tous récupéré des éléments déjà existants.",

    "**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.":
        "**Remotion pour la prévisualisation, le modèle génératif pour le final** devient le deuxième "
        "maillon standard de la scène japonaise.",

    "**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.":
        "**Astra excelle dans l'orchestration et la refonte** —— "
        "[@paojiaofty](https://x.com/paojiaofty) a jeté tout le framework plutôt que d'accepter des "
        "cartes en fondu.",

    "**People are starting to demand disclosure on \"one-shot\" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.":
        "**On commence à exiger de la transparence sur les affirmations « en une passe » :** dépôt "
        "vide ou projet existant ? quel niveau de raisonnement ? combien de tentatives ? les skills "
        "étaient-ils déjà installés ? À transformer en champ obligatoire.",

    "## Completeness Table": "## Tableau d'exhaustivité",

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
        "| ID | Type | Auteur | Texte intégral ? |\n|---|---|---|---|\n"
        "| AdCar TV | lancement de produit | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
        "| Atomik | lancement de produit | [@makwanatejas170](https://x.com/makwanatejas170) | spec oui, prompt de chat non |\n"
        "| video-shotcraft | skill de promo produit | Vincentwei1021 | invocations oui, corps du skill long |\n"
        "| Montage | échafaudage de lancement | simplexlabs | règles d'AGENTS.md |\n"
        "| FeatureReveal | vidéo de fonctionnalité | OpenReplay | ✅ |\n"
        "| Remotion officiel | invocations | Remotion | ✅ (très court) |\n"
        "| Previs parkour | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| Control MP4 de sprint | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| Poursuite latérale | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 30 compositions caméra | planche de référence | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
        "| Passage à Seedance | passage | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
        "| Lymphocytes T | explicatif | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (une ligne) |\n"
        "| YouTube de Nate | vidéo de chaîne | Nate Herk | transcrit |\n"
        "| Explicatif de Foma | vidéo en schémas | [@foma_on_x](https://x.com/foma_on_x) | consignes courtes seulement |\n"
        "| Vol de la sorcière | script de plans généré | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
        "| Six parties + JSON | méta | Elser AI | ✅ |\n"
        "| Gabarit de réalisateur | méta | The AI Average | ✅ |\n"
        "| Platine Blender | produit 3D | Kingy.ai | ✅ |\n"
        "| Skill de mouvement physique | skill | [@paojiaofty](https://x.com/paojiaofty) | non publié |",

    "## Watch List": "## Liste de veille",

    "A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.":
        "Une GitHub Action vérifie ces comptes toutes les 6 heures et ouvre une issue quand ils "
        "publient quelque chose qui ressemble à un prompt vidéo.",

    "| Account | Why |\n|---|---|\n"
    "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |\n"
    "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |\n"
    "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
    "| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |\n"
    "| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |\n"
    "| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |\n"
    "| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |\n"
    "| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |":
        "| Compte | Pourquoi |\n|---|---|\n"
        "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source des plus longs prompts de previs Remotion |\n"
        "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Previs Remotion → Seedance, les mains dans le cambouis |\n"
        "| [@makwanatejas170](https://x.com/makwanatejas170) | skill motion-flavor / Atomik |\n"
        "| [@paojiaofty](https://x.com/paojiaofty) | skill de mouvement physique, annoncé |\n"
        "| [@foma_on_x](https://x.com/foma_on_x) | flux d'explicatifs en schémas |\n"
        "| [@DeryaTR_](https://x.com/DeryaTR_) | consignes d'une ligne |\n"
        "| [@d4m1n](https://x.com/d4m1n) | réalisations en une passe dans le dépôt |\n"
        "| [@TROOVY](https://x.com/TROOVY) | point de vue d'un studio de motion professionnel |",

    "[Suggest an account →](../../issues/new?template=watch-account.yml)":
        "[Proposer un compte →](../../issues/new?template=watch-account.yml)",

    "## How to Contribute": "## Comment contribuer",

    "**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.":
        "**[→ Proposer un prompt](../../issues/new?template=new-prompt.yml)** —— collez-le, liez la "
        "source. Aucun besoin de git.",

    "Every entry needs three things:": "Chaque entrée a besoin de trois choses :",

    "| Field | Why |\n|---|---|\n"
    "| **Author** | Name or handle, written the way they write it |\n"
    "| **Source** | Direct link to the post, thread, blog, or video |\n"
    "| **Published** | Date, so readers can judge how current it is |":
        "| Champ | Pourquoi |\n|---|---|\n"
        "| **Auteur** | Nom ou pseudo, écrit comme la personne l'écrit elle-même |\n"
        "| **Source** | Lien direct vers la publication, le fil, le blog ou la vidéo |\n"
        "| **Publié** | La date, pour que le lecteur juge de l'actualité |",

    "- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.\n"
    "- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.\n"
    "- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.\n"
    "- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.":
        "- **Citez mot pour mot.** Ne rangez pas, ne reformulez pas, n'« améliorez » pas.\n"
        "- **Gardez la langue d'origine.** Ajoutez une traduction dans un bloc `<details>`, marquée "
        "non officielle —— ne remplacez jamais l'original.\n"
        "- **N'inventez jamais ce qui manque.** Si une capture coupe le prompt en deux, marquez-le "
        "`partial` et ne citez que ce qui est visible.\n"
        "- **Mettez un lien vers la doc officielle, ne la copiez pas.** Leurs API changent ; une "
        "copie périmée ici induirait en erreur.",

    "See [CONTRIBUTING.md](CONTRIBUTING.md).": "Voir [CONTRIBUTING.md](CONTRIBUTING.md).",

    "## License & Acknowledgements": "## Licence et remerciements",

    "Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).":
        "Structure du dépôt, notes éditoriales et scripts : [CC BY 4.0](LICENSE).",

    "**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.":
        "**Les prompts restent la propriété intellectuelle de leurs auteurs.** Ils sont cités ici "
        "avec attribution et lien vers l'original, à titre de référence et d'étude.",

    "Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.":
        "Merci à toutes celles et ceux qui construisent en public de la vidéo pilotée par agent —— "
        "[かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), "
        "[Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), "
        "[Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), "
        "[Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, "
        "Kingy.ai, Vincentwei1021, simplexlabs et l'équipe Remotion.",

    "**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.":
        "**Vous en faites partie ?** [Ouvrez une issue](../../issues/new?template=correction.yml) "
        "pour corriger un crédit, ajouter votre prompt complet ou faire retirer votre travail. "
        "Traité sans discussion.",


    "⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.":
        "⭐ **Mettez une étoile au dépôt** s'il vous est utile —— c'est ainsi que d'autres personnes "
        "qui construisent de la vidéo pilotée par agent le trouvent.",
}
