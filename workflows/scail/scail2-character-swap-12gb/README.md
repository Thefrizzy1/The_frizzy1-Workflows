# The_frizzy1 — SCAIL-2 Character Swap · 12 GB v1.1.0

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> Swap one person in your video for your own character (a person, an animal, a cartoon) with SCAIL-2.
> Any clip length, the original sound kept, App mode, core ComfyUI nodes only. My entry for the ComfyUI
> **#OpenSourceHiggsfield** challenge (Openjutsu track): OPENjutsu couldn't turn me into a dog, so I built my own.

| | |
|---|---|
| **Model family** | SCAIL-2 (Wan 2.1 14B based, int8) + SAM 3.1 |
| **Tasks** | Character replacement (V2V) · whole clip in 81-frame loop rounds · pick which person · original sound |
| **Needs** | 12 GB VRAM · 32 GB system RAM (tested) · ComfyUI **0.43.1** (tested) · no custom nodes |
| **Tested on** | RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 (frontend 1.57.4) · Windows 11 |
| **License** | Workflow: MIT · SCAIL-2: MIT |

## Quick start
1. Update ComfyUI (tested on **0.43.1**; older versions may not have Start Loop / End Loop or the SCAIL-2 nodes).
2. Download the 7 files in [downloads.md](downloads.md) (28.6 GB). ComfyUI's **Missing models** window offers them too.
3. Load `The_frizzy1_scail2-character-swap-12gb_v1.1.0.json`. It opens in **App mode**.
4. Fill in the inputs and press **Run**:
   - **Your video** and **Character picture** (front view, full body if you can)
   - **Describe the result**: one sentence, e.g. *A realistic golden retriever dances in a bright room.*
   - **Who is in the clip** (e.g. *man in red t-shirt*) and **What your character is** (e.g. *dog*)
   - **Which person**: `0` = the left one, `1` = the next one, empty = everyone
   - **Seconds**: `0` = the whole clip (try 3 s first)
5. The video lands in `ComfyUI/output/SCAIL2 swap/`.

## Preview

<p align="center">
<a href="samples/sample-1.webp"><img src="samples/sample-1.webp" width="32%" alt="dance clip, person swapped for a golden retriever"></a>
</p>

<sub>Made by this workflow on the RTX 3060: a 9.4 s dance clip, the dancer swapped for a golden retriever (first 4 s shown).</sub>

## Which person
SAM 3.1 finds up to 4 people that match **Who is in the clip** and sorts them left to right. `0` is the left one,
`1` the next one. Empty swaps all of them for the same character. **One character per run.**

## How it works
SCAIL-2 makes 81 frames at a time. The workflow runs it inside ComfyUI's own **Start Loop / End Loop**, one segment
per round. Every next round starts 76 frames later and gets the last 5 frames of the round before (overlap), drops
them again and colour-matches to the previous round (**reinhard_lab**), so a long clip stays one take. The clip is
padded to whole segments and cut back at the end.

Settings (benchmarked on the 3060): int8 model · DPO LoRA 1.0 · lightx2v distill LoRA 0.8 · 6 steps · CFG 1 ·
shift 5 · euler / simple · short side 512.

## Measured on the RTX 3060

| Run | Size | Wall |
|---|---|---|
| 9.4 s dance clip, whole clip, sound kept | 512×896 | 24:09 |

## Left out on purpose
Two characters in one run and a face fix pass: not reliable enough in my tests.

## Required models
See [downloads.md](downloads.md): 7 files, 28.6 GB, every file name read from the workflow `.json`.

## Required custom nodes
None, core ComfyUI only.

## Source
`source/build_scail_swap.py` builds the run graph (API format) and, with `--polish`, the shareable workflow
(titles, groups, notes, version).

## Credits & license
- SCAIL-2 by [zai-org](https://huggingface.co/zai-org/SCAIL-2) (MIT), built on Wan 2.1 14B
- ComfyUI files + int8 by [Comfy-Org](https://huggingface.co/Comfy-Org/SCAIL-2)
- lightx2v step-distill LoRA (repack by [Kijai](https://huggingface.co/Kijai/WanVideo_comfy))
- SAM 3.1 by Meta ([Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)), see its license on the model page
- Segment and overlap settings from the official ComfyUI SCAIL-2 template

Workflow: MIT, by **The_frizzy1** · [YouTube](https://www.youtube.com/@the_frizzy1)
