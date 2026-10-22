---
name: rasshifrovka-dlinnyh-zapisey
description: "Расшифровка длинных видео/Zoom локально: large-v3-turbo грузит ЦП на 100% и вешает голосовой ввод пульта — брать small int8, 2 потока, приоритет Idle; кто говорит — по подписи Zoom в углу кадра"
metadata:
  node_type: memory
  type: feedback
  originSessionId: a04c6b1d-ad2b-4961-90e0-98bb1e74780c
  modified: 2026-10-22T19:51:02.790Z
---

22.10.2026: 3,5-часовой Zoom на large-v3-turbo (6 потоков, BelowNormal) занял ЦП на 100% → «завис голосовой ввод и
расшифровка» (её слова через главную вкладку). Перезапуск: модель `small` (Systran/faster-whisper-small, теперь в кэше C:),
`compute_type=int8`, `cpu_threads=2`, `beam_size=1`, `psutil IDLE_PRIORITY_CLASS`, продолжение с места по `segments.jsonl`
(clip_timestamps). ЦП 20–25%, скорость ~3–4 мин записи за 1 мин; 3,5 ч ≈ 1 ч. Качество хуже turbo — в шапке .txt
расписать частые искажения. Скрипт-образец: `komputer\proverki\` нет — лежал во временной папке (rasshifr.py).

Кто говорит в Zoom: ffmpeg `fps=1,crop=320:180:1600:0` (правый верхний угол, плашка с именем говорящего) → сравнить
кадры. Если все кадры один человек (вебинар) — подписывать его именем, вопросы из чата он читает сам.

**Why:** голос пульта — её главный ввод; тормозить его нельзя.
**How to apply:** длинная запись (>30 мин) — сразу small/2 потока/Idle; turbo — только короткие звонки или на ночь.
Связано: [[mikrofon-audacity]], [[razbory-zvonkov]].
