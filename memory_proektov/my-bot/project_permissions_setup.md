---
name: project-permissions-setup
description: "Разрешения: инструмент называется PowerShell, а не Bash; allow-лист живёт в пользовательском settings.json"
metadata: 
  node_type: memory
  type: project
  originSessionId: a3c1d32e-112f-4457-ad82-459b33a0533d
  modified: 2026-07-30T18:43:45.037Z
---

Allow-лист вынесен в `%USERPROFILE%\.claude\settings.json` (ключ `permissions`
рядом с `hooks`, не внутри), с `defaultMode: acceptEdits`.

**Две причины, по которым правила раньше не срабатывали:**

1. **Инструмент здесь называется `PowerShell`, а не `Bash`.** Правила вида
   `Bash(npm run *)` на этой машине не совпадают ни с чем. Нужно
   `PowerShell(...)`.
2. **«Yes, and don't ask again» пишет полный literal-путь**, включая UUID
   сессии в пути к scratchpad
   (`...\C--Users-User-my-bot\<session-uuid>\scratchpad\foo.js`). На следующей
   сессии UUID другой — правило мертво. Поэтому проектный
   `my-bot\.claude\settings.local.json` разросся до 34 правил, из которых
   работали единицы. Лечится обобщённым `PowerShell(node *)`.

Ещё: `my-bot` — не git-репозиторий, но `.claude/settings.local.json` там всё
равно создаётся; привязка идёт к рабочей папке, а не к корню репозитория.

Тонкости: `deny` бьёт `allow` на любом уровне; в составных командах через `;`
или `&&` каждая часть проверяется отдельно, поэтому цепочка всё равно спросит.

Связано: [[feedback-no-questions]].
