---
layout: publication
title: Scalable Graph Attention-based Instance Selection Via Mini-batch Sampling And
  Hierarchical Hashing
authors: Zahiriddin Rustamov, Ayham Zaitouny, Nazar Zaki
conference: Arxiv
year: 2025
citations: 0
bibkey: rustamov2025scalable
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.20293'}]
tags: [Hashing Methods, Efficient Learning]
---
Instance selection (IS) is important in machine learning for reducing dataset
size while keeping key characteristics. Current IS methods often struggle with
capturing complex relationships in high-dimensional spaces and scale with large
datasets. This paper introduces a graph attention-based instance selection
(GAIS) method that uses attention mechanisms to identify informative instances
through their structural relationships in graph representations. We present two
approaches for scalable graph construction: a distance-based mini-batch
sampling technique that reduces computation through strategic batch processing,
and a hierarchical hashing approach that allows for efficient similarity
computation through random projections. The mini-batch approach keeps class
distributions through stratified sampling, while the hierarchical hashing
method captures relationships at multiple granularities through single-level,
multi-level, and multi-view variants. Experiments across 39 datasets show that
GAIS achieves reduction rates above 96% while maintaining or improving model
performance relative to state-of-the-art IS methods. The findings shows that
the distance-based mini-batch approach offers an optimal balance of efficiency
and effectiveness for large-scale datasets, while multi-view variants provide
superior performance for complex, high-dimensional data, demonstrating that
attention-based importance scoring can effectively identify instances crucial
for maintaining decision boundaries without requiring exhaustive pairwise
comparisons.