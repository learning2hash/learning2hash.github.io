---
layout: publication
title: Approximate K-flat Nearest Neighbor Search
authors: Mulzer Wolfgang, Nguyen Huy L., Seiferth Paul, Stein Yannik
conference: "Arxiv"
year: 2014
bibkey: mulzer2014approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1411.1519"}
tags: ['ARXIV']
---
Let \(k\) be a nonnegative integer. In the approximate \(k\)-flat nearest neighbor (\(k\)-ANN) problem, we are given a set \(P \subset \mathbb\{R\}^d\) of \(n\) points in \(d\)-dimensional space and a fixed approximation factor \(c > 1\). Our goal is to preprocess \(P\) so that we can efficiently answer approximate \(k\)-flat nearest neighbor queries: given a \(k\)-flat \(F\), find a point in \(P\) whose distance to \(F\) is within a factor \(c\) of the distance between \(F\) and the closest point in \(P\). The case \(k = 0\) corresponds to the well-studied approximate nearest neighbor problem, for which a plethora of results are known, both in low and high dimensions. The case \(k = 1\) is called approximate line nearest neighbor. In this case, we are aware of only one provably efficient data structure, due to Andoni, Indyk, Krauthgamer, and Nguyen. For $k \geq 2$, we know of no previous results. We present the first efficient data structure that can handle approximate nearest neighbor queries for arbitrary \(k\). We use a data structure for \(0\)-ANN-queries as a black box, and the performance depends on the parameters of the \(0\)-ANN solution: suppose we have an \(0\)-ANN structure with query time \(O(n^\{\rho\})\) and space requirement \(O(n^\{1+\sigma\})\), for \(\rho, \sigma > 0\). Then we can answer \(k\)-ANN queries in time \(O(n^\{k/(k + 1 - \rho) + t\})\) and space \(O(n^\{1+\sigma k/(k + 1 - \rho)\} + n\log^\{O(1/t)\} n)\). Here, \(t > 0\) is an arbitrary constant and the \(O\)-notation hides exponential factors in \(k\), \(1/t\), and \(c\) and polynomials in \(d\). Our new data structures also give an improvement in the space requirement over the previous result for \(1\)-ANN: we can achieve near-linear space and sublinear query time, a further step towards practical applications where space constitutes the bottleneck.
