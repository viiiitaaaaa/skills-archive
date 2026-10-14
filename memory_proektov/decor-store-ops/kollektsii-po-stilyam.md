---
name: kollektsii-po-stilyam
description: Скилл разбивки товаров магазина по коллекциям в соответствии с интерьерными стилями 2025-2026
metadata: 
  node_type: memory
  type: project
  originSessionId: 01751d72-549c-49dc-8269-5150f5435db9
  modified: 2026-08-18T07:50:21.455Z
---

Разбивка товаров магазина по коллекциям-стилям — скилл `style-collections`
(`C:\Users\User\.claude\skills\style-collections\`): `make_sheets.py` делает контактные
листы, разметка идёт глазами в `labels.txt`, `make_collections.py` раскладывает по папкам.
Список стилей и промты — в `стили-2025-2026-промты.pdf` там же (прислан пользователем
18.08.2026 из Telegram).

10 стилей: Warm Minimalism, Organic Luxe, Color Drenching, Heritage Maximalism,
Modern Mediterranean, Neo-Japandi, Quiet Luxury 2.0, Sculptural Contemporary,
Dark Academia, Eclectic Collector's + код 0 «вне коллекций».

**Why:** пользователю важно, чтобы товар попадал ровно в одну коллекцию — «использовал
1 раз и всё». Структура разметки это гарантирует.

**How to apply:** сначала нарезка через [[narezka-kartochek-tovarov]], затем этот скилл.
Первым сделан Shop1105084156 Store (828 товаров в коллекциях из 1180), разметка лежит в
`labels.txt` в папке магазина. Остальные магазины — по мере запроса, пользователь просил
пока не продолжать.
