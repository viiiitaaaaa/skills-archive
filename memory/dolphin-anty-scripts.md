---
name: dolphin-anty-scripts
description: "Скрипты автоматизации Dolphin{anty} в C:\\Users\\User\\dolphin_anty и скилл dolphin-shots — использовать их, а не писать заново"
metadata: 
  node_type: memory
  type: project
  originSessionId: 5df6ff22-d3e4-4c08-b1ec-2bfd75f562af
  modified: 2026-08-16T19:53:55.258Z
---

Автоматизация антидетект-браузера Dolphin{anty} живёт в `C:\Users\User\dolphin_anty\`
(`dolphin.py` — Local API клиент, `shots.py` — полностраничные скрины магазина AliExpress,
`probe_pagination.py` — разведка DOM). Подробности, команды и грабли — в скилле
`dolphin-shots` (`C:\Users\User\.claude\skills\dolphin-shots\SKILL.md`).

Пользователь просил (16.08.2026) обязательно сохранить эти скрипты и продолжить работу
с ними дальше — при новых задачах по Dolphin/AliExpress сначала открывай скилл и
переиспользуй готовое, а не пиши с нуля.

Идёт пакетная задача (начата 16.08.2026): снять по 4 страницы с каждого магазина из
`C:\Users\User\Desktop\сайты али.txt` (59 уникальных ссылок). Прогресс — в
`C:\Users\User\dolphin_anty\state.json`, продолжение после любого перерыва или сброса
лимитов: `python batch.py --profile 828976678`. Проверить, где остановились:
`python batch.py --status`.

Ключевое, что уже выяснено на практике: план Dolphin был платным (automation работала), но 12.09.2026 Local API снова отвечает 402 «On free plan you can't use automation» — подписка слетела, перед автоматизацией проверять/продлевать план; при платном плане
`automation=true` работает; профиль по умолчанию `828976678` (с не-российским прокси);
скрины страниц 1-4 магазина складываются в `C:\Users\User\Desktop\скрины магазина\`.
