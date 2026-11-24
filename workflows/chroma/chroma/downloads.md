# Downloads - Chroma1-HD v1.0.0

Verified from the workflow JSON file. The three files were downloaded on 2026-11-24 and their SHA-256 and size matched the Hugging Face listings.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (Chroma1-HD, fp8mixed) | `Chroma1-HD-fp8mixed.safetensors` | `diffusion_models/` | 9.19 GB | [Comfy-Org/Chroma1-HD_repackaged](https://huggingface.co/Comfy-Org/Chroma1-HD_repackaged/resolve/main/split_files/diffusion_models/Chroma1-HD-fp8mixed.safetensors) | JSON |
| Text encoder (T5-XXL, fp8 scaled) | `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders/` | 5.16 GB | [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) | JSON |
| VAE (the Flux.1 VAE) | `ae.safetensors` | `vae/` | 0.34 GB | [Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) | JSON |

**What the workflow needs:** these three files, 14.69 GB together. None of the repos is gated; no login is needed.

| File | Bytes | SHA-256 |
|---|---|---|
| `Chroma1-HD-fp8mixed.safetensors` | 9,193,379,316 | `a2928ca6075f308f4d5e2182e2b96120fa8ad270ec6ea9b1b5c724c85c49a575` |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | 5,157,348,688 | `a498f0485dc9536735258018417c3fd7758dc3bccc0a645feaa472b34955557a` |
| `ae.safetensors` | 335,304,388 | `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38` |

These are the template's files. If you already run Flux.1, the T5 and `ae.safetensors` are the same files.

Not used, not tested: the full-precision `Chroma1-HD.safetensors` (17.8 GB, same Comfy-Org repo and the authors' repo [lodestones/Chroma1-HD](https://huggingface.co/lodestones/Chroma1-HD)) and `t5xxl_fp16.safetensors` (9.79 GB). The Comfy-Org repo holds only those two model files (listing checked 2026-11-24): no int8 or GGUF file.
