---
layout: publication
title: 'MPAD: A New Dimension-reduction Method For Preserving Nearest Neighbors In
  High-dimensional Vector Search'
authors: Jiuzhou Fu, Dongfang Zhao
conference: Arxiv
year: 2025
bibkey: fu2025mpad
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.16335'}]
tags: ["Similarity Search", "Unsupervised"]
short_authors: Jiuzhou Fu, Dongfang Zhao
---
High-dimensional vector embeddings are widely used in retrieval systems, yet
dimensionality reduction (DR) is seldom applied due to its tendency to distort
nearest-neighbor (NN) structure critical for search. Existing DR techniques
such as PCA and UMAP optimize global or manifold-preserving criteria, rather
than retrieval-specific objectives. We present MPAD: Maximum Pairwise Absolute
Difference, an unsupervised DR method that explicitly preserves approximate NN
relations by maximizing the margin between k-NNs and non-k-NNs under a soft
orthogonality constraint. This design enables MPAD to retain ANN-relevant
geometry without supervision or changes to the original embedding model.
Experiments across multiple domains show that MPAD consistently outperforms
standard DR methods in preserving neighborhood structure, enabling more
accurate search in reduced dimensions.