<div align="center">

# Awesome Astra Video Prompts

**Prompts reales para hacer vídeo con GPT-6 Astra y agentes de programación.**

Astra no genera el vídeo. Escribe código y maneja herramientas —
Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Prompts](https://img.shields.io/badge/prompts-24-blue)
![Full text](https://img.shields.io/badge/full%20text-17-success)
![Previews](https://img.shields.io/badge/previews-18-blueviolet)

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="38"></picture></a>

**Mantenido por LuxReal** — el pipeline de IA para short dramas: entra un guion y sale un montaje coherente y totalmente editable. **[Pruébalo gratis →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**

</div>

<!-- lang-switcher -->
<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <strong>Español</strong> · <a href="README.fr.md">Français</a></p>
<!-- /lang-switcher -->

> 📄 **Esta es la traducción al español de README.md.** Todos los prompts se reproducen literalmente en el idioma en que su autor los publicó; no se traducen. Solo se traduce el texto editorial: índice, descripciones, estadísticas y normas de contribución. Si hay discrepancias, prevalece la [versión en inglés](README.md).

> ⚠️ **Aviso de copyright**: todos los prompts se recopilan de publicaciones públicas de la comunidad con fines educativos y con atribución a sus autores originales. Si crees que algún contenido infringe tus derechos, [abre una incidencia](../../issues/new) y lo retiraremos de inmediato.

> 🎬 **Sobre las previsualizaciones**: los clips animados de `media/` son extractos cortos y de baja resolución de la *demo publicada* de cada autor. Se incluyen solo como referencia junto al prompt y siempre enlazan a la publicación original. Son extractos, no redistribuciones del vídeo completo. Si eres el autor y quieres que se retire el tuyo, [abre una incidencia](../../issues/new?template=correction.yml); se elimina sin discusión.

---

## Índice

- [¿Qué es esto?](#qué-es-esto)
- [Inicio rápido](#inicio-rápido)
- [Estadísticas](#estadísticas)
- [Prompts destacados](#prompts-destacados)
- [Lanzamiento de producto y marketing](#lanzamiento-de-producto-y-marketing)
- [Previz de movimiento → generativo](#previz-de-movimiento--generativo)
- [Producción de principio a fin](#producción-de-principio-a-fin)
- [Meta: prompts que escriben prompts](#meta-prompts-que-escriben-prompts)
- [Terrenos adyacentes: Blender y otros](#terrenos-adyacentes-blender-y-otros)
- [Skills y herramientas](#skills-y-herramientas)
- [Lo que ha aprendido la comunidad](#lo-que-ha-aprendido-la-comunidad)
- [Tabla de completitud](#tabla-de-completitud)
- [Lista de seguimiento](#lista-de-seguimiento)
- [Cómo contribuir](#cómo-contribuir)
- [Licencia y agradecimientos](#licencia-y-agradecimientos)

---

## ¿Qué es esto?

Astra no renderiza vídeo de forma nativa. **Escribe código, orquesta plugins y maneja el ordenador.** El vídeo terminado sale de:

- **Remotion / HyperFrames** —— gráficos en movimiento programáticos
- **Previz de movimiento en Remotion → Seedance** y otros modelos generativos
- **Previs en Blender** → renderizar o generar
- **HeyGen / ElevenLabs / ffmpeg** —— narración y montaje

Por eso, escribirle un prompt es radicalmente distinto a recitar un conjuro de texto a vídeo. Lo que emites es una orden de compilación, no la descripción de una imagen.

**Este repositorio recopila esos prompts literalmente y con crédito.** Los packs de pago y los skills privados solo dejan un marcador de posición: nunca reconstruimos lo que no se publicó.

---

## Inicio rápido

```bash
# Official Remotion Agent Skills — the base layer under almost every case here
npx -y skills@latest add remotion-dev/skills -g -y

# Cinematic product video shot library
npx skills add Vincentwei1021/video-shotcraft
```

Después, pega cualquiera de los prompts de abajo en Astra, Claude Code o Codex.

**¿Es tu primera vez?** Empieza por [FeatureReveal](#3-featurereveal--contrato-de-composición-exacto-al-fotograma) — el prompt más corto y el que mejor explica por qué importan los números de fotograma.

---

## Estadísticas

| | |
|---|---|
| **Entradas** | 24 |
| **Texto completo** | 17 |
| **Idiomas** | EN · JA · ZH |
| **Clips de previsualización** | 18 (WebP animado, `media/`) |
| **Traducciones** | 中文 · 日本語 · 한국어 · Español · Français |
| **Última actualización** | 2026-09-10 |

`full` —— completo tal como se publicó · `partial` —— solo una parte · `spec-only` —— se describe el enfoque, el texto nunca se publicó · `unpublished` —— se sabe que existe, solo un marcador de posición

---

## Prompts destacados

### 1: Previz de parkour a alta velocidad

![JA](https://img.shields.io/badge/lang-JA-red) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2096096560690209130"><img src="media/parkour-previz.webp" width="440" alt="High-Speed Parkour Motion Previz — Remotion motion previz demo"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Kashiko_AIart/status/2096096560690209130)**

#### 📖 Descripción

El prompt de Astra × Remotion más completo publicado hasta ahora (~223 me gusta / 149 guardados). Su valor no está en el tema, sino en la **lista de entregables, la validación del contacto físico y la restricción de que «la cámara no debe atravesar al personaje»**. Después lo reutilizó literalmente [@Naonekozamurai](https://x.com/Naonekozamurai) y lo pasó por Topview MCP → Seedance 2.5.

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
<summary>Restricciones clave, resumidas (no oficial)</summary>

- 15 s / horizontal / SD / 30 fps / sin sonido / sin recursos externos —— solo formas sólidas simples
- TypeScript + Remotion + `useCurrentFrame()` + sistema de coordenadas 3D compartido + WebGL
- Personaje: un único proxy «en forma de i» (cabeza esférica + torso de cápsula); el movimiento se transmite con inclinación, compresión antes del salto y hundimiento al aterrizar
- **Restricciones duras**: la cámara nunca debe atravesar al personaje en línea recta; cada punto de aterrizaje necesita una superficie de apoyo; un mismo fotograma debe dar siempre el mismo estado
- **Entregables**: MP4 + código editable + JSON de planos + pasos de re-render + verificación con ffprobe/ffmpeg
</details>

#### 📌 Detalles

- **Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart))
- **Fuente:** [x.com/Kashiko_AIart/status/2096096560690209130](https://x.com/Kashiko_AIart/status/2096096560690209130)
- **Reutilizado por:** [@Naonekozamurai](https://x.com/Naonekozamurai/status/2096871096759030114)
- **Publicado:** 2026-09-05
- **Herramientas:** GPT-6 Astra, Remotion, TypeScript, WebGL

---

### 2: AdCar TV —— vídeo de lanzamiento en una sola pasada dentro del repositorio

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/d4m1n/status/2096258259459964963"><img src="media/adcar-tv.webp" width="440" alt="AdCar TV — 44s one-shot launch video"></a>

🎬 **[Ver el vídeo completo →](https://x.com/d4m1n/status/2096258259459964963)**

#### 📖 Descripción

Se ejecuta dentro de un **repositorio de producto ya existente**: Astra importó el visor 3D, la música y los sonidos de motor del propio proyecto directamente en Remotion. Este es el patrón que hay que copiar cuando ya tienes recursos: no empieces desde una carpeta vacía.

#### 📝 Prompt

```
can we create an overall video presenting the concept of AdCar TV?

make an intro video of 30-60s showing nice visuals (maybe the 3d of the car)?
and really cool car animations / branded stuff, showing off the site etc.
Use ffmpeg, remotion and qwen 3 tts for voice, and install whatever makes sense,
and come up with a cool artboard first and then make the video.
there is some music and car sounds in the codebase already.
```

> Nota del autor: ffmpeg se usó sobre todo para acoplar la voz y la música; Astra llevó el 3D que ya existía en el repositorio directamente a Remotion.

#### 📌 Detalles

- **Autor:** Dan ⚡️ ([@d4m1n](https://x.com/d4m1n))
- **Fuente:** [x.com/d4m1n/status/2096258259459964963](https://x.com/d4m1n/status/2096258259459964963)
- **Publicado:** 2026-09-05
- **Herramientas:** GPT-6 Astra, Remotion, ffmpeg, local Qwen 3 TTS

---

### 3: FeatureReveal —— contrato de composición exacto al fotograma

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Descripción

El prompt más corto de todos y el mejor esqueleto de partida para un vídeo de changelog de SaaS. Cada animación es un **rango de fotogramas**, no una descripción vaga: eso es lo que lo hace construible en lugar de adivinable.

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

#### 📌 Detalles

- **Autor:** OpenReplay Team
- **Fuente:** [blog.openreplay.com/making-videos-claude-code-remotion](https://blog.openreplay.com/making-videos-claude-code-remotion/)
- **Publicado:** 2026-06-04
- **Compatible con:** Claude Code, Codex, Astra
- **Herramientas:** Remotion

---

### 4: El primer vuelo de la bruja —— guion de planos generado de 15 s

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Mayz1169/status/2095873015007592679"><img src="media/witch-first-flight.webp" width="440" alt="Witch's First Flight — 15s generated shot"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Mayz1169/status/2095873015007592679)**

#### 📖 Descripción

**Esto es salida, no entrada**: un guion de planos que Astra *escribió* para un modelo de vídeo. El autor fue explícito: *«Lo usé para crear el prompt de esta animación.»* Estúdialo como referencia de cómo se ve un buen guion de planos generado: tiempos segundo a segundo, bloqueos de consistencia del personaje y una larga lista de negativos.

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

#### 📌 Detalles

- **Autor:** Kiki / Mayz ([@Mayz1169](https://x.com/Mayz1169))
- **Fuente:** [x.com/Mayz1169/status/2095873015007592679](https://x.com/Mayz1169/status/2095873015007592679) · [respuesta completa](https://x.com/Mayz1169/status/2095873204351070296)
- **Publicado:** 2026-09
- **Herramientas:** GPT-6 Astra (as prompt writer) → video model

---

### 5: Linfocitos T —— una frase, cinco minutos

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/DeryaTR_/status/2095659170661904804"><img src="media/t-cells.webp" width="440" alt="T Cells — 5-minute explainer, one-line brief"></a>

🎬 **[Ver el vídeo completo →](https://x.com/DeryaTR_/status/2095659170661904804)**

#### 📖 Descripción

El ejemplo más compartido. El prompt del usuario es literalmente una línea. **Esto demuestra que una instrucción muy breve + skills ya instalados supera a un prompt largo**: Astra eligió toda la cadena de herramientas por su cuenta.

#### 📝 Prompt

```
Create a 5 minute educational video about T cells.
```

La orquestación que eligió Astra (descrita después por el autor: no es el prompt original, pero sirve como flujo de skill):

```
Use the Remotion plugin for video generation.
Use Imagegen for visuals.
You may use HeyGen for narration.
Assemble the entire educational video one-shot,
including what to say and how to explain it.
```

#### 📌 Detalles

- **Autor:** Derya Unutmaz, MD ([@DeryaTR_](https://x.com/DeryaTR_))
- **Fuente:** [x.com/DeryaTR_/status/2095659170661904804](https://x.com/DeryaTR_/status/2095659170661904804)
- **Reenvío en chino:** [@LinearUncle](https://x.com/LinearUncle/status/2095719251277701516)
- **Publicado:** 2026-09-03
- **Herramientas:** GPT-6 Astra, Remotion plugin, Imagegen, HeyGen

---

### 6: Plantilla de control en seis partes + contrato JSON de planos

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 Descripción

Una estructura reutilizable en seis partes para cualquier tarea de Astra, más un contrato JSON de planos que puedes entregar a un generador. Los bloques **Authority** y **Verification** son los que casi todo el mundo omite, y son justo los que impiden que el agente pregunte de más o entregue algo roto.

#### 📝 Prompt

Plantilla de control en seis partes:

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

Contrato JSON de planos:

```
Return valid JSON with project_summary and shots. Each shot must contain id,
story_purpose, framing, subject_action, camera, duration_seconds,
continuity_constraints and audio_cue. Total duration must equal 45 seconds.
```

Corto de 60 segundos:

```
Turn the premise below into a 60-second anime short. Preserve the theme and
character rules. Use 8–10 shots, one primary location and no crowd. Each shot
must change story information. Return logline, beat sheet, dialogue, shot table
and continuity checklist. Remove any beat that cannot be shown or heard.
```

#### 📌 Detalles

- **Autor:** Elser AI
- **Fuente:** [elser.ai/blog/gpt-6-astra-prompt-guide](https://www.elser.ai/blog/gpt-6-astra-prompt-guide)
- **Publicado:** 2026-09
- **Herramientas:** GPT-6 Astra

---

## Lanzamiento de producto y marketing

### Atomik —— película de lanzamiento de 33 segundos

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/makwanatejas170/status/2096555742597988400"><img src="media/atomik-launch.webp" width="440" alt="Atomik — 33s launch film"></a>

🎬 **[Ver el vídeo completo →](https://x.com/makwanatejas170/status/2096555742597988400)**

> Película de lanzamiento hecha de una sola pasada con un skill `motion-flavor` propio que funciona tanto en HyperFrames como en Remotion. El prompt del chat nunca se publicó; la ingeniería reproducible, sí.

Publicación en X, literal:

```
GPT-6 Astra one-shot this launch video for @atomikgrowth
with New motion-flavor skill that i made
works on both @HyperFrames_ & @Remotion
```

Especificación del repositorio —— útil como contrato de aceptación para un agente:

```
Build a 33-second launch film in Remotion + React + TypeScript + CSS/SVG.
1920×1080, 60 fps, 1980 frames, H.264/AAC.
Rocket, layouts, cursor, typography and transitions must be rendered from code.
Portfolio imagery and soundtrack are bundled local media.
Do not hide a finished-video layer inside the composition.
No AI API call is required to render.
Output: out/final-render.mp4
```

**Autor:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Fuente:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [repositorio fuente](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Publicado:** 2026-09 | **Herramientas:** Astra, Remotion, HyperFrames

---

### video-shotcraft —— skill de vídeo de producto cinematográfico

![ZH](https://img.shields.io/badge/lang-ZH-yellow) ![full](https://img.shields.io/badge/invocations-full-success)

<a href="https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd"><img src="media/shotcraft-gallery-intro.webp" width="440" alt="video-shotcraft — 38s gallery intro, produced with the skill"></a>

🎬 **[Ver el vídeo completo →](https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd)**

<a href="https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d"><img src="media/shotcraft-ink-press.webp" width="440" alt="Ink Press — the 36s promo template shipped with the skill"></a>

🎬 **[Ver el vídeo completo →](https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d)**

> 157 tarjetas de recetas de plano + implementación en Remotion + plantillas de vídeo terminado. El cuerpo del skill es un documento largo; lo que aparece aquí son las invocaciones del lado del usuario.

Instalación:

```
帮我安装这个 skill：https://github.com/Vincentwei1021/video-shotcraft
```
```bash
npx skills add Vincentwei1021/video-shotcraft
```

Invocaciones (del README oficial):

```
用 video-shotcraft 给我的桌面产品做一支宣传片。
用 deck-deal-flyin 和 row-embed 两张镜头卡展示这个功能。
参考 spotlight-hero-card，为这个页面设计一个产品特写镜头。
```
```
用 video-shotcraft 的 Ink Press 模板给我的产品做一支宣传片。
```

<details>
<summary>Frontmatter del skill (determina cuándo lo activa el agente)</summary>

```yaml
name: video-shotcraft
description: Create cinematic product videos from shot recipe cards, a validated
template, and code/audio assets (Remotion + real page screenshots + 2.5D camera
moves + beat-synced cuts + sound design). Use when the user asks to turn a
frontend project or webpage into a product video, says "use video-shotcraft to
make a video/promo", names the Ink Press template or asks to reproduce its
effect, or wants a single shot card's motion.
```

Tres modos mutuamente excluyentes: aplicar la plantilla Ink Press directamente · creación autónoma (seguir `references/pipeline.md` hasta un montaje final sin preguntar) · colaborativo (confirmar brief / dirección visual / lista de planos paso a paso).

Restricciones duras: las páginas reales deben usar capturas de pantalla, nunca una interfaz falsa dibujada a mano; la tipografía y el color deben salir de los tokens de diseño del producto, no de una «piel promocional» genérica.
</details>

**Autor:** Vincentwei1021 | **Fuente:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Herramientas:** Remotion, Astra, Claude Code, Codex

---

### Montage —— andamiaje de vídeo de lanzamiento nativo para agentes

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Un fork de Remotion hecho para agentes, orientado a películas de lanzamiento de producto.

Lo que el README te dice que le digas al agente:

```
Create a master sequence in a new folder and start creating.
Copy any of the examples to get started.
Reference AGENTS.md and leverage all animations possible.
Replace background primitives and the logo with our branding.
```

Reglas de AGENTS.md que vale la pena copiar:

```
Do NOT one-shot all sections at once without viewing them.
Build one section → register it → render key frames → verify → next section.
Every frame should have something animating.
Never use flat backgroundColor — always layer vignette + grain + corner glow.
Do NOT default to useLetterPopIn for every text entrance.
Use SF Pro Display. Never use Geist or Inter.
After every change: render stills at entrance / mid / settled, inspect, then MP4.
```

**Autor:** simplexlabs | **Fuente:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Herramientas:** Remotion

<a href="https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f"><img src="media/montage-launch-film.webp" width="440" alt="Montage — launch film rendered by the agent"></a>

🎬 **[Ver el vídeo completo →](https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f)**

---

### Invocaciones de los skills oficiales de Remotion

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Los comandos de barra oficiales. La mayoría de los prompts de la comunidad dan por hecho que están instalados.

Arranque para un agente de programación en un proyecto nuevo:

```
Ensure Node.js is installed.
Install Remotion Skills:
npx -y skills@latest add remotion-dev/skills -g -y
Then use them to create a video.
```

Invocaciones:

```
/remotion-create Make a promo video for a record store
/remotion-markup Create an animated title card using Inter
/remotion-maps Animate a route from Los Angeles to New York and make the camera follow it
/remotion-render
/remotion-studio
```

Skills disponibles: `remotion-best-practices` (enrutador), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.

**Autor:** Remotion | **Fuente:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Herramientas:** Remotion

---

### Instrucciones mínimas que aun así funcionaron

![Mixed](https://img.shields.io/badge/lang-mixed-lightgrey) ![partial](https://img.shields.io/badge/text-partial-orange)

> Instrucciones mínimas. Útiles como referencia de lo poco que basta para salir del paso, pero no como contratos.

```
游戏做好了，用 remotion 做个好看的 CM
```
**Autor:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Fuente:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)

<a href="https://x.com/guuchacha149182/status/2096813471463882947"><img src="media/game-cm.webp" width="440" alt="Game CM — one-prompt Remotion promo"></a>

🎬 **[Ver el vídeo completo →](https://x.com/guuchacha149182/status/2096813471463882947)**

```
根据最近的 changelog 比较亮眼的功能做个视频。
```
**Autor:** [@leon7hao](https://x.com/leon7hao) | **Fuente:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Nota:** GPT-6-Astra medium, sin skill instalado —— el autor señaló que el resultado fue claramente más flojo

<a href="https://x.com/leon7hao/status/2096844989900914865"><img src="media/changelog-video.webp" width="440" alt="Changelog video — no skill installed, weaker result"></a>

🎬 **[Ver el vídeo completo →](https://x.com/leon7hao/status/2096844989900914865)**

Resultados publicados sin el prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (vídeo de marketing de BrandNewStudy, una sola pasada) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (lanzamiento de app iOS, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + voz de fal + plugin de Remotion, recorrido de 90 s)

**@NickYang130 —— vídeo de marketing de BrandNewStudy, una sola pasada**

<a href="https://x.com/NickYang130/status/2096835902047932521"><img src="media/brandnewstudy-promo.webp" width="440" alt="BrandNewStudy marketing video, one-shot"></a>

🎬 **[Ver el vídeo completo →](https://x.com/NickYang130/status/2096835902047932521)**

**@stoufax —— lanzamiento de app iOS, Remotion + ElevenLabs**

<a href="https://x.com/stoufax/status/2096311328600113222"><img src="media/ios-app-launch.webp" width="440" alt="iOS app launch — Remotion + ElevenLabs"></a>

🎬 **[Ver el vídeo completo →](https://x.com/stoufax/status/2096311328600113222)**

---

## Previz de movimiento → generativo

> Esta familia no describe imágenes para un modelo de vídeo. Hace que Astra renderice primero un **MP4 de control** en Remotion y luego lo entrega a Seedance o similar como referencia de movimiento. Cada vez es más el segundo eslabón habitual en la escena japonesa.

### Instrucción de cesión a Seedance

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Naonekozamurai/status/2096871096759030114"><img src="media/seedance-handoff.webp" width="440" alt="Remotion previz control MP4 handed to Seedance 2.5"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Naonekozamurai/status/2096871096759030114)**

> Qué decir cuando le das un render de Remotion a un modelo generativo. Sin el permiso explícito para corregir, el modelo reproduce fielmente los defectos de tu marcador de posición.

```
Remotionで作成した動画はあくまで動きを参照するだけの動画。
参照動画で不自然な挙動や不自然な女の子の体勢は、動画化の際にどんどん修正して良い。
動画では、前後のつながり、動画としてのかっこよさを重視してほしい。
```

<details>
<summary>Inglés (no oficial)</summary>

```
The video made with Remotion is purely a reference for movement.
Any unnatural behavior or unnatural poses of the girl in the reference video
may be freely corrected during video generation.
In the video, prioritize continuity between shots and how good it looks as a video.
```
</details>

**Autor:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Fuente:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Publicado:** 2026-09 | **Herramientas:** Remotion → Seedance 2.5 (vía Topview MCP)

---

### MP4 de control de sprint a altísima velocidad

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2094182215894831283"><img src="media/sprint-control.webp" width="440" alt="Ultra-high-speed sprint control MP4"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Kashiko_AIart/status/2094182215894831283)**

> Fíjate en la cláusula antitrampas: construye un camino largo de verdad y avanza por él, en lugar de poner un fondo en bucle. Y **la persona y la rejilla deben compartir el mismo sistema de coordenadas 3D y la misma proyección de cámara**: nada de una cámara falsa que solo escala recursos 2D.

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

**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Herramientas:** Astra, Remotion

---

### Persecución de desplazamiento lateral, con tabla de fotogramas

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2093692302745383041"><img src="media/side-scroll-chase.webp" width="440" alt="Side-scrolling chase with a frame table"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Kashiko_AIart/status/2093692302745383041)**

> El prompt más preciso en cuanto a fotogramas de toda la colección: cada movimiento de parkour tiene asignado un rango de fotogramas explícito, con la semántica de intervalo semiabierto escrita sin ambigüedad.

```
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Herramientas:** Astra, Remotion

---

### 30 composiciones de cámara —— generador de hoja de referencia

![JA](https://img.shields.io/badge/lang-JA-red) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/Kashiko_AIart/status/2093575541916061984"><img src="media/camera-comps-30.webp" width="440" alt="30 camera compositions reference sheet"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Kashiko_AIart/status/2093575541916061984)**

> Construye un catálogo navegable de composiciones de cámara que luego puedes citar por ID cuando hables con un modelo de vídeo.

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

> ⚠️ La publicación continúa más allá de los requisitos de salida; aquí solo se cita lo visible.

**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Herramientas:** Astra, Remotion, HTML/CSS/SVG

> El mismo autor publicó también un flujo de *chanbara* (combate con espada) —— [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— pero solo el método, no el prompt: 1) una lista mínima de planos con la posición de cámara y personajes, 2) una hoja de muestras de efectos, 3) movimiento fino controlado por prompt.

<a href="https://x.com/Kashiko_AIart/status/2096533732547264921"><img src="media/chanbara.webp" width="440" alt="Chanbara sword-fight motion previz"></a>

🎬 **[Ver el vídeo completo →](https://x.com/Kashiko_AIart/status/2096533732547264921)**

---

## Producción de principio a fin

### De la idea → vídeo subible a YouTube

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

> Unos 50 minutos y alrededor de 60 $ de coste de API. La línea que sostiene todo es el rechazo de los borradores.

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

El mismo autor, vídeo resumen a partir de 152 GB de metraje del evento:

```
Create me a sizzle reel recap that's a minute long from this event.
```

> ⚠️ Transcrito de la narración del vídeo —— no existe un bloque de texto oficial para copiar.

**Autor:** Nate Herk | **Fuente:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [vídeo resumen](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Herramientas:** Astra, HeyGen, ElevenLabs, HyperFrames

---

### Explicativo con diagramas, narración primero

![EN](https://img.shields.io/badge/lang-EN-blue) ![spec-only](https://img.shields.io/badge/text-spec--only-lightgrey)

> Sin metraje generado, ninguno. Primero graba y luego construye la imagen ajustándote a las señales medidas de la narración.

Flujo de trabajo:

```
1. write and record the explanation
2. mark the moments where the picture needs to change
3. ask Astra to build those moments with shapes, labels and motion in Remotion
4. add captions timed to the recording
5. render and watch with sound
```

Instrucciones breves publicadas:

```
Use this image for the scene, plan the framing around the measured narration cues,
keep important details visible and stop the movement while the viewer reads the label
```

```
Bring the result on screen when the recording names it,
shorten the entrance animation and preserve the time needed to read the final state
```

> ⚠️ Los 10 Master Prompts del autor vienen en un pack de pago y nunca se publicaron. Aquí solo aparece el esqueleto que sí es público.

**Autor:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Fuente:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) y publicaciones siguientes | **Herramientas:** Astra, Remotion

---

## Meta: prompts que escriben prompts

### Plantilla de director / supervisor de animación

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Genera un prompt listo para producción *además de* un prompt negativo y tres ajustes de reserva: esta última parte es la que falta en casi todas las plantillas.

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

**Autor:** The AI Average | **Fuente:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Herramientas:** GPT-6 Astra

---

## Terrenos adyacentes: Blender y otros

### Turntable de producto de 8 segundos en Blender

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> Fíjate en el paso de renderizar fotogramas fijos antes de la secuencia completa: la forma más barata de detectar una trayectoria de cámara mala.

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

**Autor:** Kingy.ai | **Fuente:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Herramientas:** Blender, Astra

---

### Conocidos pero no publicados

> Confirmado que existen, sin fuente primaria pública. **Se listan, nunca se reconstruyen.**

| Qué | Quién | Estado |
|---|---|---|
| Skill de movimiento físico / soft-body —— dejar atrás las tarjetas con fundido de Remotion/HyperFrames en favor de sensación física y fuerzas de cuerpo blando, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | anunciado, skill sin publicar |
| Pipeline de chanbara con Higgsfield + previs en Blender + Seedance 2.5 | solo prensa de segunda mano | no es fuente primaria |
| Código del skill `motion-flavor` | [@makwanatejas170](https://x.com/makwanatejas170) | no se publicó por separado |
| 10 Master Prompts para explicativos con diagramas | [@foma_on_x](https://x.com/foma_on_x) | pack de pago |
| Nota larga «Remotion 制作 8 本の裏側» | [@chikaidev](https://x.com/chikaidev) | aún sin transcribir |
| 5 prompts de movimiento anunciados en respuestas | [@dawoodkhan254](https://x.com/dawoodkhan254) | anunciados, nunca publicados |

**La demo de movimiento físico / soft-body sí es pública** (el skill no):

<a href="https://x.com/paojiaofty/status/2096830622341976467"><img src="media/physics-motion.webp" width="440" alt="Physics / soft-body motion — 4K60 direct output"></a>

🎬 **[Ver el vídeo completo →](https://x.com/paojiaofty/status/2096830622341976467)**

---

## Skills y herramientas

Aquí todo el mundo le da a Astra la misma capa base. Enlazamos, no redistribuimos.

| Herramienta | Instalación / enlace | Para qué sirve |
|---|---|---|
| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | La capa base bajo casi todos los casos |
| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Se pega en `SKILL.md` / `AGENTS.md` —— no es un prompt de tarea para el usuario |
| **Remotion Studio WebMCP** | 4.0.518+ | El agente lee la selección, la línea de tiempo y la geometría directamente, sin hacer clic en capturas |
| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 tarjetas de recetas de plano + plantillas |
| **Montage** | [github](https://github.com/simplexlabs/montage) | Fork de Remotion nativo para agentes, para películas de lanzamiento |
| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Código reproducible de una película de lanzamiento |
| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Lista comunitaria más amplia |

---

## Lo que ha aprendido la comunidad

Patrones que aparecen en todos los hilos anteriores:

**Instala primero los skills y luego habla.** Sin skills, un vídeo de changelog salió «claramente flojo». Con los skills instalados, hacerlo de una sola pasada pasó a ser lo normal.

**Exige entregables, no sensaciones.** El prompt más potente de todos (el de かし子) termina con: MP4 + código editable + JSON de planos + pasos de re-render + verificación con ffprobe.

**Ajusta la línea de tiempo a la narración, no a «hazlo todo más rápido».** La solución de Foma es nombrar el momento: *la imagen ya tiene que estar ahí cuando la voz dice el resultado.*

**Ejecutarlo dentro de un repositorio de producto supera a una carpeta vacía.** AdCar, Atomik y el CM del juego aprovecharon recursos que ya existían.

**Remotion como previz y el modelo generativo como resultado final** se está convirtiendo en el segundo eslabón estándar en la escena japonesa.

**Astra destaca sobre todo en orquestación y rearquitectura**: [@paojiaofty](https://x.com/paojiaofty) tiró el framework entero antes que aceptar tarjetas con fundido.

**La gente empieza a exigir transparencia en las afirmaciones de «una sola pasada»:** ¿repositorio vacío o proyecto existente? ¿qué nivel de razonamiento? ¿cuántos reintentos? ¿los skills ya estaban instalados? Merece la pena convertirlo en campo obligatorio.

---

## Tabla de completitud

| ID | Tipo | Autor | ¿Texto completo? |
|---|---|---|---|
| AdCar TV | lanzamiento de producto | [@d4m1n](https://x.com/d4m1n) | ✅ |
| Atomik | lanzamiento de producto | [@makwanatejas170](https://x.com/makwanatejas170) | spec sí, prompt de chat no |
| video-shotcraft | skill de promo de producto | Vincentwei1021 | invocaciones sí, skill largo |
| Montage | andamiaje de lanzamiento | simplexlabs | reglas de AGENTS.md |
| FeatureReveal | vídeo de funcionalidad | OpenReplay | ✅ |
| Remotion oficial | invocaciones | Remotion | ✅ (muy corto) |
| Previz de parkour | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| MP4 de control de sprint | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| Persecución lateral | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 30 composiciones de cámara | hoja de referencia | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |
| Cesión a Seedance | cesión | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |
| Linfocitos T | explicativo | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (una línea) |
| YouTube de Nate | vídeo de canal | Nate Herk | transcrito |
| Explicativo de Foma | vídeo con diagramas | [@foma_on_x](https://x.com/foma_on_x) | solo instrucciones breves |
| Vuelo de la bruja | guion de planos generado | [@Mayz1169](https://x.com/Mayz1169) | ✅ |
| Seis partes + JSON | meta | Elser AI | ✅ |
| Plantilla de director | meta | The AI Average | ✅ |
| Turntable de Blender | producto 3D | Kingy.ai | ✅ |
| Skill de movimiento físico | skill | [@paojiaofty](https://x.com/paojiaofty) | sin publicar |

---

## Lista de seguimiento

Una GitHub Action revisa estas cuentas cada 6 horas y abre una incidencia cuando publican algo que parece un prompt de vídeo.

| Cuenta | Por qué |
|---|---|
| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Origen de los prompts de previz de Remotion más largos |
| [@Naonekozamurai](https://x.com/Naonekozamurai) | Previz en Remotion → Seedance, con las manos en la masa |
| [@makwanatejas170](https://x.com/makwanatejas170) | skill motion-flavor / Atomik |
| [@paojiaofty](https://x.com/paojiaofty) | skill de movimiento físico, anunciado |
| [@foma_on_x](https://x.com/foma_on_x) | flujo de explicativos con diagramas |
| [@DeryaTR_](https://x.com/DeryaTR_) | instrucciones de una línea |
| [@d4m1n](https://x.com/d4m1n) | una sola pasada dentro del repositorio |
| [@TROOVY](https://x.com/TROOVY) | perspectiva de un estudio de motion profesional |

[Sugerir una cuenta →](../../issues/new?template=watch-account.yml)

---

## Cómo contribuir

**[→ Enviar un prompt](../../issues/new?template=new-prompt.yml)** —— pégalo y enlaza la fuente. No hace falta git.

Cada entrada necesita tres cosas:

| Campo | Por qué |
|---|---|
| **Autor** | Nombre o usuario, escrito tal como lo escribe esa persona |
| **Fuente** | Enlace directo a la publicación, el hilo, el blog o el vídeo |
| **Publicado** | Fecha, para que el lector juzgue si sigue vigente |

**Reglas:**

- **Cita literalmente.** No lo ordenes, no lo parafrasees, no lo «mejores».
- **Mantén el idioma original.** Añade una traducción en un bloque `<details>`, marcada como no oficial —— nunca sustituyas el original.
- **Nunca inventes lo que falta.** Si una captura corta el prompt por la mitad, márcalo como `partial` y cita solo lo visible.
- **Enlaza la documentación oficial, no la copies.** Sus API cambian; una copia desactualizada aquí solo confundiría.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Licencia y agradecimientos

Estructura del repositorio, notas editoriales y scripts: [CC BY 4.0](LICENSE).

**Los prompts siguen siendo propiedad intelectual de sus autores.** Se citan aquí con atribución y enlace al original, para referencia y estudio.

Gracias a todos los que construyen vídeo con agentes en abierto: [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs y el equipo de Remotion.

**¿Eres uno de ellos?** [Abre una incidencia](../../issues/new?template=correction.yml) para corregir un crédito, añadir tu prompt completo o pedir que se retire tu trabajo. Se atiende sin discusión.

---

<div align="center">

⭐ **Dale una estrella al repositorio** si te resulta útil —— así es como lo encuentra más gente que construye vídeo con agentes.

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="32"></picture></a>

[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)

</div>
