---
name: rabota-v-code-ne-desktop
description: "Она отказалась от Claude Desktop (проекты с координатором), работает в Claude Code; голос /voice, проекты в Cursor через «Мои проекты.code-workspace»"
metadata:
  node_type: memory
  type: user
  originSessionId: be8f14ae-faa8-43be-bddf-9cde7303a9f5
  modified: 2026-10-14T17:57:36.580Z
---

14.10.2026: опыт с Claude Desktop ей «категорически не понравился» (Projects Beta с координатором: обрывы связи, «открой ветку, напиши давай», час на вход в Gemini). Остаётся на Claude Code.

Что настроено:
- Голос в терминале: `/voice` (hold = держать пробел, tap = нажать/нажать). В `~/.claude/settings.json` поставлено `"language": "russian"`.
- Cursor (`%LOCALAPPDATA%\Programs\cursor`) + расширение anthropic.claude-code 2.1.299. Файл `C:\Users\User\Мои проекты.code-workspace` — 8 папок проектов слева, файлы видно, история сессий кнопкой Session history.
- Сессии других папок в терминале: `claude --resume`, затем Ctrl+A.
- В settings.json стоит `effortLevel: medium`: трудное делать с `/effort high`.

**Why:** чтобы не предлагать ей снова Desktop/проекты.
**How to apply:** задачи на ПК — в Claude Code; переключение проектов и просмотр файлов — через Cursor workspace. Связано: [[proekty-po-papkam]], [[gemini-cli-otklyuchen-antigravity]].
