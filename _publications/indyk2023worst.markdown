---
layout: publication
title: 'Worst-case Performance Of Popular Approximate Nearest Neighbor Search Implementations:
  Guarantees And Limitations'
authors: Piotr Indyk, Haike Xu
conference: Arxiv
year: 2023
bibkey: indyk2023worst
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.19126'}]
tags: [Efficiency, Datasets, Evaluation, Graph-based ANN]
short_authors: Piotr Indyk, Haike Xu
---
Graph-based approaches to nearest neighbor search are popular and powerful
tools for handling large datasets in practice, but they have limited
theoretical guarantees. We study the worst-case performance of recent
graph-based approximate nearest neighbor search algorithms, such as HNSW, NSG
and DiskANN. For DiskANN, we show that its "slow preprocessing" version
provably supports approximate nearest neighbor search query with constant
approximation ratio and poly-logarithmic query time, on data sets with bounded
"intrinsic" dimension. For the other data structure variants studied, including
DiskANN with "fast preprocessing", HNSW and NSG, we present a family of
instances on which the empirical query time required to achieve a "reasonable"
accuracy is linear in instance size. For example, for DiskANN, we show that the
query procedure can take at least \(0.1 n\) steps on instances of size \(n\) before
it encounters any of the \(5\) nearest neighbors of the query.