---
name: vpn-happ-dlya-menya-outline-dlya-brauzera
description: Happ нужен мне (Claude) и всегда включён; Outline — только для её браузера; Happ при включении Outline НЕ выключать
metadata:
  type: feedback
---

30.10.2026 её слова: «Мне не нужно, чтобы ты выключал Happ, когда я включаю Outline. У нас Happ работает только для тебя, а Outline у нас работает только на браузере.»

**Why:** я трижды убивала Happ ради проверки Outline — сломала ей рабочий канал. Правильно было дописать сервер Outline 169.58.0.54 в directIp Happ (сделано в happ_napryamuyu.py, IP_NAPRYAMUYU).
**How to apply:** Happ не останавливать никогда; конфликт VPN решать правилами «напрямую» в Happ; проверять сайты она просит через браузер (расширение Chrome было не подключено).

**Итог 30.10.2026:** работает схема Happ (для меня) + Shadowsocks-посредник `vpn\posrednik\Shadowsocks.exe` на 127.0.0.1:1080 (системный прокси выключен) + `vpn\Chrome_cherez_outline.bat` для её браузера. Ключ Outline вставила она сама. Опера — по её слову сделать такой же ярлык.
