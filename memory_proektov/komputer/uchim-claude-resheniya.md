---
name: uchim-claude-resheniya
description: 23.10 её решения по «учим Claude» — пилот «ответ на дорого», ДА 4 улучшениям (сжать CLAUDE.md, архив переписки, сверка в Stop, deny), НЕТ шаблону плана
metadata:
  type: project
---

23.10.2026 она ответила на вопросы страницы `komputer\claude_obuchenie_dlya_vity.html`:
- Дело для пробы — **ответ клиенту на «дорого»**.
- **Да:** сжать общий CLAUDE.md до карты <200 строк; хук PreCompact (архив переписки); хук Stop со сверкой «N из M»; deny на необратимое.
- **Нет:** шаблон плана ExecPlan (оставляем чеклист отдельным файлом).

**Why:** итог изучения 66 источников ([[kak-uchit-claude]] в claude-code-priemy) — длинный CLAUDE.md соблюдается хуже, обязательное держится только хуком/deny.
**How to apply:** план и галочки — `komputer\obuchenie_istochniki\plan_vnedreniya.md`; делать в новой сессии; черновик CLAUDE.md показать до замены.
