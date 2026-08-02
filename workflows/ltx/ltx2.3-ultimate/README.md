# The_frizzy1 — LTX-2.3 Ultimate v3.0.0

> The newest LTXV-2.3 (22B) — T2V, I2V, first/last-frame and audio, with ID LoRA. Color-coded GGUF. **12 GB** target.

| | |
|---|---|
| **Model family** | LTXV-2.3 (22B) |
| **Tasks** | T2V · I2V · FFLF · Audio · ID LoRA |
| **Min VRAM** | 12 GB |
| **CivitAI** | https://civitai.com/models/2339823 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/LTX23-Ultimate |
| **YouTube** | https://www.youtube.com/watch?v=im4wolfHvMk |
| **License** | Apache-2.0 |


## Preview

**Sample clips:** [clip 1](samples/preview-1.mp4) · [clip 2](samples/preview-2.mp4) · [clip 3](samples/preview-3.mp4)

## Important notes
- Use **DEV GGUF** diffusion models (distilled possible).
- The **distilled LoRA is REQUIRED**, plus the **text projection** (embedding connector).
- Most issues = outdated nodes or ComfyUI. Install KJNodes **nightly**.

## Get the models (one command)

From the repo root, this finds ComfyUI, downloads the missing models into the right folders, and installs the custom nodes:

```bash
python scripts/frizzy.py doctor ltx/ltx2.3-ultimate --comfy "C:/path/to/ComfyUI"
```

No pip installs. Details: [scripts/README.md](../../../scripts/README.md).

## Required custom nodes
| Node | Link |
|---|---|
| ComfyUI-GGUF | https://github.com/city96/ComfyUI-GGUF |
| KJNodes (nightly) | https://github.com/kijai/ComfyUI-KJNodes |
| ComfyUI-JakeUpgrade | https://github.com/jakechai/ComfyUI-JakeUpgrade |
| VideoHelperSuite | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [LTX-2 GGUF](../ltx2) — lighter 19B generation.
