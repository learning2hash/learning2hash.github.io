---
layout: publication
title: Theoretically-efficient And Practical Parallel DBSCAN
authors: Yiqiu Wang, Yan Gu, Julian Shun
conference: Proceedings of the 2020 ACM SIGMOD International Conference on Management
  of Data
year: 2020
bibkey: wang2019theoretically
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.06255'}]
tags: []
short_authors: Yiqiu Wang, Yan Gu, Julian Shun
---
The DBSCAN method for spatial clustering has received significant attention
due to its applicability in a variety of data analysis tasks. There are fast
sequential algorithms for DBSCAN in Euclidean space that take \\(O(nlog n)\\) work
for two dimensions, sub-quadratic work for three or more dimensions, and can be
computed approximately in linear work for any constant number of dimensions.
However, existing parallel DBSCAN algorithms require quadratic work in the
worst case, making them inefficient for large datasets. This paper bridges the
gap between theory and practice of parallel DBSCAN by presenting new parallel
algorithms for Euclidean exact DBSCAN and approximate DBSCAN that match the
work bounds of their sequential counterparts, and are highly parallel
(polylogarithmic depth). We present implementations of our algorithms along
with optimizations that improve their practical performance. We perform a
comprehensive experimental evaluation of our algorithms on a variety of
datasets and parameter settings. Our experiments on a 36-core machine with
hyper-threading show that we outperform existing parallel DBSCAN
implementations by up to several orders of magnitude, and achieve speedups by
up to 33x over the best sequential algorithms.