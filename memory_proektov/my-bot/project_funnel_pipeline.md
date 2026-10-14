---
name: project-funnel-pipeline
description: "funnel.js/funnel-upload.js — воронка продаж (API sales-funnel/report, батчи по 50 nms) в колонки B и AL..AV недельных вкладок"
metadata: 
  node_type: memory
  type: project
  originSessionId: a3c1d32e-112f-4457-ad82-459b33a0533d
  modified: 2026-07-30T21:35:44.761Z
---

Метрики по артикулам за неделю (заказы, конверсии, остатки WB и пр.) берутся
из API интерактивного отчёта
(https://seller.wildberries.ru/content-analytics/interactive-report/main):
`POST seller-content.wildberries.ru/ns/analytics-api/content-analytics/api/v1/sales-funnel/report`
с заголовками `AuthorizeV3` (localStorage `wb-eu-passport-v2.access-token`) и
`Wb-Seller-Lk` (localStorage `wb-eu-portal.seller-token`), изнутри вкладки.

**Критично:** API отдаёт максимум **50 товаров** за запрос и игнорирует
page/limit/offset; скролл страницы ничего не догружает (UI показывает топ-50).
Обход — параметр `nms`: весь ассортимент запрашивается батчами по 50 nmId
из `my-goods.json` (332 шт). Кнопки экспорта в Excel на странице нет.

**Поля:** vendorCode=артикул вкладок, stockWbQty (остатки — текущие на момент
запроса, истории нет), shareOrderPercent, openCard, openToCart, cartToOrder,
orders, ordersSum (+.dynamics = «Динамика суммы заказов, %» при переданном
prevPeriod — предыдущая неделя), buyoutPercent, avgOrderCountPerDay,
timeToReady {days,hours,mins}→часы, localizationPercent.

**Конвейер:** `node funnel.js --tabs` (все недели-вкладки; или даты, или без
аргументов — прошлая неделя) → `node funnel-upload.js`. Данные копятся в
funnel/funnel-daily.json по периодам; лист «История воронки»; вкладки — SUMIFS
по артикулу (TRIM) + периоду: B «Итого по складам ВБ» + новые AL..AV
(заголовки в строке 1). ИТОГО только счётным (B, AM перешли, AP шт, AQ ₽) —
SUMIFS по всему периоду; процентам/средним ИТОГО не ставится.

Заменил собой remains.js/remains-upload.js (warehouse-remains, удалены
31.07.2026). Лист «История остатков» остался в книге, но B на него больше
не ссылается — можно удалить руками.

Связано: [[project-week-tabs-formulas]], [[project-ads-expenses-pipeline]],
[[project-storage-pipeline]].
