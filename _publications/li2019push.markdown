---
layout: publication
title: "Push for Quantization: Deep Fisher Hashing"
authors: Yunqiang Li, Wenjie Pei, Yufei zha, Jan van Gemert
conference: BMVC
year: 2019
bibkey: li2019push
additional_links:
   - {name: "PDF", url: "https://128.84.21.199/abs/1909.00206"}
tags: ['BMVC', 'CNN', 'Image Retrieval', 'Quantisation']
---
Current massive datasets demand light-weight access for analysis. Discrete hashing methods are thus beneficial because they map high-dimensional data to compact binary codes that are efficient to store and process, while preserving semantic similarity. To optimize powerful deep learning methods for image hashing, gradient-based methods are required. Binary codes, however, are discrete and thus have no continuous derivatives. Relaxing the problem by solving it in a continuous space and then quantizing the solution is not guaranteed to yield separable binary codes. The quantization needs to be included in the optimization. In this paper we push for quantization: We optimize maximum class separability in the binary space. We introduce a margin on distances between dissimilar image pairs as measured in the binary space. In addition to pair-wise distances, we draw inspiration from Fisher's Linear Discriminant Analysis (Fisher LDA) to maximize the binary distances between classes and at the same time minimize the binary distance of images within the same class. Experiments on CIFAR-10, NUS-WIDE and ImageNet100 demonstrate compact codes comparing favorably to the current state of the art.
