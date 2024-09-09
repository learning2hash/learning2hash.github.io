---
layout: publication
title: TransHash Transformer-based Hamming Hashing for Efficient Image Retrieval
authors: Chen Yongbiao, Zhang Sheng, Liu Fangxin, Chang Zhigang, Ye Mang, Qi Zhengwei
conference: "Arxiv"
year: 2021
bibkey: chen2021transhash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2105.01823"}
tags: ['ARXIV', 'Image Retrieval']
---
Deep hamming hashing has gained growing popularity in approximate nearest neighbour search for large-scale image retrieval. Until now the deep hashing for the image retrieval community has been dominated by convolutional neural network architectures e.g. . In this paper inspired by the recent advancements of vision transformers we present a pure transformer-based framework for deep hashing learning. Concretely our framework is composed of two major modules (1) Based on (ViT) we design a siamese vision transformer backbone for image feature extraction. To learn fine-grained features we innovate a dual-stream feature learning on top of the transformer to learn discriminative global and local features. (2) Besides we adopt a Bayesian learning scheme with a dynamically constructed similarity matrix to learn compact binary hash codes. The entire framework is jointly trained in an end-to-end manner.~To the best of our knowledge this is the first work to tackle deep hashing learning problems without convolutional neural networks (). We perform comprehensive experiments on three widely-studied datasets and . The experiments have evidenced our superiority against the existing state-of-the-art deep hashing methods. Specifically we achieve 8.2\ 2.6\ 12.7\ performance gains in terms of average for different hash bit lengths on three public datasets respectively.
