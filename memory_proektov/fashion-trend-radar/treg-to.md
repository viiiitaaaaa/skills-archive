---
name: treg-to
description: "treg.to подключён 23.09.2026 — один ключ к 85 платформам (TikTok, Pinterest, Google-объёмы, Amazon), $0.001 за запрос; TikTok по нашим хэштегам для США уже в радаре"
metadata:
  node_type: memory
  type: reference
  originSessionId: 3381c894-1f85-495d-903f-a4cbfcbe648b
  modified: 2026-09-22T23:02:33.261Z
---

treg.to (нашли в каталоге mcp.so 23.09.2026) — шлюз к платным API с оплатой за запрос, без подписки. Ключ команды «vi» лежит в `.env` fashion-trend-radar (`TREG_TOKEN`, `TREG_ORG=vi`). Пользователь вставила ключ в чат — при желании перевыпустить в кабинете. Их установщик `curl … | sh` не ставили — работаем REST-запросами.

Сделано: `run_tiktok_tags.py` — TikTok по хэштегам наших кандидатов, только США (`region=US`), ~$0.044 за 22 вещи; колонка T в радаре теперь живая (roll neck sweater стал 6/6, bandana cardigan 2/6). `run_tiktok_trending.py` — общемировые тренды дня (пользователю это не нужно: «мне нужно именно по нашим тегам» и «на американский рынок»).

23.09: добавлены графики на карточки радара — «Amazon · поисков в месяц» и «TikTok США · новых видео в неделю» (TikTok теперь 3 страницы, $0.073), и Instagram по нашим хэштегам (`run_instagram_tags.py`, весь мир, $0.124) — «постов в день» + ссылки. #bandanacardigan в Instagram мёртв, живёт в TikTok. Потрачено с баланса treg ≈ $0.25 из $1.

23.09 (позже): Instagram — 7-й свидетель радара (пороги 5–7/3–4/0–2). Добавлены реальные объёмы поиска Google в США (DataForSEO, $0.09 за запрос на все слова — я по ошибке запустил дважды, лишние $0.09) и продажи похожих товаров в TikTok Shop США (bandana cardigan: 30 товаров, 12 тыс. продаж, ~$58). Pinterest-поиск через treg бесполезен (только ссылки). Всего с баланса treg за день ≈ $0.47.

**How to apply:** TikTok — только по нашим хэштегам и только США. Сборы по команде. Следующие кандидаты в подключение через treg: Pinterest-поиск (для bandana cardigan), объём поиска Google по DataForSEO, Amazon. Связано с [[radar-spros-est]], [[trend-radar-bez-avtozapuska]].
