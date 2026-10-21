---
name: son-noutbuka-i-bat
description: Сон ноутбука (21.10.2026) — что держало без сна, что настроено, и что .bat с русскими буквами ломается
metadata:
  type: project
---
21.10.2026: ноутбук не засыпал ночью из-за открытых аудиопотоков (Apple Audio Device, VB-Audio Virtual Cable), а через 31 с после закрытия крышки его будила зарядка.
С её «да» включено: `C:\Users\User\pult\son_nastroyka.bat` (от администратора) — зарядка не будит, эти два звуковых драйвера не мешают сну. Отмена: `son_nastroyka.bat otmena`.
ne_spat.py теперь пишет журнал `C:\Users\User\pult\ne_spat.log`.

**Why:** .bat с кириллицей (UTF-8) cmd режет на куски («'ока' is not recognized»).
**How to apply:** .bat — только ASCII, русский текст и имена устройств — в .ps1 с BOM, который .bat вызывает. Связано: [[razresheniya-ne-sprashivat]].
