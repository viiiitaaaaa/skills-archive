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
**How to apply:** если она снова попросит Gemini на ПК, сначала проверить страну аккаунта (policies.google.com/terms → «Версия для страны»). Другие пути: другой аккаунт (она и её аккаунт не в России — не предполагать РФ) или API-ключ AI Studio. Связано: [[hermes-legkie-zadachi]], [[ollama-ustanovlen]].

15.10.2026: у неё ПЛАТНАЯ подписка Google AI Pro (купила сама — не называть Gemini «бесплатным»). Подписка работает в
приложении/сайте Gemini и в NotebookLM, но не в программах на ПК: Gemini CLI для личных Pro отключён, а ключ из AI Studio —
отдельный бесплатный уровень API, подписка его лимиты не поднимает (поэтому «Usage limit reached for gemini-3.8-flash»).

15.10.2026 новый ключ (её аккаунт с Pro) — в переменной Windows GEMINI_API_KEY (User), в чат/файлы не печатать.
Проверка `scratchpad/gemini_modeli.py` (список моделей + один вопрос «2+2»): по ключу 46 текстовых моделей.
Отвечают (бесплатный уровень): gemini-3.8-flash, gemini-3.5-flash-lite, gemini-flash-lite-latest, gemini-flash-latest.
НЕ отвечают: gemini-2.5-flash — 404 «больше не доступна новым пользователям»; gemini-pro-latest и gemini-3.1-pro-preview —
429 «превышена квота» (у Pro-моделей бесплатной квоты нет, нужна оплата API). Подписка Pro лимиты ключа не поднимает.
Лимиты в день Google официально не показывает; по форуму: flash ≈ 20 запросов/день, flash-lite ≈ 500/день; смотреть ai.dev/rate-limit.
Для объёмной работы брать flash-lite.

15.10.2026 (позже): в ~/.gemini/settings.json поставлена модель по умолчанию gemini-flash-lite-latest (копия settings.json.bak_model);
проверено `gemini --skip-trust -p` — отвечает. Памятка ей: komputer\gemini\pamyatka.html. Официально (gemini.google/subscriptions):
Pro даёт лимиты в Antigravity, AI Studio/API — отдельно, больше только платно. Снова открыто окно agy для входа по подписке.
Картинки по ключу (15.10.2026, она выбрала цель «картинки»): все 4 модели картинок (gemini-3.1-flash-image, nano-banana-2.1,
2.5-flash-image, 3.1-flash-lite-image) — 429 «превышена квота»: бесплатных картинок по API нет, нужна оплата API.
Картинки по её подписке Pro — только на сайте/в приложении Gemini руками. Для картинок у нас есть ComfyUI Cloud (скиллы product-scenes, site-mockups).

15.10.2026 вечер: в agy первый аккаунт снова «недоступно в вашей стране». Она входит ВТОРЫМ аккаунтом (зарегистрирован на её реальный
адрес). Выход/вход в окне agy: `/logout`, потом `/login` (подкоманды logout у agy.exe нет). Грабли: браузер кидает на
accounts.google.ru — с её ПК он не открывается (ERR_CONNECTION_CLOSED), а accounts.google.com открывается: в адресе менять .ru → .com.
Окно agy даёт ссылку и поле «paste the authorization code» (redirect antigravity.google/oauth-callback) — код со страницы вставить в окно.
НЕ доделано: вход вторым аккаунтом (и есть ли на нём подписка Pro — иначе agy на бесплатных лимитах); её решение, подключать ли
Gemini помощником вкладок Claude (правило не записано).
