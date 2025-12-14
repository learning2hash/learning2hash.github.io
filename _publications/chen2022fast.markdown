---
layout: publication
title: Fast And Exact Fixed-radius Neighbor Search Based On Sorting
authors: "Xinye Chen, Stefan G\xFCttel"
conference: Arxiv
year: 2022
bibkey: chen2022fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.07679'}]
tags: [Tree-based ANN, Evaluation, Efficiency]
short_authors: "Xinye Chen, Stefan G\xFCttel"
---
Fixed-radius near neighbor search is a fundamental data operation that
retrieves all data points within a user-specified distance to a query point.
There are efficient algorithms that can provide fast approximate query
responses, but they often have a very compute-intensive indexing phase and
require careful parameter tuning. Therefore, exact brute force and tree-based
search methods are still widely used. Here we propose a new fixed-radius near
neighbor search method, called SNN, that significantly improves over brute
force and tree-based methods in terms of index and query time, provably returns
exact results, and requires no parameter tuning. SNN exploits a sorting of the
data points by their first principal component to prune the query search space.
Further speedup is gained from an efficient implementation using high-level
Basic Linear Algebra Subprograms (BLAS). We provide theoretical analysis of our
method and demonstrate its practical performance when used stand-alone and when
applied within the DBSCAN clustering algorithm.