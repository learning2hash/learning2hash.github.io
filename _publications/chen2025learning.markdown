---
layout: publication
title: Learning Binarized Representations With Pseudo-positive Sample Enhancement
  For Efficient Graph Collaborative Filtering
authors: Yankai Chen, Yue Que, Xinni Zhang, Chen Ma, Irwin King
conference: ACM Transactions on Information Systems
year: 2025
bibkey: chen2025learning
citations: 0
additional_links: [{name: Code, url: 'https://github.com/QueYork/BiGeaR-SS'}, {name: Paper,
    url: 'https://arxiv.org/abs/2506.02750'}]
tags: ["Quantization"]
short_authors: Chen et al.
---
Learning vectorized embeddings is fundamental to many recommender systems for user-item matching. To enable efficient online inference, representation binarization, which embeds latent features into compact binary sequences, has recently shown significant promise in optimizing both memory usage and computational overhead. However, existing approaches primarily focus on numerical quantization, neglecting the associated information loss, which often results in noticeable performance degradation. To address these issues, we study the problem of graph representation binarization for efficient collaborative filtering. Our findings indicate that explicitly mitigating information loss at various stages of embedding binarization has a significant positive impact on performance. Building on these insights, we propose an enhanced framework, BiGeaR++, which specifically leverages supervisory signals from pseudo-positive samples, incorporating both real item data and latent embedding samples. Compared to its predecessor BiGeaR, BiGeaR++ introduces a fine-grained inference distillation mechanism and an effective embedding sample synthesis approach. Empirical evaluations across five real-world datasets demonstrate that the new designs in BiGeaR++ work seamlessly well with other modules, delivering substantial improvements of around 1%-10% over BiGeaR and thus achieving state-of-the-art performance compared to the competing methods. Our implementation is available at https://github.com/QueYork/BiGeaR-SS.