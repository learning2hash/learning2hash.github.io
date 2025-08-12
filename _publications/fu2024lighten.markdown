---
layout: publication
title: 'Lighten CARAFE: Dynamic Lightweight Upsampling With Guided Reassemble Kernels'
authors: Ruigang Fu, Qingyong Hu, Xiaohu Dong, Yinghui Gao, Biao Li, Ping Zhong
conference: Arxiv
year: 2024
bibkey: fu2024lighten
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Fu0511/Dynamic-Lightweight-Upsampling'},
  {name: Paper, url: 'https://arxiv.org/abs/2410.22139'}]
tags: []
short_authors: Fu et al.
---
As a fundamental operation in modern machine vision models, feature
upsampling has been widely used and investigated in the literatures. An ideal
upsampling operation should be lightweight, with low computational complexity.
That is, it can not only improve the overall performance but also not affect
the model complexity. Content-aware Reassembly of Features (CARAFE) is a
well-designed learnable operation to achieve feature upsampling. Albeit
encouraging performance achieved, this method requires generating large-scale
kernels, which brings a mass of extra redundant parameters, and inherently has
limited scalability. To this end, we propose a lightweight upsampling
operation, termed Dynamic Lightweight Upsampling (DLU) in this paper. In
particular, it first constructs a small-scale source kernel space, and then
samples the large-scale kernels from the kernel space by introducing learnable
guidance offsets, hence avoiding introducing a large collection of trainable
parameters in upsampling. Experiments on several mainstream vision tasks show
that our DLU achieves comparable and even better performance to the original
CARAFE, but with much lower complexity, e.g., DLU requires 91% fewer parameters
and at least 63% fewer FLOPs (Floating Point Operations) than CARAFE in the
case of 16x upsampling, but outperforms the CARAFE by 0.3% mAP in object
detection. Code is available at
https://github.com/Fu0511/Dynamic-Lightweight-Upsampling.