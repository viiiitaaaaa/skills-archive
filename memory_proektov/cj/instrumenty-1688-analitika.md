---
name: instrumenty-1688-analitika
description: "Инструменты аналитики для отбора 1688 — график расширения 1688 (iframe trend-panel, данные фоном — только снимком), 店雷达 и 知衣 как продвинутые сервисы"
metadata:
  node_type: memory
  type: reference
  originSessionId: deaa25da-85ca-436b-be83-d10899e2d7bf
  modified: 2026-10-03T22:08:27.592Z
---

- **График расширения 1688官方采购助手** на карточке: блок «商品成交趋势情况» = iframe
  air.1688.com/kapp/innovateHub/extension-dynamic-modal/trend-panel?amug_biz=oneself&amug_fl_src=awakeId_984&offerId=…
  Данные ему передаёт расширение фоновым запросом (в сети вкладки не видно, в файлах расширения адреса нет);
  открытый напрямую — нули. Рабочий способ: карточка → клик «商品成交趋势情况» → снимок/zoom графика (90 дней).
- **Список товаров магазина** (shopXXX.1688.com/page/offerlist.htm) с расширением показывает по каждой модели
  年销量 / 月代销 / 上架日期 — быстрый фильтр без открытия карточек.
- **店雷达** dianleida.net — сервис+плагин для 1688: мониторинг магазинов-конкурентов (продажи по времени),
  мониторинг товаров, горячие источники, сравнение цен «того же товара» у разных источников. Регистрация — она сама.
  **MCP** (dianleida.net/introduce/mcp/): `https://mcp.dianleida.net/mcp?secret-key=KEY`, transport http; 1 балл/вызов,
  баллы только после покупки членства; ключ — dianleida.net/mcp/. Инструменты: product_search_list (30+ фильтров:
  цена, продажи, дата выкладки, фабрика/магазин, 代发), product_billboard_list (рейтинги нед/мес), product_info
  (продажи ПО ДНЯМ за 30 дн, цена), image_search (та же модель/первоисточник), get_category_info.
  ❌ 03.10: регистрация требует подтверждения личности китайским документом — у неё нет → 店雷达 НЕ предлагать
  (и 知衣, вероятно, так же). Цены были: пробный 4 дня бесплатно (20 баллов), 368 ¥/мес (80 баллов), 1998 ¥/год.
  Подключение (если когда-то появится доступ): она вводит `! claude mcp add --transport http dianleida "<ссылка>"` (ключ не в чат). 03.10 — предложено.
- **知衣** data.zhiyitech.cn (知衣科技, 知款) — fashion big data: хиты/тренды и продажи за любой период по Taobao, Douyin,
  1688, Amazon, Temu, Pinterest; мониторинг магазинов. Платный (годовая подписка). Регистрация — она сама.
- **Apify zen-studio/1688-wholesale-scraper** (без входа в 1688, без китайских документов): keywords/offerIds,
  priceMin/priceMax, sortBy bestSelling, merchantType superFactory/verifiedMerchant; поля saledCount, offerRepurchaseRate,
  repurchaseRate, dropship.metrics (заказы 7/30 дн → признак роста), поставщик (город, тип, сотрудники). ~$3.99/1000 товаров.
  03.10: она подняла лимит Apify до $45/мес (цикл до 29.10); сборы 1688 одобрены ею — потолок на запуск $3, ~$2.5/320 моделей.
  Связь через VPN рвётся — zapusk.py умеет повторять; если упал, данные забрать по datasetId последнего запуска.
Связано: [[postavshchik-ne-tovar]], [[treg-1688-api]].
