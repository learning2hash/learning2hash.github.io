---
layout: publication
title: On A Linear Fused Gromov-wasserstein Distance For Graph Structured Data
authors: Dai Hai Nguyen, Koji Tsuda
conference: Pattern Recognition
year: 2023
bibkey: nguyen2022linear
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.04711'}]
tags: ["Distance Metric Learning"]
short_authors: Dai Hai Nguyen, Koji Tsuda
---
We present a framework for embedding graph structured data into a vector
space, taking into account node features and topology of a graph into the
optimal transport (OT) problem. Then we propose a novel distance between two
graphs, named linearFGW, defined as the Euclidean distance between their
embeddings. The advantages of the proposed distance are twofold: 1) it can take
into account node feature and structure of graphs for measuring the similarity
between graphs in a kernel-based framework, 2) it can be much faster for
computing kernel matrix than pairwise OT-based distances, particularly fused
Gromov-Wasserstein, making it possible to deal with large-scale data sets.
After discussing theoretical properties of linearFGW, we demonstrate
experimental results on classification and clustering tasks, showing the
effectiveness of the proposed linearFGW.