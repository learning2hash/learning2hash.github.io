---
layout: publication
title: 'Arkade: K-nearest Neighbor Search With Non-euclidean Distances Using GPU Ray
  Tracing'
authors: Durga Mandarapu, Vani Nagarajan, Artem Pelenitsyn, Milind Kulkarni
conference: Proceedings of the 38th ACM International Conference on Supercomputing
year: 2024
bibkey: mandarapu2023arkade
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.09168'}]
tags: ["Distance Metric Learning", "Evaluation", "Tree Based ANN"]
short_authors: Mandarapu et al.
---
High-performance implementations of \(k\)-Nearest Neighbor Search (\(k\)NN) in
low dimensions use tree-based data structures. Tree algorithms are hard to
parallelize on GPUs due to their irregularity. However, newer Nvidia GPUs offer
hardware support for tree operations through ray-tracing cores. Recent works
have proposed using RT cores to implement \(k\)NN search, but they all have a
hardware-imposed constraint on the distance metric used in the search -- the
Euclidean distance. We propose and implement two reductions to support \(k\)NN
for a broad range of distances other than the Euclidean distance: Arkade
Filter-Refine and Arkade Monotone Transformation, each of which allows
non-Euclidean distance-based nearest neighbor queries to be performed in terms
of the Euclidean distance. With our reductions, we observe that \(k\)NN search
time speedups range between \(1.6\)x-\(200\)x and \(1.3\)x-\(33.1\)x over various
state-of-the-art GPU shader core and RT core baselines, respectively. In
evaluation, we provide several insights on RT architectures' ability to
efficiently build and traverse the tree by analyzing the \(k\)NN search time
trends.