---
layout: publication
title: Spectral Clustering Using Eigenspectrum Shape Based Nystrom Sampling
authors: Djallel Bouneffouf
conference: Arxiv
year: 2020
bibkey: bouneffouf2020spectral
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.11416'}]
tags: []
short_authors: Djallel Bouneffouf
---
Spectral clustering has shown a superior performance in analyzing the cluster
structure. However, its computational complexity limits its application in
analyzing large-scale data. To address this problem, many low-rank matrix
approximating algorithms are proposed, including the Nystrom method - an
approach with proven approximate error bounds. There are several algorithms
that provide recipes to construct Nystrom approximations with variable
accuracies and computing times. This paper proposes a scalable Nystrom-based
clustering algorithm with a new sampling procedure, Centroid Minimum Sum of
Squared Similarities (CMS3), and a heuristic on when to use it. Our heuristic
depends on the eigen spectrum shape of the dataset, and yields competitive
low-rank approximations in test datasets compared to the other state-of-the-art
methods