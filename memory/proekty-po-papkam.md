---
name: proekty-po-papkam
description: 14.10.2026 память разложена по папкам проектов Claude Code; таблица папок — в глобальном CLAUDE.md
metadata:
  type: project
---

14.10.2026 по её просьбе «перенести на ПК-версию и разложить по проектам» (выбрала папки Claude Code,
не Проекты чата). Работа идёт в Claude Desktop → вкладка Code → открыть папку проекта.

Её 10 веток (уточнила 14.10): 1688+поставщики, тренд-радар, новости, книги, лидогенерация, сайт Смарт Люкс (lead-enginesite, память общая с lead-engine — один git), вакансии/резюме/питч (C:SERSSEREZYUME-VAKANSII � файлы п��р��н��с��ны из KNIGI_KUPLENO, скилл VAKANSII-SSHA поправл��н), SHOPIFY (DECOR-STORE-OPS, уж�� в CLAUDE DESKTOP), бот Д��ла, скиллы+компьют��р (домашняя).
Сд��лано: память скопирована (н�� п��р��н��с��на) в папки: CJ, FASHION-TREND-RADAR, TG_MONITOR,
lead-engine, knigi_kupleno, decor-store-ops, case-bot. В каждой есть короткий CLAUDE.md (кроме decor-store-ops, где
он уже был → AGENTS.md). Общие правила и таблица «тема → папка» — в ~/.claude/CLAUDE.md.
Копии до правок: MEMORY.backup-2026-10-14.md.bak, CLAUDE.backup-2026-10-14.md.bak.

**Why:** одна куча из 138 заметок в домашней папке; в проекте нужно помнить только своё.
**How to apply:** новое по проекту записывать в память папки проекта. Google Диск в раскладку не включать
(её слово «зачем нам сейчас гугл диск»): «Дела» ведём из case-bot. Русские пути Claude Code превращает в чёрточки,
и память таких папок может смешиваться. Копии в проектах могут расходиться с домашней памятью — главная копия в проекте.

14.10 вечер: в Claude Desktop → Code → **Projects (Beta)** она создала проекты по веткам. В поле Context — НЕ папки
(лимит 1000 файлов, а в радаре один .venv на 14 тыс. и .env с ключами), а копии файлов правил из
`Desktop\Файлы для проектов Claude\<Проект>.md`. После правки CLAUDE.md какого-то проекта — положить туда новую копию и сказать ей.

14.10: все ветки на GitHub (закрытые): sourcing-1688 (cj), fashion-trend-radar, tg-monitor, knigi-kupleno, rezyume-vakansii
+ раньше lead-engine, case-bot, decor-store-ops, skills-archive. В .gitignore каждой: .env, *token*.json, *_keys.json,
картинки, PDF, тексты книг, fakty_o_ney.md. Создание репо/первый push авто-режим блокирует — давать ей команду с «!».

Хвосты на 14.10 (ночь): в lead-engine не закоммичены site/CLAUDE.md и чужие правки site/* (DESIGN.md, qa_site.py…) —
коммитить только по её слову; Context проекта «Тренд-радар» — проверить, не попал ли .env (если она жала «first 1000 files»).
Файл «Скиллы и компьютер.md» и «Что мы умеем и знаем.md» тоже в Desktop\Файлы для проектов Claude (каталог обновляется сам
при katalog.py). Вакансии/резюме/питч переехали в C:\Users\User\rezyume-vakansii.
