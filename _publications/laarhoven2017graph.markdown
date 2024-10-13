---
layout: publication
title: Graph-based Time-space Trade-offs For Approximate Near Neighbors
authors: Laarhoven Thijs
conference: ""
year: 2017
bibkey: laarhoven2017graph
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1712.03158"}
tags: ['Graph', 'Independent']
---
We take a first step towards a rigorous asymptotic analysis of graph-based approaches for finding (approximate) nearest neighbors in high-dimensional spaces, by analyzing the complexity of (randomized) greedy walks on the approximate near neighbor graph. For random data sets of size \(n = 2^{o(d)}\) on the \(d\)-dimensional Euclidean unit sphere, using near neighbor graphs we can provably solve the approximate nearest neighbor problem with approximation factor \(c > 1\) in query time \(n^{\rho_q + o(1)}\) and space $n^\{1 + \rho\_s + o(1)\}\(, for arbitrary \)\rho\_q, \rho\_s \geq 0$ satisfying \begin\\{align\\} (2c^2 - 1) \rho\_q + 2 c^2 (c^2 - 1) \sqrt\\{\rho\_s (1 - \rho\_s)\\} \geq c^4. \end\\{align\\} Graph-based near neighbor searching is especially competitive with hash-based methods for small \(c\) and near-linear memory, and in this regime the asymptotic scaling of a greedy graph-based search matches the recent optimal hash-based trade-offs of Andoni-Laarhoven-Razenshteyn-Waingarten [SODA'17]. We further study how the trade-offs scale when the data set is of size $n = 2^\{\Theta(d)\}$, and analyze asymptotic complexities when applying these results to lattice sieving.
