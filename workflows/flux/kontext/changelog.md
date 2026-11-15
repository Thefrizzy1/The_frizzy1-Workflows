# Changelog - Flux Kontext GGUF
## v2.3.0 (2026-11-14)
- TeaCache (its pack no longer imports on ComfyUI 0.44/0.45: `cannot import name 'precompute_freqs_cis'`) replaced by core
  **EasyCache** (core defaults: reuse 0.2, start 0.15, end 0.95). Needs ComfyUI 0.45+.
- PathchSageAttentionKJ removed: use the launch flag --use-sage-attention instead. VAELoaderKJ replaced by core VAELoader.
- In-graph "How to use" and "Downloads" notes added, with an attention tip.
- Run on ComfyUI 0.45.3 (RTX PRO 4000 24 GB, 64 GB RAM, sage attention), seed 42, the 3 style LoRAs set to None (not on the test server): 83 s first run with EasyCache, 134 s with EasyCache set to never reuse. The 35-step pass: 1.34 s/it with EasyCache, 3.21 s/it without (2.4x faster); same scene, pose and light, small details differ. Not run on a 4 GB card with v2.3.0.
- File renamed to `The_frizzy1_flux-kontext-gguf_v2.3.0.json`; v2.2.0 in `source/`.

## v2.2.0 (CivitAI v2.2)
- Fixed settings, Torch Compile.
## v2.0.0 (CivitAI v2.0)
- Two-pass setup.
## v1.0.0
- Initial release.
