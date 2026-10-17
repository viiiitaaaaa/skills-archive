---
name: napominanie-gotovo-v-bot
description: "Готовые задачи вкладок пульта сами уходят ей в личку бота @adocs657412bot пачкой (pult\\gotovo_tg.py), включено 16.10.2026"
metadata:
  node_type: memory
  type: project
  originSessionId: e81dd920-3c2c-4e39-81fa-f88ab58b97ef
  modified: 2026-10-16T17:40:09.809Z
---

16.10.2026 по её слову включено: `agent_status.py done` и `razdat.py uborka-done` (если всё готово) ставят запись в очередь
`pult\gotovo_tg.py`; почтальон ждёт 90 с и шлёт одно сообщение «✅ <категория> — <задача>: <суть>» + файл, только на её OWNER_ID,
без кнопок, без повторов (12 ч). Подробно — PLAN.md «Напоминание о готовых задачах».

**Why:** она хочет знать о готовом, отойдя от компьютера; 15.10 боты перехватывали друг друга — поэтому без кнопок и один получатель.
**How to apply:** чтобы задача дала напоминание, вкладка должна закрыть её через табло (`agent_status.py done`, с `--file` итога).
Жалуется на шум — увеличить WAIT/REPEAT в gotovo_tg.py; журнал `pult\gotovo\zhurnal.log`. Связано: [[pult-sdelano-15-10]].
