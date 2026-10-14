---
name: kuplennye-knigi
description: "Купленные книги по маркетингу и Claude в G:\\Мой диск\\куплено — 15 законспектированы 09.10.2026, приёмы разнесены по скиллам; Principles of Marketing 18e битый"
metadata:
  node_type: memory
  type: project
  originSessionId: 3b09cccd-d886-4de7-9cd7-91480ab64594
  modified: 2026-10-09T18:49:48.045Z
---

09.10.2026 она положила купленные книги в `G:\Мой диск\куплено` и выбрала «изучить в скиллы» (оригиналы не удалять — куплены).
Сделано: 15 книг прочитаны целиком → конспекты `~\.claude\skills\knowledge-library\references\knigi\` (оглавление `00_spisok.md`);
приёмы без повторов → `references\iz_knig.md` + раздел «Из книг (09.10.2026)» в SKILL.md скиллов dropship-lessons, dropship-audit,
b2b-sbor, vendor-check, shopify-admin, shopify-collections, site-design, site-mockups, product-scenes, trend-radar, sourcing-1688,
claude-code-priemy, tg-news, dela, knowledge-library. Советы книг, противоречащие её решениям, — только в разделах «Расходится», не правила.

**Why:** её правило — принятое/купленное изучать целиком и применять к делу ([[prinyato-izuchat-vse-ssylki]]).
**How to apply:**
- Индонезийскую «Seni Penulisan Efektif untuk Digital Marketing» она велела пропустить — не конспектировать; `seni_penulisan_copywriting.md` = черновик.
- «Principles of Marketing, 18e.epub» в папке битый (31 КБ, обрыв загрузки) — когда перекачает, конспектировать тем же порядком
  (рабочая папка `C:\Users\User\knigi_kupleno`: to_txt.py, ZADANIE_AGENTU.md, razbor.py, ZADANIE_SLIYANIE.md, CHECKLIST.md).
- Выжимка всех книг живёт в «Рабочей панели» новостей, блок «Книги» (`tg_monitor\panel_books.html`, её просьба 09.10 «в новостной радар перенеси»); новую книгу — дописать и туда. Начатая презентация-колода (artifact 7pKwh2TV543BBQsJmToHrA, опубликована только обложка) брошена ради панели.
- 09.10 вечером — второе прочтение оригиналов (её: «маловато… ещё раз прочти книги»): `knigi\dop\` (MM ×3, Grewal ×2, остальные по файлу; Design Matters доделан по заметкам — все 17 книг). Приёмы СТРОГО разложены по скиллам (её: «приёмы раскладываешь… это строго, нафига тогда перечитывали») — `razlozhit_dop.py` → `iz_knig_2.md` в 20 скиллах. Потом она сама велела «делай прогон в третий раз» — `knigi\dop3\` по ZADANIE_PROHOD_3.md (врезки, таблицы, упражнения), раскладка `razlozhit_dop.py 3` → `iz_knig_3.md`. Четвёртый — не предлагать. Третий остановлен на 71% лимита ([[limit-70-stop]]): полностью готовы 4 тонкие книги, SEO 2025, 4.0, 6.0, 7.0, 10 грехов, Entrepreneurial, Мукминов; ЧАСТИЧНО (файлы в dop3 есть, но кусок недочитан) — MM a/b/c, Grewal a/b, Vuibert, Digital Age, Design Matters, Dickey. Частичное уже разложено (567 раскладок). Если она скажет «продолжи третий прогон» — новые агенты по ZADANIE_PROHOD_3.md с указанием «дописать существующий файл dop3, начать с места, где он кончается», затем `razlozhit_dop.py 3` → build_books.py → news.py --build → sync_skills.ps1.
- 10.10 ВСЁ ДОЧИТАНО: третий прогон по всем 17 книгам (dop3, 1 059 раскладок); 21 новая книга 10.10 → `knigi\novye\` (to_txt_new.py, ZADANIE_NOVYE.md): e-commerce, продажи, нейминг, дизайн, учебники Belch/Hill/Grewal 8e (по частям), сканы Consumer Behavior (img_consumer) и Экман кит. (img_ekman) — 2 183 раскладки в `iz_knig_novye.md`. Не обрабатывали: оружие (Firearms), Market Garden, Art Market; Principles of Marketing 18e битый. В Hill PDF после строки 53190 вшита чужая книга (Icke) — не брать.
- 13.10 — 13 книг (ИИ-агенты, RAG, Mom Test, Minto, Pitch Anything, Prediction Machines, Whalen, Knaflic, OpenVPN) вместе с Hermes:
  `to_txt_13_10.py` → `txt13\` → `hermes_pereskaz.py` (куски по 8 тыс. слов, модель Hermes, текст В ЗАПРОСЕ, 2 потока) →
  агенты по `ZADANIE_13_10.md` → `knigi\novye13\` → `razlozhit_dop.py novye13` (841) → build_books.py (теперь берёт и novye, и novye13)
  → news.py --build → sync. Недокачаны (.tmp, ждут её перекачки): AI Engineering (Huyen), Building Resilient Distributed Systems
  (Newman), Lean Analytics, Obviously Awesome. Следующие книги — помощники на Sonnet + выборочная сверка (см. скилл hermes).
- 13.10 вечером: Obviously Awesome + OpenVPN Cookbook → novye13 (Hermes + помощники Sonnet).
  **Битые книги ЗАБЫТЬ** (её 13.10: «мы дофига обработали, про битые забудь»): AI Engineering, Building Resilient, Lean Analytics,
  Principles of Marketing 18e — не напоминать, не просить перекачать. Её перезагрузка 15:15 тоже битая (2–3 КБ, в epub только content.opf);
  если сама положит новые — признак целой: >1 МБ и в zip есть главы (xhtml), не 3 записи.
  Грабля: epub без toc.ncx роняет ebooklib → `to_txt_13_10b.py` читает главы по spine прямо из zip.
- Новые книги в «куплено» → тот же конвейер: текст → агент на книгу → конспект → слияние по скиллам → sync_skills.ps1.
- 13.10 16:24 через бот «Дела» пришла Alan Weiss «Million Dollar Consulting» (2016) → `куплено\Million Dollar Consulting (Alan Weiss, 2016).epub`, тот же конвейер (to_txt_13_10b ep_zip → hermes_pereskaz → помощник Sonnet → novye13\million_dollar_consulting.md, 71 приём, 33 в b2b-sbor). Книги, присланные в бот, класть в «куплено» и прогонять так же без вопросов.
- 13.10 вечером: Million Dollar Consulting (Weiss; делало второе окно), The Challenger Sale, Show Your Work!, The SPIN Selling Fieldbook → novye13 (Hermes + помощники Sonnet, исправлено 5–7 ошибок Hermes на книгу) → razlozhit_dop.py novye13 = 1 158 раскладок → build_books → news --build → sync. Применены: резюме, питч WB v8, питч по автозапчастям (rezyume-vakansii\vyzhimka_rezyume_pitch.md).
- 14.10 ночью: 8 книг НЛП/переговоры/уверенность (O'Connor Introducing NLP, Dilts Sleight of Mouth и Changing Belief Systems, Bandler Using Your Brain и Take Charge, Voss Never Split the Difference, Babcock Ask for It, Mohr Playing Big) — `to_txt_14_10.py` → Hermes (78 кусков, 0 ошибок) → помощники Sonnet (исправлено 6–12 ошибок Hermes на книгу) → novye13 → razlozhit (1 781 всего; dogovorennosti 300, love-scripts 37) → build_books → news --build → sync. Выжимка — раздел «Главное из книг 14.10» в скилле dogovorennosti. Дубль Восса «(1)» удалён по SHA-256; два издания Introducing NLP — одинаковый текст, оба файла оставлены.
- 14.10 днём: книги об обучении (Make It Stick, A Mind for Numbers, Ultralearning) + Колотилов «Продажи B2B», Lean Analytics → конспекты и раскладка (2 338 всего; kak-uchitsya 165). Хвост закрыт 14.10 вечером (её «доделай книги»): Peak, Moonwalking, Second Brain, Fluent Forever, Huyen AI Engineering, Newman Resilient → novye13 (Hermes + 6 помощников Sonnet, исправлено 4–12 ошибок Hermes на книгу) → razlozhit 2 957 (kak-uchitsya 374) → build_books → news --build → sync; «Главное» в kak-uchitsya дописано по всем 7 книгам об обучении. AI Engineering и Building Resilient теперь целые (PDF/epub 14.10) — «битые забыть» к ним больше не относится.
