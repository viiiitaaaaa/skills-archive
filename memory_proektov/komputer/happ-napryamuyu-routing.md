---
name: happ-napryamuyu-routing
description: "Сайт «напрямую мимо VPN» — дописать в komputer\\proverki\\napryamuyu.txt; Happ берёт правило из routing.json сразу, сторож раз в час возвращает после обновления подписки"
metadata:
  node_type: memory
  type: project
  originSessionId: d1c314d1-1a5d-480b-b7fe-7e6252d6ce98
  modified: 2026-10-21T22:18:06.011Z
---

22.10.2026 нашла рабочий путь без её рук: `%LOCALAPPDATA%\Happ\routing.json`, профиль «1688» (выбран у подписки),
список `directSites` — Happ подхватывает правку файла СРАЗУ, без перезапуска (config.json — бесполезен, routing.json — работает).
Проверка «напрямую»: `Get-NetTCPConnection` — у xray связь с адреса Wi-Fi 192.168.0.102 к IP сайта = мимо VPN.

- Список сайтов — `komputer\proverki\napryamuyu.txt`; скрипт `happ_napryamuyu.py` (`--test` — только проверить),
  задача Планировщика «Happ напрямую» каждый час (подписка «Обходы4» обновляется каждые 6 ч — её слово).
  Журнал — `proverki\otchety\happ_napryamuyu.log`. Копия до правки — `Happ\routing.backup-20261022.json`.
- Напрямую ПК выходит с российского адреса (Prolink, Видное), через VPN — Лондон.
- **22.10 её «да»: ВСЕ .ru и .рф напрямую** (строки `ru` и `xn--p1ai` в napryamuyu.txt; проверено: ya.ru, mos.ru, .рф — напрямую, github/wikipedia — через VPN). kremlin.ru/президент.рф закрыты сами (таймаут и у российских узлов check-host).
- Подписка сама уже пускала многие .ru напрямую (lenta.ru, rbc.ru шли мимо VPN до нас) — видимо, по geoip:ru.
- mosoblsud.ru мёртв для всех (DNS суда отказывает даже российским узлам check-host, 22.10). Настоящий сайт
  Мособлсуда — **oblsud.mo.sudrf.ru** (oblsud--mo.sudrf.ru), поиск дел с кодом-картинкой; sudrf.ru добавлен напрямую.

**Why:** её просьба 22.10 «пустить без VPN» (суды, почта, СМИ) и «учесть, что подписка обновляется каждые 6 часов».
**How to apply:** новый сайт не пускает с VPN — дописать строку в napryamuyu.txt и запустить скрипт; не перезаписывать
routing.json целиком. См. [[happ-napryamuyu-bez-vpn]] (старая память в домашней папке, способ с импортом сервера).
