# The_frizzy1 · Fibo 2.0 Edit Turbo · 12 GB v1.0.0

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> Fibo 2.0 Edit Turbo on a 12 GB card: say what the picture should look like, the prompt enhancer writes Fibo's
> structured caption, 4 steps later the edit is done. One workflow file, core ComfyUI nodes only.

| | |
|---|---|
| **Model family** | Fibo 2.0 Edit Turbo (int8) |
| **Tasks** | Edit one image |
| **Needs** | 12 GB VRAM · 32 GB system RAM (ComfyUI peaked at 3.4 GB) · ComfyUI **0.43+** |
| **Tested on** | RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 · sage attention |
| **YouTube explainer** | (no video yet) |
| **License** | Workflow: MIT · Fibo 2.0: **CC BY-NC 4.0, non-commercial only** |

## Quick start
1. Update ComfyUI to **0.43 or newer** (no custom nodes).
2. Download the 4 files in [downloads.md](downloads.md). If you have FLUX 3 Klein, you already have two of them.
3. Load `The_frizzy1_fibo2-edit-turbo-12gb_v1.0.0.json`, load your picture, write the edit, **Run**.

## Preview

<p align="center">
<a href="samples/sample-1.webp"><img src="samples/sample-1.webp" width="31%" alt="the input picture"></a>
<a href="samples/sample-2.webp"><img src="samples/sample-2.webp" width="31%" alt="sweater to yellow raincoat"></a>
<a href="samples/sample-3.webp"><img src="samples/sample-3.webp" width="31%" alt="net to bright blue"></a>
</p>

<sub>Input (my own FLUX 3 Klein picture), "His sweater is a bright yellow raincoat.", "The net is bright blue."
Made on the RTX 3060 with the enhancer on.</sub>

## Keep the prompt enhancer on

Fibo reads a structured JSON caption, not a sentence. The enhancer (Qwen3-VL 8B) looks at your picture and writes it.
I switched it off once and gave Fibo the plain sentence "The net is bright blue.": the fisherman got a white blazer, red curly
hair and sunglasses, and the net stayed red. Off only makes sense if you write the JSON yourself.

Write what the result looks like, not what stays the same.

## Measured on the RTX 3060

*Wall* = queue to finished. VRAM is the whole card as nvidia-smi reports it (about 0.7 GB is Windows).

| Run | Size | Wall | Peak VRAM | Peak RAM (ComfyUI) |
|---|---|---|---|---|
| Edit, first run after starting ComfyUI (loads Fibo + enhancer) | about 1 MP | 1 min 9 s | 11.3 GB | 3.2 GB |
| Edit, new prompt, enhancer on | about 1 MP | 1 min 6 s | 11.4 GB | 3.4 GB |
| Edit, enhancer off (wrong result, see above) | about 1 MP | 15 s | 11.6 GB | 3.2 GB |

Most of the time is the enhancer: without it the whole run took 15 s.

Lighter than the official template: Qwen3-VL-4B int8 (the same file as FLUX 3 Klein's) instead of bf16.

## Required models
See [downloads.md](downloads.md): 4 files, every file name read from the workflow `.json`.

## Required custom nodes
None - core ComfyUI **0.43+**.

## License

Workflow: MIT. Fibo 2.0: CC BY-NC 4.0, so no commercial use of the model. Qwen3-VL: Apache-2.0.
