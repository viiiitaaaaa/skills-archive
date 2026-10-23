---
name: brauzery-mcp-ispolzovanie
description: "Playwright MCP нужен (книги, komputer, вакансии, запчасти, пульт), stealth-browser почти не используется; советы «что нужно» — только по счёту вызовов"
metadata:
  node_type: memory
  type: project
  originSessionId: 475576a5-44fa-4958-a06e-fff3aba417e5
  modified: 2026-10-23T10:59:46.764Z
---

Проверка 23.10.2026 (агент proverka): Playwright MCP — 671 вызов, последние 22.10, в knigi-kupleno, komputer,
rezyume-vakansii, zapchasti, pult, lead-engine-site; агент design-review на нём. Stealth-browser — 61 вызов,
последний 09.10, только домашняя папка; в fashion-trend-radar ни одного. Оба стоят глобально в ~\.claude.json,
вместе ~260 МБ на каждую вкладку.

**Урок:** я сначала сказала ей «Playwright — для Смарт Люкс, stealth — для радара» по памяти — оказалось неверно.
**How to apply:** про «нужен ли инструмент» отвечать только по счёту реальных вызовов (tool_use в .jsonl), не по памяти.
