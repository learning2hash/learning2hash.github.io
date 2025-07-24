---
layout: publication
title: Hessian-aware Quantized Node Embeddings For Recommendation
authors: Huiyuan Chen, Kaixiong Zhou, Kwei-herng Lai, Chin-chia Michael Yeh, Yan Zheng,
  Xia Hu, Hao Yang
conference: Proceedings of the 17th ACM Conference on Recommender Systems
year: 2023
bibkey: chen2023hessian
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01032'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Recommender Systems", "Scalability"]
short_authors: Chen et al.
---
Graph Neural Networks (GNNs) have achieved state-of-the-art performance in
recommender systems. Nevertheless, the process of searching and ranking from a
large item corpus usually requires high latency, which limits the widespread
deployment of GNNs in industry-scale applications. To address this issue, many
methods compress user/item representations into the binary embedding space to
reduce space requirements and accelerate inference. Also, they use the
Straight-through Estimator (STE) to prevent vanishing gradients during
back-propagation. However, the STE often causes the gradient mismatch problem,
leading to sub-optimal results.
  In this work, we present the Hessian-aware Quantized GNN (HQ-GNN) as an
effective solution for discrete representations of users/items that enable fast
retrieval. HQ-GNN is composed of two components: a GNN encoder for learning
continuous node embeddings and a quantized module for compressing
full-precision embeddings into low-bit ones. Consequently, HQ-GNN benefits from
both lower memory requirements and faster inference speeds compared to vanilla
GNNs. To address the gradient mismatch problem in STE, we further consider the
quantized errors and its second-order derivatives for better stability. The
experimental results on several large-scale datasets show that HQ-GNN achieves
a good balance between latency and performance.