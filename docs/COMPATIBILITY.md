# Compatibility Matrices

Quick cross-reference of what runs where. All rows below are derived from the actual workflow files unless
marked *Not verified*.

---

## Workflow × task

| Workflow | T2V | I2V | V2V/Animate | T2I | Img edit | Audio | FFLF |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Wan 2.1 GGUF Low-VRAM | ✅ | ✅ | ✅ (VACE) | — | — | — | ✅ |
| Wan 2.1 FLF2V | — | ✅ | — | — | — | — | ✅ |
| Wan 2.2 GGUF Low-VRAM | ✅ | ✅ | — | — | — | — | — |
| Wan 2.2 Animate | — | — | ✅ | — | — | — | — |
| Flux Kontext GGUF | — | — | — | ✅ | ✅ | — | — |
| Flux.2 Dev GGUF | — | — | — | ✅ | — | — | — |
| Qwen Image & Edit 2509 | — | — | — | ✅ | ✅ | — | — |
| Z-Image Turbo GGUF | — | — | — | ✅ | — | — | — |
| Hunyuan Video Low-VRAM | ✅ | ✅ | — | — | — | — | — |
| LTX-2 GGUF | ✅ | ✅ | — | — | — | ✅ | — |
| LTX-2.3 Ultimate | ✅ | ✅ | — | — | — | ✅ | ✅ |
| AI Audio Maker | — | — | — | — | — | ✅ | — |

## VRAM guidance

Minimum = will run (slowly, low quant). Comfortable = the creator's tested target.

| Workflow | Minimum | Comfortable | Tested hardware (from creator) |
|---|---|---|---|
| Wan 2.1 GGUF Low-VRAM | 4 GB | 8–12 GB | RTX 3050 Laptop 4 GB |
| Wan 2.2 GGUF Low-VRAM | 4 GB (5B: 8 GB) | 12 GB | RTX 3050 Laptop 4 GB |
| Wan 2.2 Animate | 4 GB (Q4) | 12 GB (Q8) | RTX 3050 4 GB / RTX 3060 12 GB |
| Flux Kontext GGUF | 4 GB | 8 GB | 4 GB laptop |
| Qwen Image & Edit 2509 | 4 GB (Q4_K_S) | 12 GB (Q8) | 4 GB / 12 GB |
| Hunyuan Video Low-VRAM | 4 GB | 8 GB+ | RTX 3050 Laptop (slow) |
| LTX-2 GGUF | 4 GB (+Triton) | 12 GB | RTX 3060 12 GB + 48 GB RAM |
| LTX-2.3 Ultimate | 12 GB | 12 GB+ | RTX 3060 12 GB |
| Flux.2 / Z-Image / AI Audio | *Not verified* | *Not verified* | needs JSON |

## Quantisation cheat-sheet (GGUF)

| Quant | Relative VRAM | Quality | Use when |
|---|---|---|---|
| Q8_0 | Highest | Best | You have the headroom |
| Q6_K / Q5_K_S / Q5_1 | Medium | Best balance | **Default recommendation** |
| Q4_K_M / Q4_K_S | Low | Good | 4 GB GPUs |
| Q3_K_M | Lower | Usable | Very tight VRAM |
| Q2_K | Lowest | Rough | Last resort / 14B on 4 GB |

## Shared custom nodes

| Node | Wan 2.1 | Wan 2.2 | Animate | Flux K | Qwen | Hunyuan | LTX-2 | LTX-2.3 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ComfyUI-GGUF / calcuis gguf | ✅ | ✅ | — | ✅ | — | ✅ | ✅ | ✅ |
| KJNodes | ✅ | ✅ | ✅ | — | ✅ | — | ✅ | ✅ |
| WanVideoWrapper | ✅ | ✅ | — | — | — | — | — | — |
| VideoHelperSuite | ✅ | ✅ | ✅ | — | — | — | — | ✅ |
| controlnet_aux | — | — | ✅ | — | — | — | — | — |
| segment-anything-2 | — | — | ✅ | — | — | — | — | — |
| Tiled KSampler | ✅ | ✅ | — | — | — | ✅ (opt) | — | — |

Full node links live in each workflow's `README.md`.
