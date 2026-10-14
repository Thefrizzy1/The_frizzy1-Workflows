# Benchmarks: the same workflows on a 4 GB laptop and a 12 GB desktop

Every number here was measured on the creator's own machines with the bench-suite harness (one job at a time, wall
time from queue to output, VRAM from nvidia-smi in MiB, system RAM and swap in GB). Quality isn't scored here: the
outputs are in the videos.

- **Laptop:** ASUS Zephyrus M16 · RTX 3050 Ti Laptop **4 GB** · i7-12700H · 16 GB RAM
- **Desktop:** RTX 3060 **12 GB** · Ryzen 5 5600X · 32 GB RAM

## Round 3 (2026-10-14): the newest workflows, the same graph on both machines
Laptop: ASUS Zephyrus M16, RTX 3050 Ti 4 GB, i7-12700H, 16 GB RAM, plugged in, Armoury Crate Ultimate, fans 100%.
It ran 2026-10-14, 16:23–17:12, on ComfyUI 0.39.2 with PyTorch attention. Kroma, Krea 2 and Ming pick Comfy Kitchen inside the graph.
Desktop: RTX 3060 12 GB, 32 GB RAM, ran 2026-10-12/13 on ComfyUI 0.39.2 with Sage attention.
Same graph, prompt, seed, size and inputs on both machines. All 15 laptop jobs were OK on the first try, no out-of-memory.

| Job | Laptop 4 GB | Desktop 12 GB | Laptop peaks: VRAM / RAM / swap | Differences besides the machine |
|---|---|---|---|---|
| YuE2 · text to music, ABC off | 3:26 | 40 s | 3854 MiB / 13.9 GB / 0.1 GB | attention (Sage vs PyTorch) |
| YuE2 · text to music, ABC on | 4:32 | 59 s | 3828 MiB / 14.0 GB / 0.1 GB | attention |
| YuE2 · cover | 5:20 (cold) | 50 s | 3879 MiB / 14.1 GB / 0.1 GB | attention; laptop cold (SheetSage2 load) |
| Kroma w4a8 · 1K soccer | 38 s | 24 s | 3220 MiB / 13.8 GB / 0.6 GB | — |
| Kroma w4a8 · 1K editorial | 42 s | 19 s | 3220 MiB / 13.8 GB / 0.6 GB | — |
| Kroma w4a8 · 2K soccer | 2:55 | 1:23 | 3908 MiB / 15.5 GB / 0.7 GB | — |
| Ming 0.1 · 1K poster | 42 s | 17 s | 3906 MiB / 14.5 GB / 1.2 GB | — |
| Ming 0.1 · transparent sticker | 44 s | 17 s | 3910 MiB / 14.6 GB / 1.2 GB | — |
| Qwen 2.1 Turbo · 1K image | 26 s | 13 s | 3432 MiB / 13.8 GB / 1.2 GB | text encoder (laptop w4a8, desktop int8); attention |
| Qwen 2.1 Turbo · edit | 52 s | 24 s | 3512 MiB / 14.1 GB / 1.4 GB | text encoder; attention |
| Qwen 2.1 Turbo · remove background | 50 s | 29 s | 3512 MiB / 13.8 GB / 1.4 GB | text encoder; attention |
| Krea 2 Turbo int8 · 1K soccer | 38 s | 22 s | 3240 MiB / 13.8 GB / 1.4 GB | — |
| Krea 2 Turbo int8 · 1K editorial | 42 s | 20 s | 3240 MiB / 13.8 GB / 1.4 GB | — |
| H3 Ultimate v2.3 · T2V 0.4 MP 5 s | 8:46 | 2:53 | 3508 MiB / 15.7 GB / 9.1 GB | model + encoder (laptop W4A8 + Q2_K_M GGUF, desktop int8 + nvfp4); attention |
| H3 Ultimate v2.3 · Extend with sound | 11:27 | 3:53 | 3900 MiB / 15.7 GB / 9.0 GB | model + encoder; attention |

