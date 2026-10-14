---
name: gemini-cli-otklyuchen-antigravity
description: "Gemini CLI не работает с личной подпиской Pro (отключён Google 18.06.2026); Antigravity CLI (agy) стоит, но аккаунт gokjhfrr «не в той стране»"
metadata:
  node_type: memory
  type: project
  originSessionId: be8f14ae-faa8-43be-bddf-9cde7303a9f5
  modified: 2026-10-14T17:17:41.317Z
---

14.10.2026: пытались подключить Gemini (Pro) к компьютеру для пересказов (Hermes).
- Gemini CLI 0.64 (OAuth) → «IneligibleTierError: client no longer supported… migrate to Antigravity». Google отключил Gemini CLI для Pro/Ultra/free личных аккаунтов 18.06.2026. Переустановка и другой аккаунт не помогут.
- Поставлен Antigravity CLI `agy` 1.3.5: `%LOCALAPPDATA%\agy\bin\agy.exe`, данные в `~\.gemini\antigravity-cli`. Вход gokjhfrr@gmail.com (аккаунт с Pro) прошёл, но «not eligible… not available in your location». IP при этом был DE (DigitalOcean), то есть страна берётся из привязки аккаунта.
- Грабли входа: в режиме `-p` agy ждёт код ровно 60 с и читает его только с клавиатуры (из pipe не берёт). Входить нужно в обычном окне `agy`, там вход через браузер проходит сам.
- Для старого Gemini CLI вход без localhost работает через redirect codeassist.google.com/authcode (скрипт делался в scratchpad), но толку нет, клиент отключён.

**Why:** чтобы не повторять 2 часа попыток входа.
**How to apply:** если она снова попросит Gemini на ПК, сначала проверить страну аккаунта (policies.google.com/terms → «Версия для страны»). Другие пути: другой аккаунт с не-РФ страной или API-ключ AI Studio. Связано: [[hermes-legkie-zadachi]], [[ollama-ustanovlen]].
