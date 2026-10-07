"""1) PDF из папки -> .txt рядом; 2) субтитры YouTube по id -> outdir/NN_id.txt
usage: yt_pdf.py pdf <dir> | yt <outdir> id1 id2 ..."""
import sys, pathlib

mode = sys.argv[1]
if mode == "pdf":
    from pypdf import PdfReader
    for p in sorted(pathlib.Path(sys.argv[2]).glob("*.pdf")):
        r = PdfReader(str(p))
        out = []
        for i, pg in enumerate(r.pages, 1):
            out.append(f"--- slide {i} ---\n" + (pg.extract_text() or ""))
        p.with_suffix(".txt").write_text("\n".join(out), encoding="utf8")
        print(p.name, len(r.pages))
else:
    from youtube_transcript_api import YouTubeTranscriptApi
    out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    api = YouTubeTranscriptApi()
    for n, vid in enumerate(sys.argv[3:], 1):
        try:
            tr = api.fetch(vid, languages=["en"])
            words, lines, cur = 0, [], []
            for s in tr:
                cur.append(s.text.replace("\n", " "))
                if len(cur) >= 12:
                    lines.append(f"[{int(s.start)//60}:{int(s.start)%60:02d}] " + " ".join(cur)); cur = []
            if cur: lines.append(" ".join(cur))
            (out / f"{n:02d}_{vid}.txt").write_text("\n".join(lines), encoding="utf8")
            print("ok", vid, sum(len(l.split()) for l in lines))
        except Exception as e:
            print("FAIL", vid, type(e).__name__, str(e)[:200])
