# Wan 2.1 vs Wan 2.2 vs Wan 2.2 Animate — read this before mixing files

This is the single most common source of confusion (and "it won't load" errors) across the video workflows.
Wan 2.1, Wan 2.2 and Wan 2.2 Animate are **three different model families**. Files are **not**
interchangeable between them. This page explains what belongs to what, verified from the actual workflow JSONs.

---

## The three families at a glance

| | **Wan 2.1** | **Wan 2.2** | **Wan 2.2 Animate** |
|---|---|---|---|
| What it is | First-gen Wan video | MoE (high-noise + low-noise experts), better motion & cinematics | Reference-driven character animation from a driving video |
| Sizes used here | 1.3B and 14B | 14B (A14B, dual expert) + 5B (TI2V) | 14B |
| Diffusion file(s) | **one** GGUF | often **two** GGUFs (high + low noise) | **one** Animate GGUF + lightx2v high-noise LoRA |
| VAE | `wan_2.1_vae` | `Wan2.2_VAE` (5B) **or** `wan_2.1_vae` (14B) | `wan_2.1_vae` / `Wan2.1_VAE.pth` |
| Text encoder | `t5xxl_um_fp8_e4m3fn_scaled` (UMT5) | same UMT5 | `umt5_xxl_fp8_e4m3fn_scaled` |
| Status | **Older** — lighter, still great on 4 GB | Current mainline video model | Current, specialised (animation only) |
| Workflow | [wan2.1/gguf-lowvram](../workflows/wan2.1/gguf-lowvram) | [wan2.2/gguf-lowvram](../workflows/wan2.2/gguf-lowvram) | [wan2.2/animate](../workflows/wan2.2/animate) |

---

## The traps

1. **Two models, not one (Wan 2.2 14B).** The 14B Wan 2.2 T2V/I2V workflows load **two** GGUFs — a
   *high-noise* and a *low-noise* expert (verified: `wan2.2_t2v_high_noise_14B_Q2_K` + `..._low_noise_...`).
   If you only downloaded one, the second loader errors. The 5B TI2V path uses a **single** file
   (`Wan2.2-TI2V-5B-Q5_1`) — don't confuse the two.

2. **VAE mismatch.** The **5B** TI2V path needs `Wan2.2_VAE.safetensors`. The **14B** 2.2 paths and all of
   Wan 2.1 use `wan_2.1_vae`. Feeding the 5B VAE into a 14B graph (or vice-versa) produces garbled or black output.

3. **Animate ≠ generation.** Wan 2.2 Animate does **not** make video from a prompt alone. It needs a
   **reference image + a driving video** and drives motion onto the subject. If you just want text→video, use
   the 2.2 or 2.1 workflow, not Animate.

4. **The lightx2v LoRA is family-specific.** Animate uses a high-noise lightx2v LoRA
   (`wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise`). The 2.2 14B pack uses
   `Wan21_I2V_14B_lightx2v_cfg_step_distill_lora_rank64` / `lightx2v_T2V_14B_cfg_step_distill_v2`. They speed up
   different graphs — grabbing the wrong one gives poor results, not an outright error, so it's easy to miss.

5. **"Wan 2.1 is better on 4 GB" is sometimes true.** For the smallest GPUs the 1.3B Wan 2.1 models are faster
   and lighter than any 2.2 14B path. 2.2 buys quality/motion at a real VRAM/time cost. Pick per hardware, not by version number.

---

## Quick decision

- **4 GB and you just want *a* video, fast:** Wan 2.1 (1.3B T2V/I2V).
- **4–12 GB and you want the best quality:** Wan 2.2 14B (remember: two GGUFs).
- **8 GB sweet spot, single file:** Wan 2.2 TI2V-5B.
- **Animating a character from footage:** Wan 2.2 Animate.
- **First-frame → last-frame control:** Wan 2.1 FLF2V.

Exact files and links per family: [docs/DOWNLOADS.md](DOWNLOADS.md).
