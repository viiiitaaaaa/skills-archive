---
name: artlist-product-ads
description: Produce vertical (9:16) product ad videos for TikTok, Reels and Shorts from real product photos using the Artlist MCP connector — generating scene stills, animating them into clips, adding voice-over, and assembling the final cut with ffmpeg. Use this skill whenever the user wants an ad, promo, commercial, reel, TikTok video, or marketing video for a physical product, whenever they upload product photos and ask to "animate", "make a video", "turn into a reel", and whenever they mention Artlist, generating video from images, or e-commerce creatives for dropshipping or marketplace listings. Also use it when the user only asks for a video prompt or ad script for a product — the scripting and cost rules here apply before any generation starts.
---

# Artlist Product Ads

Turn real product photos into a vertical ad video. The pipeline is:

**product photo → scene stills (cheap) → animated clips (expensive) → voice-over → ffmpeg assembly**

Never skip to the end. Every stage is a checkpoint where mistakes cost 5x less to fix than at the next one.

## Non-negotiables

These come from expensive mistakes. Violate them and you burn the user's credits.

**Always pass `aspect_ratio` explicitly.** Every Artlist model defaults to 16:9. If the user wants vertical and you omit the setting, you get 16:9 and pay again. Same for `resolution` and `duration` — call `get_model_config` and set them yourself rather than trusting defaults.

**Show the price, then wait.** Before any generation, state the cost in credits. After every generation, call `get_balance` and report what's left. Do this even for cheap operations — users track their credits and being surprised by a 60-credit charge erodes trust as fast as a 2000-credit one. Never set `confirmCost: true` on your own initiative.

**Never generate a multi-scene ad from one text prompt.** A cinematic 6-scene script fed to a text-to-video model produces one shot of the first sentence and ignores the rest. This is the single most common failure. Split the script into one short prompt per scene.

**Use the user's real product as reference.** Text-to-video invents a product that isn't theirs. Always go image-to-video from a still that contains the actual item. Pass `input: { assetId }` or `input: { generationId, outputIndex }`.

**Animation prompts describe camera movement, not the product.** The still already holds the product. A long prompt re-describing it makes the model regenerate and drift. Write: "Slow push-in, warm light sliding across the surface, camera almost still." Add "the product stays exactly as in the reference image."

**No brand marks.** For accessories to branded devices (watch bands, phone cases, laptop sleeves), never show or name the brand — platforms ban it and so do marketplaces. Say "smartwatch", "blank dark screen", "no logos or brand marks anywhere" in every prompt. Describe the device generically in the script too. This extends to screen content: a lit watch face reproduces the vendor's interface design, so if the user wants the screen on, specify "plain solid white, completely blank, no icons, no numbers" and negative-prompt the interface. Never let the model invent a plausible-looking UI.

