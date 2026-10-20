<div align="center">

# Awesome Astra Video Prompts

**De vrais prompts pour faire de la vidéo avec GPT-6 Astra et des agents de codage.**

Astra ne produit pas la vidéo. Il écrit du code et pilote des outils —
Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Prompts](https://img.shields.io/badge/prompts-24-blue)
![Full text](https://img.shields.io/badge/full%20text-17-success)
![Previews](https://img.shields.io/badge/previews-18-blueviolet)

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="38"></picture></a>

**Maintenu par LuxReal** — le pipeline de short drama par IA : un script en entrée, un montage cohérent et entièrement éditable en sortie. **[Essayer gratuitement →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**

</div>

<!-- lang-switcher -->
<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <strong>Français</strong></p>
<!-- /lang-switcher -->

> 📄 **Ceci est la traduction française de README.md.** Tous les prompts sont reproduits mot pour mot dans la langue de publication de leur auteur ; ils ne sont pas traduits. Seul le texte éditorial est traduit : sommaire, descriptions, statistiques et règles de contribution. En cas d'écart, la [version anglaise](README.md) fait foi.

> ⚠️ **Mention de copyright** : tous les prompts sont collectés dans des publications publiques de la communauté à des fins pédagogiques, avec attribution à leurs auteurs originaux. Si vous estimez qu'un contenu porte atteinte à vos droits, [ouvrez une issue](../../issues/new) et nous le retirerons rapidement.

> 🎬 **À propos des aperçus** : les clips animés de `media/` sont de courts extraits en basse résolution de la *démo publiée* de chaque auteur. Ils sont placés à côté du prompt à titre de référence et renvoient toujours vers la publication d'origine. Ce sont des extraits, pas une redistribution des vidéos complètes. Si vous êtes l'auteur et souhaitez le retrait du vôtre, [ouvrez une issue](../../issues/new?template=correction.yml) ; il sera retiré sans discussion.

---

## Sommaire

- [Présentation](#présentation)
- [Démarrage rapide](#démarrage-rapide)
- [Statistiques](#statistiques)
- [Prompts en vedette](#prompts-en-vedette)
- [Lancement de produit et marketing](#lancement-de-produit-et-marketing)
- [Prévisualisation de mouvement → génératif](#prévisualisation-de-mouvement--génératif)
- [Production de bout en bout](#production-de-bout-en-bout)
- [Méta : des prompts qui écrivent des prompts](#méta--des-prompts-qui-écrivent-des-prompts)
- [Domaines voisins : Blender et autres](#domaines-voisins--blender-et-autres)
- [Skills et outils](#skills-et-outils)
- [Ce que la communauté a appris](#ce-que-la-communauté-a-appris)
- [Tableau d'exhaustivité](#tableau-dexhaustivité)
- [Liste de veille](#liste-de-veille)
- [Comment contribuer](#comment-contribuer)
- [Licence et remerciements](#licence-et-remerciements)

---

## Présentation

Astra ne fait pas de rendu vidéo nativement. **Il écrit du code, orchestre des plugins et pilote l'ordinateur.** La vidéo finale vient de :

- **Remotion / HyperFrames** —— du motion design programmatique
- **Prévisualisation de mouvement Remotion → Seedance** et autres modèles génératifs
- **Previs Blender** → rendu ou génération
- **HeyGen / ElevenLabs / ffmpeg** —— narration et montage

C'est pourquoi lui écrire un prompt n'a rien à voir avec la formule magique d'un text-to-video. Vous émettez un ordre de fabrication, pas la description d'une image.

**Ce dépôt recueille ces prompts mot pour mot, avec attribution.** Les packs payants et les skills privés n'ont qu'un emplacement réservé : nous ne reconstituons jamais ce qui n'a pas été publié.

---

## Démarrage rapide

```bash
# Official Remotion Agent Skills — the base layer under almost every case here
npx -y skills@latest add remotion-dev/skills -g -y

# Cinematic product video shot library
npx skills add Vincentwei1021/video-shotcraft
```

Collez ensuite n'importe quel prompt ci-dessous dans Astra, Claude Code ou Codex.

**Première visite ?** Commencez par [FeatureReveal](#3-featurereveal--contrat-de-composition-à-limage-près) —— le prompt le plus court, et celui qui montre le mieux pourquoi les numéros d'image comptent.

---

## Statistiques

| | |
|---|---|
| **Entrées** | 24 |
| **Texte intégral** | 17 |
| **Langues** | EN · JA · ZH |
| **Clips d'aperçu** | 18 (WebP animé, `media/`) |
| **Traductions** | 中文 · 日本語 · 한국어 · Español · Français |
| **Dernière mise à jour** | 2026-09-10 |

`full` —— complet tel que publié · `partial` —— une partie seulement · `spec-only` —— approche décrite, formulation jamais publiée · `unpublished` —— existence connue, emplacement réservé uniquement

---

## Prompts en vedette

### 1: Previs de parkour à grande vitesse

![JA](https://img.shields.io/badge/lang-JA-red) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2096096560690209130"><img src="media/parkour-previz.webp" width="440" alt="High-Speed Parkour Motion Previz — Remotion motion previz demo"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Kashiko_AIart/status/2096096560690209130)**

#### 📖 Description

Le prompt Astra × Remotion le plus complet publié à ce jour (~223 j'aime / 149 signets). Sa valeur ne tient pas au sujet, mais à la **liste des livrables, à la validation des contacts physiques et à la contrainte « la caméra ne doit pas traverser le personnage »**. Réutilisé mot pour mot ensuite par [@Naonekozamurai](https://x.com/Naonekozamurai), puis passé par Topview MCP → Seedance 2.5.

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
<summary>Contraintes clés, résumées (non officiel)</summary>

- 15 s / paysage / SD / 30 fps / sans son / aucun élément externe —— uniquement des formes pleines simples
- TypeScript + Remotion + `useCurrentFrame()` + repère 3D partagé + WebGL
- Personnage : un seul proxy « en i » (tête sphérique + torse en capsule) ; le mouvement passe par l'inclinaison, la compression avant l'appel et l'enfoncement à la réception
- **Contraintes dures** : la caméra ne doit jamais traverser le personnage en ligne droite ; chaque point de réception a besoin d'une surface d'appui ; une même image doit toujours donner le même état
- **Livrables** : MP4 + source éditable + JSON de plans + étapes de re-rendu + vérification ffprobe/ffmpeg
</details>

#### 📌 Détails

- **Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart))
- **Source :** [x.com/Kashiko_AIart/status/2096096560690209130](https://x.com/Kashiko_AIart/status/2096096560690209130)
- **Réutilisé par :** [@Naonekozamurai](https://x.com/Naonekozamurai/status/2096871096759030114)
- **Publié :** 2026-09-05
- **Outils :** GPT-6 Astra, Remotion, TypeScript, WebGL

---

### 2: AdCar TV —— vidéo de lancement en une passe, dans le dépôt

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/d4m1n/status/2096258259459964963"><img src="media/adcar-tv.webp" width="440" alt="AdCar TV — 44s one-shot launch video"></a>

🎬 **[Voir la vidéo complète →](https://x.com/d4m1n/status/2096258259459964963)**

#### 📖 Description

À exécuter dans un **dépôt produit déjà existant** : Astra a importé la visionneuse 3D, la musique et les sons de moteur du projet directement dans Remotion. C'est le schéma à reproduire quand vous avez déjà des éléments : ne partez pas d'un dossier vide.

#### 📝 Prompt

```
can we create an overall video presenting the concept of AdCar TV?

make an intro video of 30-60s showing nice visuals (maybe the 3d of the car)?
and really cool car animations / branded stuff, showing off the site etc.
Use ffmpeg, remotion and qwen 3 tts for voice, and install whatever makes sense,
and come up with a cool artboard first and then make the video.
there is some music and car sounds in the codebase already.
```

> Note de l'auteur : ffmpeg a surtout servi à poser la voix et la musique ; Astra a tiré la 3D déjà présente dans le dépôt directement vers Remotion.

#### 📌 Détails

- **Auteur :** Dan ⚡️ ([@d4m1n](https://x.com/d4m1n))
- **Source :** [x.com/d4m1n/status/2096258259459964963](https://x.com/d4m1n/status/2096258259459964963)
- **Publié :** 2026-09-05
- **Outils :** GPT-6 Astra, Remotion, ffmpeg, local Qwen 3 TTS

---

### 3: FeatureReveal —— contrat de composition à l'image près

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Description

Le prompt le plus court de tous, et le meilleur squelette de départ pour une vidéo de changelog SaaS. Chaque animation est une **plage d'images**, pas une description vague : c'est ce qui la rend constructible au lieu d'être devinable.

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

#### 📌 Détails

- **Auteur :** OpenReplay Team
- **Source :** [blog.openreplay.com/making-videos-claude-code-remotion](https://blog.openreplay.com/making-videos-claude-code-remotion/)
- **Publié :** 2026-06-04
- **Compatible avec :** Claude Code, Codex, Astra
- **Outils :** Remotion

---

### 4: Le premier vol de la sorcière —— script de plans généré de 15 s

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Mayz1169/status/2095873015007592679"><img src="media/witch-first-flight.webp" width="440" alt="Witch's First Flight — 15s generated shot"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Mayz1169/status/2095873015007592679)**

#### 📖 Description

**C'est une sortie, pas une entrée** —— un script de plans qu'Astra a *écrit* pour un modèle vidéo. L'auteur est explicite : *« Je m'en suis servi pour créer le prompt de cette animation. »* À étudier comme référence de ce à quoi ressemble un bon script de plans généré : des temps seconde par seconde, des verrous de cohérence du personnage et une longue liste de négatifs.

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

#### 📌 Détails

- **Auteur :** Kiki / Mayz ([@Mayz1169](https://x.com/Mayz1169))
- **Source :** [x.com/Mayz1169/status/2095873015007592679](https://x.com/Mayz1169/status/2095873015007592679) · [réponse complète](https://x.com/Mayz1169/status/2095873204351070296)
- **Publié :** 2026-09
- **Outils :** GPT-6 Astra (as prompt writer) → video model

---

### 5: Lymphocytes T —— une phrase, cinq minutes

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/DeryaTR_/status/2095659170661904804"><img src="media/t-cells.webp" width="440" alt="T Cells — 5-minute explainer, one-line brief"></a>

🎬 **[Voir la vidéo complète →](https://x.com/DeryaTR_/status/2095659170661904804)**

#### 📖 Description

L'exemple le plus repartagé. Le prompt utilisateur tient littéralement en une ligne. **Cela prouve qu'une consigne très courte + des skills déjà installés battent un long prompt** : Astra a choisi toute la chaîne d'outils lui-même.

#### 📝 Prompt

```
Create a 5 minute educational video about T cells.
```

L'orchestration qu'Astra a choisie (décrite après coup par l'auteur —— ce n'est pas le prompt d'origine, mais c'est utilisable comme flux de skill) :

```
Use the Remotion plugin for video generation.
Use Imagegen for visuals.
You may use HeyGen for narration.
Assemble the entire educational video one-shot,
including what to say and how to explain it.
```

#### 📌 Détails

- **Auteur :** Derya Unutmaz, MD ([@DeryaTR_](https://x.com/DeryaTR_))
- **Source :** [x.com/DeryaTR_/status/2095659170661904804](https://x.com/DeryaTR_/status/2095659170661904804)
- **Relais en chinois :** [@LinearUncle](https://x.com/LinearUncle/status/2095719251277701516)
- **Publié :** 2026-09-03
- **Outils :** GPT-6 Astra, Remotion plugin, Imagegen, HeyGen

---

### 6: Gabarit de contrôle en six parties + contrat JSON de plans

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Description

Une structure réutilisable en six parties pour n'importe quelle tâche Astra, plus un contrat JSON de plans à remettre à un générateur. Les blocs **Authority** et **Verification** sont ceux que la plupart des gens oublient —— et c'est précisément ce qui empêche l'agent de trop poser de questions ou de livrer quelque chose de cassé.

#### 📝 Prompt

Gabarit de contrôle en six parties :

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

Contrat JSON de plans :

```
Return valid JSON with project_summary and shots. Each shot must contain id,
story_purpose, framing, subject_action, camera, duration_seconds,
continuity_constraints and audio_cue. Total duration must equal 45 seconds.
```

Court de 60 secondes :

```
Turn the premise below into a 60-second anime short. Preserve the theme and
character rules. Use 8–10 shots, one primary location and no crowd. Each shot
must change story information. Return logline, beat sheet, dialogue, shot table
and continuity checklist. Remove any beat that cannot be shown or heard.
```

#### 📌 Détails

- **Auteur :** Elser AI
- **Source :** [elser.ai/blog/gpt-6-astra-prompt-guide](https://www.elser.ai/blog/gpt-6-astra-prompt-guide)
- **Publié :** 2026-09
- **Outils :** GPT-6 Astra

---

## Lancement de produit et marketing

### Atomik —— film de lancement de 33 secondes

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/makwanatejas170/status/2096555742597988400"><img src="media/atomik-launch.webp" width="440" alt="Atomik — 33s launch film"></a>

🎬 **[Voir la vidéo complète →](https://x.com/makwanatejas170/status/2096555742597988400)**

> Film de lancement réalisé en une passe avec un skill `motion-flavor` maison, qui fonctionne aussi bien sur HyperFrames que sur Remotion. Le prompt du chat n'a jamais été publié ; l'ingénierie reproductible, si.

Publication X, mot pour mot :

```
GPT-6 Astra one-shot this launch video for @atomikgrowth
with New motion-flavor skill that i made
works on both @HyperFrames_ & @Remotion
```

Spécification tirée du dépôt —— utile comme contrat de recette pour un agent :

```
Build a 33-second launch film in Remotion + React + TypeScript + CSS/SVG.
1920×1080, 60 fps, 1980 frames, H.264/AAC.
Rocket, layouts, cursor, typography and transitions must be rendered from code.
Portfolio imagery and soundtrack are bundled local media.
Do not hide a finished-video layer inside the composition.
No AI API call is required to render.
Output: out/final-render.mp4
```

**Auteur :** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source :** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [dépôt source](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Publié :** 2026-09 | **Outils :** Astra, Remotion, HyperFrames

---

### video-shotcraft —— skill de vidéo produit cinématographique

![ZH](https://img.shields.io/badge/lang-ZH-yellow) ![full](https://img.shields.io/badge/invocations-full-success)

<a href="https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd"><img src="media/shotcraft-gallery-intro.webp" width="440" alt="video-shotcraft — 38s gallery intro, produced with the skill"></a>

🎬 **[Voir la vidéo complète →](https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd)**

<a href="https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d"><img src="media/shotcraft-ink-press.webp" width="440" alt="Ink Press — the 36s promo template shipped with the skill"></a>

🎬 **[Voir la vidéo complète →](https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d)**

> 157 fiches recettes de plans + implémentation Remotion + gabarits de vidéos finies. Le corps du skill est un long document ; ce qui figure ici, ce sont les invocations côté utilisateur.

Installation :

```
帮我安装这个 skill：https://github.com/Vincentwei1021/video-shotcraft
```
```bash
npx skills add Vincentwei1021/video-shotcraft
```

Invocations (d'après le README officiel) :

```
用 video-shotcraft 给我的桌面产品做一支宣传片。
用 deck-deal-flyin 和 row-embed 两张镜头卡展示这个功能。
参考 spotlight-hero-card，为这个页面设计一个产品特写镜头。
```
```
用 video-shotcraft 的 Ink Press 模板给我的产品做一支宣传片。
```

<details>
<summary>Frontmatter du skill (détermine quand l'agent l'active)</summary>

```yaml
name: video-shotcraft
description: Create cinematic product videos from shot recipe cards, a validated
template, and code/audio assets (Remotion + real page screenshots + 2.5D camera
moves + beat-synced cuts + sound design). Use when the user asks to turn a
frontend project or webpage into a product video, says "use video-shotcraft to
make a video/promo", names the Ink Press template or asks to reproduce its
effect, or wants a single shot card's motion.
```

Trois modes exclusifs : appliquer directement le gabarit Ink Press · création autonome (suivre `references/pipeline.md` jusqu'au montage final sans rien demander) · collaboratif (valider brief / direction visuelle / liste de plans étape par étape).

Contraintes dures : les vraies pages doivent utiliser des captures d'écran, jamais une fausse interface dessinée à la main ; la typographie et la couleur doivent provenir des design tokens du produit, pas d'un « habillage promo » générique.
</details>

**Auteur :** Vincentwei1021 | **Source :** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Outils :** Remotion, Astra, Claude Code, Codex

---

### Montage —— échafaudage de vidéo de lancement pensé pour les agents

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Un fork de Remotion conçu pour les agents, destiné aux films de lancement de produit.

Ce que le README vous dit de dire à l'agent :

```
Create a master sequence in a new folder and start creating.
Copy any of the examples to get started.
Reference AGENTS.md and leverage all animations possible.
Replace background primitives and the logo with our branding.
```

Les règles d'AGENTS.md qui valent la peine d'être reprises :

```
Do NOT one-shot all sections at once without viewing them.
Build one section → register it → render key frames → verify → next section.
Every frame should have something animating.
Never use flat backgroundColor — always layer vignette + grain + corner glow.
Do NOT default to useLetterPopIn for every text entrance.
Use SF Pro Display. Never use Geist or Inter.
After every change: render stills at entrance / mid / settled, inspect, then MP4.
```

**Auteur :** simplexlabs | **Source :** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Outils :** Remotion

<a href="https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f"><img src="media/montage-launch-film.webp" width="440" alt="Montage — launch film rendered by the agent"></a>

🎬 **[Voir la vidéo complète →](https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f)**

---

### Invocations officielles des skills Remotion

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Les commandes slash officielles. La plupart des prompts de la communauté partent du principe qu'elles sont installées.

Amorçage pour un agent de codage sur un projet neuf :

```
Ensure Node.js is installed.
Install Remotion Skills:
npx -y skills@latest add remotion-dev/skills -g -y
Then use them to create a video.
```

Invocations :

```
/remotion-create Make a promo video for a record store
/remotion-markup Create an animated title card using Inter
/remotion-maps Animate a route from Los Angeles to New York and make the camera follow it
/remotion-render
/remotion-studio
```

Skills disponibles : `remotion-best-practices` (routeur), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.

**Auteur :** Remotion | **Source :** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Outils :** Remotion

---

### Des consignes minimales qui ont quand même fonctionné

![Mixed](https://img.shields.io/badge/lang-mixed-lightgrey) ![partial](https://img.shields.io/badge/text-partial-orange)

> Consignes minimales. Utiles comme repère du peu qu'on peut se permettre —— mais pas comme contrats.

```
游戏做好了，用 remotion 做个好看的 CM
```
**Auteur :** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source :** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)

<a href="https://x.com/guuchacha149182/status/2096813471463882947"><img src="media/game-cm.webp" width="440" alt="Game CM — one-prompt Remotion promo"></a>

🎬 **[Voir la vidéo complète →](https://x.com/guuchacha149182/status/2096813471463882947)**

```
根据最近的 changelog 比较亮眼的功能做个视频。
```
**Auteur :** [@leon7hao](https://x.com/leon7hao) | **Source :** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Remarque :** GPT-6-Astra medium, aucun skill installé —— l'auteur rapporte un résultat nettement plus faible

<a href="https://x.com/leon7hao/status/2096844989900914865"><img src="media/changelog-video.webp" width="440" alt="Changelog video — no skill installed, weaker result"></a>

🎬 **[Voir la vidéo complète →](https://x.com/leon7hao/status/2096844989900914865)**

Résultats publiés sans le prompt : [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (vidéo marketing BrandNewStudy, en une passe) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (lancement d'app iOS, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + voix fal + plugin Remotion, visite guidée de 90 s)

**@NickYang130 —— vidéo marketing BrandNewStudy, en une passe**

<a href="https://x.com/NickYang130/status/2096835902047932521"><img src="media/brandnewstudy-promo.webp" width="440" alt="BrandNewStudy marketing video, one-shot"></a>

🎬 **[Voir la vidéo complète →](https://x.com/NickYang130/status/2096835902047932521)**

**@stoufax —— lancement d'app iOS, Remotion + ElevenLabs**

<a href="https://x.com/stoufax/status/2096311328600113222"><img src="media/ios-app-launch.webp" width="440" alt="iOS app launch — Remotion + ElevenLabs"></a>

🎬 **[Voir la vidéo complète →](https://x.com/stoufax/status/2096311328600113222)**

---

## Prévisualisation de mouvement → génératif

> Cette famille ne décrit pas des images pour un modèle vidéo. Elle fait d'abord rendre à Astra un **MP4 de contrôle** dans Remotion, puis le remet à Seedance ou équivalent comme référence de mouvement. C'est de plus en plus le deuxième maillon standard de la scène japonaise.

### Consigne de passage à Seedance

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Naonekozamurai/status/2096871096759030114"><img src="media/seedance-handoff.webp" width="440" alt="Remotion previz control MP4 handed to Seedance 2.5"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Naonekozamurai/status/2096871096759030114)**

> Quoi dire quand vous confiez un rendu Remotion à un modèle génératif. Sans autorisation explicite de corriger, le modèle reproduit fidèlement les défauts de votre proxy.

```
Remotionで作成した動画はあくまで動きを参照するだけの動画。
参照動画で不自然な挙動や不自然な女の子の体勢は、動画化の際にどんどん修正して良い。
動画では、前後のつながり、動画としてのかっこよさを重視してほしい。
```

<details>
<summary>Anglais (non officiel)</summary>

```
The video made with Remotion is purely a reference for movement.
Any unnatural behavior or unnatural poses of the girl in the reference video
may be freely corrected during video generation.
In the video, prioritize continuity between shots and how good it looks as a video.
```
</details>

**Auteur :** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source :** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Publié :** 2026-09 | **Outils :** Remotion → Seedance 2.5 (via Topview MCP)

---

### Control MP4 de sprint ultra-rapide

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2094182215894831283"><img src="media/sprint-control.webp" width="440" alt="Ultra-high-speed sprint control MP4"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Kashiko_AIart/status/2094182215894831283)**

> Notez la clause anti-triche : construire une vraie route bien longue et réellement avancer dessus, plutôt que de boucler un arrière-plan. Et **le personnage et la grille doivent partager le même repère 3D et la même projection caméra** —— pas de fausse caméra qui se contente de mettre à l'échelle des éléments 2D.

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

**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source :** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Outils :** Astra, Remotion

---

### Poursuite en défilement latéral, avec table d'images

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2093692302745383041"><img src="media/side-scroll-chase.webp" width="440" alt="Side-scrolling chase with a frame table"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Kashiko_AIart/status/2093692302745383041)**

> Le prompt le plus précis image par image de toute la collection : chaque mouvement de parkour se voit attribuer une plage d'images explicite, avec la sémantique d'intervalle semi-ouvert écrite noir sur blanc.

```
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source :** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Outils :** Astra, Remotion

---

### 30 compositions de caméra —— générateur de planche de référence

![JA](https://img.shields.io/badge/lang-JA-red) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/Kashiko_AIart/status/2093575541916061984"><img src="media/camera-comps-30.webp" width="440" alt="30 camera compositions reference sheet"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Kashiko_AIart/status/2093575541916061984)**

> Construit un catalogue de compositions de caméra à parcourir, que vous pourrez ensuite citer par identifiant quand vous parlez à un modèle vidéo.

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

> ⚠️ La publication continue au-delà des exigences de sortie ; seuls les éléments visibles sont cités.

**Auteur :** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source :** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Outils :** Astra, Remotion, HTML/CSS/SVG

> Le même auteur a aussi publié un flux *chanbara* (combat au sabre) —— [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— mais seulement la méthode, pas le prompt : 1) une liste de plans minimale avec les positions de caméra et de personnages, 2) une planche d'échantillons d'effets, 3) le mouvement fin piloté par prompt.

<a href="https://x.com/Kashiko_AIart/status/2096533732547264921"><img src="media/chanbara.webp" width="440" alt="Chanbara sword-fight motion previz"></a>

🎬 **[Voir la vidéo complète →](https://x.com/Kashiko_AIart/status/2096533732547264921)**

---

## Production de bout en bout

### De l'idée → une vidéo YouTube prête à publier

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

> Environ 50 minutes, et à peu près 60 $ de coût d'API. La ligne qui porte tout, c'est le refus des brouillons.

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

Le même auteur, montage rétrospectif à partir de 152 Go de rushes de l'événement :

```
Create me a sizzle reel recap that's a minute long from this event.
```

> ⚠️ Transcrit depuis la narration de la vidéo —— il n'existe aucun bloc de texte officiel à copier.

**Auteur :** Nate Herk | **Source :** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [montage rétrospectif](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Outils :** Astra, HeyGen, ElevenLabs, HyperFrames

---

### Explicatif en schémas, la narration d'abord

![EN](https://img.shields.io/badge/lang-EN-blue) ![spec-only](https://img.shields.io/badge/text-spec--only-lightgrey)

> Aucune image générée. On enregistre d'abord, puis on construit l'image en suivant les repères mesurés de la narration.

Déroulé :

```
1. write and record the explanation
2. mark the moments where the picture needs to change
3. ask Astra to build those moments with shapes, labels and motion in Remotion
4. add captions timed to the recording
5. render and watch with sound
```

Consignes courtes publiées :

```
Use this image for the scene, plan the framing around the measured narration cues,
keep important details visible and stop the movement while the viewer reads the label
```

```
Bring the result on screen when the recording names it,
shorten the entrance animation and preserve the time needed to read the final state
```

> ⚠️ Les 10 Master Prompts de l'auteur sont vendus dans un pack payant et n'ont jamais été publiés. Seul le squelette public figure ici.

**Auteur :** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source :** [x.com](https://x.com/foma_on_x/status/2096845194788217049) et publications suivantes | **Outils :** Astra, Remotion

---

## Méta : des prompts qui écrivent des prompts

### Gabarit de réalisateur / superviseur d'animation

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Produit un prompt prêt à produire, *plus* un prompt négatif et trois ajustements de repli —— cette dernière partie manque dans la plupart des gabarits.

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

**Auteur :** The AI Average | **Source :** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Outils :** GPT-6 Astra

---

## Domaines voisins : Blender et autres

### Platine produit de 8 secondes sous Blender

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Notez l'étape « rendre des images fixes avant la séquence complète » —— le moyen le moins coûteux de repérer une trajectoire de caméra ratée.

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

**Auteur :** Kingy.ai | **Source :** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Outils :** Blender, Astra

---

### Connus mais non publiés

> Existence confirmée, aucune source primaire publique. **Répertoriés, jamais reconstitués.**

| Quoi | Qui | État |
|---|---|---|
| Skill de mouvement physique / soft-body —— abandonner les cartes en fondu de Remotion/HyperFrames au profit d'une sensation physique et de forces de corps mou, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | annoncé, skill non publié |
| Pipeline chanbara Higgsfield + previs Blender + Seedance 2.5 | presse de seconde main uniquement | pas une source primaire |
| Code source du skill `motion-flavor` | [@makwanatejas170](https://x.com/makwanatejas170) | jamais publié séparément |
| 10 Master Prompts pour explicatifs en schémas | [@foma_on_x](https://x.com/foma_on_x) | pack payant |
| Note longue « Remotion 制作 8 本の裏側 » | [@chikaidev](https://x.com/chikaidev) | pas encore transcrite |
| 5 prompts de mouvement annoncés en réponse | [@dawoodkhan254](https://x.com/dawoodkhan254) | annoncés, jamais publiés |

**La démo de mouvement physique / soft-body est publique, elle** (le skill, non) :

<a href="https://x.com/paojiaofty/status/2096830622341976467"><img src="media/physics-motion.webp" width="440" alt="Physics / soft-body motion — 4K60 direct output"></a>

🎬 **[Voir la vidéo complète →](https://x.com/paojiaofty/status/2096830622341976467)**

---

## Skills et outils

Ici, tout le monde donne à Astra la même couche de base. On met des liens, on ne distribue pas.

| Outil | Installation / lien | À quoi ça sert |
|---|---|---|
| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | La couche de base sous presque tous les cas |
| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | À coller dans `SKILL.md` / `AGENTS.md` —— ce n'est pas un prompt de tâche utilisateur |
| **Remotion Studio WebMCP** | 4.0.518+ | L'agent lit directement la sélection, la timeline et la géométrie au lieu de cliquer sur des captures |
| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 fiches recettes de plans + gabarits |
| **Montage** | [github](https://github.com/simplexlabs/montage) | Fork Remotion natif pour agents, destiné aux films de lancement |
| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Source reproductible d'un film de lancement |
| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Liste communautaire plus large |

---

## Ce que la communauté a appris

Des motifs qui reviennent dans tous les fils ci-dessus :

**Installez d'abord les skills, puis parlez.** Sans skills, une vidéo de changelog est sortie « nettement en dessous ». Une fois les skills installés, réussir en une passe est devenu la norme.

**Exigez des livrables, pas des impressions.** Le prompt le plus solide de tous (celui de かし子) se termine par : MP4 + source éditable + JSON de plans + étapes de re-rendu + vérification ffprobe.

**Alignez la timeline sur la narration, pas sur « accélère tout ».** La solution de Foma consiste à nommer le moment : *l'image doit déjà être là quand la voix dit le résultat.*

**Travailler dans un dépôt produit vaut mieux qu'un dossier vide.** AdCar, Atomik et le CM du jeu ont tous récupéré des éléments déjà existants.

**Remotion pour la prévisualisation, le modèle génératif pour le final** devient le deuxième maillon standard de la scène japonaise.

**Astra excelle dans l'orchestration et la refonte** —— [@paojiaofty](https://x.com/paojiaofty) a jeté tout le framework plutôt que d'accepter des cartes en fondu.

**On commence à exiger de la transparence sur les affirmations « en une passe » :** dépôt vide ou projet existant ? quel niveau de raisonnement ? combien de tentatives ? les skills étaient-ils déjà installés ? À transformer en champ obligatoire.

---

## Tableau d'exhaustivité

| ID | Type | Auteur | Texte intégral ? |
|---|---|---|---|
| AdCar TV | lancement de produit | [@d4m1n](https://x.com/d4m1n) | ✅ |
| Atomik | lancement de produit | [@makwanatejas170](https://x.com/makwanatejas170) | spec oui, prompt de chat non |
| video-shotcraft | skill de promo produit | Vincentwei1021 | invocations oui, corps du skill long |
| Montage | échafaudage de lancement | simplexlabs | règles d'AGENTS.md |
| FeatureReveal | vidéo de fonctionnalité | OpenReplay | ✅ |
| Remotion officiel | invocations | Remotion | ✅ (très court) |
| Previs parkour | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| Control MP4 de sprint | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| Poursuite latérale | previs de mouvement | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 30 compositions caméra | planche de référence | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |
| Passage à Seedance | passage | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |
| Lymphocytes T | explicatif | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (une ligne) |
| YouTube de Nate | vidéo de chaîne | Nate Herk | transcrit |
| Explicatif de Foma | vidéo en schémas | [@foma_on_x](https://x.com/foma_on_x) | consignes courtes seulement |
| Vol de la sorcière | script de plans généré | [@Mayz1169](https://x.com/Mayz1169) | ✅ |
| Six parties + JSON | méta | Elser AI | ✅ |
| Gabarit de réalisateur | méta | The AI Average | ✅ |
| Platine Blender | produit 3D | Kingy.ai | ✅ |
| Skill de mouvement physique | skill | [@paojiaofty](https://x.com/paojiaofty) | non publié |

---

## Liste de veille

Une GitHub Action vérifie ces comptes toutes les 6 heures et ouvre une issue quand ils publient quelque chose qui ressemble à un prompt vidéo.

| Compte | Pourquoi |
|---|---|
| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source des plus longs prompts de previs Remotion |
| [@Naonekozamurai](https://x.com/Naonekozamurai) | Previs Remotion → Seedance, les mains dans le cambouis |
| [@makwanatejas170](https://x.com/makwanatejas170) | skill motion-flavor / Atomik |
| [@paojiaofty](https://x.com/paojiaofty) | skill de mouvement physique, annoncé |
| [@foma_on_x](https://x.com/foma_on_x) | flux d'explicatifs en schémas |
| [@DeryaTR_](https://x.com/DeryaTR_) | consignes d'une ligne |
| [@d4m1n](https://x.com/d4m1n) | réalisations en une passe dans le dépôt |
| [@TROOVY](https://x.com/TROOVY) | point de vue d'un studio de motion professionnel |

[Proposer un compte →](../../issues/new?template=watch-account.yml)

---

## Comment contribuer

**[→ Proposer un prompt](../../issues/new?template=new-prompt.yml)** —— collez-le, liez la source. Aucun besoin de git.

Chaque entrée a besoin de trois choses :

| Champ | Pourquoi |
|---|---|
| **Auteur** | Nom ou pseudo, écrit comme la personne l'écrit elle-même |
| **Source** | Lien direct vers la publication, le fil, le blog ou la vidéo |
| **Publié** | La date, pour que le lecteur juge de l'actualité |

**Règles :**

- **Citez mot pour mot.** Ne rangez pas, ne reformulez pas, n'« améliorez » pas.
- **Gardez la langue d'origine.** Ajoutez une traduction dans un bloc `<details>`, marquée non officielle —— ne remplacez jamais l'original.
- **N'inventez jamais ce qui manque.** Si une capture coupe le prompt en deux, marquez-le `partial` et ne citez que ce qui est visible.
- **Mettez un lien vers la doc officielle, ne la copiez pas.** Leurs API changent ; une copie périmée ici induirait en erreur.

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Licence et remerciements

Structure du dépôt, notes éditoriales et scripts : [CC BY 4.0](LICENSE).

**Les prompts restent la propriété intellectuelle de leurs auteurs.** Ils sont cités ici avec attribution et lien vers l'original, à titre de référence et d'étude.

Merci à toutes celles et ceux qui construisent en public de la vidéo pilotée par agent —— [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs et l'équipe Remotion.

**Vous en faites partie ?** [Ouvrez une issue](../../issues/new?template=correction.yml) pour corriger un crédit, ajouter votre prompt complet ou faire retirer votre travail. Traité sans discussion.

---

<div align="center">

⭐ **Mettez une étoile au dépôt** s'il vous est utile —— c'est ainsi que d'autres personnes qui construisent de la vidéo pilotée par agent le trouvent.

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="32"></picture></a>

[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)

</div>
