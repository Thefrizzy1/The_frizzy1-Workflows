# Changelog - Qwen Image 2.1 Ultimate · 12 GB
## v2.1.1 (2026-11-14)
- Notes only, graph unchanged. "How to use" note rewritten: what it does, inputs, settings, tips, attention line (--use-sage-attention / --use-ck-attention), Tested on line (adds ComfyUI 0.45.3 on a 24 GB card). Downloads note moved down so the notes do not overlap.
- Converts and validates on ComfyUI 0.45.3. v2.1.0 kept in `source/`.

## v2.1.0
- New mode **Edit: remove background (PNG)** (official template prompt, Image 1 only, transparent PNG).
- Tested on the RTX 3060 (ComfyUI 0.39.2, 1 MP): Turbo 29 s, base 54 s; clean on a portrait and a product shot, failed (almost fully transparent) on a wide room shot 3 out of 3 times. Every mode validated; normal Edit re-tested.
- v2.0.0 kept in `source/`.

## v2.0.0
- First Ultimate release: text to image, edit (1–3 images), ControlNet pose / depth / edges (Fun ControlNet Union, core since ComfyUI 0.38), Turbo on/off. Core nodes only.
- ControlNet modes run at their own size (ControlNet megapixels, default 1): at 2K the ControlNet broke in my test.
- Inputs ship bypassed; "Needs …" checks stop a run whose mode needs a bypassed input.
- Tested in every mode on the RTX 3060 (ComfyUI 0.39.2).
