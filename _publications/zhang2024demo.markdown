---
layout: publication
title: DEMO A Statistical Perspective For Efficient Image-text Matching
authors: Zhang Fan, Hua Xian-sheng, Chen Chong, Luo Xiao
conference: "Arxiv"
year: 2024
bibkey: zhang2024demo
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2405.11496"}
tags: ['ARXIV', 'Cross Modal', 'Supervised']
---
Image-text matching has been a long-standing problem which seeks to connect vision and language through semantic understanding. Due to the capability to manage large-scale raw data unsupervised hashing-based approaches have gained prominence recently. They typically construct a semantic similarity structure using the natural distance which subsequently provides guidance to the model optimization process. However the similarity structure could be biased at the boundaries of semantic distributions causing error accumulation during sequential optimization. To tackle this we introduce a novel hashing approach termed Distribution-based Structure Mining with Consistency Learning (DEMO) for efficient image-text matching. From a statistical view DEMO characterizes each image using multiple augmented views which are considered as samples drawn from its intrinsic semantic distribution. Then we employ a non-parametric distribution divergence to ensure a robust and precise similarity structure. In addition we introduce collaborative consistency learning which not only preserves the similarity structure in the Hamming space but also encourages consistency between retrieval distribution from different directions in a self-supervised manner. Through extensive experiments on three benchmark image-text matching datasets we demonstrate that DEMO achieves superior performance compared with many state-of-the-art methods.
