---
layout: publication
title: 'High-dimensional Approximate Nearest Neighbor Search: With Reliable And Efficient
  Distance Comparison Operations'
authors: Jianyang Gao, Cheng Long
conference: Proceedings of the ACM on Management of Data
year: 2023
bibkey: gao2023high
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09855'}]
tags: [Efficiency, Evaluation]
short_authors: Jianyang Gao, Cheng Long
---
Approximate K nearest neighbor (AKNN) search is a fundamental and challenging
problem. We observe that in high-dimensional space, the time consumption of
nearly all AKNN algorithms is dominated by that of the distance comparison
operations (DCOs). For each operation, it scans full dimensions of an object
and thus, runs in linear time wrt the dimensionality. To speed it up, we
propose a randomized algorithm named ADSampling which runs in logarithmic time
wrt to the dimensionality for the majority of DCOs and succeeds with high
probability. In addition, based on ADSampling we develop one general and two
algorithm-specific techniques as plugins to enhance existing AKNN algorithms.
Both theoretical and empirical studies confirm that: (1) our techniques
introduce nearly no accuracy loss and (2) they consistently improve the
efficiency.