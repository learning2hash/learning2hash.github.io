---
layout: publication
title: Tensor-train Point Cloud Compression And Efficient Approximate Nearest-neighbor
  Search
authors: Georgii Novikov, Alexander Gneushev, Alexey Kadeishvili, Ivan Oseledets
conference: Arxiv
year: 2024
bibkey: novikov2024tensor
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.04462'}]
tags: [Evaluation, Similarity Search]
short_authors: Novikov et al.
---
Nearest-neighbor search in large vector databases is crucial for various
machine learning applications. This paper introduces a novel method using
tensor-train (TT) low-rank tensor decomposition to efficiently represent point
clouds and enable fast approximate nearest-neighbor searches. We propose a
probabilistic interpretation and utilize density estimation losses like Sliced
Wasserstein to train TT decompositions, resulting in robust point cloud
compression. We reveal an inherent hierarchical structure within TT point
clouds, facilitating efficient approximate nearest-neighbor searches. In our
paper, we provide detailed insights into the methodology and conduct
comprehensive comparisons with existing methods. We demonstrate its
effectiveness in various scenarios, including out-of-distribution (OOD)
detection problems and approximate nearest-neighbor (ANN) search tasks.