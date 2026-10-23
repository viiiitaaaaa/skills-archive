---
name: mom-test-30-situacij-perplexity
description: Тест Mom Test по 30 ситуациям Perplexity (23.10 вечер): 27/30 → правила 25–29; остальные книги Perplexity ждут её слова
metadata:
  type: project
---
Ситуации лежат в `perplexity_knigi\01_mom_test.md` (30, по 4 части; запрос сделала старая вкладка, ссылка perplexity.ai/search/69454cc3-…). Прогон: `retest_23_10_p\` (vhod/otvety/otvety_p2/sud). Первый счёт 27/30 был по НЕсверенному ключу Perplexity (завышен). Ключ сверен с книгой (79 ✅/43 🟡/12 ❌ «нет в книге») → `sud\klyuch_mom_test_sverennyy.md`; по нему до правил 24/30, после правил 25–29 25/30; новый класс ошибок — ложное «в книге нет» → правило 30 (не перепроверено). Журнал в `dogovorennosti\references\retest_2310_pravila.md`.
**Why:** её слово 23.10: «подождём, чтобы подозрения не вызвать» — новые запросы в Perplexity по другим книгам НЕ слать, пока не скажет; тест сделан на уже полученных ситуациях.
**How to apply:** ключ Perplexity для новых книг СВЕРЯТЬ с текстом книги ДО прогона (3 проверяющих по 10 ситуаций), а не после; судить только по сверенному ключу. Voss, Klaff, Weiss и т.д. из Perplexity — только по её слову (шаблон `perplexity_knigi\_prompt.md`); сначала искать готовые ответы в истории чатов. Связано: [[ne-dublirovat-platnyy-zapros]], [[retest-10-knig-23-10]].
