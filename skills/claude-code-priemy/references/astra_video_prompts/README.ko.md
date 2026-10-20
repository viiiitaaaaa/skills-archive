<div align="center">

# Awesome Astra Video Prompts

**GPT-6 Astra와 코딩 에이전트로 영상을 만드는, 실제로 쓰인 프롬프트 모음.**

Astra는 영상을 직접 출력하지 않습니다. 코드를 쓰고 도구를 움직입니다 ——
Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Prompts](https://img.shields.io/badge/prompts-24-blue)
![Full text](https://img.shields.io/badge/full%20text-17-success)
![Previews](https://img.shields.io/badge/previews-18-blueviolet)

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="38"></picture></a>

**LuxReal이 운영·유지보수합니다** —— AI 숏드라마 파이프라인. 대본을 넣으면 장면과 인물의 일관성을 유지한 채 전 과정을 편집할 수 있는 영상이 나옵니다. **[무료로 시작하기 →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**

</div>

<!-- lang-switcher -->
<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · <a href="README.ja.md">日本語</a> · <strong>한국어</strong> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a></p>
<!-- /lang-switcher -->

> 📄 **이 문서는 README.md의 한국어 번역입니다.** 모든 프롬프트는 작성자가 공개한 원문 그대로, 한 글자도 바꾸지 않고 실었으며 번역하지 않았습니다. 번역한 것은 목차·설명·통계·기여 규칙 등 편집 문장뿐입니다. 내용이 다를 경우 [영어 원문](README.md)을 기준으로 합니다.

> ⚠️ **저작권 안내**: 모든 프롬프트는 공개 커뮤니티 게시물에서 수집했으며, 학습 목적으로 사용하고 원작자를 명시했습니다. 권리를 침해한다고 판단되면 [이슈를 열어](../../issues/new) 주세요. 즉시 삭제하겠습니다.

> 🎬 **미리보기 안내**: `media/` 아래의 애니메이션 클립은 각 작성자가 *공개한 데모 영상*에서 잘라낸 짧고 저해상도인 발췌본입니다. 프롬프트 옆에 참고용으로 두었고, 항상 원문 게시물로 연결됩니다. 발췌본이며 원본 영상을 재배포하는 것이 아닙니다. 작성자 본인이 삭제를 원하시면 [이슈를 열어](../../issues/new?template=correction.yml) 주세요. 이견 없이 삭제합니다.

---

## 목차

- [이것은 무엇인가](#이것은-무엇인가)
- [빠른 시작](#빠른-시작)
- [통계](#통계)
- [주목할 프롬프트](#주목할-프롬프트)
- [제품 출시와 마케팅](#제품-출시와-마케팅)
- [모션 프리비즈 → 생성](#모션-프리비즈--생성)
- [엔드투엔드 제작](#엔드투엔드-제작)
- [메타: 프롬프트를 쓰는 프롬프트](#메타-프롬프트를-쓰는-프롬프트)
- [인접 영역: Blender와 기타](#인접-영역-blender와-기타)
- [Skill과 도구](#skill과-도구)
- [커뮤니티가 배운 것](#커뮤니티가-배운-것)
- [완성도 표](#완성도-표)
- [관찰 목록](#관찰-목록)
- [기여 방법](#기여-방법)
- [라이선스와 감사의 말](#라이선스와-감사의-말)

---

## 이것은 무엇인가

Astra는 영상을 네이티브로 렌더링하지 않습니다. **코드를 쓰고, 플러그인을 엮고, 컴퓨터를 조작합니다.** 완성된 영상은 다음에서 나옵니다:

- **Remotion / HyperFrames** —— 프로그램 방식의 모션 그래픽
- **Remotion 모션 프리비즈 → Seedance** 및 기타 생성 모델
- **Blender 프리비즈** → 렌더링 또는 생성
- **HeyGen / ElevenLabs / ffmpeg** —— 내레이션과 합성

그래서 프롬프트를 쓰는 일은 text-to-video 주문을 외는 것과 근본적으로 다릅니다. 여러분이 내리는 것은 그림 설명이 아니라 빌드 명령입니다.

**이 저장소는 그 프롬프트들을 출처와 함께 한 글자도 바꾸지 않고 수록합니다.** 유료 팩과 비공개 skill은 자리표시자만 남깁니다 —— 공개되지 않은 것을 복원하지는 않습니다.

---

## 빠른 시작

```bash
# Official Remotion Agent Skills — the base layer under almost every case here
npx -y skills@latest add remotion-dev/skills -g -y

# Cinematic product video shot library
npx skills add Vincentwei1021/video-shotcraft
```

그런 다음 아래 프롬프트 중 아무거나 Astra, Claude Code, Codex에 붙여 넣으면 됩니다.

**처음이신가요?** [FeatureReveal](#3-featurereveal--프레임-단위로-정확한-합성-계약)부터 보세요 —— 가장 짧으면서, 프레임 번호가 왜 중요한지 보여주는 예시입니다.

---

## 통계

| | |
|---|---|
| **항목 수** | 24 |
| **전문 공개** | 17 |
| **언어** | EN · JA · ZH |
| **미리보기 클립** | 18 (애니메이션 WebP, `media/`) |
| **번역** | 中文 · 日本語 · 한국어 · Español · Français |
| **최종 갱신** | 2026-09-10 |

`full` —— 공개된 그대로 완전 · `partial` —— 일부만 · `spec-only` —— 방식만 설명, 문구는 비공개 · `unpublished` —— 존재는 확인되나 자리표시자만

---

## 주목할 프롬프트

### 1: 고속 파쿠르 모션 프리비즈

![JA](https://img.shields.io/badge/lang-JA-red) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2096096560690209130"><img src="media/parkour-previz.webp" width="440" alt="High-Speed Parkour Motion Previz — Remotion motion previz demo"></a>

🎬 **[전체 영상 보기 →](https://x.com/Kashiko_AIart/status/2096096560690209130)**

#### 📖 설명

지금까지 공개된 것 중 가장 완성도 높은 Astra × Remotion 프롬프트(약 223 좋아요 / 149 북마크). 가치는 소재가 아니라 **산출물 체크리스트, 물리적 접촉 검증, 그리고 '카메라가 캐릭터를 뚫고 지나가서는 안 된다'는 제약**에 있습니다. 이후 [@Naonekozamurai](https://x.com/Naonekozamurai)가 그대로 재사용해 Topview MCP → Seedance 2.5로 넘겼습니다.

#### 📝 프롬프트

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
<summary>핵심 제약 (비공식 요약)</summary>

- 15초 / 가로 / SD / 30fps / 무음 / 외부 소재 없음 —— 단순한 입체 도형만
- TypeScript + Remotion + `useCurrentFrame()` + 공유 3D 좌표계 + WebGL
- 캐릭터: 'i자형' 프록시 1개(구형 머리 + 캡슐형 몸통). 기울기, 도약 전 압축, 착지 시 가라앉음으로 동작을 전달
- **강한 제약**: 카메라는 캐릭터를 직선으로 뚫고 지나갈 수 없음 / 착지점에는 반드시 지지면이 있어야 함 / 같은 프레임은 항상 같은 상태를 반환해야 함
- **산출물**: MP4 + 편집 가능한 소스 + 샷 JSON + 재렌더링 절차 + ffprobe/ffmpeg 검증
</details>

#### 📌 세부 정보

- **작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart))
- **출처:** [x.com/Kashiko_AIart/status/2096096560690209130](https://x.com/Kashiko_AIart/status/2096096560690209130)
- **재사용:** [@Naonekozamurai](https://x.com/Naonekozamurai/status/2096871096759030114)
- **게시일:** 2026-09-05
- **도구:** GPT-6 Astra, Remotion, TypeScript, WebGL

---

### 2: AdCar TV —— 기존 제품 저장소 안에서 원샷 제작

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/d4m1n/status/2096258259459964963"><img src="media/adcar-tv.webp" width="440" alt="AdCar TV — 44s one-shot launch video"></a>

🎬 **[전체 영상 보기 →](https://x.com/d4m1n/status/2096258259459964963)**

#### 📖 설명

**이미 있는 제품 저장소** 안에서 실행 —— Astra는 프로젝트 자체의 3D 뷰어, 음악, 엔진 사운드를 그대로 Remotion으로 가져왔습니다. 소재가 이미 있을 때 베껴야 할 패턴입니다. 빈 폴더에서 시작하지 마세요.

#### 📝 프롬프트

```
can we create an overall video presenting the concept of AdCar TV?

make an intro video of 30-60s showing nice visuals (maybe the 3d of the car)?
and really cool car animations / branded stuff, showing off the site etc.
Use ffmpeg, remotion and qwen 3 tts for voice, and install whatever makes sense,
and come up with a cool artboard first and then make the video.
there is some music and car sounds in the codebase already.
```

> 작성자 메모: ffmpeg는 주로 음성과 음악을 붙이는 데 사용했습니다. Astra는 저장소에 있던 3D를 Remotion으로 직접 끌어왔습니다.

#### 📌 세부 정보

- **작성자:** Dan ⚡️ ([@d4m1n](https://x.com/d4m1n))
- **출처:** [x.com/d4m1n/status/2096258259459964963](https://x.com/d4m1n/status/2096258259459964963)
- **게시일:** 2026-09-05
- **도구:** GPT-6 Astra, Remotion, ffmpeg, local Qwen 3 TTS

---

### 3: FeatureReveal —— 프레임 단위로 정확한 합성 계약

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 설명

여기서 가장 짧은 프롬프트이자, SaaS 체인지로그 영상을 만들 때 가장 좋은 출발 골격입니다. 모든 애니메이션이 **프레임 범위**로 지정되어 있고 모호한 설명이 없습니다 —— 그래서 추측이 아니라 구현이 가능합니다.

#### 📝 프롬프트

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

#### 📌 세부 정보

- **작성자:** OpenReplay Team
- **출처:** [blog.openreplay.com/making-videos-claude-code-remotion](https://blog.openreplay.com/making-videos-claude-code-remotion/)
- **게시일:** 2026-06-04
- **호환:** Claude Code, Codex, Astra
- **도구:** Remotion

---

### 4: 마녀의 첫 비행 —— 15초 생성용 샷 스크립트

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Mayz1169/status/2095873015007592679"><img src="media/witch-first-flight.webp" width="440" alt="Witch's First Flight — 15s generated shot"></a>

🎬 **[전체 영상 보기 →](https://x.com/Mayz1169/status/2095873015007592679)**

#### 📖 설명

**이것은 입력이 아니라 출력입니다** —— Astra가 영상 모델을 위해 *써낸* 샷 스크립트입니다. 작성자는 분명히 밝혔습니다: *"이 애니메이션의 프롬프트를 만들기 위해 사용했습니다."* 좋은 생성용 샷 스크립트가 어떤 모습인지 참고하세요: 초 단위 비트, 캐릭터 일관성 고정, 그리고 긴 네거티브 목록.

#### 📝 프롬프트

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

#### 📌 세부 정보

- **작성자:** Kiki / Mayz ([@Mayz1169](https://x.com/Mayz1169))
- **출처:** [x.com/Mayz1169/status/2095873015007592679](https://x.com/Mayz1169/status/2095873015007592679) · [전체 답글](https://x.com/Mayz1169/status/2095873204351070296)
- **게시일:** 2026-09
- **도구:** GPT-6 Astra (as prompt writer) → video model

---

### 5: T 세포 —— 한 문장, 5분

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/DeryaTR_/status/2095659170661904804"><img src="media/t-cells.webp" width="440" alt="T Cells — 5-minute explainer, one-line brief"></a>

🎬 **[전체 영상 보기 →](https://x.com/DeryaTR_/status/2095659170661904804)**

#### 📖 설명

가장 많이 공유된 사례입니다. 사용자 프롬프트는 문자 그대로 한 줄입니다. **아주 짧은 요청 + 이미 설치된 skill이 긴 프롬프트를 이긴다는 것을 증명합니다** —— 툴체인 전체를 Astra가 스스로 골랐습니다.

#### 📝 프롬프트

```
Create a 5 minute educational video about T cells.
```

Astra가 선택한 오케스트레이션 (작성자가 나중에 설명한 것으로, 원래 프롬프트는 아니지만 skill 흐름으로 쓸 수 있습니다):

```
Use the Remotion plugin for video generation.
Use Imagegen for visuals.
You may use HeyGen for narration.
Assemble the entire educational video one-shot,
including what to say and how to explain it.
```

#### 📌 세부 정보

- **작성자:** Derya Unutmaz, MD ([@DeryaTR_](https://x.com/DeryaTR_))
- **출처:** [x.com/DeryaTR_/status/2095659170661904804](https://x.com/DeryaTR_/status/2095659170661904804)
- **중국어 재게시:** [@LinearUncle](https://x.com/LinearUncle/status/2095719251277701516)
- **게시일:** 2026-09-03
- **도구:** GPT-6 Astra, Remotion plugin, Imagegen, HeyGen

---

### 6: 6단계 제어 템플릿 + 샷 JSON 계약

![EN](https://img.shields.io/badge/lang-EN-blue) ![featured](https://img.shields.io/badge/⭐-featured-gold) ![full](https://img.shields.io/badge/text-full-success)

#### 📖 설명

어떤 Astra 작업에도 쓸 수 있는 재사용 가능한 6단계 구조와, 생성기에 넘길 수 있는 JSON 샷 계약입니다. **Authority**와 **Verification** 블록은 대부분의 사람이 빼먹는 부분인데, 바로 이것이 에이전트가 과하게 캐묻거나 망가진 결과물을 내놓는 것을 막아줍니다.

#### 📝 프롬프트

6단계 제어 템플릿:

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

샷 JSON 계약:

```
Return valid JSON with project_summary and shots. Each shot must contain id,
story_purpose, framing, subject_action, camera, duration_seconds,
continuity_constraints and audio_cue. Total duration must equal 45 seconds.
```

60초 단편:

```
Turn the premise below into a 60-second anime short. Preserve the theme and
character rules. Use 8–10 shots, one primary location and no crowd. Each shot
must change story information. Return logline, beat sheet, dialogue, shot table
and continuity checklist. Remove any beat that cannot be shown or heard.
```

#### 📌 세부 정보

- **작성자:** Elser AI
- **출처:** [elser.ai/blog/gpt-6-astra-prompt-guide](https://www.elser.ai/blog/gpt-6-astra-prompt-guide)
- **게시일:** 2026-09
- **도구:** GPT-6 Astra

---

## 제품 출시와 마케팅

### Atomik —— 33초 런치 필름

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/makwanatejas170/status/2096555742597988400"><img src="media/atomik-launch.webp" width="440" alt="Atomik — 33s launch film"></a>

🎬 **[전체 영상 보기 →](https://x.com/makwanatejas170/status/2096555742597988400)**

> 직접 만든 `motion-flavor` skill로 원샷에 만든 런치 영상입니다. 이 skill은 HyperFrames와 Remotion 양쪽에서 동작합니다. 채팅 프롬프트는 공개되지 않았고, 재현 가능한 구현이 공개되었습니다.

X 게시물 원문:

```
GPT-6 Astra one-shot this launch video for @atomikgrowth
with New motion-flavor skill that i made
works on both @HyperFrames_ & @Remotion
```

저장소의 사양 —— 에이전트용 인수 계약으로 쓸 수 있습니다:

```
Build a 33-second launch film in Remotion + React + TypeScript + CSS/SVG.
1920×1080, 60 fps, 1980 frames, H.264/AAC.
Rocket, layouts, cursor, typography and transitions must be rendered from code.
Portfolio imagery and soundtrack are bundled local media.
Do not hide a finished-video layer inside the composition.
No AI API call is required to render.
Output: out/final-render.mp4
```

**작성자:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **출처:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [소스 저장소](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **게시일:** 2026-09 | **도구:** Astra, Remotion, HyperFrames

---

### video-shotcraft —— 시네마틱 제품 영상 skill

![ZH](https://img.shields.io/badge/lang-ZH-yellow) ![full](https://img.shields.io/badge/invocations-full-success)

<a href="https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd"><img src="media/shotcraft-gallery-intro.webp" width="440" alt="video-shotcraft — 38s gallery intro, produced with the skill"></a>

🎬 **[전체 영상 보기 →](https://github.com/user-attachments/assets/cba2df8a-4b2e-4247-bace-d0b1dea9c2bd)**

<a href="https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d"><img src="media/shotcraft-ink-press.webp" width="440" alt="Ink Press — the 36s promo template shipped with the skill"></a>

🎬 **[전체 영상 보기 →](https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d)**

> 157장의 샷 레시피 카드 + Remotion 구현 + 완성 영상 템플릿. skill 본체는 긴 문서이고, 여기 실린 것은 사용자 쪽 호출 방식입니다.

설치:

```
帮我安装这个 skill：https://github.com/Vincentwei1021/video-shotcraft
```
```bash
npx skills add Vincentwei1021/video-shotcraft
```

호출 예시 (공식 README에서):

```
用 video-shotcraft 给我的桌面产品做一支宣传片。
用 deck-deal-flyin 和 row-embed 两张镜头卡展示这个功能。
参考 spotlight-hero-card，为这个页面设计一个产品特写镜头。
```
```
用 video-shotcraft 的 Ink Press 模板给我的产品做一支宣传片。
```

<details>
<summary>Skill frontmatter (에이전트가 언제 활성화하는지 결정)</summary>

```yaml
name: video-shotcraft
description: Create cinematic product videos from shot recipe cards, a validated
template, and code/audio assets (Remotion + real page screenshots + 2.5D camera
moves + beat-synced cuts + sound design). Use when the user asks to turn a
frontend project or webpage into a product video, says "use video-shotcraft to
make a video/promo", names the Ink Press template or asks to reproduce its
effect, or wants a single shot card's motion.
```

상호 배타적인 세 가지 모드: Ink Press 템플릿 바로 적용 · 자율 제작(`references/pipeline.md`를 따라 묻지 않고 완성 컷까지) · 협업(브리프 / 비주얼 방향 / 샷 리스트를 단계별로 확인).

강한 제약: 실제 페이지는 반드시 스크린샷을 써야 하고 손으로 그린 가짜 UI는 금지. 서체와 색상은 제품의 디자인 토큰에서 매핑해야 하며, 범용 '프로모 스킨'을 덮어쓰면 안 됩니다.
</details>

**작성자:** Vincentwei1021 | **출처:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **도구:** Remotion, Astra, Claude Code, Codex

---

### Montage —— 에이전트 네이티브 런치 영상 스캐폴드

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 에이전트를 위해 만든 Remotion 포크. 겨냥한 것은 제품 런치 영상.

README가 에이전트에게 이렇게 말하라고 안내합니다:

```
Create a master sequence in a new folder and start creating.
Copy any of the examples to get started.
Reference AGENTS.md and leverage all animations possible.
Replace background primitives and the logo with our branding.
```

AGENTS.md에서 훔칠 만한 규칙:

```
Do NOT one-shot all sections at once without viewing them.
Build one section → register it → render key frames → verify → next section.
Every frame should have something animating.
Never use flat backgroundColor — always layer vignette + grain + corner glow.
Do NOT default to useLetterPopIn for every text entrance.
Use SF Pro Display. Never use Geist or Inter.
After every change: render stills at entrance / mid / settled, inspect, then MP4.
```

**작성자:** simplexlabs | **출처:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **도구:** Remotion

<a href="https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f"><img src="media/montage-launch-film.webp" width="440" alt="Montage — launch film rendered by the agent"></a>

🎬 **[전체 영상 보기 →](https://github.com/user-attachments/assets/e7257684-72e1-47a3-a9e6-0c94b801dc8f)**

---

### Remotion 공식 skill 호출

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 공식 슬래시 커맨드. 커뮤니티 프롬프트 대부분이 이것들이 설치되어 있다고 전제합니다.

새 프로젝트에서 코딩 에이전트를 부트스트랩하는 방법:

```
Ensure Node.js is installed.
Install Remotion Skills:
npx -y skills@latest add remotion-dev/skills -g -y
Then use them to create a video.
```

호출:

```
/remotion-create Make a promo video for a record store
/remotion-markup Create an animated title card using Inter
/remotion-maps Animate a route from Los Angeles to New York and make the camera follow it
/remotion-render
/remotion-studio
```

사용 가능한 skill: `remotion-best-practices`(라우터), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.

**작성자:** Remotion | **출처:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **도구:** Remotion

---

### 그래도 통한 극단적으로 짧은 요청

![Mixed](https://img.shields.io/badge/lang-mixed-lightgrey) ![partial](https://img.shields.io/badge/text-partial-orange)

> 최소한의 요청. 얼마나 적게 써도 되는지 기준으로는 유용하지만, 계약서는 아닙니다.

```
游戏做好了，用 remotion 做个好看的 CM
```
**작성자:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **출처:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)

<a href="https://x.com/guuchacha149182/status/2096813471463882947"><img src="media/game-cm.webp" width="440" alt="Game CM — one-prompt Remotion promo"></a>

🎬 **[전체 영상 보기 →](https://x.com/guuchacha149182/status/2096813471463882947)**

```
根据最近的 changelog 比较亮眼的功能做个视频。
```
**작성자:** [@leon7hao](https://x.com/leon7hao) | **출처:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **비고:** GPT-6-Astra medium, skill 미설치 —— 작성자는 결과가 눈에 띄게 약했다고 밝혔습니다

<a href="https://x.com/leon7hao/status/2096844989900914865"><img src="media/changelog-video.webp" width="440" alt="Changelog video — no skill installed, weaker result"></a>

🎬 **[전체 영상 보기 →](https://x.com/leon7hao/status/2096844989900914865)**

프롬프트 없이 결과만 올린 사례: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521)(BrandNewStudy 마케팅 영상, 원샷) · [@stoufax](https://x.com/stoufax/status/2096311328600113222)(iOS 앱 출시, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)(`/goal` + fal 음성 + Remotion 플러그인, 90초 워크스루)

**@NickYang130 —— BrandNewStudy 마케팅 영상, 원샷**

<a href="https://x.com/NickYang130/status/2096835902047932521"><img src="media/brandnewstudy-promo.webp" width="440" alt="BrandNewStudy marketing video, one-shot"></a>

🎬 **[전체 영상 보기 →](https://x.com/NickYang130/status/2096835902047932521)**

**@stoufax —— iOS 앱 출시, Remotion + ElevenLabs**

<a href="https://x.com/stoufax/status/2096311328600113222"><img src="media/ios-app-launch.webp" width="440" alt="iOS app launch — Remotion + ElevenLabs"></a>

🎬 **[전체 영상 보기 →](https://x.com/stoufax/status/2096311328600113222)**

---

## 모션 프리비즈 → 생성

> 이 계열은 영상 모델에게 그림을 설명하지 않습니다. 먼저 Astra가 Remotion으로 **control MP4**를 렌더링하게 하고, 그것을 Seedance 같은 모델에 모션 참조로 넘깁니다. 일본 씬에서는 점점 주류가 되어 가는 두 번째 연결 고리입니다.

### Seedance 전달 지시

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Naonekozamurai/status/2096871096759030114"><img src="media/seedance-handoff.webp" width="440" alt="Remotion previz control MP4 handed to Seedance 2.5"></a>

🎬 **[전체 영상 보기 →](https://x.com/Naonekozamurai/status/2096871096759030114)**

> Remotion 렌더 결과를 생성 모델에 넘길 때 뭐라고 말할지. 수정 허가를 명시하지 않으면 모델은 플레이스홀더의 결함을 충실히 재현합니다.

```
Remotionで作成した動画はあくまで動きを参照するだけの動画。
参照動画で不自然な挙動や不自然な女の子の体勢は、動画化の際にどんどん修正して良い。
動画では、前後のつながり、動画としてのかっこよさを重視してほしい。
```

<details>
<summary>영어 (비공식)</summary>

```
The video made with Remotion is purely a reference for movement.
Any unnatural behavior or unnatural poses of the girl in the reference video
may be freely corrected during video generation.
In the video, prioritize continuity between shots and how good it looks as a video.
```
</details>

**작성자:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **출처:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **게시일:** 2026-09 | **도구:** Remotion → Seedance 2.5 (Topview MCP 경유)

---

### 초고속 질주 control MP4

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2094182215894831283"><img src="media/sprint-control.webp" width="440" alt="Ultra-high-speed sprint control MP4"></a>

🎬 **[전체 영상 보기 →](https://x.com/Kashiko_AIart/status/2094182215894831283)**

> 반칙 방지 조항에 주목하세요: 배경을 루프시키는 대신, 충분히 긴 실제 길을 만들고 실제로 앞으로 나아가야 합니다. 그리고 **인물과 그리드는 반드시 같은 3D 좌표계와 카메라 투영을 써야 합니다** —— 2D 소재를 확대·축소하는 가짜 카메라는 안 됩니다.

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

**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **출처:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **도구:** Astra, Remotion

---

### 횡스크롤 추격, 프레임 표 포함

![JA](https://img.shields.io/badge/lang-JA-red) ![full](https://img.shields.io/badge/text-full-success)

<a href="https://x.com/Kashiko_AIart/status/2093692302745383041"><img src="media/side-scroll-chase.webp" width="440" alt="Side-scrolling chase with a frame table"></a>

🎬 **[전체 영상 보기 →](https://x.com/Kashiko_AIart/status/2093692302745383041)**

> 수록된 것 중 프레임 정밀도가 가장 높은 프롬프트. 모든 파쿠르 동작에 명시적인 프레임 범위가 배정되어 있고, 반개구간(half-open) 의미까지 적혀 있습니다.

```
Remotionで1920×1080の、横スクロール追従式モーションコンテを作ってください。

夏の光が差す、来園者でにぎわう現代的な遊園地を舞台に、短パン姿のかし子が先頭を逃げ、成人のママが後方から追います。二人を色分けしたシンプルな全身2.5Dプロキシで表現し、入場ゲート、待機列の柵、壁、高低差のある足場、ベンチ、低い柵、回転木馬の支柱、水路、コースター軌道を、左から右へ続く一つのコースとして配置してください。

動作順は、P パームスピン → Q クイックステップ → V 垂直ウォールクライム → W ウォールラン → AB コークスクリュー → AD ドロップロール → A 加速スプリント → O ワンハンドヴォルト → B バックフリップ → S スピードヴォルト → R リバースヴォルト → AD ドロップロール → AC ラシェ → AB コークスクリュー → A 加速スプリントです。

時間境界は、P 0–20f、Q 20–72f、V 72–116f、W 116–132f、AB 132–156f、AD 156–168f、A 168–176f、O 176–188f、B 188–224f、S 224–236f、R 236–252f、AD 252–260f、AC 260–286f、AB 286–316f、A 316–361fとします。開始frameを含み、終了frameを含まない区間として扱ってください。

カメラは最後まで真横から少しだけ立体感のある横追走を維持し、約4300pxのコースをスクロールさせながら、かし子を画面左から約720pxの位置へ保ちます。上下補正は±18px以内とし、予備動作、踏切、手足の接触、重心移動、着地、回復が常に読める大きさにしてください。

Qは横方向の移動だけを52fへ延ばし、腕脚と上下の踏み替えは元の16f周期を等倍で反復します。Vも登る位置は44fで進めながら、腕脚は元の26f周期で等倍動作させます。全身をスロー再生にせず、左右の関節を正しく接続し、通常時の脚は腰から下へ伸ばし、足先は自然な外向きのハの字にしてください。

画面上へタイトル、コード、字幕、矢印、一覧、制作メモなどのUIを表示しないclean-control映像とします。音声なしのH.264 MP4を `motion-conte-control.mp4` としてレンダーし、各動作のコード、名称、開始・終了frameを `motion-conte-manifest.json` に保存してください。
```

**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **출처:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **도구:** Astra, Remotion

---

### 카메라 구도 30종 —— 레퍼런스 시트 생성기

![JA](https://img.shields.io/badge/lang-JA-red) ![partial](https://img.shields.io/badge/text-partial-orange)

<a href="https://x.com/Kashiko_AIart/status/2093575541916061984"><img src="media/camera-comps-30.webp" width="440" alt="30 camera compositions reference sheet"></a>

🎬 **[전체 영상 보기 →](https://x.com/Kashiko_AIart/status/2093575541916061984)**

> 훑어볼 수 있는 카메라 구도 카탈로그를 만듭니다. 이후 영상 모델과 대화할 때 ID로 바로 참조할 수 있습니다.

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

> ⚠️ 게시물은 출력 요구사항 이후로도 이어지지만, 보이는 부분만 인용했습니다.

**작성자:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **출처:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **도구:** Astra, Remotion, HTML/CSS/SVG

> 같은 작성자가 *참바라*(검극) 워크플로도 공개했습니다 —— [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— 다만 방법만 있고 프롬프트는 없습니다: 1) 카메라와 캐릭터 위치만 표시한 최소 샷 리스트, 2) 이펙트 샘플 시트, 3) 프롬프트로 제어하는 세밀한 동작.

<a href="https://x.com/Kashiko_AIart/status/2096533732547264921"><img src="media/chanbara.webp" width="440" alt="Chanbara sword-fight motion previz"></a>

🎬 **[전체 영상 보기 →](https://x.com/Kashiko_AIart/status/2096533732547264921)**

---

## 엔드투엔드 제작

### 아이디어 → 바로 업로드 가능한 YouTube 영상

![EN](https://img.shields.io/badge/lang-EN-blue) ![partial](https://img.shields.io/badge/text-partial-orange)

> 약 50분, API 비용은 대략 60달러. 핵심은 '초안은 받지 않는다'는 그 한 줄입니다.

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

같은 작성자가 152GB 행사 영상으로 만든 하이라이트:

```
Create me a sizzle reel recap that's a minute long from this event.
```

> ⚠️ 영상 내레이션을 받아쓴 것입니다 —— 공식 붙여넣기 텍스트는 없습니다.

**작성자:** Nate Herk | **출처:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [하이라이트 영상](https://www.youtube.com/watch?v=QhmhUgccaS0) | **도구:** Astra, HeyGen, ElevenLabs, HyperFrames

---

### 내레이션 우선 도해 영상

![EN](https://img.shields.io/badge/lang-EN-blue) ![spec-only](https://img.shields.io/badge/text-spec--only-lightgrey)

> 생성 영상은 전혀 쓰지 않습니다. 먼저 녹음하고, 계측한 내레이션 큐에 맞춰 그림을 만듭니다.

워크플로:

```
1. write and record the explanation
2. mark the moments where the picture needs to change
3. ask Astra to build those moments with shapes, labels and motion in Remotion
4. add captions timed to the recording
5. render and watch with sound
```

공개된 짧은 지시:

```
Use this image for the scene, plan the framing around the measured narration cues,
keep important details visible and stop the movement while the viewer reads the label
```

```
Bring the result on screen when the recording names it,
shorten the entrance animation and preserve the time needed to read the final state
```

> ⚠️ 작성자의 10가지 Master Prompts는 유료 번들에 포함되어 공개된 적이 없습니다. 여기에는 공개된 뼈대만 실었습니다.

**작성자:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **출처:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) 및 이후 게시물 | **도구:** Astra, Remotion

---

## 메타: 프롬프트를 쓰는 프롬프트

### 감독 / 애니메이션 슈퍼바이저 템플릿

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 바로 쓸 수 있는 프롬프트에*더해* 네거티브 프롬프트와 세 가지 대안 조정안을 내놓습니다 —— 마지막 항목이 대부분의 템플릿에 빠져 있습니다.

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

**작성자:** The AI Average | **출처:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **도구:** GPT-6 Astra

---

## 인접 영역: Blender와 기타

### Blender 8초 제품 턴테이블

![EN](https://img.shields.io/badge/lang-EN-blue) ![full](https://img.shields.io/badge/text-full-success)

> 전체 시퀀스 전에 스틸을 렌더링하는 단계에 주목하세요 —— 카메라 경로가 잘못됐는지 가장 싸게 잡아내는 방법입니다.

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

**작성자:** Kingy.ai | **출처:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **도구:** Blender, Astra

---

### 존재하지만 미공개

> 존재는 확인되었으나 공개된 1차 출처가 없습니다. **등재만 하고, 복원하지 않습니다.**

| 무엇 | 누가 | 상태 |
|---|---|---|
| 물리 / 소프트바디 모션 skill —— Remotion/HyperFrames의 페이드인 카드를 버리고 물리적 질감과 소프트바디 힘으로, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | 예고됨, skill 미공개 |
| Higgsfield + Blender 프리비즈 + Seedance 2.5 검극 파이프라인 | 2차 보도만 존재 | 1차 출처 아님 |
| `motion-flavor` skill 소스 | [@makwanatejas170](https://x.com/makwanatejas170) | 별도 공개 안 됨 |
| 도해 영상용 10가지 Master Prompts | [@foma_on_x](https://x.com/foma_on_x) | 유료 번들 |
| 「Remotion 制作 8本の裏側」장문 노트 | [@chikaidev](https://x.com/chikaidev) | 아직 받아쓰지 않음 |
| 답글에서 주장한 5가지 모션 프롬프트 | [@dawoodkhan254](https://x.com/dawoodkhan254) | 주장만, 게시 없음 |

**물리 / 소프트바디 모션 데모 자체는 공개되어 있습니다** (skill은 비공개):

<a href="https://x.com/paojiaofty/status/2096830622341976467"><img src="media/physics-motion.webp" width="440" alt="Physics / soft-body motion — 4K60 direct output"></a>

🎬 **[전체 영상 보기 →](https://x.com/paojiaofty/status/2096830622341976467)**

---

## Skill과 도구

여기 있는 모두가 Astra에 같은 토대를 넣고 있습니다. 링크만 걸고, 직접 배포하지는 않습니다.

| 도구 | 설치 / 링크 | 용도 |
|---|---|---|
| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | 거의 모든 사례 밑에 깔린 토대 |
| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | `SKILL.md` / `AGENTS.md`에 붙여넣는 것 —— 사용자 작업 프롬프트가 아님 |
| **Remotion Studio WebMCP** | 4.0.518+ | 스크린샷을 클릭하는 대신 선택 영역·타임라인·지오메트리를 직접 읽음 |
| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 샷 레시피 카드 157장 + 템플릿 |
| **Montage** | [github](https://github.com/simplexlabs/montage) | 런치 영상용 에이전트 네이티브 Remotion 포크 |
| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | 재현 가능한 런치 영상 소스 |
| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | 더 넓은 커뮤니티 목록 |

---

## 커뮤니티가 배운 것

위의 모든 스레드에서 반복해서 나타나는 패턴:

**먼저 skill을 설치하고, 그다음 말하세요.** skill 없이 만든 체인지로그 영상은 '눈에 띄게 아쉬운' 결과였습니다. 설치한 뒤에는 원샷이 흔해졌습니다.

**분위기가 아니라 산출물을 요구하세요.** 여기서 가장 강력한 프롬프트(かし子의 것)는 MP4 + 편집 가능한 소스 + 샷 JSON + 재렌더링 절차 + ffprobe 검증으로 끝납니다.

**'전체적으로 더 빠르게'가 아니라 타임라인을 내레이션에 맞추세요.** Foma의 해법은 그 순간을 지목하는 것입니다: *내레이션이 결과를 말할 때 그림은 이미 거기 있어야 한다.*

**빈 폴더보다 제품 저장소 안에서 돌리는 편이 낫습니다.** AdCar, Atomik, 그리고 게임 CM 모두 이미 있는 소재를 끌어왔습니다.

**Remotion은 프리비즈로, 생성 모델은 최종 결과물로** —— 일본 씬에서 표준적인 두 번째 연결 고리가 되어 가고 있습니다.

**Astra가 가장 강한 지점은 오케스트레이션과 재설계** —— [@paojiaofty](https://x.com/paojiaofty)는 페이드인 카드를 받아들이느니 프레임워크를 통째로 버렸습니다.

**'원샷'이라는 주장에 정보 공개를 요구하는 움직임이 시작됐습니다:** 빈 저장소인가 기존 프로젝트인가? 추론 등급은? 몇 번 재시도했나? skill은 미리 설치했나? 필수 항목으로 만들 만합니다.

---

## 완성도 표

| ID | 유형 | 작성자 | 전문 있음? |
|---|---|---|---|
| AdCar TV | 제품 출시 | [@d4m1n](https://x.com/d4m1n) | ✅ |
| Atomik | 제품 출시 | [@makwanatejas170](https://x.com/makwanatejas170) | 사양은 있음, 채팅 프롬프트는 없음 |
| video-shotcraft | 제품 프로모 skill | Vincentwei1021 | 호출은 있음, skill 본체는 김 |
| Montage | 런치 스캐폴드 | simplexlabs | AGENTS.md 규칙 |
| FeatureReveal | 기능 영상 | OpenReplay | ✅ |
| Remotion 공식 | 호출 | Remotion | ✅ (아주 짧음) |
| 파쿠르 프리비즈 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 질주 control MP4 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 횡스크롤 추격 | 모션 프리비즈 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |
| 카메라 구도 30종 | 레퍼런스 시트 | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |
| Seedance 전달 | 전달 지시 | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |
| T 세포 | 해설 영상 | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (한 줄) |
| Nate의 YouTube | 채널 영상 | Nate Herk | 받아쓰기 |
| Foma 도해 | 도해 영상 | [@foma_on_x](https://x.com/foma_on_x) | 짧은 지시만 |
| 마녀의 첫 비행 | 생성용 샷 스크립트 | [@Mayz1169](https://x.com/Mayz1169) | ✅ |
| 6단계 + JSON | 메타 | Elser AI | ✅ |
| 감독 템플릿 | 메타 | The AI Average | ✅ |
| Blender 턴테이블 | 3D 제품 | Kingy.ai | ✅ |
| 물리 모션 skill | skill | [@paojiaofty](https://x.com/paojiaofty) | 미공개 |

---

## 관찰 목록

GitHub Action이 6시간마다 이 계정들을 확인하고, 영상 프롬프트로 보이는 글을 올리면 이슈를 생성합니다.

| 계정 | 이유 |
|---|---|
| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | 가장 긴 Remotion 모션 프리비즈 프롬프트의 출처 |
| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion 프리비즈 → Seedance, 실전파 |
| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |
| [@paojiaofty](https://x.com/paojiaofty) | 예고된 물리 모션 skill |
| [@foma_on_x](https://x.com/foma_on_x) | 도해 영상 워크플로 |
| [@DeryaTR_](https://x.com/DeryaTR_) | 한 줄 요청 |
| [@d4m1n](https://x.com/d4m1n) | 저장소 안에서 원샷 |
| [@TROOVY](https://x.com/TROOVY) | 프로 모션 스튜디오의 시선 |

[계정 추천하기 →](../../issues/new?template=watch-account.yml)

---

## 기여 방법

**[→ 프롬프트 제출하기](../../issues/new?template=new-prompt.yml)** —— 붙여 넣고 출처를 링크하면 됩니다. git은 필요 없습니다.

모든 항목에는 세 가지가 필요합니다:

| 항목 | 필요한 이유 |
|---|---|
| **작성자** | 이름 또는 핸들. 본인이 쓰는 표기 그대로 |
| **출처** | 게시물·스레드·블로그·영상으로 가는 직접 링크 |
| **게시일** | 얼마나 최신인지 독자가 판단할 수 있도록 |

**규칙:**

- **한 글자도 바꾸지 말고 인용하세요.** 정리하지 말고, 바꿔 쓰지 말고, '개선'하지 마세요.
- **원문 언어를 유지하세요.** 번역은 `<details>` 블록에 비공식이라고 표시해 넣고, 원문을 대체해서는 안 됩니다.
- **빠진 부분을 지어내지 마세요.** 스크린샷이 프롬프트의 절반만 담았다면 `partial`로 표시하고 보이는 부분만 인용하세요.
- **공식 문서는 링크만 하고 복사하지 마세요.** API는 바뀌므로 오래된 사본은 오해를 낳습니다.

자세한 내용은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

---

## 라이선스와 감사의 말

저장소 구조, 편집 노트, 스크립트: [CC BY 4.0](LICENSE).

**프롬프트의 저작권은 각 작성자에게 있습니다.** 출처와 원문 링크를 함께 밝혀 참고와 연구 목적으로 인용했습니다.

에이전트 기반 영상 제작을 공개적으로 만들어 가는 모든 분께 감사합니다 —— [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, 그리고 Remotion 팀.

**여러분도 그중 한 명인가요?** [이슈를 열면](../../issues/new?template=correction.yml) 크레딧을 고치고, 프롬프트 전문을 추가하고, 작업물 삭제를 요청할 수 있습니다. 이견 없이 처리합니다.

---

<div align="center">

유용하다면 ⭐ **이 저장소에 Star를** —— 다른 사람들이 그것으로 찾습니다.

<a href="https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo-dark.png"><img src="https://raw.githubusercontent.com/LuxRealGrowth/awesome-astra-video-prompts/main/media/luxreal-logo.png" alt="LuxReal" height="32"></picture></a>

[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)

</div>
