# disk-hygiene — порядок на дисках

Скилл Claude Code (см. `SKILL.md`) и скрипты для трёх работ:

1. **Разбор папок по темам** — `scripts/sort_by_rules.py` (правила «шаблон имени → папка» в JSON, образец `scripts/rules.example.json`; личные правила `rules.local.json` в git не хранятся).
2. **Полные рефераты вместо учебных исходников** — `referats/`: извлечение текста (`extract_text.py`), расшифровка видео/аудио (`transcribe.py`, faster-whisper), список «файл → тема» (`manifest_template.py`), инструкция помощникам (`BRIEF.md`), перевод в Word (`md2docx.py`), финал с удалением исходников (`finalize.py`).
3. **Место на C: и в Google Диске** — `scripts/scan_disk.ps1` + `report.py` (WizTree → отчёт), `scripts/clean.ps1` (кэши и старые версии, проверка нужных ревизий playwright), `scripts/drive_sync_roots.py` (что реально синхронизирует Google Drive), `scripts/compare_dirs.py` (что есть только в одном месте).

Все скрипты по умолчанию работают вхолостую; удаление — только с `-Apply` / `--apply`.

Требуется: Python 3 (`pypdf`, `lxml`, `python-docx`, `openpyxl`, `faster-whisper`, `pypdfium2`, `Pillow`), WizTree, PowerShell 5.1.
