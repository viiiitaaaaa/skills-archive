---
name: spisok-knig-itog-20-10
description: Сводный список проверенных книг по скиллам (до/после) на 20.10.2026 и что не сделано — её просьба «запомни этот список»
metadata:
  type: project
---
Проверка книги = карточки приёмов → слепой тест (6 реплик «до», 6 новых «после») → судья по критериям, написанным заранее. Итог — `knigi_kupleno\sistema\14_ITOG_nlp5_testy.md`; бэкапы скиллов — `sistema\bekap_skillov_*`.

Результаты (прошло из 6 «до» → «после», запретные):
- Вчера: Voss, Hall, Weiss, Klaff, Mom Test (love-scripts, dogovorennosti): ~3 из 30 → ~8 из 30.
- НЛП-пять (love-scripts): Dilts CBS, Dilts SoM, O'Connor, Bandler UYB, Bandler Take Charge: 3 из 30, запретных 13 → 8 из 30, запретных 3; блок C (20 реплик) 5, запретных 0.
- dogovorennosti: Challenger 0→2; SPIN 2→2; Колотилов 0→1 (запретных 1); Obviously Awesome 0→1.
- claude-code-priemy: Co-Intelligence 0→2; Build an AI Agent 0→1.
- dropship-lessons: Amazon FBA 0→0 (запретных 2→0); Entrepreneurial Marketing 0→1 (запретных 4→0).
- kak-uchitsya: Make It Stick 0→2 (критерии под учёбу); Mind for Numbers 0→0 (мерка была неверной — перепроверить).
Вывод: опасные ошибки почти везде ушли; «прошло» растёт не везде; слабости формы — метка источника, расшифровка терминов, один вопрос первым, цвет данных.
Не сделано: Mind for Numbers с критериями под учёбу; книги про тело (кишечник Кропка, Strong Curves); ОКР-книги (сверка/v_skilly); перенос в бота «Равновесие» — СДЕЛАН 20.10 (коммит cec2914 в main lyubov-bot): знания `znaniya/dogovorennosti/` (8 книг + каркас + правила) и `znaniya/nlp5/` (5 книг + правила 18–41), маршруты и убраны номера телефонов в CLAUDE.md бота. Не сделано: слепой тест на самом боте.
**How to apply:** при вопросе «что с книгами» — читать этот файл и 14_ITOG. Правила: kak-uchitsya только про учёбу (см. [[test-5-nlp-knig-19-10]]).

**20.10 — тест бота «Равновесие» (симуляция 10 сообщений):** 5/4/1, запретных 0; поправки в CLAUDE.md бота запушены; итог sistema	est_bota\sud.md. Повторного прогона нет. Следующие варианты: Mind for Numbers с критериями под учёбу; книги про тело; реальная проверка бота её живыми сообщениями.

**20.10 — повторный прогон бота:** 3/7/0, запретных 0 (первый прогон 5/4/1). Поправки п.7 в CLAUDE.md бота запушены. Дальше — её живые сообщения; без новых прогонов (лимит).
**«Споки» 20.10:** knigi_kupleno запушен (main), скиллы dogovorennosti/love-scripts/dropship-lessons/kak-uchitsya/claude-code-priemy скопированы в automation-scripts\claude-skills и запушены; бот lyubov-bot запушен ранее. Хвосты на завтра: Mind for Numbers с критериями под учёбу; книги про тело (Кропка, Strong Curves); ОКР-книги (сверка/v_skilly); живая проверка бота; решение про числа-ориентиры в учёбе (на её слово); режим auto без вопросов (хук не ловит).
