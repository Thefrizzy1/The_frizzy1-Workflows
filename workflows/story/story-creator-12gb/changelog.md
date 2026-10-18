# Changelog — Story Creator · 12 GB

## v1.4.0 — 2026-10-18
- **Script-first.** The scene list is now a script with tags: a `WORLD:` first line (the look of the whole story),
  `[camera]` at the start of a line (shot + movement, into the picture and the video prompt), `|| Name: text` for
  dialogue on screen, `|| text` for the narrator, and `[continue]` for a transition into the next scene (the clip ends
  on the next scene's still) instead of a cut. The *One shot* mode is gone; `[continue]` replaces it per line.
- Stills come straight from each script line ("direct"), with the character picture only for how the hero looks.
- The built-in writer (*Write the scenes for me*, 8B Qwen text encoder) stays in, switched off; the guide recommends a
  big chatbot with the structure prompt in [HOW_TO_WRITE_A_SCRIPT.md](HOW_TO_WRITE_A_SCRIPT.md).
- From v1.2/v1.3 (not released on their own): one narrator voice for the whole story, scene length from the spoken
  line (3-9 s), narrator scenes made without voices, dialogue made louder, the hiss above 4-6 kHz in the scene sound
  turned down, each scene's voice saved on its own, upscale to 1080p, Music off = no YuE2.

## v1.1.0 — 2026-10-15
- **The narrator is separated from the characters' voices.** After `||`, a line that starts with a name and a colon
  (`Pip: …`) is dialogue: the character says it on screen. Anything else is the narrator: the scene is told that nobody
  talks and all mouths stay closed, the narrator line is made in its own small H3 pass (256×160, only its sound is used)
  and laid on top, with the scene's own sound 8 dB under it.
- Test on the RTX 3060 (6 scenes: 3 narrator, 3 dialogue): 23 min 48 s. The narrator pass took 31–36 s per narrator
  line. Whisper heard all 6 lines exactly.
- How to use: tips for side characters, per-scene loudness, and a chatbot prompt for the scene list (in the README).

## v1.0.0 — 2026-10-15
- First version (in `source/`): scene list → Qwen Image 2.1 Turbo stills (one character picture, every still an edit
  of it) → MiniMax H3 image to video with sound (the narrator line in the scene prompt) → YuE2 music → the joined story.
  Modes: *Scenes* and *One shot*.
