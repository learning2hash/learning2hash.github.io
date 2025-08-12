---
layout: publication
title: Multi-scale Wavelet Transformer For Face Forgery Detection
authors: Jie Liu, Jingjing Wang, Peng Zhang, Chunmao Wang, di Xie, Shiliang Pu
conference: Lecture Notes in Computer Science
year: 2023
bibkey: liu2022multi
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.03899'}]
tags: []
short_authors: Liu et al.
---
Currently, many face forgery detection methods aggregate spatial and
frequency features to enhance the generalization ability and gain promising
performance under the cross-dataset scenario. However, these methods only
leverage one level frequency information which limits their expressive ability.
To overcome these limitations, we propose a multi-scale wavelet transformer
framework for face forgery detection. Specifically, to take full advantage of
the multi-scale and multi-frequency wavelet representation, we gradually
aggregate the multi-scale wavelet representation at different stages of the
backbone network. To better fuse the frequency feature with the spatial
features, frequency-based spatial attention is designed to guide the spatial
feature extractor to concentrate more on forgery traces. Meanwhile,
cross-modality attention is proposed to fuse the frequency features with the
spatial features. These two attention modules are calculated through a unified
transformer block for efficiency. A wide variety of experiments demonstrate
that the proposed method is efficient and effective for both within and cross
datasets.