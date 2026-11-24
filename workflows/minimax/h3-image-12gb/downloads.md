# Downloads — MiniMax H3 Image · 12 GB

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`). The same three files for all three workflows.

| Folder | File (click = download) | Size |
|---|---|---|
| `diffusion_models/` | [minimax_h3_image_pruned_w4a8.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_w4a8.safetensors) | 12.5 GB |
| `text_encoders/` | [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | 15.7 GB |
| `vae/` | [minimax_h3_image_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) | 1.2 GB |

**Total 29.4 GB.** SHA-256 of all three matched the Hugging Face listing on 2026-11-24. The text encoder is the same file as for MiniMax H3 video: if you have it, you only need the other two.

Custom nodes: none (core ComfyUI 0.45+).

## Other files in the Comfy-Org repository (not used here)

| File | Size | Why not |
|---|---|---|
| `minimax_h3_image_pruned_int8_convrot.safetensors` | 21.0 GB | the templates' model; larger than the W4A8 file. Not tested here |
| `minimax_h3_image_pruned_bf16.safetensors` | 40.2 GB | full precision |
| `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` | 27.1 GB | the templates' text encoder; larger than the NVFP4 file. Not tested here |
| `qwen3.5_9b_w4a8_gptq.safetensors` | 7.3 GB | the templates' prompt expander; these workflows have none |
| `qwen3.8_27b_minimax_h3_image_pe_w4a8_gptq.safetensors` | 17.3 GB | MiniMax's own prompt expander (W4A8 copy); not used |

Any of the larger files can be picked in the loaders instead; none of them were run here.

Licence: MiniMax-H3-Image Community License ([read it](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE)). It does not cover use in the EU, the UK, South Korea or the USA.
