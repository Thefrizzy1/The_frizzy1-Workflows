# Downloads - HiDream-O1-Image · 12 GB

Every file name below was read from the workflow `.json`.

Click a file name to download it. Put it in the folder shown (inside `ComfyUI/models/`).

| For | Folder | File (click = download) | Size |
|---|---|---|---|
| the image model (required) | `checkpoints/` | [hidream_o1_image_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/resolve/main/checkpoints/hidream_o1_image_fp8_scaled.safetensors) | 8.07 GB |
| Gemma prompt rewrite (required, also when the rewrite is off) | `text_encoders/` | [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) | 9.06 GB |

_Tested on: RTX PRO 4000 Blackwell 24 GB · ComfyUI 0.45.3 (also inside a 10 GiB ComfyUI budget). Not run on a 12 GB card._

Total 17.1 GB. Sizes are the byte counts of the Hugging Face listing (checked 2026-11-24), and the downloaded files matched them and their SHA-256.

No custom nodes: core ComfyUI (HiDream-O1 support from [PR #13817](https://github.com/Comfy-Org/ComfyUI/pull/13817), May 2026); only 0.45.3 was tested.

Other files in [Comfy-Org/HiDream-O1-Image](https://huggingface.co/Comfy-Org/HiDream-O1-Image): `hidream_o1_image_bf16.safetensors` (16.4 GB, the template's file; one edit and one text-to-image run here, change the loader to use it), `hidream_o1_image_mxfp8.safetensors` (8.92 GB, not tried), and the Dev (distilled, 28-step) files (not tried; they need the Dev template's settings).

Licences: HiDream-O1-Image: MIT. Gemma 4 (Comfy-Org repackage): Apache-2.0.
