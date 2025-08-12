---
layout: publication
title: 'MASTAF: A Model-agnostic Spatio-temporal Attention Fusion Network For Few-shot
  Video Classification'
authors: Rex Liu, Huanle Zhang, Hamed Pirsiavash, Xin Liu
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: liu2021mastaf
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04585'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
We propose MASTAF, a Model-Agnostic Spatio-Temporal Attention Fusion network
for few-shot video classification. MASTAF takes input from a general video
spatial and temporal representation,e.g., using 2D CNN, 3D CNN, and Video
Transformer. Then, to make the most of such representations, we use self- and
cross-attention models to highlight the critical spatio-temporal region to
increase the inter-class variations and decrease the intra-class variations.
Last, MASTAF applies a lightweight fusion network and a nearest neighbor
classifier to classify each query video. We demonstrate that MASTAF improves
the state-of-the-art performance on three few-shot video classification
benchmarks(UCF101, HMDB51, and Something-Something-V2), e.g., by up to 91.6%,
69.5%, and 60.7% for five-way one-shot video classification, respectively.