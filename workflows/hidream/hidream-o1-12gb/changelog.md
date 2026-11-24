# Changelog - HiDream-O1-Image · 12 GB
## v1.0.0 (2026-11-24)
- First version. Built from the ComfyUI template `image_hidream_o1`: text to image and edit in one file, optional Gemma 4 prompt rewrite. Core nodes only.
- Changes from the template: the fp8 checkpoint (8.07 GB) instead of bf16; Width, Height, Steps and Seed are inputs in group 1; new default prompt; Gemma gets the picture only in edit mode; `TextGenerate` (deprecated in ComfyUI 0.45.3) replaced by `TextGenerateV2` with the same settings; the picture loader starts with ComfyUI's own `example.png` (it must always hold a picture, also for text to image); a **Resize picture to 4 MP?** switch in group 1. Sampler settings unchanged (40 steps, CFG 5, dpmpp_2m_sde_gpu, seam smoothing).
- Run on ComfyUI 0.45.3, RTX PRO 4000 24 GB, also inside a 10 GiB ComfyUI budget (11.3 GiB whole GPU). Not run on a 12 GB card.
