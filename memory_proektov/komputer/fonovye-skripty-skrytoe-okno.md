---
name: fonovye-skripty-skrytoe-okno
description: Фоновые скрипты (Планировщик, pythonw) вызывают консольные программы только с creationflags=subprocess.CREATE_NO_WINDOW — иначе мигают окна PowerShell
metadata:
  type: feedback
---

26.10.2026 её жалоба: «постоянно открывается и перезапускается PowerShell, окно горит и мешает работать». Причина — `proverki\vpn_sledim.py` (pythonw, каждые 30 с) вызывал powershell и python без скрытия окна.
**Why:** без флага каждый вызов subprocess из фонового скрипта открывает видимое окно консоли.
**How to apply:** в любом фоновом/плановом скрипте каждый `subprocess.run/Popen` — с `creationflags=subprocess.CREATE_NO_WINDOW`. Исправлены: vpn_sledim, happ_snimok, itog_dnya, pakety_proverka, vpn_obryvy; raspisanie\ уже было с флагом. Ручные proverit_komandu и proverka_koda не трогали.
