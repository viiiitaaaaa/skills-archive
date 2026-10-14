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
LASKA = re.compile(r"обожаю|люблю тебя|солнышк|котик|зайк|умничк|молодец|хорош(ий|ая) мой|моя хорош|спасибо,? (мо[её]|солн)", re.I)


def make_wav():
    # мурчание = низкий шум, который «вздрагивает» ~25 раз в секунду, вдох-выдох по 1,2 с
    rate, sec = 22050, 2.6
    random.seed(7)
    frames, lp = bytearray(), 0.0
    for i in range(int(rate * sec)):
        t = i / rate
        lp += 0.04 * (random.uniform(-1, 1) - lp)          # сглаживаем шум — остаётся низкий гул
        flutter = 0.55 + 0.45 * math.sin(2 * math.pi * 25 * t) ** 2
        breath = 0.35 + 0.65 * abs(math.sin(math.pi * t / 1.3))
        fade = min(1, t / 0.15, (sec - t) / 0.3)
        v = int(max(-1, min(1, lp * 9 * flutter * breath * fade)) * 20000)
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
    subprocess.Popen(
        ["powershell", "-NoProfile", "-Command", f"(New-Object Media.SoundPlayer '{WAV}').PlaySync()"],
        creationflags=0x08000000 | 0x00000008,   # без окна, отдельно от Claude
    )


if __name__ == "__main__":
    main()