**Two failed attempts at the same defect means stop.** Image models fail at some things structurally, not because the prompt was worded badly — bead counts, strand counts, saturated color outside macro. After two honest attempts, say plainly that the model has hit its ceiling and offer the alternatives (accept it, cut the shot, use the user's real photo) instead of rolling again. A user who has watched 400 credits disappear into one shot loses confidence in the whole pipeline.

**When a clip animates wrong, change the still — not the animation prompt.** Animation prompts steer motion weakly; composition steers it strongly. A hand resting on a surface reads as anchored and will not rotate however many times you ask. Rebuild the still with the hand holding something, wrist already turned, and the motion follows for free. Three prompt rewrites cost 900 credits; one new still costs 60.

## Stage 1 — Script before pixels

Write the full script and get it approved before generating anything. A script costs nothing to rewrite; a clip costs 300.

Present it as a table: shot number, seconds, what's in frame, camera movement, on-screen caption, voice-over line. Include running total duration.

Target 20–30 seconds. Six to seven shots at 4–5 seconds each. Longer kills completion rate on short-form platforms.

**Shot 1 is the hook.** Do not open with abstract macro texture — the viewer doesn't know what's being sold and scrolls. Open with the product recognizable and something visually arresting: held up against backlight, in motion, in use. Macro detail belongs at position 2 as proof of quality.

Beautiful is not the same as legible. A wide lifestyle shot — a hand crossing a wheat field at sunrise — can be gorgeous and still fail as a hook, because the product occupies 5% of the frame and reads as a dark smudge. The hook needs the product at roughly a third of the frame height. Say this when writing the shot, and check it on the still before animating: if you can't identify the product at thumbnail size, neither can the viewer.

See `references/script-templates.md` for a proven 7-shot structure, caption formulas, and voice-over line patterns.

**Language follows the audience, not the user.** A Russian-speaking seller targeting US buyers needs English voice-over and English captions. Say this out loud if they ask for their own language — a foreign-language track tanks reach with the algorithm and the viewer. Offer a translation table for their review instead, and note that a second language version costs only the voice-over since the footage is reused.

## Stage 2 — Scene stills

Generate one still per shot at the cheapest settings. This is where the user picks and where mistakes are cheap.

Cheapest known image model: **Nano Banana 2 I2I at 512px, `modelId` 2249** — 60 credits per image. Pass the product photo as reference so materials and colors match.

Generate 1 image by default. Offer 2 variants (120 credits) only when the shot is critical or the model is likely to struggle — counting repeated elements, hands, text.

Show every result and let the user choose before moving on.

**Editing a still:** pass `input: { generationId, outputIndex }` and write a minimal prompt naming only the change plus "keep everything else identical." Re-describing the whole image makes the model regenerate it.

**Counting is the model's weak spot.** If the product has a countable structure — three rows of beads, five buttons, two straps — the model will get it wrong and repeated prompting rarely fixes it. Name each element separately ("one top strand, one middle strand, one bottom strand") rather than stating a number. If two attempts fail, stop burning credits on prompt tweaks and pass the real product photo as a second reference so the model copies the structure instead of counting.

**Saturated color survives only in macro.** In a full scene the model harmonises the product into the ambient light, so red stone goes brown, turquoise veining disappears, dyed fabric goes muddy. Asking for "vivid, saturated, crisp directional light" helps once and then stops helping. Plan around it: let the macro shot carry the true color and accept the muting elsewhere. Once a viewer has seen the material close up, they read the duller version as the same object rather than a different one. Naming a light source inside the scene — a candle beside the wrist, sun rim-lighting the beads — works better than adjectives about color.

**Edits drift.** Editing a still (removing an object, lighting a screen, deleting a strand) is the right tool and usually lands the requested change, but the model re-renders the whole frame: framing widens, fabric shifts hue, the product changes scale. Say this out loud when handing back an edit, because the user is looking at the one thing they asked for and will not notice the rest until assembly. Two edits deep, compare against the original before going a third.

## Stage 3 — Animate

Cheapest known video model: **Kling 1.6 Standard I2V, `modelId` 1007** — 300 credits for 5s at 720p, which is also its minimum resolution. Cheaper-sounding 480p models cost more.

One clip per approved still. Keep prompts to one or two sentences about motion. Slow, minimal movement reads as premium and hides model artifacts; fast movement exposes them.

Check each clip for warped hands, drifting product geometry, and melting detail — these are Kling's failure modes on fingers and small repeated shapes.

See `references/models-and-costs.md` for the full price table and model selection logic.

## Stage 4 — Voice-over

Generate **one file per shot**, not one continuous read. Separate files let you slide each line under its own clip during assembly.

Cost is roughly 7–11 credits per short line — trivial compared to video, so audition freely.

`list_voices` with `gender` filter, then present voices by name and character. Never show voice IDs. **Set `accent` explicitly** — it defaults to British. `voice_stability` runs 0 to 1; around 0.7 gives calm and even delivery, lower is livelier.

Audition one line on two voices before committing to the full set.

Reported `durationSeconds` on each result tells you the real timing — use it to finalize clip lengths. Roughly 2.2 words per second at a calm pace.

## Stage 5 — Assemble

Artlist stores results on its own CDN, which the sandbox cannot reach. **Ask the user to download the clips and voice files and upload them into the conversation.** Say this early so they aren't surprised at the end.

Assembly is ffmpeg and costs no credits. See `references/ffmpeg-assembly.md` for the working filter chains: 9:16 canvas with blurred fill, Ken Burns on stills, caption plates, fades, and audio layering. Typography decisions are their own topic — see `references/captions-and-type.md` before drawing any text.

**Never ship system-font captions.** DejaVu and Liberation are Arial clones and make a premium product look like a spreadsheet. Real typefaces are free and one curl away; the reference file has the recipe.

**Decide captions on real frames, not mockups.** Users reject the plate treatment when they see it as a flat swatch and choose it once they see it over actual footage, because a translucent plate is the only thing that stays readable across a bright window and a candlelit table. Rendering options costs nothing, so render three or four over the user's own shot and let them point.

**End cards.** Brands often have a closing frame — logo, product name, offer, CTA. Two to two and a half seconds is right: long enough for a one-line voice tag, short enough not to tank completion rate. Fade the last shot to black and the card in, and flag any offer text baked into the image, since it dates the creative the day the promotion ends.

**Leave the music track out.** Trending audio added in the platform's own editor gets materially more reach than embedded music. Deliver the cut with voice-over only and tell the user why. If they insist on music, ask them to upload an mp3 — the Artlist connector exposes generation tools, not the music library.

## Working with real footage

If the user has actual video of the product — supplier clips, phone footage — that beats anything generated, and costs nothing. Cut it in alongside the AI shots.

Watch for product mismatch: supplier demo videos often show a different colorway than the photos. Flag it rather than quietly assembling an ad where the product changes color mid-cut.

## Keeping decisions moving

This workflow asks the user for a lot of choices, and each unanswered one blocks a paid step. Some habits that keep it from stalling:

**When they answer part of a question, decide the rest and say so.** Users routinely quote a question back, or answer the second of two. Don't re-ask — make the call, state it in one line, and note that it's reversible. Re-asking reads as stalling when they've already said "just do it".

**When two options are both cheap, build both.** If one alternative already exists from an earlier generation, offering the comparison costs one generation instead of two and ends the debate faster than argument.

**Verify what you can actually see, and say what you can't.** You see the first frame of a clip, never the motion. State that plainly and tell the user exactly what to check — drifting fingers, product geometry, a screen that turns off. After assembly, sample frames across the cut and look at them; a caption that collides with the product or a black bar is invisible until you do.

**Report the balance after every generation.** Not because the rule says so, but because this workflow spends the user's money in 300-credit increments and a running total is the only thing that makes the tradeoffs discussable.

## Reference files

- `references/script-templates.md` — 7-shot structure, caption and voice-over formulas, hook patterns
- `references/models-and-costs.md` — verified model IDs, prices, settings, selection logic
- `references/ffmpeg-assembly.md` — tested filter chains for 9:16 assembly
- `references/captions-and-type.md` — fonts, caption treatments, end cards, safe areas
