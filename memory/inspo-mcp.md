---
name: inspo-mcp
description: "Inspo MCP подключён 22.09.2026 — база 832 реальных сайтов для дизайна интерфейсов; no-ai-slop ждёт проверки, ax и untidetect-tools отвергнуты"
metadata:
  node_type: memory
  type: reference
  originSessionId: 3381c894-1f85-495d-903f-a4cbfcbe648b
  modified: 2026-09-22T19:15:28.479Z
---

Inspo (github.com/Nutlope/inspo, MIT) подключён к Claude Code на уровне пользователя: `claude mcp add --scope user`, адрес https://inspomcp.dev/api/mcp (HTTP, без аккаунта). Даёт палитры, шрифты, DESIGN.md и готовые блоки 832 сайтов; `recommend(brief)` — главный инструмент. Использовать при дизайне страниц, подложек магазина (site-mockups), Shopify-темы, артефактов. Установщик заодно прописал его в `~/.cursor/mcp.json`.

Решения по ссылкам из новостей 22.09: **no-ai-slop** (petergyang, MIT) — установлен 22.09 вручную (SKILL.md + eval.md в ~/.claude/skills/no-ai-slop, без `npx skills add`), проверен: только правила редактуры, без кода и сети; правила англоязычные — для описаний товаров и текстов на английском; **google/ax** — не нужен (оркестратор для команд); **untidetect-tools** — не ставить: средства обхода защиты, противоречит правилам [[trend-radar-bez-avtozapuska]] и проекта (Dolphin уже есть).
