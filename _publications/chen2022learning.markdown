---
layout: publication
title: Learning Binarized Graph Representations With Multi-faceted Quantization Reinforcement For Top-k Recommendation
authors: Chen Yankai, Guo Huifeng, Zhang Yingxue, Ma Chen, Tang Ruiming, Li Jingjie, King Irwin
conference: "Arxiv"
year: 2022
bibkey: chen2022learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2206.02115"}
tags: ['ARXIV', 'Graph', 'Quantisation']
---
Learning vectorized embeddings is at the core of various recommender systems for user-item matching. To perform efficient online inference, representation quantization, aiming to embed the latent features by a compact sequence of discrete numbers, recently shows the promising potentiality in optimizing both memory and computation overheads. However, existing work merely focuses on numerical quantization whilst ignoring the concomitant information loss issue, which, consequently, leads to conspicuous performance degradation. In this paper, we propose a novel quantization framework to learn Binarized Graph Representations for Top-K Recommendation (BiGeaR). BiGeaR introduces multi-faceted quantization reinforcement at the pre-, mid-, and post-stage of binarized representation learning, which substantially retains the representation informativeness against embedding binarization. In addition to saving the memory footprint, BiGeaR further develops solid online inference acceleration with bitwise operations, providing alternative flexibility for the realistic deployment. The empirical results over five large real-world benchmarks show that BiGeaR achieves about 22&#37;~40&#37; performance improvement over the state-of-the-art quantization-based recommender system, and recovers about 95&#37;~102&#37; of the performance capability of the best full-precision counterpart with over 8x time and space reduction.
