---
layout: publication
title: Faster Approximation Algorithms For K-center Via Data Reduction
authors: Arnold Filtser, Shaofeng H. -C. Jiang, Yi Li, Anurag Murty Naredla, Ioannis
  Psarros, Qiaoyuan Yang, Qin Zhang
conference: Arxiv
year: 2025
bibkey: filtser2025faster
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.05888'}]
tags: []
short_authors: Filtser et al.
---
We study efficient algorithms for the Euclidean \(k\)-Center problem, focusing
on the regime of large \(k\). We take the approach of data reduction by
considering \(\alpha\)-coreset, which is a small subset \(S\) of the dataset \(P\)
such that any \(\beta\)-approximation on \(S\) is an \((\alpha +
\beta)\)-approximation on \(P\). We give efficient algorithms to construct
coresets whose size is \(k \cdot o(n)\), which immediately speeds up existing
approximation algorithms. Notably, we obtain a near-linear time
\(O(1)\)-approximation when \(k = n^c\) for any \(0 < c < 1\). We validate the
performance of our coresets on real-world datasets with large \(k\), and we
observe that the coreset speeds up the well-known Gonzalez algorithm by up to
\(4\) times, while still achieving similar clustering cost. Technically, one of
our coreset results is based on a new efficient construction of consistent
hashing with competitive parameters. This general tool may be of independent
interest for algorithm design in high dimensional Euclidean spaces.