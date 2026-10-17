---
name: dlya-chzhana-kitayskiy-sverhu
description: "Любой текст для Чжана — китайский сверху, русский перевод снизу; показывать ей только двуязычный otchet_itog_*.html, не proverka.html"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8188739f-ef7f-4956-804c-e809c3633607
  modified: 2026-10-16T23:18:35.730Z
---

Вита 17.10.2026 (не в первый раз): «Сначала вставляем китайский, а потом с него перевод на русский. Почему опять всё на русском?»

**Why:** она отчитывается Чжану, сама китайский не читает; русская версия ей для проверки, а уходит китайская.
**How to apply:** правки в `skripty\`, потом `python skripty\sobrat_vse.py`, копия `otchet_itog_ЧЧММ.html`, показ `razdat show`. Блоки `.q` (вопросы) в исходнике ставить zh первым. `proverka.html` — только русский, внутренний, не показывать. Перед показом проверить, что голых русских строк нет. Про деньги и формат Чжану не писать. Связано: [[itogovyj-dokument-dlya-chzhana]], [[otchet-dvuyazychnyj-sostoyanie]].
