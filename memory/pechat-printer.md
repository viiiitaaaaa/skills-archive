---
name: pechat-printer
description: Печать по команде «распечатай» — скилл pechat, принтер RICOH SP 221SNw (подключён 07.10.2026)
metadata:
  type: reference
---
«Распечатай …» = скилл pechat: `python C:\Users\User\.claude\skills\pechat\print_file.py "<файл>"` — сразу на принтер, без открытия программ.
Основной принтер — «RICOH SP 221SNw DDST» по Wi-Fi 192.168.0.104 (порт IP_192.168.0.104); по USB не печатал. Скан — только по USB (scan.py), обработка fix_scan.py; двусторонняя — рецепт в скилле. Сеть искать в обход Happ (ping -S + arp), см. скилл. Системный по умолчанию Xprinter XP-365B — этикеточный, документы на него не слать. HP Color Laser 150 — только «в цвете».
**Why:** 07.10 попросила «чтобы я по команде могла через клод код печатать сразу».
**How to apply:** нашла файл → печатаю без вопросов; .gdoc/.docx — через PDF-версию. См. [[net-word]], [[dela-papki-ponyatno]].
