---
layout: publication
title: 'ARM 4-BIT PQ: Simd-based Acceleration For Approximate Nearest Neighbor Search
  On ARM'
authors: Yusuke Matsui, Yoshiki Imaizumi, Naoya Miyamoto, Naoki Yoshifuji
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: matsui2022arm
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.02505'}]
tags: ["Efficiency", "ICASSP", "Quantization"]
short_authors: Matsui et al.
---
We accelerate the 4-bit product quantization (PQ) on the ARM architecture.
Notably, the drastic performance of the conventional 4-bit PQ strongly relies
on x64-specific SIMD register, such as AVX2; hence, we cannot yet achieve such
good performance on ARM. To fill this gap, we first bundle two 128-bit
registers as one 256-bit component. We then apply shuffle operations for each
using the ARM-specific NEON instruction. By making this simple but critical
modification, we achieve a dramatic speedup for the 4-bit PQ on an ARM
architecture. Experiments show that the proposed method consistently achieves a
10x improvement over the naive PQ with the same accuracy.