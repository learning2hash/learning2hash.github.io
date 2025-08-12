---
layout: publication
title: Efficient Principal Subspace Projection Of Streaming Data Through Fast Similarity
  Matching
authors: Andrea Giovannucci, Victor Minden, Cengiz Pehlevan, Dmitri B. Chklovskii
conference: 2018 IEEE International Conference on Big Data (Big Data)
year: 2018
bibkey: giovannucci2018efficient
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.02083'}]
tags: []
short_authors: Giovannucci et al.
---
Big data problems frequently require processing datasets in a streaming
fashion, either because all data are available at once but collectively are
larger than available memory or because the data intrinsically arrive one data
point at a time and must be processed online. Here, we introduce a
computationally efficient version of similarity matching, a framework for
online dimensionality reduction that incrementally estimates the top
K-dimensional principal subspace of streamed data while keeping in memory only
the last sample and the current iterate. To assess the performance of our
approach, we construct and make public a test suite containing both a synthetic
data generator and the infrastructure to test online dimensionality reduction
algorithms on real datasets, as well as performant implementations of our
algorithm and competing algorithms with similar aims. Among the algorithms
considered we find our approach to be competitive, performing among the best on
both synthetic and real data.