---
layout: publication
title: Massively Parallel Algorithms And Hardness For Single-linkage Clustering Under
  \(\ell_p\)-distances
authors: Grigory Yaroslavtsev, Adithya Vadapalli
conference: Arxiv
year: 2017
bibkey: yaroslavtsev2017massively
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01431'}]
tags: ["Efficiency"]
short_authors: Grigory Yaroslavtsev, Adithya Vadapalli
---
We present massively parallel (MPC) algorithms and hardness of approximation
results for computing Single-Linkage Clustering of \(n\) input \(d\)-dimensional
vectors under Hamming, \(\ell_1, ℓ₂\) and \(\ell_\infty\) distances. All our
algorithms run in \(O(log n)\) rounds of MPC for any fixed \(d\) and achieve
\((1+\epsilon)\)-approximation for all distances (except Hamming for which we
show an exact algorithm). We also show constant-factor inapproximability
results for \(o(log n)\)-round algorithms under standard MPC hardness
assumptions (for sufficiently large dimension depending on the distance used).
Efficiency of implementation of our algorithms in Apache Spark is demonstrated
through experiments on a variety of datasets exhibiting speedups of several
orders of magnitude.