---
name: razdat-kavychki
description: В --task для razdat.py нельзя двойные кавычки — PowerShell рвёт аргументы; писать «ёлочки»
metadata:
  node_type: memory
  type: feedback
  originSessionId: ae3bb8cb-12a2-402e-a8b3-1e365807cd22
  modified: 2026-10-15T02:05:59.335Z
---

В тексте `--task` / `--text` для `razdat.py` не ставить двойные кавычки " — PowerShell разрывает аргумент, задание уходит обрезанным. Писать «ёлочки».

**Why:** 15.10.2026 задания терялись/обрезались, пришлось отправлять повторно.
**How to apply:** каждый вызов razdat.py new/send/todo — только «ёлочки» внутри текста.
