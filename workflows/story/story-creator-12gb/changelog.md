# Changelog — Story Creator · 12 GB

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
