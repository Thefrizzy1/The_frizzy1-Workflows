# Downloads — AI Audio Maker v1.0.0

Verified from the workflow JSON. MMAudio files typically go in `ComfyUI/models/mmaudio/`.

| Role | Filename | Source | Verified? |
|---|---|---|---|
| MMAudio model | `mmaudio_large_44k_v2_fp16.safetensors` | [Kijai/MMAudio_safetensors](https://huggingface.co/Kijai/MMAudio_safetensors) | JSON |
| Synchformer | `mmaudio_synchformer_fp16.safetensors` | Kijai/MMAudio_safetensors | JSON |
| MMAudio VAE | `mmaudio_vae_44k_fp16.safetensors` | Kijai/MMAudio_safetensors | JSON |
| CLIP (feature) | `apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors` | Kijai/MMAudio_safetensors | JSON |

<!-- direct-links:start -->
## Direct links (what `frizzy.py get` downloads)

Generated from this folder's `models.json` (checked 2026-10-14: every link resolves). File names are exactly what
the workflow `.json` loads; subfolders inside the model folder are fine.

| Need | Folder (`ComfyUI/models/`) | File the workflow loads | Download | Note |
|---|---|---|---|---|
| required | `mmaudio/` | `mmaudio_large_44k_v2_fp16.safetensors` | [download](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_large_44k_v2_fp16.safetensors) |  |
| required | `mmaudio/` | `mmaudio_synchformer_fp16.safetensors` | [download](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_synchformer_fp16.safetensors) |  |
| required | `mmaudio/` | `mmaudio_vae_44k_fp16.safetensors` | [download](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/mmaudio_vae_44k_fp16.safetensors) |  |
| required | `mmaudio/` | `apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors` | [download](https://huggingface.co/Kijai/MMAudio_safetensors/resolve/main/apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors) |  |

**Custom node packs this workflow uses:** [ComfyUI-MMAudio](https://github.com/kijai/ComfyUI-MMAudio), [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite).

One command: `python scripts/frizzy.py doctor audio/ai-audio-maker` (finds ComfyUI, downloads what's missing, installs the nodes).
<!-- direct-links:end -->
