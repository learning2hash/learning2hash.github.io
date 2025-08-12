---
layout: publication
title: Dynamic Grained Encoder For Vision Transformers
authors: Lin Song, Songyang Zhang, Songtao Liu, Zeming Li, Xuming He, Hongbin Sun,
  Jian Sun, Nanning Zheng
conference: Arxiv
year: 2023
bibkey: song2023dynamic
citations: 11
additional_links: [{name: Code, url: 'https://github.com/StevenGrove/vtpack'}, {name: Paper,
    url: 'https://arxiv.org/abs/2301.03831'}]
tags: ["Efficiency"]
short_authors: Song et al.
---
Transformers, the de-facto standard for language modeling, have been recently
applied for vision tasks. This paper introduces sparse queries for vision
transformers to exploit the intrinsic spatial redundancy of natural images and
save computational costs. Specifically, we propose a Dynamic Grained Encoder
for vision transformers, which can adaptively assign a suitable number of
queries to each spatial region. Thus it achieves a fine-grained representation
in discriminative regions while keeping high efficiency. Besides, the dynamic
grained encoder is compatible with most vision transformer frameworks. Without
bells and whistles, our encoder allows the state-of-the-art vision transformers
to reduce computational complexity by 40%-60% while maintaining comparable
performance on image classification. Extensive experiments on object detection
and segmentation further demonstrate the generalizability of our approach. Code
is available at https://github.com/StevenGrove/vtpack.