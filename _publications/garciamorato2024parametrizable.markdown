---
layout: publication
title: A Parametrizable Algorithm for Distributed Approximate Similarity Search with
  Arbitrary Distances
authors: Garcia-morato et al.
conference: Advances in Database Systems
year: 2024
bibkey: garciamorato2024parametrizable
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.13795'}]
tags: ["Similarity-Search"]
---
Recent studies have explored alternative distance measures for similarity
search in spaces with diverse topologies, emphasizing the importance of
selecting an appropriate distance function to improve the performance of
k-Nearest Neighbour search algorithms. However, a critical gap remains in
accommodating such diverse similarity measures, as most existing methods for
exact or approximate similarity search are explicitly designed for metric
spaces.
  To address this need, we propose PDASC (Parametrizable Distributed
Approximate Similarity Search with Clustering), a novel Approximate Nearest
Neighbour search algorithm. PDASC combines an innovative multilevel indexing
structure particularly adept at managing outliers, highly imbalanced datasets,
and sparse data distributions, with the flexibility to support arbitrary
distance functions achieved through the integration of clustering algorithms
that inherently accommodate them.
  Experimental results show that PDASC constitutes a reliable ANN search
method, suitable for operating in distributed data environments and for
handling datasets defined in different topologies, where the selection of the
most appropriate distance function is often non-trivial.