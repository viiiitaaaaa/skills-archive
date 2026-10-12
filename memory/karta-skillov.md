---
name: karta-skillov
description: "Карта всех 32 скиллов (28.09.2026: +disk-hygiene) — страница-артефакт, доска Whimsical и сценарии «Карта · …» в n8n; как пересобрать"
metadata:
  node_type: memory
  type: project
  originSessionId: e13e5c0c-70b5-4b9a-95d6-1816062d0d0c
  modified: 2026-09-27T13:11:06.962Z
---

27.09.2026 она попросила «все процессы по всем скиллам, чтобы видеть твою логику и правильно ли ты её строишь»,
подключить через n8n и Whimsical (оба установлены, Whimsical открыт в Chrome, аккаунт «VI»).
- Страница: https://claude.ai/artifact/WZp11Ran7n2ib77RobkAmJ (вкладки по группам, схема + правила + фразы запуска).
- Whimsical: доска «Карта всех скиллов ARTMELLIO» (team «Everyone at VI»); вставляется Mermaid-текстом через Ctrl+V
  на холст — Whimsical сам рисует схему с цветами. Отдельные схемы: artmellio-system\docs\skill-map\whimsical\*.mmd,
  всё на одну доску — ALL_ONE_BOARD.mmd.
- n8n: 29 выключенных сценариев «Карта · <скилл>» (узлы-заглушки + заметка с правилами), импорт
  `n8n import:workflow --separate --input=artmellio-system\n8n\map`. При первом запуске n8n просил создать
  учётку владельца — это делает она сама (пароль).
- Сборщик: artmellio-system\docs\skill-map\build_skill_map.py (из skills_all.json; схемы написаны строго по тексту скиллов).
- Найдено расхождение: dolphin-shots, dsers-import, product-links — в тексте старые профили Dolphin (828976678/836461485),
  а правило — всегда 859648353 ([[dolphin-profile-id]]). 27.09 ИСПРАВЛЕНО во всех скиллах и скриптах (в т.ч.
  shopify-admin, shopify-collections, artmellio-system, dropship-audit — там был «Декор» 836461485); карта пересобрана.
- n8n: build_skill_map.py берёт id уже импортированных карт из n8n\map\_existing_ids.json (export:workflow --all) —
  повторный импорт обновляет, а не дублирует.

- 27.09 (вечер): на опубликованной странице группы изменены вручную — tg-news в «Поиск и тренды», style-collections в
  «Магазин Shopify»; перенесено и в skills_all.json. Страница пересобирается из опубликованной версии (строка `const SKILLS = …`),
  а не из старой копии в scratchpad прошлой сессии.

**How to apply:** после правки любого скилла — пересобрать карту (skills_all.json → build_skill_map.py → переопубликовать
страницу, при желании перезалить доску и импорт n8n).

- 27.09 (поздно): добавлен скилл dela (группа «Маркетплейсы и документы»); на странице запись дописана в строку const SKILLS, версия 6.
