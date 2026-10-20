# -*- coding: utf-8 -*-
"""Spanish translation table for README.md."""

TOC_TITLE = "Índice"

SWITCHER = (
    '<p><a href="README.md">English</a> · <a href="README.zh-CN.md">中文</a> · '
    '<a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · '
    '<strong>Español</strong> · <a href="README.fr.md">Français</a></p>'
)

NOTICE = (
    "> 📄 **Esta es la traducción al español de README.md.** Todos los prompts se reproducen "
    "literalmente en el idioma en que su autor los publicó; no se traducen. Solo se traduce el "
    "texto editorial: índice, descripciones, estadísticas y normas de contribución. Si hay "
    "discrepancias, prevalece la [versión en inglés](README.md)."
)

REPLACE = [
    ("**Author:**", "**Autor:**"),
    ("**Source:**", "**Fuente:**"),
    ("**Published:**", "**Publicado:**"),
    ("**Tools:**", "**Herramientas:**"),
    ("**Reused by:**", "**Reutilizado por:**"),
    ("**Works with:**", "**Compatible con:**"),
    ("**Chinese relay:**", "**Reenvío en chino:**"),
    ("**Note:**", "**Nota:**"),
    ("**Rules:**", "**Reglas:**"),
    ("**Are you one of them?**", "**¿Eres uno de ellos?**"),
    ("🎬 **[Watch the full video →](", "🎬 **[Ver el vídeo completo →]("),
    ("[source repo](", "[repositorio fuente]("),
    ("[sizzle reel](", "[vídeo resumen]("),
    ("[full reply](", "[respuesta completa]("),
    (" and following posts", " y publicaciones siguientes"),
]

SKIP = {
    "# Awesome Astra Video Prompts",
    "[Discord](https://discord.gg/EUgCVYQFJJ) · [LuxReal](https://www.luxreal.com/?utm_source=GitHub&utm_medium=website&utm_campaign=shortdrama_skills)",
}

