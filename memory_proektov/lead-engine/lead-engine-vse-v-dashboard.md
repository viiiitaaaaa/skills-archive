---
name: lead-engine-vse-v-dashboard
description: "lead-engine — всю информацию выводить в панель (дашборд), отдельные таблицы на Диске не плодить"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9611721f-bd15-4f13-8684-410c745286d4
  modified: 2026-09-30T23:04:50.974Z
---

01.10.2026: «ВСЮ инфу в дашборд. Не плоди таблицы».
**Why:** после каждого сбора я клала на Диск новый xlsx (выгрузка каждого запуска, своды, каталоги) — она смотрит панель, таблицы только засоряют папку.
**How to apply:** новые данные → data/raw (json) / data/lists (tsv) в проекте → блок в dashboard/build_dashboard.py + template.html → пересобрать и открыть панель. apify_run.py пишет таблицу на Диск только с --xlsx. На Диске остаются панель и одна общая база база_lead_engine_*.xlsx. См. [[lead-engine-proekt]].
