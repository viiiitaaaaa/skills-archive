---
name: rasshifrovka-kurs5
description: "Локальная расшифровка курса 5 (D:\\rehcs\\extracted\\5) — где скрипт, как продолжить; 22.10 диск D: отвалился"
metadata:
  node_type: memory
  type: project
  originSessionId: abdaa5c4-f3b0-4f18-af94-39e6d4c0d9ad
  modified: 2026-10-22T16:07:01.328Z
---

Расшифровка 45 видео курса 5 — локально faster-whisper (`D:\whisper\rasshifrovka.py <папка>`, модель small int8 в
`D:\whisper\models`, ждёт свободную память ≥2,5 ГБ, готовые .txt пропускает). 22.10.2026 вечером диск D: (внешний USB,
сбоит — дело 7480c38f) пропал из системы — расшифровка встала примерно на 17–20 из 45.

**Why:** она просила «без траты лимитов»; диск D: ненадёжен.
**How to apply:** когда она переподключит D: — проверить `_rasshifrovka.log`, запустить заново той же командой
(PowerShell, Hidden, BelowNormal, TEMP/HF_HOME на D:) и сразу поставить на табло [[fonovye-zadachi-na-tablo]].
Дело в «Моих делах» 55980e71 закрыть, когда 45 из 45.
