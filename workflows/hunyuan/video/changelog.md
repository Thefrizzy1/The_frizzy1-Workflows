# Changelog: Hunyuan Video Low-VRAM
## v1.1.2 (2026-11-14)
- Notes only, graph unchanged: added a "How to use" note (inputs, settings, outputs, tips, tested-on, attention flags) and a "Downloads" note (same files as downloads.md), both left of the graph.
- Checked against ComfyUI 0.45.3: core nodes all exist; not validated on the test server (HunyuanVideoWrapper and HunyuanVideoSamplerSave packs and three model files missing there). Not run on 0.45.3.
- v1.1.1 json moved to source/.
## v1.1.1 (repo fix)
- Corrected the diffusion loader from `flux1-dev-Q5_K_S.gguf` (leftover) to `fast-hunyuan-video-t2v-720p-Q5_K_M.gguf`. Original kept in source/.
## v1.1.0 (CivitAI v1.1)
- Added Text2Vid.
## v1.0.0
- Initial release (I2V).
