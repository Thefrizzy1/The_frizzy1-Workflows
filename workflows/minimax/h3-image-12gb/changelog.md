# Changelog — MiniMax H3 Image · 12 GB
## Edit v2.0.0 and area edit v2.0.0 (2026-11-26)
- Same one-node layout as text to image v2.0.0: picture loader(s) on the left, one big node with every setting (instruction, switches, box, megapixels, seed, the three model files), Result, Before / after and (area edit) Area that changes on the right. Built by `source/make_v2_edits.py` from the v1.0.0 files; the job the frontend sends is the same as v1.0.0 (checked: same nodes, values and links).
- First runs on a 12 GB card: RTX 3060, 32 GB RAM, ComfyUI 0.45.3, models unloaded before each run, 3648x5472 photos. Area edit at 8.3 MP: 139 to 160 s, at 16 MP: 218 s; edit at 8.3 MP (2400x3616 out): 134 to 198 s. Whole card 11.33 to 11.49 GiB, ComfyUI RAM up to 19.7 GiB, the PC up to 31.9 of 32 GB.
- The v1.0.0 edit and area-edit files moved to `source/`. README: RTX 3060 numbers for both, 32 GB RAM as the minimum, a note on colours shifting a little inside the area.

## v2.0.0 (2026-11-24)
- Text to image is **one node** now (a single subgraph): prompt, shape, megapixels, seed and the model files on the outside, App mode set. Same 6 steps and the same pixels as v1.0.0, which moved to source/.
- First run on a 12 GB card: RTX 3060, ComfyUI 0.45.3, 7.5 MP: 66 s with the models unloaded first, 59 s for a new prompt, 44 s for a new seed, 11.4 to 11.5 GiB peak VRAM, 15.7 GiB ComfyUI RAM.
- No Turbo mode: the 2-step pDMD LoRA was tested and left out (soft, grid pattern; see README).
- Edit and area edit files unchanged (v1.0.0). `source/build.py` still builds the v1.0.0 files.

## v1.0.0 (2026-11-24)
- Initial release: three workflows on MiniMax H3 Image, built from the ComfyUI templates *MiniMax-H3-Image: Text to Image* and *Image Edit* and restructured into numbered groups with every input in group 1 and App mode. Core nodes only.
- Text to image (7.5 MP default), edit (Picture 1 + optional Picture 2), and a new area edit (box in percent or a painted mask, 31 px soft edge, pasted back into the untouched picture at its own size).
- 12 GB files: W4A8 model + NVFP4 text encoder (29.4 GB in all). No prompt expander. Sampler as the templates: 6 steps, CFG 1, euler / simple.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, also inside 12 and 10 GiB VRAM budgets: 30 to 31 s for text to image at 7.5 MP, 42 to 44 s for an edit at 4 MP, 66 to 68 s with two pictures; whole GPU 10.8 to 11.4 GiB in the 10 GiB budget, ComfyUI RAM up to 20.6 GiB. Not verified on a 12 GB card.
