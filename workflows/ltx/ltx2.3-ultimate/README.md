# The_frizzy1 - LTX-2.3 Ultimate · 12 GB v3.0.1

<a href="https://www.youtube.com/watch?v=im4wolfHvMk&list=PLQ3PcJNbU2Ls"><img src="https://img.youtube.com/vi/im4wolfHvMk/mqdefault.jpg" width="640" alt="Watch the video"></a>

☕ If this workflow saved you time: **[Buy me a coffee](https://buymeacoffee.com/the_frizzy1)**

> LTXV-2.3 (22B) - T2V, I2V, first/last-frame and audio, with ID LoRA. Color-coded GGUF. **12 GB** target.

| | |
|---|---|
| **Model family** | LTXV-2.3 (22B) |
| **Tasks** | T2V · I2V · FFLF · Audio · ID LoRA |
| **Workflow file** | `The_frizzy1_ltx2.3-ultimate_v3.0.1.json` |
| **Min VRAM** | 12 GB |
| **CivitAI** | https://civitai.com/models/2339823 |
| **Hugging Face** | https://huggingface.co/The-frizzy1/LTX23-Ultimate |
| **YouTube** | https://www.youtube.com/watch?v=im4wolfHvMk&list=PLQ3PcJNbU2Ls |
| **License** | Workflow: MIT · LTX-2 Community License Agreement · Gemma 3 text encoder: Gemma Terms of Use |
| **Newer** | [LTX 2.5 Ultimate](../../ltx/ltx-2.5-ultimate-12gb) (12 GB). |


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

## ComfyUI version
Needs a recent ComfyUI with the core LTX-2.3 nodes (LTXVReferenceAudio, TextGenerateLTX2Prompt, ComfyMathExpression).
Checked on ComfyUI 0.45.3: the graph converts and every core node it uses exists there. The JakeUpgrade, Impact-Pack and
Easy-Use nodes and the models are not installed on the check server, so it was not validated or run on 0.45.3.

## Required custom nodes
| Node | Link | Used for |
|---|---|---|
| ComfyUI-GGUF | https://github.com/city96/ComfyUI-GGUF | GGUF model loading (with KJNodes' GGUFLoaderKJ) |
| KJNodes (nightly) | https://github.com/kijai/ComfyUI-KJNodes | GGUFLoaderKJ, VAELoaderKJ, LTXVImgToVideoInplaceKJ, LTXVAddGuideMulti, PathchSageAttentionKJ |
| ComfyUI-JakeUpgrade | https://github.com/jakechai/ComfyUI-JakeUpgrade | CR ... Input Switch JK (model, latent, conditioning, audio, image, text) |
| VideoHelperSuite | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite | VHS_LoadAudioUpload |
| ComfyUI-Impact-Pack | https://github.com/ltdrdata/ComfyUI-Impact-Pack | ImpactConditionalBranchSelMode |
| ComfyUI-Easy-Use | https://github.com/yolain/ComfyUI-Easy-Use | easy float, easy boolean |

Attention: you can start ComfyUI with `--use-sage-attention` (same speed, lower peak VRAM in a 24 GB Z-Image test). `--use-ck-attention` gave a different image for the same seed in that test.

## Required models
Full verified table + links: **[downloads.md](downloads.md)**.

## Changelog
See [changelog.md](changelog.md).

## Related workflows
- [LTX-2 GGUF](../ltx2) - lighter 19B generation.
