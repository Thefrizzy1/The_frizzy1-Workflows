# Changelog — MiniMax H3 Image · 12 GB
## v1.0.0 (2026-11-24)
- Initial release: three workflows on MiniMax H3 Image, built from the ComfyUI templates *MiniMax-H3-Image: Text to Image* and *Image Edit* and restructured into numbered groups with every input in group 1 and App mode. Core nodes only.
- Text to image (7.5 MP default), edit (Picture 1 + optional Picture 2), and a new area edit (box in percent or a painted mask, 31 px soft edge, pasted back into the untouched picture at its own size).
- 12 GB files: W4A8 model + NVFP4 text encoder (29.4 GB in all). No prompt expander. Sampler as the templates: 6 steps, CFG 1, euler / simple.
- Run on ComfyUI 0.45.3, RTX PRO 4000 Blackwell 24 GB, also inside 12 and 10 GiB VRAM budgets: 30 to 31 s for text to image at 7.5 MP, 42 to 44 s for an edit at 4 MP, 66 to 68 s with two pictures; whole GPU 10.8 to 11.4 GiB in the 10 GiB budget, ComfyUI RAM up to 20.6 GiB. Not verified on a 12 GB card.
