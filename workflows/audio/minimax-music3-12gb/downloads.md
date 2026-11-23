# Downloads · MiniMax Music 3 · 12 GB v1.1.0

Every file name below was read from the workflow `.json`. The three files were downloaded on 2026-11-22 and their SHA-256 matched Hugging Face. Sizes are decimal GB, as Hugging Face shows them.

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| Diffusion model (DiT, int8) | `diffusion_models/` | [minimax_music3_dit_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/diffusion_models/minimax_music3_dit_int8_convrot.safetensors) | 2.50 GB |
| Text encoder (writes the song plan), pruned int8 | `text_encoders/` | [minimax_music3_text_encoder_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/text_encoders/minimax_music3_text_encoder_pruned_int8_convrot.safetensors) | 9.20 GB |
| Audio VAE | `vae/` | [minimax_music3_dav.safetensors](https://huggingface.co/Comfy-Org/MiniMax-Music-3/resolve/main/vae/minimax_music3_dav.safetensors) | 0.22 GB |

Total 11.9 GB. No custom nodes.

- The same repo also has an fp16 DiT (4.91 GB, the template's default), an fp32 DiT (9.83 GB) and bf16 text encoders (16.71 GB pruned, 18.47 GB full). None of them was run here. There is no GGUF file in the repo (checked 2026-11-22).
- Licence: MiniMax Music 3 is under the [MiniMax-Music3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-Music3/blob/main/LICENSE) (commercial use with conditions). The Comfy-Org repackage is tagged Apache-2.0. Workflow: MIT.
