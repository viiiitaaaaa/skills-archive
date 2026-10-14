---
name: treg-1688-api
description: "1688 через treg.to API (ключ радара) — поиск по словам отдаёт 60 товаров с offerRepurchaseRate (повторные закупки ТОВАРА), продажами, ценой; карточка по ID — остатки, 代发, минимум. Без браузера и капчи"
metadata:
  node_type: memory
  type: reference
  originSessionId: 5fa2a60a-0d7d-43bb-95d4-fc422b5def7c
  modified: 2026-09-28T00:26:51.158Z
---

28.09.2026 найдено после её упрёка «я дала столько утилит, а ты мудрил полдня» (использовал только браузер).
Ключ — `C:\Users\User\fashion-trend-radar\fashion-trend-radar\.env` (TREG_TOKEN, TREG_ORG=vi), заголовки X-Treg-Token / X-Treg-Org.
- Поиск: GET `https://treg.to/call/justoneapi.x.1688-search-item-list-v1?keyword=格纹半身裙&page=1` — $0.0148 за удачный
  (60 товаров). code 301 «COLLECT FAILED» — бесплатно, повторить через 5 с. Поля товара: offerId, offerRepurchaseRate
  (доля повторных закупок ТОВАРА; у магазина отдельно turnHead.percent — числа разные: 晴雅 5% против 60%), bookedCount
  (продажи), priceInfo.price, shop.text, tpYear, factoryInspection, superFactory, sameDesignUrl (группа «та же модель»),
  offerPicUrl. Пустой rate бывает у новых/рекламных (block=P4P — реклама, выкидывать).
- Карточка: GET `…/justoneapi.x.1688-get-item-detail-v1?itemId=ID` — $0.0148: цена, saledCount, остаток
  (price.alipayIntegralInfo.originalOrderPrice.canBookedAmount; по размерам в skuCore), beginAmount, order.sceneList (代发),
  продавец, все фото. 复购率 в карточке НЕТ.
- Поиска по фото в treg нет. Образцы ответов: cj\sverka\treg_1688_test.json, treg_1688_search.json.
Совпадает ли offerRepurchaseRate с панелью на странице — проверить на 1–2 товарах, потом доверять.
Связано: [[treg-to]], [[povtornye-zakupki-60]], [[plan-pdd-vs-1688-otbor]].

28.09 тест: rep из API выше панели ~на 7 п.п. (61→54, 50→43) — годится как сито, решает панель. Из 52 юбок прошли 5,
по панели подтверждены 维芝雅 584772625175 (54%, 45 ¥, 1800+/год, ~870 на размер) и 盛夏佳依 834085115699 (43%, 31 ¥).
Той же модели на PDD ни у кого нет. Баланс treg кончился ($0.009) — полный прогон после её пополнения.
