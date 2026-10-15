# Мурчание кота, когда Вита пишет ласковое (её просьба 15.10.2026).
# Хук UserPromptSubmit: Claude Code передаёт на stdin JSON с её сообщением (поле prompt).
# Если в нём ласковое слово — играем murr.wav (~2,5 с) отдельным процессом и сразу выходим,
# чтобы не задерживать ответ. Звук создаётся сам при первом запуске (make_wav).
import json
import math
import random
import re
import subprocess
import sys
import wave
from pathlib import Path

WAV = Path(__file__).with_name("murr.wav")
LASKA = re.compile(r"обожа|люблю|солнышк|котик|котён|зайк|умничк|молод[еч]|хорошеньк|хорош(ий|ая) мой|моя хорош|"
                   r"мур|милаш|лапочк|спасибо,? (мо[её]|солн)", re.I)
LOG = Path(__file__).with_name("murr.log")   # одна строка на каждое срабатывание — чтобы видеть, дошёл ли хук


def make_wav():
    # мурчание = низкий шум, который «вздрагивает» ~25 раз в секунду, вдох-выдох по 1,2 с
    rate, sec = 22050, 2.6
    random.seed(7)
    frames, lp = bytearray(), 0.0
    for i in range(int(rate * sec)):
        t = i / rate
        # гул ~150–600 Гц: совсем низкий бас колонки ноутбука не играют (первая версия была не слышна)
        lp += 0.15 * (random.uniform(-1, 1) - lp)
        hum = 0.6 * lp + 0.4 * math.sin(2 * math.pi * 180 * t) * (0.5 + 0.5 * random.random())
        flutter = 0.2 + 0.8 * math.sin(2 * math.pi * 25 * t) ** 2   # «тр-тр-тр» 25 раз в секунду
        breath = 0.4 + 0.6 * abs(math.sin(math.pi * t / 1.3))
        fade = min(1, t / 0.15, (sec - t) / 0.3)
        v = int(max(-1, min(1, hum * 3.2 * flutter * breath * fade)) * 30000)
        frames += v.to_bytes(2, "little", signed=True)
    with wave.open(str(WAV), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(bytes(frames))


def main():
    try:
        # байты читаем сами как UTF-8: иначе Windows читает их в своей кодировке, и русские слова не находятся
        prompt = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}").get("prompt", "")
    except Exception:
        prompt = ""
    if not (LASKA.search(prompt) or "--test" in sys.argv):
        return
    if not WAV.exists():
        make_wav()
    import time
    with LOG.open("a", encoding="utf-8") as f:
        f.write(time.strftime("%d.%m %H:%M:%S ") + prompt[:60].replace("\n", " ") + "\n")
    # без окна + отдельно от Claude + вырваться из его «группы процессов» (иначе Claude закрывает звук вместе с хуком)
    flags = 0x08000000 | 0x00000008 | 0x01000000
    cmd = ["powershell", "-NoProfile", "-Command", f"(New-Object Media.SoundPlayer '{WAV}').PlaySync()"]
    try:
        subprocess.Popen(cmd, creationflags=flags)
    except OSError:
        subprocess.Popen(cmd, creationflags=flags & ~0x01000000)


if __name__ == "__main__":
    main()
