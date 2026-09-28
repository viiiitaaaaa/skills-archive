# ffmpeg Assembly

Canvas: 1080x1920, 30fps, H.264, yuv420p. Costs no credits.

Check for a Cyrillic-capable font before drawing non-Latin captions: `fc-list | grep -i dejavu`. `DejaVuSans-Bold.ttf` covers Latin and Cyrillic.

## Fitting any source into 9:16

Generated clips already come 9:16 and need no treatment. Landscape footage — supplier videos, phone clips — needs either a blurred-fill backdrop or a crop.

Blurred fill keeps the whole frame visible:

```bash
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
     boxblur=40:4,eq=brightness=-0.12:saturation=0.8,setsar=1[bg];
[0:v]scale=1080:-1,setsar=1[fg];
[bg][fg]overlay=0:(H-h)/2:shortest=1[v]
```

Cropping fills the frame properly and reads better when the subject sits reliably in one part of the frame. For 1280x720 with a centered subject, `crop=720:720:340:0,scale=1080:1080` works — verify against sampled frames before committing.

## Ken Burns on a still

Upscale before `zoompan` or the motion stutters.

```bash
# push in over DUR seconds at 30fps
[0:v]scale=3200:3200,
     zoompan=z='min(zoom+0.0013,1.28)':d=$((DUR*30)):
     x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1080:fps=30[fg]
```

Pull back instead: `z='if(lte(on,1),1.28,max(zoom-0.0013,1.0))'`

## Captions

Font choice, treatments, placement and end cards are covered in `captions-and-type.md`; read it before drawing text. The mechanics:

Two-tier plate — headline over subline, both on translucent boxes, sitting in the lower third above the platform's own UI overlay:

```bash
drawtext=fontfile=$FONT:text='HEADLINE':fontcolor=white:fontsize=68:
  x=(w-text_w)/2:y=1520:box=1:boxcolor=black@0.45:boxborderw=22,
drawtext=fontfile=$FONT:text='subline':fontcolor=0xE8C97A:fontsize=42:
  x=(w-text_w)/2:y=1625:box=1:boxcolor=black@0.35:boxborderw=16
```

Keep captions above y=1700 — TikTok and Reels cover the bottom of the frame with their own interface.

## Transitions

Per-segment fades are simpler and more robust than `xfade` across a concat, and read as intentional on slow footage:

```bash
fade=t=in:st=0:d=0.35,fade=t=out:st=$(python3 -c "print($DUR-0.35)"):d=0.35
```

## Concatenating

Render each segment separately with identical codec, resolution and framerate, then stream-copy them together. **Paths in the concat list are relative to the list file's own directory** — a list at `seg/list.txt` referencing `seg/s1.mp4` resolves to `seg/seg/s1.mp4` and fails.

```bash
printf "file 's1.mp4'\nfile 's2.mp4'\n" > seg/list.txt
ffmpeg -f concat -safe 0 -i seg/list.txt -c copy out.mp4
```

## Layering voice-over

With one audio file per shot, place each at its shot's start offset using `adelay`, mix with `amix`, then mux against the silent video:

```bash
ffmpeg -i video.mp4 -i vo1.mp3 -i vo2.mp3 -filter_complex \
 "[1:a]adelay=0|0[a1];[2:a]adelay=5000|5000[a2];\
  [a1][a2]amix=inputs=2:normalize=0[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac out_final.mp4
```

Offsets in milliseconds. If a line overruns its shot, slow the clip rather than trimming the voice — `setpts=1.12*PTS` on a slow camera move is invisible.

Offset each line ~900ms into its shot rather than at the cut, so the image registers before the voice starts. For 5-second shots that gives 900 / 5600 / 10600 / 15600 / 20900. Add `normalize=0` to `amix` or every line drops in level as inputs are added, and `apad` so the track doesn't end early and truncate the video.

Verify the mix landed by sampling levels rather than trusting the command succeeded:

```bash
for t in 1 6 11 16 21 26; do
  ffmpeg -hide_banner -nostats -ss $t -t 1.2 -i out.mp4 -af volumedetect -f null - 2>&1 \
    | grep -o "max_volume:.*" | sed "s/^/t=$t /"
done
```

A silent window means an offset landed in a gap. Note that `-af volumedetect` needs `-hide_banner -nostats` and stderr capture; with `-v error` the measurement is suppressed and you get nothing back.

## Verifying before delivery

Sample frames across the finished cut and look at them:

```bash
for t in 2 8 14 20 26; do
  ffmpeg -y -ss $t -i out_final.mp4 -vframes 1 -vf scale=450:800 chk_$t.png
done
```

Confirm captions sit inside the safe area, no black bars crept in, and the product stays consistent between shots. Then check duration and dimensions with `ffprobe`.

Strip embedded audio from generated clips (`-an`) unless it is the voice-over — model-generated audio is unusable and only complicates the mix.
