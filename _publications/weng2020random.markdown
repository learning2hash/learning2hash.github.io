---
layout: publication
title: 'Random VLAD Based Deep Hashing For Efficient Image Retrieval'
authors: Li Weng, Lingzhi Ye, Jiangmin Tian, Jiuwen Cao, Jianzhong Wang
conference: "Arxiv"
year: 2020
citations: 1
bibkey: weng2020random
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2002.02333'}
tags: ['Cross-Modal', 'Deep', 'Quantisation', 'Retrieval Models', 'Evaluation', 'Deep Hashing', 'Quantization', 'Hashing', 'Applications']
---
Image hash algorithms generate compact binary representations that can be
quickly matched by Hamming distance, thus become an efficient solution for
large-scale image retrieval. This paper proposes RV-SSDH, a deep image hash
algorithm that incorporates the classical VLAD (vector of locally aggregated
descriptors) architecture into neural networks. Specifically, a novel neural
network component is formed by coupling a random VLAD layer with a latent hash
layer through a transform layer. This component can be combined with
convolutional layers to realize a hash algorithm. We implement RV-SSDH as a
point-wise algorithm that can be efficiently trained by minimizing
classification error and quantization loss. Comprehensive experiments show this
new architecture significantly outperforms baselines such as NetVLAD and SSDH,
and offers a cost-effective trade-off in the state-of-the-art. In addition, the
proposed random VLAD layer leads to satisfactory accuracy with low complexity,
thus shows promising potentials as an alternative to NetVLAD.
