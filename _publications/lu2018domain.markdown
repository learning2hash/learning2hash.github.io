---
layout: publication
title: Domain-aware SE Network For Sketch-based Image Retrieval With Multiplicative
  Euclidean Margin Softmax
authors: Peng Lu, Gao Huang, Hangyu Lin, Wenming Yang, Guodong Guo, Yanwei Fu
conference: Arxiv
year: 2018
bibkey: lu2018domain
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.04275'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Lu et al.
---
This paper proposes a novel approach for Sketch-Based Image Retrieval (SBIR),
for which the key is to bridge the gap between sketches and photos in terms of
the data representation. Inspired by channel-wise attention explored in recent
years, we present a Domain-Aware Squeeze-and-Excitation (DASE) network, which
seamlessly incorporates the prior knowledge of sample sketch or photo into SE
module and make the SE module capable of emphasizing appropriate channels
according to domain signal. Accordingly, the proposed network can switch its
mode to achieve a better domain feature with lower intra-class discrepancy.
Moreover, while previous works simply focus on minimizing intra-class distance
and maximizing inter-class distance, we introduce a loss function, named
Multiplicative Euclidean Margin Softmax (MEMS), which introduces multiplicative
Euclidean margin into feature space and ensure that the maximum intra-class
distance is smaller than the minimum inter-class distance. This facilitates
learning a highly discriminative feature space and ensures a more accurate
image retrieval result. Extensive experiments are conducted on two widely used
SBIR benchmark datasets. Our approach achieves better results on both datasets,
surpassing the state-of-the-art methods by a large margin.