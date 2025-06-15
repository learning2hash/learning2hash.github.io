---
layout: publication
title: Deep Optimized Multiple Description Image Coding Via Scalar Quantization Learning
authors: Zhao Lijun, Bai Huihui, Wang Anhong, Zhao Yao
conference: "Arxiv"
year: 2020
citations: 0
bibkey: zhao2020deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2001.03851"}
tags: ['ARXIV', 'Quantisation', 'Supervised', 'Self-Supervised']
---
In this paper, we introduce a deep multiple description coding (MDC)
framework optimized by minimizing multiple description (MD) compressive loss.
First, MD multi-scale-dilated encoder network generates multiple description
tensors, which are discretized by scalar quantizers, while these quantized
tensors are decompressed by MD cascaded-ResBlock decoder networks. To greatly
reduce the total amount of artificial neural network parameters, an
auto-encoder network composed of these two types of network is designed as a
symmetrical parameter sharing structure. Second, this autoencoder network and a
pair of scalar quantizers are simultaneously learned in an end-to-end
self-supervised way. Third, considering the variation in the image spatial
distribution, each scalar quantizer is accompanied by an importance-indicator
map to generate MD tensors, rather than using direct quantization. Fourth, we
introduce the multiple description structural similarity distance loss, which
implicitly regularizes the diversified multiple description generations, to
explicitly supervise multiple description diversified decoding in addition to
MD reconstruction loss. Finally, we demonstrate that our MDC framework performs
better than several state-of-the-art MDC approaches regarding image coding
efficiency when tested on several commonly available datasets.
