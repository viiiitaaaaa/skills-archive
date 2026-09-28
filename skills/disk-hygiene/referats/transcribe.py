"""Расшифровка всех видео/аудио папки локально (faster-whisper) в <out>/<путь с "\\"→"__">.txt.
python transcribe.py "<папка>" <out> [--lang ru|en] [--model large-v3-turbo|small.en] [--only <подстрока пути>]
Уже расшифрованное пропускает — можно прерывать и продолжать. Две модели одновременно не запускать (не хватит памяти)."""
import argparse, os
from faster_whisper import WhisperModel

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--lang", default="ru"); ap.add_argument("--model", default="large-v3-turbo")
ap.add_argument("--only", default="")
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
m = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=os.cpu_count() // 2 or 1)
jobs = sorted(os.path.join(r, f) for r, _, fs in os.walk(a.src) for f in fs
              if f.lower().endswith((".mp4", ".m4a", ".ogg", ".wav", ".mp3", ".opus")) and a.only in os.path.join(r, f))
for p in jobs:
    out = os.path.join(a.out, os.path.relpath(p, a.src).replace(os.sep, "__") + ".txt")
    if os.path.exists(out): continue
    seg, _ = m.transcribe(p, language=a.lang, vad_filter=True, beam_size=1)
    open(out, "w", encoding="utf-8").write(" ".join(s.text.strip() for s in seg))
    print("ok", os.path.basename(p), flush=True)
print("ВСЁ", flush=True)