"—" = the same files, and the attention is picked inside the graph on both machines. VRAM is nvidia-smi MiB; RAM and swap in GB.

Cold warm-ups on the laptop (not reported above): YuE2 12 s, Kroma 28 s, Ming 26 s, Qwen 16 s, Krea 2 int8 22 s, H3 3:27.

For context, with different prompts and versions: round 1 (ComfyUI 0.37.4) ran Krea 2 Turbo as the **Q4_K_M GGUF** at 1K, 2:23–2:35 per image, with other prompts.

Notes:
- ComfyUI 0.39.2 loads scipy at startup. Windows Smart App Control blocked one of scipy's files, and Frizzy turned Smart App Control off himself.
- The laptop stays on 0.39.2 from now on. Rounds 1+2 ran on 0.37.4.

## Rounds 1-2 (2026-10-01 / 02): GGUF models on the 4 GB laptop (ComfyUI 0.37.4)
Warm-up runs left out (the first run after a model load). A **failed** row is an out-of-memory try; the next row is its retry.

| job | model | size | try | result | wall | exec | sampling s/step | VRAM peak | RAM peak | swap peak | GPU temp max | started |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| t1_img_zimage_portrait_1024 | Z-Image Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 1:00 | 59 s | 5.697 | 3730 MiB | 15.42 GB | 0.88 GB | 91 °C | 2026-10-01 16:21:22 |
| t1_img_zimage_text_1024 | Z-Image Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 1:04 | 1:03 | 6.121 | 3730 MiB | 15.05 GB | 1.4 GB | 90 °C | 2026-10-01 16:22:23 |
| t1_img_zimage_crowd_1024 | Z-Image Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 1:06 | 1:06 | 6.544 | 3378 MiB | 14.95 GB | 0.97 GB | 89 °C | 2026-10-01 16:23:27 |
| t1_img_krea2_portrait_1024 | Krea 2 Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 2:23 | 2:22 | 15.082 | 3572 MiB | 15.47 GB | 3.57 GB | 89 °C | 2026-10-01 16:25:47 |
| t1_img_krea2_text_1024 | Krea 2 Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 2:33 | 2:32 | 16.603 | 3604 MiB | 15.44 GB | 2.69 GB | 92 °C | 2026-10-01 16:28:10 |
| t1_img_krea2_crowd_1024 | Krea 2 Turbo Q4_K_M GGUF | 1024x1024 | 1 | OK | 2:35 | 2:34 | 16.552 | 3508 MiB | 15.5 GB | 3.5 GB | 90 °C | 2026-10-01 16:30:43 |
| t2_img_zimage_portrait_2048 | Z-Image Turbo Q4_K_M GGUF | 2048x2048 | 1 | OK | 5:04 | 5:03 | 33.701 | 3912 MiB | 15.68 GB | 1.56 GB | 90 °C | 2026-10-01 16:36:05 |
| t2_img_zimage_text_2048 | Z-Image Turbo Q4_K_M GGUF | 2048x2048 | 1 | OK | 5:22 | 5:22 | 35.678 | 3863 MiB | 15.2 GB | 1.85 GB | 93 °C | 2026-10-01 16:41:09 |
| t2_img_zimage_crowd_2048 | Z-Image Turbo Q4_K_M GGUF | 2048x2048 | 1 | OK | 5:26 | 5:26 | 36.05 | 3862 MiB | 14.77 GB | 1.66 GB | 90 °C | 2026-10-01 16:46:32 |
| t2_wan22anim_face_320x576 | Wan 2.2 Animate Q3_K_M GGUF + face video | 320x576 | 1 | OK | 7:14 | 7:13 | 1.434, 50.882 | 3884 MiB | 15.69 GB | 11.28 GB | 90 °C | 2026-10-01 17:55:33 |
| t1_ltx_i2v_cyborg_576x320 | LTX 2.5 distilled Q3_K_M GGUF | 576x320 | 1 | OK | 5:42 | 5:40 | 8.565, 26.772 | 3893 MiB | 15.69 GB | 8.98 GB | 89 °C | 2026-10-01 18:20:49 |
| t2_ltx_t2v_832x448 | LTX 2.5 distilled Q3_K_M GGUF | 832x448 | 1 | OK | 5:32 | 5:31 | 8.535, 15.751 | 3892 MiB | 15.69 GB | 9.08 GB | 91 °C | 2026-10-01 18:26:31 |
| t2_ltx_flf2v_576x320 | LTX 2.5 distilled Q3_K_M GGUF | 576x320 | 1 | OK | 3:49 | 3:47 | 12.696 | 3862 MiB | 15.69 GB | 8.25 GB | 92 °C | 2026-10-01 18:41:45 |
| t3_img_qwen21turbo_text_1024 | Qwen Image 2.1 Q4_K_M GGUF + Viggle 6-step | 1024x1024 | 1 | OK | 54 s | 54 s | 7.402 | 3192 MiB | 13.91 GB | 0.74 GB | 89 °C | 2026-10-01 19:02:41 |
| t3_h3_t2v_448x256 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo | 448x256 | 1 | OK | 13:09 | 13:07 | 82.732 | 3898 MiB | 15.69 GB | 7.69 GB | 89 °C | 2026-10-01 19:24:32 |
| t3_h3_i2v_cyborg_576x320 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo | 576x320 | 1 | OK | 11:39 | 11:38 | 70.614 | 3895 MiB | 15.69 GB | 7.44 GB | 94 °C | 2026-10-01 19:37:41 |
| t2_ltx_i2v_cyborg_832x448 | LTX 2.5 distilled Q3_K_M GGUF | 832x448 | 1 | OK | 5:43 | 5:41 | 8.598, 18.883 | 3849 MiB | 15.69 GB | 9.62 GB | 92 °C | 2026-10-01 20:04:01 |
| t1_ltx_t2v_576x320 | LTX 2.5 distilled Q3_K_M GGUF | 576x320 | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 12 s |  |  | 3799 MiB | 14.89 GB | 1.59 GB | 89 °C | 2026-10-01 20:18:35 |
| t1_ltx_t2v_576x320 | LTX 2.5 distilled Q3_K_M GGUF | 576x320 | 2 | OK (cold) | 3:52 | 3:51 | 7.464, 10.66 | 3815 MiB | 15.65 GB | 9.03 GB | 90 °C | 2026-10-01 20:18:50 |
| x_ltx_t2v_0.4mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 12 s |  |  | 3800 MiB | 14.82 GB | 1.55 GB | 88 °C | 2026-10-01 21:16:16 |
| x_ltx_t2v_0.4mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 2 | OK (cold) | 7:22 | 7:21 | 9.336, 19.356 | 3832 MiB | 15.69 GB | 9.2 GB | 90 °C | 2026-10-01 21:16:31 |
| x_ltx_flf2v_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 18 s |  |  | 3816 MiB | 14.7 GB | 1.75 GB | 89 °C | 2026-10-01 21:29:40 |
| x_ltx_flf2v_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 2 | OK (cold) | 17:05 | 17:03 | 62.056 | 3848 MiB | 15.69 GB | 10.38 GB | 92 °C | 2026-10-01 21:30:01 |
| x_krea2_t2i_4mp | Krea 2 Turbo Q4_K_M GGUF |  | 1 | OK | 7:16 | 7:15 | 50.099 | 3877 MiB | 15.51 GB | 3.71 GB | 91 °C | 2026-10-01 22:32:16 |
| x_krea2_t2i_1mp_prompt-enhancer | Krea 2 Turbo Q4_K_M GGUF |  | 1 | OK | 5:50 | 5:48 | 0.671, 12.619 | 3175 MiB | 15.53 GB | 2.38 GB | 90 °C | 2026-10-01 22:39:32 |
| x_h3_t2v_0.4mp_5s_turbo8 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo |  | 1 | OK | 184:59 | 184:57 | 1540.736 | 3914 MiB | 15.69 GB | 14.24 GB | 90 °C | 2026-10-02 00:12:49 |
| x_h3_i2v_0.4mp_5s_turbo8 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo |  | 1 | OK | 183:46 | 183:44 | 1532.433 | 3951 MiB | 15.68 GB | 14.07 GB | 91 °C | 2026-10-02 03:17:48 |
| x_h3_last_0.4mp_5s_turbo8 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo |  | 1 | OK | 82:06 | 82:04 | 663.872 | 3951 MiB | 15.69 GB | 14.64 GB | 90 °C | 2026-10-02 06:21:34 |
| x_h3_flf2v_0.4mp_5s_turbo8 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo |  | 1 | OK | 20:32 | 20:30 | 116.445 | 3253 MiB | 15.69 GB | 15.93 GB | 84 °C | 2026-10-02 07:43:40 |
| t4_h3k_t2v_448x256 | MiniMax H3 FL2VA W4A8 (Kijai) + int8 VAE + Q2_K_M encoder + 8-step turbo, Comfy Kitchen attention | 448x256 | 1 | OK | 3:23 | 3:21 | 11.566 | 3825 MiB | 15.7 GB | 8.47 GB | 90 °C | 2026-10-02 11:40:37 |
| t4_h3k_i2v_cyborg_576x320 | MiniMax H3 FL2VA W4A8 (Kijai) + int8 VAE + Q2_K_M encoder + 8-step turbo, Comfy Kitchen attention | 576x320 | 1 | OK | 4:00 | 3:58 | 14.717 | 3444 MiB | 15.69 GB | 8.79 GB | 89 °C | 2026-10-02 11:44:00 |
| t4_h3k_i2v_cyborg_832x448 | MiniMax H3 FL2VA W4A8 (Kijai) + int8 VAE + Q2_K_M encoder + 8-step turbo, Comfy Kitchen attention | 832x448 | 1 | OK | 5:21 | 5:19 | 23.57 | 3833 MiB | 15.7 GB | 7.45 GB | 89 °C | 2026-10-02 11:48:00 |
| x_ltx_i2v_0.4mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | OK | 7:30 | 7:29 | 9.294, 22.23 | 3853 MiB | 15.68 GB | 9.7 GB | 89 °C | 2026-10-02 12:48:38 |
| x_ltx_t2v_0.9mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 7:42 |  |  | 3835 MiB | 15.68 GB | 9.93 GB | 90 °C | 2026-10-02 13:26:24 |
| x_ltx_i2v_0.9mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 32 s |  |  | 3875 MiB | 15.69 GB | 2.09 GB | 87 °C | 2026-10-02 13:46:43 |
| x_ltx_i2v_0.9mp_5s | LTX 2.5 distilled Q3_K_M GGUF |  | 2 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 29 s |  |  | 3875 MiB | 14.96 GB | 2.49 GB | 88 °C | 2026-10-02 13:47:18 |
| x_ltx_t2v_0.9mp_10s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 17:15 |  |  | 3915 MiB | 15.69 GB | 11.44 GB | 91 °C | 2026-10-02 13:59:14 |
| x_ltx_i2v_0.9mp_10s | LTX 2.5 distilled Q3_K_M GGUF |  | 1 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 12 s |  |  | 3853 MiB | 14.67 GB | 2.29 GB | 87 °C | 2026-10-02 14:36:14 |
| x_ltx_i2v_0.9mp_10s | LTX 2.5 distilled Q3_K_M GGUF |  | 2 | **failed**: Allocation on device 0 would exceed allowed memory. (out of memory) | 27 s |  |  | 3853 MiB | 14.7 GB | 2.04 GB | 87 °C | 2026-10-02 14:36:29 |
| x_h3_t2v_0.9mp_5s_turbo8 | MiniMax H3 FL2VA Q2_K GGUF + Q2_K_M encoder + 8-step turbo |  | 1 | OK | 126:51 | 126:50 | 913.026 | 3909 MiB | 15.69 GB | 8.74 GB | 92 °C | 2026-10-02 14:56:51 |
