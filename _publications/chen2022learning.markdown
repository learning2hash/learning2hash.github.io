---
layout: publication
title: Learning Binarized Graph Representations with Multi-faceted Quantization Reinforcement
  for Top-K Recommendation
authors: Chen et al.
conference: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2022
bibkey: chen2022learning
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.02115'}]
tags: [KDD, Recommender Systems, Quantization]
---
Learning vectorized embeddings is at the core of various recommender systems
for user-item matching. To perform efficient online inference, representation
quantization, aiming to embed the latent features by a compact sequence of
discrete numbers, recently shows the promising potentiality in optimizing both
memory and computation overheads. However, existing work merely focuses on
numerical quantization whilst ignoring the concomitant information loss issue,
which, consequently, leads to conspicuous performance degradation. In this
paper, we propose a novel quantization framework to learn Binarized Graph
Representations for Top-K Recommendation (BiGeaR). BiGeaR introduces
multi-faceted quantization reinforcement at the pre-, mid-, and post-stage of
binarized representation learning, which substantially retains the
representation informativeness against embedding binarization. In addition to
saving the memory footprint, BiGeaR further develops solid online inference
acceleration with bitwise operations, providing alternative flexibility for the
realistic deployment. The empirical results over five large real-world
benchmarks show that BiGeaR achieves about 22%~40% performance improvement over
the state-of-the-art quantization-based recommender system, and recovers about
95%~102% of the performance capability of the best full-precision counterpart
with over 8x time and space reduction.