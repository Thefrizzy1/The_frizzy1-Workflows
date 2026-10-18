# The_frizzy1 — Story Creator · 12 GB v1.4.0
> A script → a whole story video: the same character in every scene, every scene moving, characters talking on screen,
> a narrator, music. The "long AI story video" trend, run on your own PC. Qwen Image 2.1 Turbo makes the stills,
> MiniMax H3 turns each one into a moving scene with sound, YuE2 makes the song. Core ComfyUI nodes only, tested on an
> RTX 3060.

| | |
|---|---|
| **Model families** | Qwen Image 2.1 (stills) · MiniMax H3 (video + sound) · YuE2 (music) |
| **Task** | Story video from a script: `WORLD:` line, `[camera]` tags, dialogue, narrator, cuts or `[continue]` transitions |
| **Workflow file** | `The_frizzy1_story-creator-12gb_v1.4.0.json` (older versions in `source/`) |
| **Needs** | 12 GB VRAM · 32 GB system RAM · ComfyUI **0.39+** |
| **Tested on** | RTX 3060 12 GB · Ryzen 5 5600X · 32 GB DDR4 · ComfyUI 0.39.2 |
| **License** | Workflow: MIT · Qwen Image 2.1: Qwen Research License (non-commercial) · MiniMax H3: MiniMax H3 Community License · YuE2: CC-BY-NC-4.0 (non-commercial) |

## Quick start
1. Update ComfyUI to **0.39 or newer** (Start Loop / End Loop, MiniMax H3, YuE2; no custom nodes).
2. Download the files in [downloads.md](downloads.md) (9 files: 3 for the stills, 5 for the video, 1 for the music).
3. **Write the script with a big chatbot**: paste the prompt from [HOW_TO_WRITE_A_SCRIPT.md](HOW_TO_WRITE_A_SCRIPT.md)
   into ChatGPT, Claude or Gemini with your idea.
4. Load `The_frizzy1_story-creator-12gb_v1.4.0.json`, paste the script into **Script**, set the **Style** and describe
   your **Character** (or switch on *Use my own character picture* and un-bypass the loader). **Run**.

## The script format
```
WORLD: A snowy northern land in winter, soft blue and pink light, cozy and magical
[wide, slow push-in] Inside a cozy den by the fire: Pip, a small orange fox in a knitted blue scarf, sits next to Grandpa, an old grey fox with a walking stick || In a den under a snowy hill lived a little fox named Pip.
[medium shot] Inside the cozy den: Pip, the small orange fox in the blue scarf, jumps up and points at a painting of green lights on the wall || Pip: Grandpa, are the northern lights real?
[continue] [wide shot] Morning outside the round wooden door of the den: Pip waves goodbye, holding a small wooden compass || So the next morning, Pip set off with the compass.
```

| Tag | What it does |
|---|---|
| `WORLD:` | The look of the whole story, in front of every scene (first line, optional). |
| `[camera]` | Shot and camera movement, into the picture and the video prompt. |
| `what we see` | The scene: place, every character with their full look, objects, the action from start to end. |
| `\|\| text` | The narrator says it (one voice for the whole story, off screen). |
| `\|\| Name: text` | That character says it on screen. |
| `[continue]` | A transition instead of a cut: the clip ends on the next scene's picture. |

Scene length is automatic (3-9 s, from how much is said). The rules that make the pictures match the words, a
before/after and the chatbot prompt: [HOW_TO_WRITE_A_SCRIPT.md](HOW_TO_WRITE_A_SCRIPT.md). A full 58-line (about
5 minutes) example: [samples/example_script_5min.txt](samples/example_script_5min.txt).

**Why a big chatbot and not the built-in writer:** *Write the scenes for me* (the 8B Qwen text encoder writes the list
from a story idea) is still in the workflow, but switched off. In the tests its lines were short and vague and it
dropped how side characters look (a white rabbit became a second fox). A detailed hand-written script got 10 of 12
scene stills right on the first try.

## Preview

<p align="center"><img src="samples/sample-1.webp" width="70%" alt="Four scenes of a test story"></p>
<p align="center">
<img src="samples/sample-3.webp" width="48%" alt="The character picture and three scene stills: the same fox">
</p>

<sub>Top: a test story (v1.1). Bottom: one character picture, then every still is an edit of it, so it stays the same
fox. RTX 3060.</sub>

## How it works
1. **Music first** (if on): YuE2 makes a song from the *Music style* + *lyrics*; every scene later gets its own slice.
2. **Story world**: the `WORLD:` line (or, without one, the 8B writer makes it from the scenes).
3. **Stills**: Qwen Image 2.1 Turbo makes one character picture, then every scene's still as an edit of it
   (`<Picture 1>`), from the scene's own line.
4. **Scenes**: a Start Loop / End Loop goes through the stills; MiniMax H3 (8-step turbo LoRA) turns each one into a
   clip with sound, as long as its line needs. Dialogue lines go into the scene; narrator lines get their own small H3
   pass (only its sound is used, one narrator voice for the whole story), laid on top of a scene made without voices.
   A `[continue]` line uses the next still as the clip's last frame.
5. Each scene and its voice are saved as they finish; at the end they're joined into the story.

## Times on the RTX 3060 (0.4 MP)

| Story | Scenes | Time |
|---|---|---|
| 1 min (v1.0, turbo LoRA, 5 s scenes) | 12 | 43 min 38 s |
| 3 min (v1.0, turbo LoRA, 5 s scenes) | 36 | 2 h 05 min |
| 5 min (v1.2, FastH3, no upscale) | 58 | 3 h 35 min |

Most of the time is H3. ComfyUI's memory grows about 0.6 GB per scene on a 32 GB PC: for more than about 30 scenes,
run the script in two halves (two runs) and join them in your editor.

## Limits
- The main character stays the same (one character picture); side characters only exist in your words, so describe
  them fully in every line they're in.
- Over-the-shoulder shots and characters cut off at the frame edge go wrong (the hero twice, or two characters melted).
- The loudness differs per scene (H3 makes each scene's sound). Level it in your editor if you need it even.

## Required models
See [downloads.md](downloads.md) — every file was read from the workflow `.json`.

## Required custom nodes
None - core ComfyUI **0.39+**.
