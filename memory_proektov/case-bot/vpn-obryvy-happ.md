---
name: vpn-obryvy-happ
description: "Ошибки сети у бота (URLError, ssl handshake timeout) = обрывы самого туннеля Happ (адаптер happ-xray), 3–19 раз в день; счётчик komputer\\proverki\\vpn_obryvy.py"
metadata:
  node_type: memory
  type: project
  originSessionId: ce2476cd-94b0-4cdd-9675-4eca39ac4efa
  modified: 2026-10-20T21:08:23.607Z
---

Разобрано 20.10.2026. Весь интернет ПК идёт через туннель Happ (xray, адаптер `happ-xray`). Он сам пропадает на ~1 с несколько раз в день — в этот миг рвутся ВСЕ соединения (бот, Google Диск G:, запросы Claude). За неделю 14–20.10 — 60 обрывов.

- Не Wi-Fi: «STESHA» рвётся только ~04–05 утра (похоже, ночная перезагрузка роутера).
- Не обновление подписки «Обходы4» (оно в xx:36 каждый час, обрывы в другое время).
- След в логе `C:\ProgramData\Happ\logs\happd.log`: `[push] MCS socket ... RemoteHostClosedError` и через 2 с `[WFP] Created 21 filters`; в журнале Windows NetworkProfile/Operational событие 10001 «Сеть отключена» с именем happ-xray.
- В боте уже стоят повторы отправки (коммит e074a62) — переживает обрыв.

**Why:** «бот тупит» и сорванные запросы — из-за этого, а не из-за кода.
**How to apply:** на «сколько обрывов VPN» — `python C:\Users\User\komputer\proverki\vpn_obryvy.py 7`. Решение за ней: сменить сервер в Happ (8 серверов в подписке), не помогло — режим «системный прокси» вместо TUN. Пункт в её «Моих делах».
