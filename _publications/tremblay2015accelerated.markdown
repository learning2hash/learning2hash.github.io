---
layout: publication
title: Accelerated Spectral Clustering Using Graph Filtering Of Random Signals
authors: Nicolas Tremblay, Gilles Puy, Pierre Borgnat, Remi Gribonval, Pierre Vandergheynst
conference: 2016 IEEE International Conference on Acoustics, Speech and Signal Processing
  (ICASSP)
year: 2016
bibkey: tremblay2015accelerated
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.08863'}]
tags: ["ICASSP"]
short_authors: Tremblay et al.
---
We build upon recent advances in graph signal processing to propose a faster
spectral clustering algorithm. Indeed, classical spectral clustering is based
on the computation of the first k eigenvectors of the similarity matrix'
Laplacian, whose computation cost, even for sparse matrices, becomes
prohibitive for large datasets. We show that we can estimate the spectral
clustering distance matrix without computing these eigenvectors: by graph
filtering random signals. Also, we take advantage of the stochasticity of these
random vectors to estimate the number of clusters k. We compare our method to
classical spectral clustering on synthetic data, and show that it reaches equal
performance while being faster by a factor at least two for large datasets.