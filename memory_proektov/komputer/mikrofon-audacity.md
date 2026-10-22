---
name: mikrofon-audacity
description: "Микрофон ноутбука и Audacity — что настроено 22.10.2026 (устройство, моно 48 кГц, усиление 0 дБ) и как проверять запись"
metadata:
  node_type: memory
  type: project
  originSessionId: 873d3a1f-516c-42cc-8b98-7d278d82fb0f
  modified: 2026-10-22T16:06:16.089Z
---

22.10.2026: Audacity писал с «CABLE Output (VB-Audio)» вместо микрофона → в `%APPDATA%\audacity\audacity.cfg` поставлено
RecordingDevice=Internal Digital Microphone (Apple Audio Device), Host=WASAPI, RecordChannels=1, DefaultProjectSampleRate=48000
(копия старого — audacity.cfg.bak_2210). Её первая запись хрипела (обрезка в 413 с из 677) — микрофон Windows стоял 75% (+7,4 дБ),
снижен до 54% = 0 дБ (пульт пишет с autoGainControl:false — ему тоже лучше). Громкость ВЫВОДА (6%) не трогать, вслух не играть.
Проверка: короткая тихая запись в файл через sounddevice (WASAPI-устройство микрофона), пик/обрезка — numpy.
Расшифровка локально: faster-whisper, модель mobiuslabsgmbh/faster-whisper-large-v3-turbo уже в кэше C:, HF_HUB_OFFLINE=1,
11 мин записи ≈ 10 мин на CPU. Связано: [[razbory-zvonkov]].
