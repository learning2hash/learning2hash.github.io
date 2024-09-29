---
layout: publication
title: Correlation Hashing Network For Efficient Cross45;modal Retrieval
authors: Cao Yue, Long Mingsheng, Wang Jianmin, Yu Philip S.
conference: "Arxiv"
year: 2016
bibkey: cao2016correlation
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1602.06697"}
tags: ['ARXIV', 'Cross Modal', 'Quantisation', 'Supervised']
---
Hashing is widely applied to approximate nearest neighbor search for large45;scale multimodal retrieval with storage and computation efficiency. Cross45;modal hashing improves the quality of hash coding by exploiting semantic correlations across different modalities. Existing cross45;modal hashing methods first transform data into low45;dimensional feature vectors and then generate binary codes by another separate quantization step. However suboptimal hash codes may be generated since the quantization error is not explicitly minimized and the feature representation is not jointly optimized with the binary codes. This paper presents a Correlation Hashing Network (CHN) approach to cross45;modal hashing which jointly learns good data representation tailored to hash coding and formally controls the quantization error. The proposed CHN is a hybrid deep architecture that constitutes a convolutional neural network for learning good image representations a multilayer perception for learning good text representations two hashing layers for generating compact binary codes and a structured max45;margin loss that integrates all things together to enable learning similarity45;preserving and high45;quality hash codes. Extensive empirical study shows that CHN yields state of the art cross45;modal retrieval performance on standard benchmarks.
