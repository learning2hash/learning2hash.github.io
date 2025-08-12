---
layout: publication
title: On Geodesic Distances And Contextual Embedding Compression For Text Classification
authors: Rishi Jha, Kai Mihata
conference: Proceedings of the Fifteenth Workshop on Graph-Based Methods for Natural
  Language Processing (TextGraphs-15)
year: 2021
bibkey: jha2021geodesic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.11295'}]
tags: []
short_authors: Rishi Jha, Kai Mihata
---
In some memory-constrained settings like IoT devices and over-the-network
data pipelines, it can be advantageous to have smaller contextual embeddings.
We investigate the efficacy of projecting contextual embedding data (BERT) onto
a manifold, and using nonlinear dimensionality reduction techniques to compress
these embeddings. In particular, we propose a novel post-processing approach,
applying a combination of Isomap and PCA. We find that the geodesic distance
estimations, estimates of the shortest path on a Riemannian manifold, from
Isomap's k-Nearest Neighbors graph bolstered the performance of the compressed
embeddings to be comparable to the original BERT embeddings. On one dataset, we
find that despite a 12-fold dimensionality reduction, the compressed embeddings
performed within 0.1% of the original BERT embeddings on a downstream
classification task. In addition, we find that this approach works particularly
well on tasks reliant on syntactic data, when compared with linear
dimensionality reduction. These results show promise for a novel geometric
approach to achieve lower dimensional text embeddings from existing
transformers and pave the way for data-specific and application-specific
embedding compressions.