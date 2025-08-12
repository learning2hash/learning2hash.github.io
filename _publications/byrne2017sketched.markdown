---
layout: publication
title: Sketched Clustering Via Hybrid Approximate Message Passing
authors: Evan Byrne, Antoine Chatalic, Remi Gribonval, Philip Schniter
conference: IEEE Transactions on Signal Processing
year: 2019
bibkey: byrne2017sketched
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.02849'}]
tags: ["Datasets"]
short_authors: Byrne et al.
---
In sketched clustering, a dataset of \\(T\\) samples is first sketched down to a
vector of modest size, from which the centroids are subsequently extracted.
Advantages include i) reduced storage complexity and ii) centroid extraction
complexity independent of \\(T\\). For the sketching methodology recently proposed
by Keriven, et al., which can be interpreted as a random sampling of the
empirical characteristic function, we propose a sketched clustering algorithm
based on approximate message passing. Numerical experiments suggest that our
approach is more efficient than the state-of-the-art sketched clustering
algorithm "CL-OMPR" (in both computational and sample complexity) and more
efficient than k-means++ when \\(T\\) is large.