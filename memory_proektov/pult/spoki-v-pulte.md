---
name: spoki-v-pulte
description: "«Споки» в пульте говорится один раз в «Главной» — razdat.py spoki рассылает по вкладкам, spoki-wait один раз выгружает скиллы на GitHub"
metadata:
  node_type: memory
  type: project
  originSessionId: ae3bb8cb-12a2-402e-a8b3-1e365807cd22
  modified: 2026-10-14T19:08:57.908Z
---

С 14.10.2026 она не говорит «споки» в каждой вкладке. Говорит один раз в «Главной», дальше по dispatcher.md:
`razdat.py spoki` — каждая открытая вкладка сохраняет память и скиллы по своей задаче и отмечается `spoki-done`;
`razdat.py spoki-wait` (в фоне) ждёт все отметки до 20 мин и один раз запускает `skills-archive\sync_skills.ps1`.

**Why:** её слова: «я ж не буду на каждую вкладку… говорить споки». Если GitHub запускать из каждой вкладки, одновременные выгрузки мешают друг другу.

**How to apply:** правило «споки» из общей памяти (spoki-sohranit-vse) в пульте выполняется так. Переписки сами лежат на ПК в `~/.claude/projects/<папка>/*.jsonl`, а вкладки пульта — в `pult\state.json`. Переписки на GitHub не выгружать без её слова.
