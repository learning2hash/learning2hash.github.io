---
layout: publication
title: 'QFF: Quantized Fourier Features For Neural Field Representations'
authors: Jae Yong Lee, Yuqun Wu, Chuhang Zou, Shenlong Wang, Derek Hoiem
conference: Arxiv
year: 2022
bibkey: lee2022qff
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.00914'}]
tags: ["Quantization"]
short_authors: Lee et al.
---
Multilayer perceptrons (MLPs) learn high frequencies slowly. Recent
approaches encode features in spatial bins to improve speed of learning
details, but at the cost of larger model size and loss of continuity. Instead,
we propose to encode features in bins of Fourier features that are commonly
used for positional encoding. We call these Quantized Fourier Features (QFF).
As a naturally multiresolution and periodic representation, our experiments
show that using QFF can result in smaller model size, faster training, and
better quality outputs for several applications, including Neural Image
Representations (NIR), Neural Radiance Field (NeRF) and Signed Distance
Function (SDF) modeling. QFF are easy to code, fast to compute, and serve as a
simple drop-in addition to many neural field representations.