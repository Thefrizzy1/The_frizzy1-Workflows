# Downloads - Mage-Flow v1.0.0

Verified from the workflow JSON file. All three files were downloaded on 2026-11-24; SHA-256 and size matched the Hugging Face listing of [Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow), and each link below answered with that SHA-256 as its x-linked-etag.

| Role | Filename | Folder | Size | Source | Verified? |
|---|---|---|---|---|---|
| Diffusion model (Mage-Flow 4B, int8) | `mage_flow_int8_convrot.safetensors` | `diffusion_models/` | 4.16 GB | [Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_int8_convrot.safetensors) | JSON + SHA-256 |
| Text encoder (Qwen3-VL 4B) | `qwen3vl_4b_bf16.safetensors` | `text_encoders/` | 8.88 GB | [Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) | JSON + SHA-256 |
| VAE (Mage-VAE) | `mage_flow_vae_bf16.safetensors` | `vae/` | 0.35 GB | [Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) | JSON + SHA-256 |

**What the workflow needs:** these three files, 13.38 GB together. The repo is not gated; no login is needed.

| File | Bytes | SHA-256 |
|---|---|---|
| `mage_flow_int8_convrot.safetensors` | 4,159,146,848 | `e081068163d7793b7e0d54ae2a773d3ac1c0d5b099c09b69dcbff36448485ae8` |
| `qwen3vl_4b_bf16.safetensors` | 8,875,719,384 | `36f3ff447ef59201722e8f9ce6020c9819fdcfba6aa2608c4e09b1c0ce114e34` |
| `mage_flow_vae_bf16.safetensors` | 345,053,056 | `34e076dc1e8a15321e1e07be5111d59cf16dd10b804b7c7e20b4de29013427e0` |

Other files in the same repo, not used and not tested here: `mage_flow_bf16` (8.23 GB, same model at full precision), `mage_flow_base_*` (Base, 30 steps), `mage_flow_turbo_*` (4 steps, CFG 1), and the `mage_flow_edit_*` files (image editing).

The authors' repos (`microsoft/Mage-Flow`, `-Base`, `-Turbo`) answered 401 on 2026-11-24 (removed or private), so the Comfy-Org copy is the only download source checked.
