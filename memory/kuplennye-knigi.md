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
- Новые книги в «куплено» → тот же конвейер: текст → агент на книгу → конспект → слияние по скиллам → sync_skills.ps1.

