---
layout: publication
title: High-performance And Flexible Parallel Algorithms For Semisort And Related
  Problems
authors: Xiaojun Dong, Yunshu Wu, Zhongqi Wang, Laxman Dhulipala, Yan Gu, Yihan Sun
conference: Proceedings of the 35th ACM Symposium on Parallelism in Algorithms and
  Architectures
year: 2023
bibkey: dong2023high
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.10078'}]
tags: []
short_authors: Dong et al.
---
Semisort is a fundamental algorithmic primitive widely used in the design and
analysis of efficient parallel algorithms. It takes input as an array of
records and a function extracting a *key* per record, and reorders them so
that records with equal keys are contiguous. Since many applications only
require collecting equal values, but not fully sorting the input, semisort is
broadly applicable, e.g., in string algorithms, graph analytics, and geometry
processing, among many other domains. However, despite dozens of recent papers
that use semisort in their theoretical analysis and the existence of an
asymptotically optimal parallel semisort algorithm, most implementations of
these parallel algorithms choose to implement semisort by using comparison or
integer sorting in practice, due to potential performance issues in existing
semisort implementations.
  In this paper, we revisit the semisort problem, with the goal of achieving a
high-performance parallel semisort implementation with a flexible interface.
Our approach can easily extend to two related problems, *histogram* and
*collect-reduce*. Our algorithms achieve strong speedups in practice, and
importantly, outperform state-of-the-art parallel sorting and semisorting
methods for almost all settings we tested, with varying input sizes,
distribution, and key types. We also test two important applications with
real-world data, and show that our algorithms improve the performance over
existing approaches. We believe that many other parallel algorithm
implementations can be accelerated using our results.