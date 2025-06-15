---
layout: publication
title: 'Parlayann: Scalable And Deterministic Parallel Graph-based Approximate Nearest Neighbor Search Algorithms'
authors: Magdalen Dobson Manohar et al.
conference: "Arxiv"
year: 2023
citations: 4
bibkey: manohar2023scalable
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2305.04359'}
tags: ['Deep', 'Unsupervised', 'Retrieval Models', 'Unimodal', 'Datasets', 'Vector Indexing', 'Applications']
---
Approximate nearest-neighbor search (ANNS) algorithms are a key part of the
modern deep learning stack due to enabling efficient similarity search over
high-dimensional vector space representations (i.e., embeddings) of data. Among
various ANNS algorithms, graph-based algorithms are known to achieve the best
throughput-recall tradeoffs. Despite the large scale of modern ANNS datasets,
existing parallel graph based implementations suffer from significant
challenges to scale to large datasets due to heavy use of locks and other
sequential bottlenecks, which 1) prevents them from efficiently scaling to a
large number of processors, and 2) results in nondeterminism that is
undesirable in certain applications.
  In this paper, we introduce ParlayANN, a library of deterministic and
parallel graph-based approximate nearest neighbor search algorithms, along with
a set of useful tools for developing such algorithms. In this library, we
develop novel parallel implementations for four state-of-the-art graph-based
ANNS algorithms that scale to billion-scale datasets. Our algorithms are
deterministic and achieve high scalability across a diverse set of challenging
datasets. In addition to the new algorithmic ideas, we also conduct a detailed
experimental study of our new algorithms as well as two existing non-graph
approaches. Our experimental results both validate the effectiveness of our new
techniques, and lead to a comprehensive comparison among ANNS algorithms on
large scale datasets with a list of interesting findings.
