---
layout: publication
title: 'Simultaneous Compression And Quantization: A Joint Approach For Efficient
  Unsupervised Hashing'
authors: Hoang et al.
conference: Computer Vision and Image Understanding
year: 2019
bibkey: hoang2019simultaneous
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.06645'}]
tags: ["Quantization", "Unsupervised", "Neural Hashing", "Supervised", "Hashing Methods"]
---
For unsupervised data-dependent hashing, the two most important requirements
are to preserve similarity in the low-dimensional feature space and to minimize
the binary quantization loss. A well-established hashing approach is Iterative
Quantization (ITQ), which addresses these two requirements in separate steps.
In this paper, we revisit the ITQ approach and propose novel formulations and
algorithms to the problem. Specifically, we propose a novel approach, named
Simultaneous Compression and Quantization (SCQ), to jointly learn to compress
(reduce dimensionality) and binarize input data in a single formulation under
strict orthogonal constraint. With this approach, we introduce a loss function
and its relaxed version, termed Orthonormal Encoder (OnE) and Orthogonal
Encoder (OgE) respectively, which involve challenging binary and orthogonal
constraints. We propose to attack the optimization using novel algorithms based
on recent advances in cyclic coordinate descent approach. Comprehensive
experiments on unsupervised image retrieval demonstrate that our proposed
methods consistently outperform other state-of-the-art hashing methods.
Notably, our proposed methods outperform recent deep neural networks and GAN
based hashing in accuracy, while being very computationally-efficient.