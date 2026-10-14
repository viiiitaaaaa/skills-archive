---
name: upscayl-tile-size
description: Upscayl падает с «vkQueueSubmit failed -4» — запускать с маленьким Tile Size (64), сама программа или upscayl-bin -t 64
metadata:
  type: reference
---

06.10.2026 Upscayl на её ноутбуке (Radeon Pro 555X) падал на 0% с ошибкой «vkQueueSubmit failed -4» — видеокарте не хватает памяти на кусок по умолчанию.
Рабочий запуск: `"C:\Program Files\Upscayl\resources\bin\upscayl-bin.exe" -i <файл> -o <файл>_upscayl_4x.png -m "C:/Program Files/Upscayl/resources/models" -n upscayl-standard-4x -f png -t 64`.
В самой программе: Settings → Tile Size = 64 (или 128).
06.10 настроено навсегда: localStorage `tileSize`=64 (через запуск `Upscayl.exe --remote-debugging-port=9333` и CDP). Её слова «ты к нему просто подключись» — чинить самой, не давать инструкции.
**How to apply:** если она присылает этот лог — увеличить картинку самой командой выше и подсказать настройку.
