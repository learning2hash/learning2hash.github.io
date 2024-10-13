---
layout: publication
title: Language Embedded 3D Gaussians For Open-vocabulary Scene Understanding
authors: Shi Jin-chuan, Wang Miao, Duan Hao-bin, Guan Shao-hua
conference: "Arxiv"
year: 2023
bibkey: shi2023language
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.18482"}
tags: ['ARXIV', 'Cross Modal', 'Quantisation', 'Supervised']
---
Open-vocabulary querying in 3D space is challenging but essential for scene
understanding tasks such as object localization and segmentation.
Language-embedded scene representations have made progress by incorporating
language features into 3D spaces. However, their efficacy heavily depends on
neural networks that are resource-intensive in training and rendering. Although
recent 3D Gaussians offer efficient and high-quality novel view synthesis,
directly embedding language features in them leads to prohibitive memory usage
and decreased performance. In this work, we introduce Language Embedded 3D
Gaussians, a novel scene representation for open-vocabulary query tasks.
Instead of embedding high-dimensional raw semantic features on 3D Gaussians, we
propose a dedicated quantization scheme that drastically alleviates the memory
requirement, and a novel embedding procedure that achieves smoother yet high
accuracy query, countering the multi-view feature inconsistencies and the
high-frequency inductive bias in point-based representations. Our comprehensive
experiments show that our representation achieves the best visual quality and
language querying accuracy across current language-embedded representations,
while maintaining real-time rendering frame rates on a single desktop GPU.
