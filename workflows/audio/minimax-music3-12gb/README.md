# The_frizzy1 · MiniMax Music 3 · 12 GB v1.0.0

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> MiniMax Music 3 on a 12 GB card: write a caption and lyrics, get a song with vocals as mp3. One workflow file,
> core ComfyUI nodes only.

| | |
|---|---|
| **Model family** | MiniMax Music 3 (DiT int8) |
| **Tasks** | Text + lyrics → Music (vocals or instrumental) |
| **Needs** | 12 GB VRAM · 32 GB system RAM (ComfyUI peaked at 4.3 GB) · ComfyUI **0.42+** |
| **Tested on** | RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 · sage attention |
| **YouTube explainer** | (no video yet) |
| **License** | Workflow: MIT · MiniMax Music 3: Apache-2.0 |

## Quick start
1. Update ComfyUI to **0.42 or newer** (no custom nodes).
2. Download the 3 files in [downloads.md](downloads.md).
3. Load `The_frizzy1_minimax-music3-12gb_v1.0.0.json`, write caption and lyrics, set the length, **Run**.

## Listen

| What | File | Length | Wall |
|---|---|---|---|
| The template's lo-fi caption + lyrics, 60 s | [song-1-60s.mp3](samples/song-1-60s.mp3) | 1:00 | 2 min 20 s |
| Same caption + lyrics, 120 s | [song-2-120s.mp3](samples/song-2-120s.mp3) | 2:00 | 4 min 28 s |

## How to fill it in
1. **caption**: genre, BPM, key, mood, instruments.
2. **lyrics**: sections in brackets ([Verse], [Chorus]). Leave empty for instrumental.
3. **max_duration** in seconds.

## Measured on the RTX 3060

*Wall* = queue to finished. VRAM is the whole card as nvidia-smi reports it (about 0.7 GB is Windows).

| Run | Size | Wall | Peak VRAM | Peak RAM (ComfyUI) |
|---|---|---|---|---|
| 60 s of music, first run after starting ComfyUI | 60 s | 2 min 20 s | 11.3 GB | 3.6 GB |
| 120 s of music | 120 s | 4 min 28 s | 11.5 GB | 4.3 GB |

Lighter than the official template: the int8 DiT (2.5 GB) instead of fp16 (4.9 GB).

## Required models
See [downloads.md](downloads.md): 3 files, every file name read from the workflow `.json`.

## Required custom nodes
None - core ComfyUI **0.42+**.

## License

Workflow: MIT. MiniMax Music 3: Apache-2.0.
