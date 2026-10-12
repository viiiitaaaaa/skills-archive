---
name: apify-lead-engine
description: Apify — источник Яндекс Карт/2ГИС/Авито/Циан/Telegram для lead-engine; Bright Data Яндекс не берёт; ключ в lead-engine\.env
metadata:
  node_type: memory
  type: reference
  originSessionId: fef7417a-8a46-4007-b4c8-05a288f6b471
  modified: 2026-10-02T14:05:49.286Z
---

30.09.2026: аккаунт exhilarated_prestige переведён на STARTER ($19/мес, цикл 30-го числа по 29-е; неизрасходованное сгорает). Яндекс Карты и отзывы дешевле через Bright Data (parsers/yandex_maps_bd.py), Apify — для Instagram, Telegram, Авито, 2ГИС, Циан, контактов с сайтов.
Ключ — C:\Users\User\lead-engine\.env (APIFY_TOKEN; она вставила его в чат — можно перевыпустить). Лучшие сборщики — parsers\apify_actors.json.
Яндекс Карты: m_mamaev/yandex-maps-places-scraper, locations="Московская область", короткие названия (с «коттеджный посёлок» и «Москва и МО» — 0 результатов).
Всегда ставить maxTotalChargeUsd (потолок трат). Перед запуском проверять, на что действует потолок скрипта — на запуск целиком
или на каждый элемент: 02.10 tg_members --cap 1.2 был «на каждый чат» → 2.18 $ вместо обещанных ~1.1 (исправлено: теперь общий).
Остаток Starter на 02.10 ≈0.5 $ до 29.10. treg.to Яндекс Карт не умеет (только поиск Яндекса $0.015).
См. [[lead-engine-proekt]].
