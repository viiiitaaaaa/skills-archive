---
name: sessiya-14-10-cikl-vakansii-rezyume
description: "Сессия 14.10 — полный цикл Frivent и автозапчастей по книгам, LinkedIn ограничен, 30 вакансий, универсальное резюме; хвосты"
metadata:
  node_type: memory
  type: project
  originSessionId: 612252cb-56ea-4557-85cc-cebb46406127
  modified: 2026-10-14T13:29:21.078Z
---

14.10.2026 сделано (всё .html, копии на Диске):
- «Полный цикл Frivent по схеме» v2 — 249 приёмов из книг и скиллов по веткам: https://claude.ai/artifact/GXY2usGHwkuQDGFduRZCzx
  (lead-engine\docs\полный_цикл_frivent.html + полный_цикл_приёмы.txt + dashboard\build_polny_cikl.py). См. [[lead-engine-proekt]].
- «Полный цикл: автозапчасти» (опт СТО/мастерским/магазинам/паркам + розница), 128 приёмов, без Frivent:
  https://claude.ai/artifact/4aiFNKWsuksEjw3asVHvWq (knigi_kupleno\avtozapchasti\; Диск «ARTMELLIO — инвесторы»). Только RU.
- 30 удалённых вакансий США/Европа с разбором «что делают / что уметь / что есть / чего нет»:
  https://claude.ai/artifact/UEB8cT4w1UjAUithRmSFwG (knigi_kupleno\vakansii_30.json, build_vakansii.py). Из России реально 16.
  Частые требования: ИИ 15/30, отчёты 12, английский 12, HubSpot/CRM 11, Google/Meta Ads 9.
- Резюме обезличенное универсальное (RU по умолчанию + EN кнопкой): https://claude.ai/artifact/QhT8e3Xc1SiXSmrqLSduKG
  (knigi_kupleno\rezyume_universal.html). В MEMORY есть план другой сессии «2 резюме (А WB, Б ИИ-продажи)» — сверить.

Второй заход 14.10 (вечер):
- Парсер вакансий `knigi_kupleno\sbor_vakansiy.py` — открытые API без ключей: Himalayas, Remotive,
  RemoteOK, Jobicy, Arbeitnow. Фильтр: наш профиль ролей + от 75 000 $/год; зарплату берёт из полей,
  а где нет — из текста (с проверкой контекста, чтобы не поймать выручку или бюджет). Итог
  `vakansii_sbor_<дата>.json`. Грабли: Himalayas отдаёт ~200 свежих, у половины зарплаты нет;
  Jobicy ругается 400 на часть разделов; валюты вне USD/EUR/GBP/CAD врут — отбрасываем.
- «Вакансии и наш опыт» — 22 вакансии от 75 000 $, по каждой три столбца (совпадает / частично /
  не совпадает) и процент: https://claude.ai/artifact/5JJLAf6jZGLXcrntxigt8Q
  (`sravnenie_dannye.json` — разбор руками, `build_sravnenie.py` — сборка). Из России реально 9.
  Лучшее попадание: Invisible Technologies 75%, Zuora 62% (у них в требованиях прямо Claude Code),
  Mozilla 56% (Claude Code + Cowork). Главный барьер почти везде — не опыт, а страна проживания.
  Чего не хватает чаще всего: Salesforce/HubSpot, GA4/GTM, SEMrush/Ahrefs, экспертный SQL,
  Google/Meta Ads, годы в B2B SaaS.
- Третий заход: **приоритет США, Россия последней** (её слово). Сборщик расширен до 9 источников
  (+ Working Nomads, The Muse по разделам, Remotive с поиском по словам, Jobicy geo=usa,
  8 страниц Arbeitnow) — собрано **48** вакансий, в сверке **37**, из них США 21, из России 9.
  Грабли: The Muse даёт 20 000 страниц и тащит медсестёр и сборщиков SpaceX — слово из названия
  совпадает, поэтому для него проверяем только название и держим длинный список BAD_WORDS.
  Сопоставление разбора с данными — по компании **и** названию: у Walmart две вакансии, у NetBox Labs две.
  Новое американское: Walmart «агентная автоматизация» и «закупочная платформа» по 220 000 $,
  TikTok рост 374 000 $, Sunrun категорийный менеджер 198 000 $, Cox аналитика поставок,
  SpaceX закупки (у них в пожеланиях ИИ для закупки — но **ITAR**, нужен паспорт США).
- Резюме усиленное, RU + EN кнопкой: https://claude.ai/artifact/Uv6mKTgzFnjRFQPQgFYqLB
  (`rezyume_pro.html`). Роль «операционный партнёр», достижения первым блоком с цифрой и способом,
  язык подогнан под эти 22 вакансии. Цифры только настоящие, сумм заработка и счётчиков ИИ нет.

**Хвосты (ждут её):** LinkedIn ограничен ([[linkedin-ogranichen-avtosbor]]) — документ или поддержка, новый аккаунт не
заводить; в резюме уточнить уровень английского и год старта (стоит 2022); автозапчасти — версия 中文 + RU по её слову;
советы по переговорам с Пашей собрать отдельно, если попросит.
