---
name: artmellio-system-dev-vetka
description: "artmellio-system: рабочая ветка feature/operations-panel, ветка dev разошлась — push в dev не проходит, силой не перезаписывать (07.10)"
metadata:
  node_type: memory
  type: project
  originSessionId: fc38aaa6-d001-4d24-8b62-c3816db45c2b
  modified: 2026-10-07T13:31:17.607Z
---

07.10.2026: в репозитории `C:\Users\User\artmellio-system` текущая ветка — `feature/operations-panel`. Ветка `dev`
разошлась с ней, обычный `git push origin HEAD:dev` отклоняется (non-fast-forward). Документ уроков
`docs/uroki-iz-novostey.md` ушёл только в рабочую ветку.

**Why:** скилл dropship-lessons велит пушить и в dev; делать это силой нельзя — можно затереть чужие правки.

**How to apply:** при следующем обновлении уроков слить ветки обычным merge (или спросить её, какая ветка главная),
а не `--force`. [[uroki-iz-novostey]] [[globalnyy-claude-md]]
