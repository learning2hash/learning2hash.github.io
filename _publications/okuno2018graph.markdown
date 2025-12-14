---
layout: publication
title: Graph Embedding With Shifted Inner Product Similarity And Its Improved Approximation
  Capability
authors: Akifumi Okuno, Geewook Kim, Hidetoshi Shimodaira
conference: Arxiv
year: 2018
bibkey: okuno2018graph
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.03463'}]
tags: [Distance Metric Learning, Graph-based ANN, Datasets]
short_authors: Akifumi Okuno, Geewook Kim, Hidetoshi Shimodaira
---
We propose shifted inner-product similarity (SIPS), which is a novel yet very
simple extension of the ordinary inner-product similarity (IPS) for
neural-network based graph embedding (GE). In contrast to IPS, that is limited
to approximating positive-definite (PD) similarities, SIPS goes beyond the
limitation by introducing bias terms in IPS; we theoretically prove that SIPS
is capable of approximating not only PD but also conditionally PD (CPD)
similarities with many examples such as cosine similarity, negative Poincare
distance and negative Wasserstein distance. Since SIPS with sufficiently large
neural networks learns a variety of similarities, SIPS alleviates the need for
configuring the similarity function of GE. Approximation error rate is also
evaluated, and experiments on two real-world datasets demonstrate that graph
embedding using SIPS indeed outperforms existing methods.