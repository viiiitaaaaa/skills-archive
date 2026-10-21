# Проверка сайта «4 новичка» (пост Вайб-кодинг, 21.10.2026; разобрано 22.10)

Что это: перед показом сайта людям — 4 субагента (помощника) по очереди проходят путь
«главная → первое успешное действие» (у нас: отправленная заявка с UTM) в браузере (Playwright MCP) и пишут,
где застряли. Дополняет `site/qa_site.py` (тот ловит поломки вёрстки, а этот — где человеку непонятно).

Роли:
1. Нетерпеливый — бегло смотрит, жмёт первую кнопку, уходит при первой ошибке.
2. Скептик — читает цены, политику конфиденциальности, условия; останавливается на непонятном.
3. Смартфон — 375 px, медленная сеть (3G); скрытая кнопка и горизонтальная прокрутка = проблема.
4. Ломатель — неверные данные в форму, «назад» посреди, двойной клик по «Отправить» (не ушла ли заявка дважды).

Правила для нас:
- Только превью (frivent-site…workers.dev), не боевой домен; тестовая почта, настоящих заявок не слать
  (или пометка «ТЕСТ» в поле, чтобы не путать с лидами).
- Скриншоты — в `site/qa/first-users/`; одинаковые проблемы в одном месте = одна; сортировка по числу «пользователей».
- Цены, политика, условия — только записать для неё (политика ждёт юриста), остальное исправить одним проходом
  на превью, затем 4 НОВЫХ субагента (не видевших таблицу) повторяют — сравнение «до/после».
- Субагенты — Sonnet (кнопки в браузере — дешёвым моделям), задания им по-английски, отчёт ей — по-русски.
- Запуск — по её «делай» (8 субагентов = заметный расход лимита).

Промпт-основа (EN, для агента):
"Find where first-time users get stuck. Check a browser MCP is available (else stop and give the Playwright MCP
install command). Define the first successful action (submitted lead form) and state it at the top. Run 4 subagents
one after another (impatient / skeptic / mobile 375px + slow 3G / stress tester), each from the home page to the
first success. Screenshot every hesitation, dead end or 'want to close the tab' to qa/first-users/ with stage, what
was seen, what was attempted. Each reports: would return? clicks to success. Preview only, test email. Merge
duplicates, sort by number of users hit. Pricing/terms/privacy — report only. Fix the rest in one pass, then run
4 fresh subagents under the same conditions and compare before/after."
