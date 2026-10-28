# The_frizzy1 · MOSS-Image · 12 GB v1.0.0

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> MOSS-Image on a 12 GB card: text to image, layout with boxes, editing, and control from a photo's shape. Four
> workflow files, core ComfyUI nodes only, with the prompt enhancer from the official templates.

| | |
|---|---|
| **Model family** | MOSS-Image (SFT, int8) |
| **Tasks** | Text → Image · Layout (bounding boxes) · Edit · Control (MoGe shape) |
| **Needs** | 12 GB VRAM · 32 GB system RAM (ComfyUI peaked at 5.2 GB) · ComfyUI **0.43+** |
| **Tested on** | RTX 3060 12 GB · Ryzen 5 5600X · 32 GB RAM · ComfyUI 0.43.1 · sage attention |
| **YouTube explainer** | (no video yet) |
| **License** | Workflow: MIT · MOSS-Image: Apache-2.0 |

## Quick start
1. Update ComfyUI to **0.43 or newer** (no custom nodes).
2. Download the files in [downloads.md](downloads.md). Edit and control need their extra files, text to image does not.
3. Load the `.json` for what you want to do, write your prompt, **Run**.

## Preview

<p align="center">
<a href="samples/sample-1.webp"><img src="samples/sample-1.webp" width="31%" alt="text to image, 1 MP"></a>
<a href="samples/sample-2.webp"><img src="samples/sample-2.webp" width="31%" alt="edit, 1 MP"></a>
<a href="samples/sample-3.webp"><img src="samples/sample-3.webp" width="31%" alt="control from a photo, 1 MP"></a>
</p>

<sub>Made by these workflows on the RTX 3060: text to image, the fisherman's sweater edited into a yellow raincoat, and
an astronaut in the fisherman's pose (control). The fisherman is my own FLUX 3 Klein picture.</sub>

## The four files

| File | What it does |
|---|---|
| `The_frizzy1_moss-image-t2i-12gb_v1.0.0.json` | Text to image. Short prompt is fine, the enhancer writes the long caption |
| `The_frizzy1_moss-image-layout-12gb_v1.0.0.json` | Text to image with boxes: say what goes where |
| `The_frizzy1_moss-image-edit-12gb_v1.0.0.json` | Edit one picture with the edit LoRA |
| `The_frizzy1_moss-image-control-12gb_v1.0.0.json` | New picture in the shape of your photo (MoGe reads it, no map needed) |

Lighter than the official templates: the w4a8 text encoder (7.3 GB) instead of int8, and MoGe 3 ViT-L (0.74 GB)
instead of ViT-G (2.5 GB) in the control file.

## Measured on the RTX 3060

*Wall* = queue to finished. VRAM is the whole card as nvidia-smi reports it (about 0.7 GB is Windows).

| Run | Size | Wall | Peak VRAM | Peak RAM (ComfyUI) |
|---|---|---|---|---|
| Text to image, first run after starting ComfyUI (loads the files) | 1 MP | 1 min 16 s | 11.3 GB | 3.8 GB |
| Text to image, new prompt (enhancer + image) | 1 MP | 55 s | 11.3 GB | 3.9 GB |
| Text to image, same prompt, new seed | 1 MP | 43 s | 11.0 GB | 3.9 GB |
| Layout (template boxes) | 1 MP | 45 s | 11.5 GB | 3.9 GB |
| Edit, one image | 1 MP | 1 min 11 s | 11.3 GB | 4.0 GB |
| Control (MoGe mask) | 1 MP | 58 s | 11.3 GB | 5.2 GB |

Layout: the knight and the ruin went where the boxes said. The text did not: the template asks for 5 text blocks,
I got one garbled title, one garbled line, and the other 3 empty (seed 1). Edit and control looked right.

## Required models
See [downloads.md](downloads.md): every file name read from the workflow `.json`.

## Required custom nodes
None - core ComfyUI **0.43+**.

## Troubleshooting
- **No box editor in the layout file:** it needs Nodes 2.0 (ComfyUI icon → Nodes 2.0).
- **Control follows the photo too loosely:** in the MoGe subgraph set **Render MoGe Geometry** to *depth* instead of *mask*.

## License

Workflow: MIT. MOSS-Image: Apache-2.0.
