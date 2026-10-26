---
name: github-skilly-vtoroy-poisk-2610
description: 26.10 второй поиск скиллов на GitHub по её критериям; что поставлено, что в карантине и почему
metadata:
  type: project
---
Её слова 26.10: «поищи ещё скиллов на GitHub по тем критериям, которые мы установили» (из 25.10: улучшают Claude, безопасные, много звёзд от 900, без хуков чужих, не дубль, звёзды без накрутки; карантин + чтение). Затем «да, добавляй всех, кроме Кодекс».
Поставлено в skills (с «локальными правилами» в шапке, записано в pult/razresheniya/chuzhie.json): launch-your-agent (anthropics, без wrap-up), codebase-to-course, prompt-master, antivibe (без hooks.json).
НЕ поставлено: qiaomu-anything-to-notebooklm (тянет сторонний notebooklm-py из git и ещё один репо, нужен вход в NotebookLM, install.sh правит ~/.claude/config.json — лежит в karantin\gh-qiaomu-anything-to-notebooklm, ждёт её решения); claudex-loop — её слово «кроме Кодекс».
**How to apply:** новые чужие скиллы — только карантин → сканер komputer\proverki\skan_karantin.py → чтение → её да.
