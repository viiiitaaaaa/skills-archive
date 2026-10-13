---
name: tablo-zadach-agentov
description: "С 13.10 каждую долгую задачу (мою, субагентов, Hermes) ставить на табло ~/.claude/agent_status.py — оно видно строками внизу Claude Code"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e994540f-d5ab-4cfe-8186-497676e3e8a3
  modified: 2026-10-13T11:14:28.183Z
---

Её: «сделай строку обработки агентов… я нигде не вижу, на какой стадии обработка». Строка состояния (statusline.py):
1) модель · контекст · кэш; 2) сессия 5 ч · неделя · ЦП · память; 3+) задачи с табло.
`python ~/.claude/agent_status.py set <id> --title … --who Claude|Hermes --stage … --total N --glob "<готовые файлы>"`,
стадию менять тем же `set`, в конце `done <id>`.

**Why:** долгие сборы идут в фоне, а она не видит, где они сейчас.
**How to apply:** перед запуском любой фоновой/многошаговой работы — `set`; при смене стадии — `set --stage`; после — `done`.
Дополняет [[dolgie-sbory-progress]], [[hermes-legkie-zadachi]].
