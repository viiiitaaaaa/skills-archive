# Captions and Type

Captions carry the sales argument on their own — most short-form viewing starts muted. Treat them as a design task, not a text overlay.

## Get real fonts first

The sandbox ships DejaVu and Liberation. Both are Arial/Times clones and read as cheap on a premium product; users notice immediately even when they can't name why.

`raw.githubusercontent.com` is reachable, and Google's font repo lives there:

```bash
base=https://raw.githubusercontent.com/google/fonts/main/ofl
curl -sLo Jost.ttf     "$base/jost/Jost%5Bwght%5D.ttf"
curl -sLo Playfair.ttf "$base/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"
curl -sLo Bebas.ttf    "$base/bebasneue/BebasNeue-Regular.ttf"
```

Most are **variable** fonts. `drawtext` renders the default instance, which is usually Regular and looks limp at caption size. Pin a weight first:

```python
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.ttLib import TTFont
instantiateVariableFont(TTFont('Playfair.ttf'), {'wght': 600}).save('Playfair-SemiBold.ttf')
```

`pip install fonttools --break-system-packages` if it isn't there.

Say "free" carefully. Users hear it as "cheap default". The distinction that lands: Liberation is a *system clone*; Playfair and Jost are professional typefaces that happen to be openly licensed, and are used by real jewellery and fashion brands.

## Choosing a pairing

| Face | Character | Fits |
|---|---|---|
| Playfair Display | High-contrast serif | Jewellery, craft, heritage |
| Cormorant | Lighter, more delicate serif | Very premium, small runs |
| Jost | Geometric sans, narrow | Modern, clean; good sublines |
| Montserrat | Wide geometric sans | Safe, ubiquitous, a bit anonymous |
| Bebas Neue | Condensed caps | Fits long lines; reads as promo |
| Oswald | Narrow sans | Sport, urgency, discounting |

A serif headline over a sans subline is the reliable pairing for craft goods. Bebas and Oswald pull toward fitness and clearance — fine for a discount push, wrong for stone jewellery.

## Present options as rendered frames

Don't describe typefaces. Render each candidate over the user's actual footage at full frame, save as JPEG, and hand over the files so they can look on a phone. It costs nothing and ends the discussion in one round instead of four.

Flat-color mockups mislead badly. A treatment that looks heavy on a swatch is often the only readable option over real footage.

## Two treatments that work

**Plate** — white bold caps on a translucent dark box, gold subline on a lighter box beneath. Survives any background. This is what users pick once they see it in situ.

```
drawtext=fontfile=$HEAD:textfile=h.txt:fontcolor=white:fontsize=66:
  x=(w-text_w)/2:y=1500:box=1:boxcolor=black@0.45:boxborderw=22,
drawtext=fontfile=$SUB:textfile=s.txt:fontcolor=0xE8C97A:fontsize=40:
  x=(w-text_w)/2:y=1612:box=1:boxcolor=black@0.35:boxborderw=16
```

**Floating caps with a rule** — letterspaced caps, no box, a short em-dash rule beneath. Prettier, but fails over bright backgrounds. If you use it, add a top scrim: a 1080×700 RGBA gradient PNG from ~40% black to transparent, overlaid before the text. `drawtext` has no letter-spacing option — insert spaces between characters by hand.

Use `textfile=` rather than inline `text=`. It sidesteps every escaping problem, apostrophes included.

## Placement

Keep captions out of the platform's furniture: the bottom ~200px and the right ~15% are covered by the interface. The lower third above y≈1700 is the default home.

Put the caption where the product isn't. On a closing hero shot with the product low in frame, the slogan belongs at the top — ask, or just move it and show the result.

Two short lines beat one long line on a phone: the same words at roughly 1.5× the size, and no collision with the right-hand button column.

## Sublines

Two-tier captions need a second line per shot, so write them during the script stage rather than inventing them at assembly:

| Headline | Subline |
|---|---|
| NOT A WATCH BAND | handmade stone jewelry |
| NO TWO ARE ALIKE | real imperial jasper |
| ANY PLACE, ANY STYLE | linen, tailoring, denim |
| STYLE THAT'S EASY | no clasp, no fuss |

The subline is where objection-handling goes when no shot demonstrates it.

## End cards

The user supplies the card as an image. Fit it and hold:

```bash
ffmpeg -loop 1 -i endcard.png -t 2.2 \
 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,\
pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,fps=30,setsar=1,fade=t=in:st=0:d=0.45" \
 -c:v libx264 -crf 18 -pix_fmt yuv420p -r 30 s6.mp4
```

The preceding shot's fade-out to black makes the join invisible. A one-line brand tag ("It's <brand>") costs 2 credits and lands at about 1.2s — delay it ~600ms into the card so it doesn't clip the fade.

Read the card critically before shipping: baked-in offers date the creative, and small light text on a two-second card is unreadable on a phone. Say so; you can't reflow a flattened image.

## Practical snags

**Signed Artlist URLs sometimes fail to download** for the user. Regenerating a short voice line is 2 credits and produces a fresh link — cheaper than debugging. The account's generation history also works.

**`/mnt/user-data/uploads` throws transient `Input/output error`.** Retry the copy two or three times with a short sleep before concluding a file is missing.

**Output files may be undeletable** for the same reason. If a superseded render can't be removed, give the final file a distinct name and tell the user which one is current.