BLOCKS = {
    # ── LuxReal house CTA (rendered at the top of README.md) ─────────────
    "**Maintained by LuxReal** — the AI short-drama pipeline: script in, a consistent and fully editable cut out. **[Try it free →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**":
        "**Mantenido por LuxReal** — el pipeline de IA para short dramas: entra un guion y sale un montaje coherente y totalmente editable. **[Pruébalo gratis →](https://www.luxreal.com/?utm_source=GitHub&utm_medium=readme&utm_campaign=astra_prompts)**",
    "**Real prompts for making video with GPT-6 Astra and coding agents.**":
        "**Prompts reales para hacer vídeo con GPT-6 Astra y agentes de programación.**",

    "Astra doesn't output video. It writes code and drives tools —\n"
    "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg":
        "Astra no genera el vídeo. Escribe código y maneja herramientas —\n"
        "Remotion · HyperFrames · Blender · Seedance · HeyGen · ElevenLabs · ffmpeg",

    "> ⚠️ **Copyright Notice**: All prompts are collected from public community posts for educational purposes, with attribution to their original authors. If you believe any content infringes on your rights, please [open an issue](../../issues/new) and we will remove it promptly.":
        "> ⚠️ **Aviso de copyright**: todos los prompts se recopilan de publicaciones públicas de "
        "la comunidad con fines educativos y con atribución a sus autores originales. Si crees que "
        "algún contenido infringe tus derechos, [abre una incidencia](../../issues/new) y lo "
        "retiraremos de inmediato.",

    "> 🎬 **About the previews**: the animated clips under `media/` are short, low-resolution excerpts of each author's *published demo*, included only as a reference next to the prompt and always linked back to the original post. They are excerpts — not redistributions of the full videos. If you are the author and want yours gone, [open an issue](../../issues/new?template=correction.yml); it is removed without argument.":
        "> 🎬 **Sobre las previsualizaciones**: los clips animados de `media/` son extractos cortos y "
        "de baja resolución de la *demo publicada* de cada autor. Se incluyen solo como referencia "
        "junto al prompt y siempre enlazan a la publicación original. Son extractos, no "
        "redistribuciones del vídeo completo. Si eres el autor y quieres que se retire el tuyo, "
        "[abre una incidencia](../../issues/new?template=correction.yml); se elimina sin discusión.",

    "## Table of Contents": "## Índice",
    "- [What is this?](#what-is-this)\n- [Quick Start](#quick-start)\n- [Statistics](#statistics)\n- [Featured Prompts](#featured-prompts)\n- [Product Launch & Marketing](#product-launch--marketing)\n- [Motion Previz → Generative](#motion-previz--generative)\n- [End-to-End Production](#end-to-end-production)\n- [Meta: Prompts That Write Prompts](#meta-prompts-that-write-prompts)\n- [Adjacent: Blender & Others](#adjacent-blender--others)\n- [Skills & Tooling](#skills--tooling)\n- [What the Community Learned](#what-the-community-learned)\n- [Completeness Table](#completeness-table)\n- [Watch List](#watch-list)\n- [How to Contribute](#how-to-contribute)\n- [License & Acknowledgements](#license--acknowledgements)":
        "@@TOC@@",

    "## What is this?": "## ¿Qué es esto?",

    "Astra doesn't render video natively. **It writes code, orchestrates plugins, and operates the computer.** Finished video comes from:":
        "Astra no renderiza vídeo de forma nativa. **Escribe código, orquesta plugins y maneja el "
        "ordenador.** El vídeo terminado sale de:",

    "- **Remotion / HyperFrames** — programmatic motion graphics\n"
    "- **Remotion motion previz → Seedance** and other generative models\n"
    "- **Blender previs** → render or generate\n"
    "- **HeyGen / ElevenLabs / ffmpeg** — narration and assembly":
        "- **Remotion / HyperFrames** —— gráficos en movimiento programáticos\n"
        "- **Previz de movimiento en Remotion → Seedance** y otros modelos generativos\n"
        "- **Previs en Blender** → renderizar o generar\n"
        "- **HeyGen / ElevenLabs / ffmpeg** —— narración y montaje",

    "That makes prompting it fundamentally different from writing a text-to-video spell. You're issuing a build order, not describing a picture.":
        "Por eso, escribirle un prompt es radicalmente distinto a recitar un conjuro de texto a "
        "vídeo. Lo que emites es una orden de compilación, no la descripción de una imagen.",

    "**This repo collects those prompts verbatim, with credit.** Paid packs and private skills get a placeholder — we never reconstruct what wasn't published.":
        "**Este repositorio recopila esos prompts literalmente y con crédito.** Los packs de pago y "
        "los skills privados solo dejan un marcador de posición: nunca reconstruimos lo que no se "
        "publicó.",

    "## Quick Start": "## Inicio rápido",

    "Then paste any prompt below into Astra, Claude Code, or Codex.":
        "Después, pega cualquiera de los prompts de abajo en Astra, Claude Code o Codex.",

    "**New here?** Start with [FeatureReveal](#3-featurereveal--frame-exact-composition-contract) — the shortest prompt that shows why frame numbers matter.":
        "**¿Es tu primera vez?** Empieza por [FeatureReveal](#@@A3@@) — el prompt más corto y el que "
        "mejor explica por qué importan los números de fotograma.",

    "## Statistics": "## Estadísticas",

    "| | |\n|---|---|\n| **Entries** | 24 |\n| **Full text available** | 17 |\n| **Languages** | EN · JA · ZH |\n| **Preview clips** | 18 (animated WebP, `media/`) |\n| **Translations** | 中文 · 日本語 · 한국어 · Español · Français |\n| **Last updated** | 2026-09-10 |":
        "| | |\n|---|---|\n| **Entradas** | 24 |\n| **Texto completo** | 17 |\n"
        "| **Idiomas** | EN · JA · ZH |\n| **Clips de previsualización** | 18 (WebP animado, `media/`) |\n"
        "| **Traducciones** | 中文 · 日本語 · 한국어 · Español · Français |\n"
        "| **Última actualización** | 2026-09-10 |",

    "`full` — complete as published · `partial` — some of it · `spec-only` — approach described, wording never released · `unpublished` — known to exist, placeholder only":
        "`full` —— completo tal como se publicó · `partial` —— solo una parte · "
        "`spec-only` —— se describe el enfoque, el texto nunca se publicó · "
        "`unpublished` —— se sabe que existe, solo un marcador de posición",

    "## Featured Prompts": "## Prompts destacados",
    "#### 📖 Description": "#### 📖 Descripción",
    "#### 📝 Prompt": "#### 📝 Prompt",
    "#### 📌 Details": "#### 📌 Detalles",

    "### 1: High-Speed Parkour Motion Previz":
        "### 1: Previz de parkour a alta velocidad",

    "The most complete Astra × Remotion prompt published so far (~223 likes / 149 bookmarks). Its value isn't the subject matter — it's the **deliverables checklist, the physical-contact validation, and the \"camera must not pass through the character\" constraint**. Later reused verbatim by [@Naonekozamurai](https://x.com/Naonekozamurai) and pushed through Topview MCP → Seedance 2.5.":
        "El prompt de Astra × Remotion más completo publicado hasta ahora (~223 me gusta / "
        "149 guardados). Su valor no está en el tema, sino en la **lista de entregables, la "
        "validación del contacto físico y la restricción de que «la cámara no debe atravesar al "
        "personaje»**. Después lo reutilizó literalmente "
        "[@Naonekozamurai](https://x.com/Naonekozamurai) y lo pasó por Topview MCP → Seedance 2.5.",

    "<details>\n<summary>Key constraints, summarized (unofficial)</summary>":
        "<details>\n<summary>Restricciones clave, resumidas (no oficial)</summary>",

    "- 15s / landscape / SD / 30fps / silent / no external assets — simple solid shapes only\n"
    "- TypeScript + Remotion + `useCurrentFrame()` + shared 3D coordinate system + WebGL\n"
    "- Character: one \"i-shaped\" proxy (sphere head + capsule torso); motion conveyed by lean, compression before takeoff, sink on landing\n"
    "- **Hard constraints**: camera must never pass straight through the character; every landing point needs a support surface; same frame must always yield the same state\n"
    "- **Deliverables**: MP4 + editable source + shot JSON + re-render steps + ffprobe/ffmpeg verification\n"
    "</details>":
        "- 15 s / horizontal / SD / 30 fps / sin sonido / sin recursos externos —— solo formas "
        "sólidas simples\n"
        "- TypeScript + Remotion + `useCurrentFrame()` + sistema de coordenadas 3D compartido + WebGL\n"
        "- Personaje: un único proxy «en forma de i» (cabeza esférica + torso de cápsula); el "
        "movimiento se transmite con inclinación, compresión antes del salto y hundimiento al aterrizar\n"
        "- **Restricciones duras**: la cámara nunca debe atravesar al personaje en línea recta; cada "
        "punto de aterrizaje necesita una superficie de apoyo; un mismo fotograma debe dar siempre "
        "el mismo estado\n"
        "- **Entregables**: MP4 + código editable + JSON de planos + pasos de re-render + "
        "verificación con ffprobe/ffmpeg\n"
        "</details>",

    "### 2: AdCar TV — In-Repo One-Shot Launch Video":
        "### 2: AdCar TV —— vídeo de lanzamiento en una sola pasada dentro del repositorio",

    "Run inside an **existing product repo** — Astra imported the project's own 3D viewer, music, and engine sounds straight into Remotion. This is the pattern to copy when you already have assets: don't start from an empty folder.":
        "Se ejecuta dentro de un **repositorio de producto ya existente**: Astra importó el visor 3D, "
        "la música y los sonidos de motor del propio proyecto directamente en Remotion. Este es el "
        "patrón que hay que copiar cuando ya tienes recursos: no empieces desde una carpeta vacía.",

    "> Author's note: ffmpeg was mainly used to attach voice and music; Astra pulled the repo's existing 3D directly into Remotion.":
        "> Nota del autor: ffmpeg se usó sobre todo para acoplar la voz y la música; Astra llevó el 3D "
        "que ya existía en el repositorio directamente a Remotion.",

    "### 3: FeatureReveal — Frame-Exact Composition Contract":
        "### 3: FeatureReveal —— contrato de composición exacto al fotograma",

    "The shortest prompt here, and the best starting skeleton for a SaaS changelog video. Every animation is a **frame range**, not a vague description — that's what makes it buildable instead of guessable.":
        "El prompt más corto de todos y el mejor esqueleto de partida para un vídeo de changelog de "
        "SaaS. Cada animación es un **rango de fotogramas**, no una descripción vaga: eso es lo que "
        "lo hace construible en lugar de adivinable.",

    "### 4: Witch's First Flight — 15s Generated Shot Script":
        "### 4: El primer vuelo de la bruja —— guion de planos generado de 15 s",

    "**This is output, not input** — a shot script Astra *wrote* for a video model. The author was explicit: *\"I used it to create the prompt for this animation.\"* Study it as a reference for what a good generated shot script looks like: second-by-second beats, character consistency locks, and a long negative list.":
        "**Esto es salida, no entrada**: un guion de planos que Astra *escribió* para un modelo de "
        "vídeo. El autor fue explícito: *«Lo usé para crear el prompt de esta animación.»* "
        "Estúdialo como referencia de cómo se ve un buen guion de planos generado: tiempos segundo a "
        "segundo, bloqueos de consistencia del personaje y una larga lista de negativos.",

    "### 5: T Cells — One Sentence, Five Minutes":
        "### 5: Linfocitos T —— una frase, cinco minutos",

    "The most re-shared example. The user prompt is literally one line. **This proves that a very short brief + skills already installed beats a long prompt** — Astra chose the whole toolchain itself.":
        "El ejemplo más compartido. El prompt del usuario es literalmente una línea. "
        "**Esto demuestra que una instrucción muy breve + skills ya instalados supera a un prompt "
        "largo**: Astra eligió toda la cadena de herramientas por su cuenta.",

    "The orchestration Astra chose (described by the author afterwards — not the original prompt, but usable as a skill flow):":
        "La orquestación que eligió Astra (descrita después por el autor: no es el prompt original, "
        "pero sirve como flujo de skill):",

    "### 6: Six-Part Control Template + Shot JSON Contract":
        "### 6: Plantilla de control en seis partes + contrato JSON de planos",

    "A reusable six-part structure for any Astra task, plus a JSON shot contract you can hand to a generator. The **Authority** and **Verification** blocks are the parts most people leave out — and they're what stop the agent from either asking too much or shipping something broken.":
        "Una estructura reutilizable en seis partes para cualquier tarea de Astra, más un contrato "
        "JSON de planos que puedes entregar a un generador. Los bloques **Authority** y "
        "**Verification** son los que casi todo el mundo omite, y son justo los que impiden que el "
        "agente pregunte de más o entregue algo roto.",

    "Six-part control template:": "Plantilla de control en seis partes:",
    "Shot JSON contract:": "Contrato JSON de planos:",
    "60-second short:": "Corto de 60 segundos:",

    "## Product Launch & Marketing": "## Lanzamiento de producto y marketing",

    "### Atomik — 33-Second Launch Film": "### Atomik —— película de lanzamiento de 33 segundos",

    "> One-shot launch film using a self-made `motion-flavor` skill that works on both HyperFrames and Remotion. The chat prompt was never published; the reproducible engineering was.":
        "> Película de lanzamiento hecha de una sola pasada con un skill `motion-flavor` propio que "
        "funciona tanto en HyperFrames como en Remotion. El prompt del chat nunca se publicó; la "
        "ingeniería reproducible, sí.",

    "X post, verbatim:": "Publicación en X, literal:",

    "Spec from the repo — useful as an acceptance contract for an agent:":
        "Especificación del repositorio —— útil como contrato de aceptación para un agente:",

    "**Author:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | **Source:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · [source repo](https://github.com/Tejashmakwana/astra-atomik-launch-video) | **Published:** 2026-09 | **Tools:** Astra, Remotion, HyperFrames":
        "**Autor:** Tejas ([@makwanatejas170](https://x.com/makwanatejas170)) | "
        "**Fuente:** [x.com](https://x.com/makwanatejas170/status/2096555742597988400) · "
        "[repositorio fuente](https://github.com/Tejashmakwana/astra-atomik-launch-video) | "
        "**Publicado:** 2026-09 | **Herramientas:** Astra, Remotion, HyperFrames",

    "### video-shotcraft — Cinematic Product Video Skill":
        "### video-shotcraft —— skill de vídeo de producto cinematográfico",

    "> 157 shot-recipe cards + Remotion implementation + finished-video templates. The skill body is a long document; these are the user-side invocations.":
        "> 157 tarjetas de recetas de plano + implementación en Remotion + plantillas de vídeo "
        "terminado. El cuerpo del skill es un documento largo; lo que aparece aquí son las "
        "invocaciones del lado del usuario.",

    "Install:": "Instalación:",
    "Invocations (from the official README):": "Invocaciones (del README oficial):",

    "<details>\n<summary>Skill frontmatter (determines when the agent activates it)</summary>":
        "<details>\n<summary>Frontmatter del skill (determina cuándo lo activa el agente)</summary>",

    "Three mutually exclusive modes: apply the Ink Press template directly · autonomous creation (follow `references/pipeline.md` to a finished cut without asking) · collaborative (confirm brief / visual direction / shot list step by step).":
        "Tres modos mutuamente excluyentes: aplicar la plantilla Ink Press directamente · creación "
        "autónoma (seguir `references/pipeline.md` hasta un montaje final sin preguntar) · "
        "colaborativo (confirmar brief / dirección visual / lista de planos paso a paso).",

    "Hard constraints: real pages must use screenshots, never hand-drawn fake UI; type and color must map from the product's design tokens, not a generic \"promo skin\".\n</details>":
        "Restricciones duras: las páginas reales deben usar capturas de pantalla, nunca una interfaz "
        "falsa dibujada a mano; la tipografía y el color deben salir de los tokens de diseño del "
        "producto, no de una «piel promocional» genérica.\n</details>",

    "**Author:** Vincentwei1021 | **Source:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | **Tools:** Remotion, Astra, Claude Code, Codex":
        "**Autor:** Vincentwei1021 | "
        "**Fuente:** [github.com/Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | "
        "**Herramientas:** Remotion, Astra, Claude Code, Codex",

    "### Montage — Agent-Native Launch Video Scaffold":
        "### Montage —— andamiaje de vídeo de lanzamiento nativo para agentes",

    "> A Remotion fork built for agents, aimed at product launch films.":
        "> Un fork de Remotion hecho para agentes, orientado a películas de lanzamiento de producto.",

    "What the README tells you to say to the agent:":
        "Lo que el README te dice que le digas al agente:",

    "The AGENTS.md rules worth stealing:": "Reglas de AGENTS.md que vale la pena copiar:",

    "**Author:** simplexlabs | **Source:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | **Tools:** Remotion":
        "**Autor:** simplexlabs | **Fuente:** [github.com/simplexlabs/montage](https://github.com/simplexlabs/montage) | "
        "**Herramientas:** Remotion",

    "### Remotion Official Skill Invocations": "### Invocaciones de los skills oficiales de Remotion",

    "> The official slash commands. Most community prompts assume these are installed.":
        "> Los comandos de barra oficiales. La mayoría de los prompts de la comunidad dan por hecho "
        "que están instalados.",

    "Bootstrap for a coding agent on a fresh project:":
        "Arranque para un agente de programación en un proyecto nuevo:",

    "Invocations:": "Invocaciones:",

    "Available skills: `remotion-best-practices` (router), `remotion-create`, `remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, `remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, `remotion-upgrade`, `remotion-multimedia`.":
        "Skills disponibles: `remotion-best-practices` (enrutador), `remotion-create`, "
        "`remotion-markup`, `remotion-studio`, `remotion-render`, `remotion-maps`, "
        "`remotion-captions`, `remotion-saas`, `remotion-interactivity`, `remotion-docs`, "
        "`remotion-upgrade`, `remotion-multimedia`.",

    "**Author:** Remotion | **Source:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | **Tools:** Remotion":
        "**Autor:** Remotion | **Fuente:** [remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills) | "
        "**Herramientas:** Remotion",

    "### Short Briefs That Still Worked": "### Instrucciones mínimas que aun así funcionaron",

    "> Minimal briefs. Useful as a baseline for how little you can get away with — not as contracts.":
        "> Instrucciones mínimas. Útiles como referencia de lo poco que basta para salir del paso, "
        "pero no como contratos.",

    "**Author:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | **Source:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)":
        "**Autor:** かな ([@guuchacha149182](https://x.com/guuchacha149182)) | "
        "**Fuente:** [x.com](https://x.com/guuchacha149182/status/2096813471463882947)",

    "**Author:** [@leon7hao](https://x.com/leon7hao) | **Source:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | **Note:** GPT-6-Astra medium, no skill installed — author reported the result was noticeably weaker":
        "**Autor:** [@leon7hao](https://x.com/leon7hao) | "
        "**Fuente:** [x.com](https://x.com/leon7hao/status/2096844989900914865) | "
        "**Nota:** GPT-6-Astra medium, sin skill instalado —— el autor señaló que el resultado fue "
        "claramente más flojo",

    "Results posted without the prompt: [@NickYang130](https://x.com/NickYang130/status/2096835902047932521) (BrandNewStudy marketing video, one-shot) · [@stoufax](https://x.com/stoufax/status/2096311328600113222) (iOS app launch, Remotion + ElevenLabs) · [@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510) (`/goal` + fal voice + Remotion plugin, 90s walkthrough)":
        "Resultados publicados sin el prompt: "
        "[@NickYang130](https://x.com/NickYang130/status/2096835902047932521)"
        " (vídeo de marketing de BrandNewStudy, una sola pasada) · "
        "[@stoufax](https://x.com/stoufax/status/2096311328600113222)"
        " (lanzamiento de app iOS, Remotion + ElevenLabs) · "
        "[@nosimaJcrypto](https://x.com/nosimaJcrypto/status/2096834488185528510)"
        " (`/goal` + voz de fal + plugin de Remotion, recorrido de 90 s)",

    "**@NickYang130 — BrandNewStudy marketing video, one-shot**":
        "**@NickYang130 —— vídeo de marketing de BrandNewStudy, una sola pasada**",

    "**@stoufax — iOS app launch, Remotion + ElevenLabs**":
        "**@stoufax —— lanzamiento de app iOS, Remotion + ElevenLabs**",

    "## Motion Previz → Generative": "## Previz de movimiento → generativo",

    "> This family doesn't describe pictures for a video model. It has Astra render a **control MP4** in Remotion first, then hands that to Seedance or similar as motion reference. Increasingly the mainstream second link in the JP scene.":
        "> Esta familia no describe imágenes para un modelo de vídeo. Hace que Astra renderice "
        "primero un **MP4 de control** en Remotion y luego lo entrega a Seedance o similar como "
        "referencia de movimiento. Cada vez es más el segundo eslabón habitual en la escena "
        "japonesa.",

    "### Seedance Handoff Instruction": "### Instrucción de cesión a Seedance",

    "> What to say when you feed a Remotion render to a generative model. Without the explicit permission to correct, the model faithfully reproduces your placeholder's flaws.":
        "> Qué decir cuando le das un render de Remotion a un modelo generativo. Sin el permiso "
        "explícito para corregir, el modelo reproduce fielmente los defectos de tu marcador de "
        "posición.",

    "<details>\n<summary>English (unofficial)</summary>":
        "<details>\n<summary>Inglés (no oficial)</summary>",

    "**Author:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | **Source:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | **Published:** 2026-09 | **Tools:** Remotion → Seedance 2.5 (via Topview MCP)":
        "**Autor:** なお ([@Naonekozamurai](https://x.com/Naonekozamurai)) | "
        "**Fuente:** [x.com](https://x.com/Naonekozamurai/status/2096871096759030114) | "
        "**Publicado:** 2026-09 | **Herramientas:** Remotion → Seedance 2.5 (vía Topview MCP)",

    "### Ultra-High-Speed Sprint Control MP4": "### MP4 de control de sprint a altísima velocidad",

    "> Note the anti-cheat clause: build one real long road and actually move forward through it, rather than looping a background. And **person and grid must share the same 3D coordinate system and camera projection** — no fake camera that just scales 2D assets.":
        "> Fíjate en la cláusula antitrampas: construye un camino largo de verdad y avanza por él, en "
        "lugar de poner un fondo en bucle. Y **la persona y la rejilla deben compartir el mismo "
        "sistema de coordenadas 3D y la misma proyección de cámara**: nada de una cámara falsa que "
        "solo escala recursos 2D.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | **Tools:** Astra, Remotion":
        "**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2094182215894831283) | "
        "**Herramientas:** Astra, Remotion",

    "### Side-Scrolling Chase, with a Frame Table":
        "### Persecución de desplazamiento lateral, con tabla de fotogramas",

    "> The most frame-precise prompt in the collection: every parkour move is assigned an explicit frame range, half-open interval semantics spelled out.":
        "> El prompt más preciso en cuanto a fotogramas de toda la colección: cada movimiento de "
        "parkour tiene asignado un rango de fotogramas explícito, con la semántica de intervalo "
        "semiabierto escrita sin ambigüedad.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | **Tools:** Astra, Remotion":
        "**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2093692302745383041) | "
        "**Herramientas:** Astra, Remotion",

    "### 30 Camera Compositions — Reference Sheet Generator":
        "### 30 composiciones de cámara —— generador de hoja de referencia",

    "> Builds a browsable camera-composition catalogue you can then reference by ID when talking to a video model.":
        "> Construye un catálogo navegable de composiciones de cámara que luego puedes citar por "
        "ID cuando hables con un modelo de vídeo.",

    "> ⚠️ The post continues past the output requirements; only what's visible is quoted.":
        "> ⚠️ La publicación continúa más allá de los requisitos de salida; aquí solo se cita lo "
        "visible.",

    "**Author:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | **Source:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | **Tools:** Astra, Remotion, HTML/CSS/SVG":
        "**Autor:** かし子🍩 ([@Kashiko_AIart](https://x.com/Kashiko_AIart)) | "
        "**Fuente:** [x.com](https://x.com/Kashiko_AIart/status/2093575541916061984) | "
        "**Herramientas:** Astra, Remotion, HTML/CSS/SVG",

    "> Same author also published a *chanbara* (sword-fight) workflow — [x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) — but only the method, not the prompt: 1) a minimal shot list with camera and character positions only, 2) an effects sample sheet, 3) fine motion controlled by prompt.":
        "> El mismo autor publicó también un flujo de *chanbara* (combate con espada) —— "
        "[x.com](https://x.com/Kashiko_AIart/status/2096533732547264921) —— pero solo el método, no "
        "el prompt: 1) una lista mínima de planos con la posición de cámara y personajes, "
        "2) una hoja de muestras de efectos, 3) movimiento fino controlado por prompt.",

    "## End-to-End Production": "## Producción de principio a fin",

    "### Idea → Uploadable YouTube Video": "### De la idea → vídeo subible a YouTube",

    "> ~50 minutes, roughly $60 in API cost. The load-bearing line is the refusal of drafts.":
        "> Unos 50 minutos y alrededor de 60 $ de coste de API. La línea que sostiene todo es el "
        "rechazo de los borradores.",

    "Same author, sizzle reel from 152GB of event footage:":
        "El mismo autor, vídeo resumen a partir de 152 GB de metraje del evento:",

    "> ⚠️ Transcribed from the video's narration — no official paste block exists.":
        "> ⚠️ Transcrito de la narración del vídeo —— no existe un bloque de texto oficial para "
        "copiar.",

    "**Author:** Nate Herk | **Source:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · [sizzle reel](https://www.youtube.com/watch?v=QhmhUgccaS0) | **Tools:** Astra, HeyGen, ElevenLabs, HyperFrames":
        "**Autor:** Nate Herk | "
        "**Fuente:** [youtube.com/watch?v=dT5-x3u5nCg](https://www.youtube.com/watch?v=dT5-x3u5nCg) · "
        "[vídeo resumen](https://www.youtube.com/watch?v=QhmhUgccaS0) | "
        "**Herramientas:** Astra, HeyGen, ElevenLabs, HyperFrames",

    "### Narration-First Diagram Explainer": "### Explicativo con diagramas, narración primero",

    "> No generated footage at all. Record first, then build the picture to measured narration cues.":
        "> Sin metraje generado, ninguno. Primero graba y luego construye la imagen ajustándote a las "
        "señales medidas de la narración.",

    "Workflow:": "Flujo de trabajo:",
    "Published short instructions:": "Instrucciones breves publicadas:",

    "> ⚠️ The author's 10 Master Prompts ship in a paid bundle and were never posted publicly. Only the publicly published skeleton appears here.":
        "> ⚠️ Los 10 Master Prompts del autor vienen en un pack de pago y nunca se publicaron. Aquí "
        "solo aparece el esqueleto que sí es público.",

    "**Author:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | **Source:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) and following posts | **Tools:** Astra, Remotion":
        "**Autor:** Foma ([@foma_on_x](https://x.com/foma_on_x)) | "
        "**Fuente:** [x.com](https://x.com/foma_on_x/status/2096845194788217049) y publicaciones siguientes | "
        "**Herramientas:** Astra, Remotion",

    "## Meta: Prompts That Write Prompts": "## Meta: prompts que escriben prompts",

    "### Director / Animation Supervisor Template":
        "### Plantilla de director / supervisor de animación",

    "> Produces a production-ready prompt *plus* a negative prompt and three fallback adjustments — the last part is what most templates miss.":
        "> Genera un prompt listo para producción *además de* un prompt negativo y tres ajustes de "
        "reserva: esta última parte es la que falta en casi todas las plantillas.",

    "**Author:** The AI Average | **Source:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | **Tools:** GPT-6 Astra":
        "**Autor:** The AI Average | "
        "**Fuente:** [theaileverage.beehiiv.com](https://theaileverage.beehiiv.com/p/the-gpt-6-astra-build-guide) | "
        "**Herramientas:** GPT-6 Astra",

    "## Adjacent: Blender & Others": "## Terrenos adyacentes: Blender y otros",

    "### Blender 8-Second Product Turntable":
        "### Turntable de producto de 8 segundos en Blender",

    "> Note the render-stills-before-full-sequence step — the cheapest way to catch a bad camera path.":
        "> Fíjate en el paso de renderizar fotogramas fijos antes de la secuencia completa: la forma "
        "más barata de detectar una trayectoria de cámara mala.",

    "**Author:** Kingy.ai | **Source:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | **Tools:** Blender, Astra":
        "**Autor:** Kingy.ai | "
        "**Fuente:** [kingy.ai/blog/blender-openai-astra-complete-guide](https://kingy.ai/blog/blender-openai-astra-complete-guide/) | "
        "**Herramientas:** Blender, Astra",

    "### Known but Unpublished": "### Conocidos pero no publicados",

    "> Confirmed to exist, no public primary source. **Listed, never reconstructed.**":
        "> Confirmado que existen, sin fuente primaria pública. **Se listan, nunca se reconstruyen.**",

    "| What | Who | Status |\n|---|---|---|\n"
    "| Physics / soft-body motion skill — dropping Remotion/HyperFrames fade-in cards for physical feel and soft-body forces, 4K60 | [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | announced, skill unreleased |\n"
    "| Higgsfield + Blender previs + Seedance 2.5 sword-fight pipeline | secondhand press reporting only | not a primary source |\n"
    "| `motion-flavor` skill source | [@makwanatejas170](https://x.com/makwanatejas170) | not separately released |\n"
    "| 10 Master Prompts for diagram explainers | [@foma_on_x](https://x.com/foma_on_x) | paid bundle |\n"
    "| \"Remotion 制作 8 本の裏側\" long-form note | [@chikaidev](https://x.com/chikaidev) | not yet transcribed |\n"
    "| 5 motion prompts claimed in replies | [@dawoodkhan254](https://x.com/dawoodkhan254) | claimed, never posted |":
        "| Qué | Quién | Estado |\n|---|---|---|\n"
        "| Skill de movimiento físico / soft-body —— dejar atrás las tarjetas con fundido de "
        "Remotion/HyperFrames en favor de sensación física y fuerzas de cuerpo blando, 4K60 "
        "| [@paojiaofty](https://x.com/paojiaofty/status/2096830622341976467) | anunciado, skill sin publicar |\n"
        "| Pipeline de chanbara con Higgsfield + previs en Blender + Seedance 2.5 | solo prensa de segunda mano | no es fuente primaria |\n"
        "| Código del skill `motion-flavor` | [@makwanatejas170](https://x.com/makwanatejas170) | no se publicó por separado |\n"
        "| 10 Master Prompts para explicativos con diagramas | [@foma_on_x](https://x.com/foma_on_x) | pack de pago |\n"
        "| Nota larga «Remotion 制作 8 本の裏側» | [@chikaidev](https://x.com/chikaidev) | aún sin transcribir |\n"
        "| 5 prompts de movimiento anunciados en respuestas | [@dawoodkhan254](https://x.com/dawoodkhan254) | anunciados, nunca publicados |",

    "**The physics / soft-body motion demo itself is public** (the skill is not):":
        "**La demo de movimiento físico / soft-body sí es pública** (el skill no):",

    "## Skills & Tooling": "## Skills y herramientas",

    "Everyone here is feeding Astra the same base layer. We link, we don't vendor.":
        "Aquí todo el mundo le da a Astra la misma capa base. Enlazamos, no redistribuimos.",

    "| Tool | Install / Link | What it's for |\n|---|---|---|\n"
    "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | The base layer under almost every case |\n"
    "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) | Paste into `SKILL.md` / `AGENTS.md` — not a user task prompt |\n"
    "| **Remotion Studio WebMCP** | 4.0.518+ | Agent reads selection/timeline/geometry directly instead of clicking screenshots |\n"
    "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 shot recipe cards + templates |\n"
    "| **Montage** | [github](https://github.com/simplexlabs/montage) | Agent-native Remotion fork for launch films |\n"
    "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) | Reproducible launch-film source |\n"
    "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Broader community list |":
        "| Herramienta | Instalación / enlace | Para qué sirve |\n|---|---|---|\n"
        "| **Remotion Agent Skills** | `npx skills add remotion-dev/skills` | La capa base bajo casi todos los casos |\n"
        "| **Remotion system prompt** | [remotion.dev/docs/ai/system-prompt](https://www.remotion.dev/docs/ai/system-prompt) "
        "| Se pega en `SKILL.md` / `AGENTS.md` —— no es un prompt de tarea para el usuario |\n"
        "| **Remotion Studio WebMCP** | 4.0.518+ | El agente lee la selección, la línea de tiempo y la "
        "geometría directamente, sin hacer clic en capturas |\n"
        "| **video-shotcraft** | [github](https://github.com/Vincentwei1021/video-shotcraft) | 157 tarjetas de recetas de plano + plantillas |\n"
        "| **Montage** | [github](https://github.com/simplexlabs/montage) | Fork de Remotion nativo para agentes, para películas de lanzamiento |\n"
        "| **astra-atomik-launch-video** | [github](https://github.com/Tejashmakwana/astra-atomik-launch-video) "
        "| Código reproducible de una película de lanzamiento |\n"
        "| **awesome-gpt-6-astra** | [github](https://github.com/xianyu110/awesome-gpt-6-astra) | Lista comunitaria más amplia |",

    "## What the Community Learned": "## Lo que ha aprendido la comunidad",

    "Patterns that show up across every thread above:":
        "Patrones que aparecen en todos los hilos anteriores:",

    "**Install the skills first, then talk.** Without skills, a changelog video came out \"noticeably short of it\". With skills installed, one-shots became common.":
        "**Instala primero los skills y luego habla.** Sin skills, un vídeo de changelog salió "
        "«claramente flojo». Con los skills instalados, hacerlo de una sola pasada pasó a ser lo "
        "normal.",

    "**Demand deliverables, not vibes.** The strongest prompt here (かし子's) ends with: MP4 + editable source + shot JSON + re-render steps + ffprobe verification.":
        "**Exige entregables, no sensaciones.** El prompt más potente de todos (el de かし子) termina "
        "con: MP4 + código editable + JSON de planos + pasos de re-render + verificación con ffprobe.",

    "**Align the timeline to narration, not \"make it faster overall.\"** Foma's fix is naming the moment: *the picture must already be there when the voiceover says the result.*":
        "**Ajusta la línea de tiempo a la narración, no a «hazlo todo más rápido».** La solución de "
        "Foma es nombrar el momento: *la imagen ya tiene que estar ahí cuando la voz dice el "
        "resultado.*",

    "**Running inside a product repo beats an empty folder.** AdCar, Atomik, and the game CM all pulled existing assets in.":
        "**Ejecutarlo dentro de un repositorio de producto supera a una carpeta vacía.** AdCar, "
        "Atomik y el CM del juego aprovecharon recursos que ya existían.",

    "**Remotion as previz, generative model as final** is becoming the standard second link in the JP scene.":
        "**Remotion como previz y el modelo generativo como resultado final** se está convirtiendo en "
        "el segundo eslabón estándar en la escena japonesa.",

    "**Astra is strongest at orchestration and rearchitecting** — [@paojiaofty](https://x.com/paojiaofty) threw out the framework entirely rather than accept fade-in cards.":
        "**Astra destaca sobre todo en orquestación y rearquitectura**: "
        "[@paojiaofty](https://x.com/paojiaofty) tiró el framework entero antes que aceptar tarjetas "
        "con fundido.",

    "**People are starting to demand disclosure on \"one-shot\" claims:** empty repo or existing project? reasoning tier? how many retries? were skills already installed? Worth making a required field.":
        "**La gente empieza a exigir transparencia en las afirmaciones de «una sola pasada»:** "
        "¿repositorio vacío o proyecto existente? ¿qué nivel de razonamiento? ¿cuántos reintentos? "
        "¿los skills ya estaban instalados? Merece la pena convertirlo en campo obligatorio.",

    "## Completeness Table": "## Tabla de completitud",

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
        "| ID | Tipo | Autor | ¿Texto completo? |\n|---|---|---|---|\n"
        "| AdCar TV | lanzamiento de producto | [@d4m1n](https://x.com/d4m1n) | ✅ |\n"
        "| Atomik | lanzamiento de producto | [@makwanatejas170](https://x.com/makwanatejas170) | spec sí, prompt de chat no |\n"
        "| video-shotcraft | skill de promo de producto | Vincentwei1021 | invocaciones sí, skill largo |\n"
        "| Montage | andamiaje de lanzamiento | simplexlabs | reglas de AGENTS.md |\n"
        "| FeatureReveal | vídeo de funcionalidad | OpenReplay | ✅ |\n"
        "| Remotion oficial | invocaciones | Remotion | ✅ (muy corto) |\n"
        "| Previz de parkour | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| MP4 de control de sprint | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| Persecución lateral | previz de movimiento | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | ✅ |\n"
        "| 30 composiciones de cámara | hoja de referencia | [@Kashiko_AIart](https://x.com/Kashiko_AIart) | partial |\n"
        "| Cesión a Seedance | cesión | [@Naonekozamurai](https://x.com/Naonekozamurai) | ✅ |\n"
        "| Linfocitos T | explicativo | [@DeryaTR_](https://x.com/DeryaTR_) | ✅ (una línea) |\n"
        "| YouTube de Nate | vídeo de canal | Nate Herk | transcrito |\n"
        "| Explicativo de Foma | vídeo con diagramas | [@foma_on_x](https://x.com/foma_on_x) | solo instrucciones breves |\n"
        "| Vuelo de la bruja | guion de planos generado | [@Mayz1169](https://x.com/Mayz1169) | ✅ |\n"
        "| Seis partes + JSON | meta | Elser AI | ✅ |\n"
        "| Plantilla de director | meta | The AI Average | ✅ |\n"
        "| Turntable de Blender | producto 3D | Kingy.ai | ✅ |\n"
        "| Skill de movimiento físico | skill | [@paojiaofty](https://x.com/paojiaofty) | sin publicar |",

    "## Watch List": "## Lista de seguimiento",

    "A GitHub Action checks these accounts every 6 hours and opens an Issue when they post something that looks like a video prompt.":
        "Una GitHub Action revisa estas cuentas cada 6 horas y abre una incidencia cuando publican "
        "algo que parece un prompt de vídeo.",

    "| Account | Why |\n|---|---|\n"
    "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Source of the longest Remotion motion previz prompts |\n"
    "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Remotion previz → Seedance, hands-on |\n"
    "| [@makwanatejas170](https://x.com/makwanatejas170) | motion-flavor skill / Atomik |\n"
    "| [@paojiaofty](https://x.com/paojiaofty) | physics motion skill, announced |\n"
    "| [@foma_on_x](https://x.com/foma_on_x) | diagram explainer workflow |\n"
    "| [@DeryaTR_](https://x.com/DeryaTR_) | one-line briefs |\n"
    "| [@d4m1n](https://x.com/d4m1n) | in-repo one-shots |\n"
    "| [@TROOVY](https://x.com/TROOVY) | professional motion studio perspective |":
        "| Cuenta | Por qué |\n|---|---|\n"
        "| [@Kashiko_AIart](https://x.com/Kashiko_AIart) | Origen de los prompts de previz de Remotion más largos |\n"
        "| [@Naonekozamurai](https://x.com/Naonekozamurai) | Previz en Remotion → Seedance, con las manos en la masa |\n"
        "| [@makwanatejas170](https://x.com/makwanatejas170) | skill motion-flavor / Atomik |\n"
        "| [@paojiaofty](https://x.com/paojiaofty) | skill de movimiento físico, anunciado |\n"
        "| [@foma_on_x](https://x.com/foma_on_x) | flujo de explicativos con diagramas |\n"
        "| [@DeryaTR_](https://x.com/DeryaTR_) | instrucciones de una línea |\n"
        "| [@d4m1n](https://x.com/d4m1n) | una sola pasada dentro del repositorio |\n"
        "| [@TROOVY](https://x.com/TROOVY) | perspectiva de un estudio de motion profesional |",

    "[Suggest an account →](../../issues/new?template=watch-account.yml)":
        "[Sugerir una cuenta →](../../issues/new?template=watch-account.yml)",

    "## How to Contribute": "## Cómo contribuir",

    "**[→ Submit a prompt](../../issues/new?template=new-prompt.yml)** — paste it, link the source. No git required.":
        "**[→ Enviar un prompt](../../issues/new?template=new-prompt.yml)** —— pégalo y enlaza la "
        "fuente. No hace falta git.",

    "Every entry needs three things:": "Cada entrada necesita tres cosas:",

    "| Field | Why |\n|---|---|\n"
    "| **Author** | Name or handle, written the way they write it |\n"
    "| **Source** | Direct link to the post, thread, blog, or video |\n"
    "| **Published** | Date, so readers can judge how current it is |":
        "| Campo | Por qué |\n|---|---|\n"
        "| **Autor** | Nombre o usuario, escrito tal como lo escribe esa persona |\n"
        "| **Fuente** | Enlace directo a la publicación, el hilo, el blog o el vídeo |\n"
        "| **Publicado** | Fecha, para que el lector juzgue si sigue vigente |",

    "- **Quote verbatim.** Don't tidy, don't paraphrase, don't improve.\n"
    "- **Keep the original language.** Add a translation in a `<details>` block, marked unofficial — never replace the original.\n"
    "- **Never invent the missing parts.** If a screenshot cut off half the prompt, mark it `partial` and quote only what's visible.\n"
    "- **Link official docs, don't copy them.** Their APIs change; a stale copy here would mislead.":
        "- **Cita literalmente.** No lo ordenes, no lo parafrasees, no lo «mejores».\n"
        "- **Mantén el idioma original.** Añade una traducción en un bloque `<details>`, marcada "
        "como no oficial —— nunca sustituyas el original.\n"
        "- **Nunca inventes lo que falta.** Si una captura corta el prompt por la mitad, márcalo "
        "como `partial` y cita solo lo visible.\n"
        "- **Enlaza la documentación oficial, no la copies.** Sus API cambian; una copia "
        "desactualizada aquí solo confundiría.",

    "See [CONTRIBUTING.md](CONTRIBUTING.md).": "Consulta [CONTRIBUTING.md](CONTRIBUTING.md).",

    "## License & Acknowledgements": "## Licencia y agradecimientos",

    "Repo structure, editorial notes, and scripts: [CC BY 4.0](LICENSE).":
        "Estructura del repositorio, notas editoriales y scripts: [CC BY 4.0](LICENSE).",

    "**Prompts remain the copyright of their authors.** They are quoted here with attribution and a link to the original, for reference and study.":
        "**Los prompts siguen siendo propiedad intelectual de sus autores.** Se citan aquí con "
        "atribución y enlace al original, para referencia y estudio.",

    "Thanks to everyone building agent-driven video in the open — [かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), [Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), [Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), [Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, Kingy.ai, Vincentwei1021, simplexlabs, and the Remotion team.":
        "Gracias a todos los que construyen vídeo con agentes en abierto: "
        "[かし子](https://x.com/Kashiko_AIart), [なお](https://x.com/Naonekozamurai), "
        "[Dan](https://x.com/d4m1n), [Tejas](https://x.com/makwanatejas170), "
        "[Foma](https://x.com/foma_on_x), [Derya Unutmaz](https://x.com/DeryaTR_), "
        "[Kiki](https://x.com/Mayz1169), Nate Herk, OpenReplay, Elser AI, The AI Average, "
        "Kingy.ai, Vincentwei1021, simplexlabs y el equipo de Remotion.",

    "**Are you one of them?** [Open an issue](../../issues/new?template=correction.yml) to fix a credit, add your full prompt, or have your work removed. Actioned without argument.":
        "**¿Eres uno de ellos?** [Abre una incidencia](../../issues/new?template=correction.yml) "
        "para corregir un crédito, añadir tu prompt completo o pedir que se retire tu trabajo. "
        "Se atiende sin discusión.",


    "⭐ **Star this repo** if it's useful — it's how other people building agent-driven video find it.":
        "⭐ **Dale una estrella al repositorio** si te resulta útil —— así es como lo encuentra más "
        "gente que construye vídeo con agentes.",
}
