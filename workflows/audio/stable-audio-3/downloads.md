# Downloads · Stable Audio 3 Medium Base v1.0.0

Every file name below was read from the workflow `.json`. The three files were downloaded on 2026-11-24 and their size and SHA-256 matched the Hugging Face listing. Sizes are decimal GB, as Hugging Face shows them.

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| Audio model (Medium Base, includes its audio VAE) | `checkpoints/` | [stable_audio_3_medium_base.safetensors](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium_base.safetensors) | 9.22 GB |
| Text encoder of the audio model (T5Gemma) | `text_encoders/` | [t5gemma_b_b_ul2.safetensors](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors) | 1.19 GB |
| Prompt writer (Qwen3.5 2B) | `text_encoders/` | [qwen3.5_2b_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_2b_bf16.safetensors) | 4.55 GB |

Total 15.0 GB. No custom nodes. These are the three files the built-in template `audio_stable_audio_3_medium_base` loads.

- [Comfy-Org/stable-audio-3](https://huggingface.co/Comfy-Org/stable-audio-3) has one Medium Base file only (no fp8 or smaller copy, checked 2026-11-24). The same repo has Stable Audio 3 Medium (post-trained, 9.22 GB) and four Small files (2.27 GB each); none of them was run here.
- With **Let Qwen expand your idea** off, the Qwen file was not loaded in the test run. Whether the workflow starts with that file missing was not tested.
- Licence: Stable Audio 3 is under the [Stability AI Community License](https://huggingface.co/stabilityai/stable-audio-3-medium-base/blob/main/LICENSE.md): research, personal and commercial use free below US$1 million yearly revenue (commercial users register with Stability AI); you own the outputs. The Comfy-Org repackage links the same licence family (`stable-audio-community`). T5Gemma: [Gemma Terms of Use](https://huggingface.co/stabilityai/stable-audio-3-medium-base/blob/main/LICENSE_GEMMA.md). Qwen3.5 (Comfy-Org repackage): Apache-2.0. Workflow: MIT.
