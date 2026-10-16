---
name: marketpleysy-cherez-chrome
description: "Ozon, Wildberries и Авито проверять в её Chrome, а не через помощника с WebFetch — их защита от роботов не пускает"
metadata:
  node_type: memory
  type: reference
  originSessionId: e1b52f9a-2a79-4d48-bc2b-f8720401d9f7
  modified: 2026-10-16T01:48:16.074Z
---

16.10.2026: помощник с WebFetch (сервер без браузера) получил от WB ответ 403 «доступ запрещён», на Ozon попал в бесконечную
переадресацию, а Авито закрыт для чтения. В её Chrome (claude-in-chrome) все три открылись сразу: она там вошла в аккаунты.
Поиск по номеру OE: ozon.ru/search/?text=<OE>, wildberries.ru/catalog/0/search.aspx?search=<OE>,
avito.ru/rossiya/zapchasti_i_aksessuary?q=<OE>. Карточки на Ozon: `a[href*="/product/"]`, на WB: `.product-card`,
на Авито: `[data-marker="item"]`.

**How to apply:** цены на маркетплейсах сразу смотреть самой в Chrome, по одной вкладке и спокойно, без пачек.
