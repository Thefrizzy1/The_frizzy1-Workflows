# Changelog - Wan 2.2 GGUF Low-VRAM

## v1.0.1 (2026-11-14)
- Notes only, graph unchanged: added a **How to use** note and a **Downloads** note (left of the canvas) to both 14B graphs (`The_frizzy1_wan-2.2-t2v-14b_v1.0.1.json`, `The_frizzy1_wan-2.2-i2v-14b_v1.0.1.json`).
- How to use: inputs, models, sampler settings, enhancement chain, upscale + RIFE + export, tips, attention launch flags, tested-on line.
- Downloads note matches downloads.md (I2V speed LoRA rename included).
- README: custom node list fixed to what the graphs load (added Frame-Interpolation and tbox, removed WanVideoWrapper and rgthree, which neither graph uses), ComfyUI version section, checked on ComfyUI 0.45.3 (converts, not run).
- v1.0.0 graphs moved to `source/`.

## v1.0.0 (CivitAI v1.0)
- Initial release: T2V/I2V 14B (dual expert) + TI2V-5B, GGUF, lightx2v LoRA support.
