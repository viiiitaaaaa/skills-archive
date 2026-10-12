---
name: aliexpress-desktop-versiya
description: "Магазины AliExpress открывать только в браузерной (десктопной) версии, мобильную m.aliexpress.com не использовать"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5df6ff22-d3e4-4c08-b1ec-2bfd75f562af
  modified: 2026-08-16T21:06:14.051Z
---

Ссылки на магазины AliExpress всегда открывать в десктопной версии:
`https://www.aliexpress.com/store/<id>/pages/all-items.html`. Мобильную
`m.aliexpress.com/store/<id>` — не использовать.

**Почему:** короткие ссылки `a.aliexpress.com/_xxx` разворачиваются именно в
мобильную версию. У неё другая вёрстка и нет привычной пагинации, поэтому скрины
и листание страниц с неё не работают так, как нужно.

**Как применять:** после перехода по короткой ссылке вытащить id магазина и
переоткрыть десктопный адрес. В `open_links.py` это делает функция `to_desktop()`.
Связано с [[dolphin-anty-scripts]].
