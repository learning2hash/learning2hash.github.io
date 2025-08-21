---
layout: publication
title: Efficient Algorithms For T-distributed Stochastic Neighborhood Embedding
authors: George C. Linderman, Manas Rachh, Jeremy G. Hoskins, Stefan Steinerberger,
  Yuval Kluger
conference: Arxiv
year: 2017
bibkey: linderman2017efficient
citations: 192
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.09005'}]
tags: ["Datasets"]
short_authors: Linderman et al.
---
t-distributed Stochastic Neighborhood Embedding (t-SNE) is a method for
dimensionality reduction and visualization that has become widely popular in
recent years. Efficient implementations of t-SNE are available, but they scale
poorly to datasets with hundreds of thousands to millions of high dimensional
data-points. We present Fast Fourier Transform-accelerated Interpolation-based
t-SNE (FIt-SNE), which dramatically accelerates the computation of t-SNE. The
most time-consuming step of t-SNE is a convolution that we accelerate by
interpolating onto an equispaced grid and subsequently using the fast Fourier
transform to perform the convolution. We also optimize the computation of input
similarities in high dimensions using multi-threaded approximate nearest
neighbors. We further present a modification to t-SNE called "late
exaggeration," which allows for easier identification of clusters in t-SNE
embeddings. Finally, for datasets that cannot be loaded into the memory, we
present out-of-core randomized principal component analysis (oocPCA), so that
the top principal components of a dataset can be computed without ever fully
loading the matrix, hence allowing for t-SNE of large datasets to be computed
on resource-limited machines.