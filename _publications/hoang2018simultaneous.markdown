---
layout: publication
title: "Simultaneous Compression and Quantization: A Joint Approach for Efficient Unsupervised Hashing"
authors: Hoang Tuan, Do Thanh-Toan, Le Huu, Le-Tan Dang-Khoa, Cheung Ngai-Man
conference: Arxiv
year: 2018
bibkey: hoang2018simultaneous
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1802.06645"}
tags: ['ARXIV', 'GAN', 'Image Retrieval', 'Quantisation', 'Supervised', 'Unsupervised']
---
For unsupervised data-dependent hashing, the two most important requirements are to preserve similarity in the low-dimensional feature space and to minimize the binary quantization loss. A well-established hashing approach is Iterative Quantization (ITQ), which addresses these two requirements in separate steps. In this paper, we revisit the ITQ approach and propose novel formulations and algorithms to the problem. Specifically, we propose a novel approach, named Simultaneous Compression and Quantization (SCQ), to jointly learn to compress (reduce dimensionality) and binarize input data in a single formulation under strict orthogonal constraint. With this approach, we introduce a loss function and its relaxed version, termed Orthonormal Encoder (OnE) and Orthogonal Encoder (OgE) respectively, which involve challenging binary and orthogonal constraints. We propose to attack the optimization using novel algorithms based on recent advances in cyclic coordinate descent approach. Comprehensive experiments on unsupervised image retrieval demonstrate that our proposed methods consistently outperform other state-of-the-art hashing methods. Notably, our proposed methods outperform recent deep neural networks and GAN based hashing in accuracy, while being very computationally-efficient.