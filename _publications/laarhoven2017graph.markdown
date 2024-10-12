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
We take a first step towards a rigorous asymptotic analysis of graph-based approaches for finding (approximate) nearest neighbors in high-dimensional spaces, by analyzing the complexity of (randomized) greedy walks on the approximate near neighbor graph. For random data sets of size \(n = 2^\&amp;\#123;o(d)\&amp;\#125;\) on the \(d\)-dimensional Euclidean unit sphere, using near neighbor graphs we can provably solve the approximate nearest neighbor problem with approximation factor \(c > 1\) in query time \(n^\&amp;\#123;\rho\_q + o(1)\&amp;\#125;\) and space $n^&amp;\#123;1 + \rho\_s + o(1)&amp;\#125;\(, for arbitrary \)\rho\_q, \rho\_s \geq 0$ satisfying \begin&amp;\#123;align&amp;\#125; (2c^2 - 1) \rho\_q + 2 c^2 (c^2 - 1) \sqrt&amp;\#123;\rho\_s (1 - \rho\_s)&amp;\#125; \geq c^4. \end&amp;\#123;align&amp;\#125; Graph-based near neighbor searching is especially competitive with hash-based methods for small \(c\) and near-linear memory, and in this regime the asymptotic scaling of a greedy graph-based search matches the recent optimal hash-based trade-offs of Andoni-Laarhoven-Razenshteyn-Waingarten [SODA'17]. We further study how the trade-offs scale when the data set is of size $n = 2^&amp;\#123;\Theta(d)&amp;\#125;$, and analyze asymptotic complexities when applying these results to lattice sieving.
