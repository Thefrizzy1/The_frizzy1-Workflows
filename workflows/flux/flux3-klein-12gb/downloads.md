# Downloads - FLUX 3 Klein · 12 GB

Every file name below was read from the workflow `.json`.


Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

**[black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)** (gated: log in on Hugging Face and accept BFL's terms first)

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| all three files | `diffusion_models/` | [flux3-image-klein-int8-convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors) | 5.8 GB |
| all three files | `text_encoders/` | [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) | 4.9 GB |
| t2i + edit files (prompt upsampler) | `text_encoders/` | [qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) | 6.7 GB |
| all three files | `vae/` | [flux2-vae.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors) | 0.3 GB |

_Tested on: RTX 3060 12 GB · 32 GB RAM · ComfyUI 0.45.3 (t2i v2.0.0) and 0.43.1 (edit file). Low-VRAM edit file: ComfyUI 0.45.3 inside 6, 8 and 12 GiB budgets on a 24 GB lab card, not on a real 6 to 12 GB card._

Total 17.7 GB; the low-VRAM edit file (`The_frizzy1_flux3-klein-edit-lowvram_v1.1.0.json`) needs only the 3 files without the upsampler, 11.0 GB. No custom nodes: core ComfyUI **0.41 or newer** (FLUX 3 Image support). Not tested by me: the bf16 model (11.1 GB) for 16 GB+ cards, the nvfp4 model (5.3 GB) for RTX 50 cards. FLUX 3 Image Klein: FLUX Kommunity License.

Not used: GGUF files of Klein (they need the ComfyUI-GGUF custom node) and the TrueRelight LoRA (core ComfyUI 0.45.3 does not load its keys). See the README.
