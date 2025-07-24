---
layout: publication
title: Adaptive Estimation For Approximate K-nearest-neighbor Computations
authors: Daniel Lejeune, Richard G. Baraniuk, Reinhard Heckel
conference: Proceedings of Machine Learning Research 89 (2019)3099-3107
year: 2019
bibkey: lejeune2019adaptive
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.09465'}]
tags: []
short_authors: Daniel Lejeune, Richard G. Baraniuk, Reinhard Heckel
---
Algorithms often carry out equally many computations for "easy" and "hard"
problem instances. In particular, algorithms for finding nearest neighbors
typically have the same running time regardless of the particular problem
instance. In this paper, we consider the approximate k-nearest-neighbor
problem, which is the problem of finding a subset of O(k) points in a given set
of points that contains the set of k nearest neighbors of a given query point.
We propose an algorithm based on adaptively estimating the distances, and show
that it is essentially optimal out of algorithms that are only allowed to
adaptively estimate distances. We then demonstrate both theoretically and
experimentally that the algorithm can achieve significant speedups relative to
the naive method.