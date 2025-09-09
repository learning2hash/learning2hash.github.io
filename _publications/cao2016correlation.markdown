---
layout: publication
title: Correlation Autoencoder Hashing For Supervised Cross-modal Search
authors: Yue Cao, Mingsheng Long, Jianmin Wang, Han Zhu
conference: Proceedings of the 2016 ACM on International Conference on Multimedia
  Retrieval
year: 2016
bibkey: cao2016correlation
citations: 99
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.06697'}]
tags: ["Compact Codes", "Efficiency", "Evaluation", "Hashing Methods", "Multimodal Retrieval", "Quantization", "Scalability"]
short_authors: Cao et al.
---
Hashing is widely applied to approximate nearest neighbor search for large-scale multimodal retrieval with storage and computation efficiency. Cross-modal hashing improves the quality of hash coding by exploiting semantic correlations across different modalities. Existing cross-modal hashing methods first transform data into low-dimensional feature vectors, and then generate binary codes by another separate quantization step. However, suboptimal hash codes may be generated since the quantization error is not explicitly minimized and the feature representation is not jointly optimized with the binary codes.
This paper presents a Correlation Hashing Network (CHN) approach to cross-modal hashing, which jointly learns good data representation tailored to hash coding and formally controls the quantization error. The proposed CHN is a hybrid deep architecture that constitutes a convolutional neural network for learning good image representations, a multilayer perception for learning good text representations, two hashing layers for generating compact binary codes, and a structured max-margin loss that integrates all things together to enable learning similarity-preserving and high-quality hash codes. Extensive empirical study shows that CHN yields state of the art cross-modal retrieval performance on standard benchmarks.