---
layout: publication
title: Hardness Of Approximate Nearest Neighbor Search
authors: Rubinstein Aviad
conference: "Arxiv"
year: 2018
bibkey: rubinstein2018hardness
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1803.00904"}
tags: ['ARXIV']
---
We prove conditional near-quadratic running time lower bounds for approximate Bichromatic Closest Pair with Euclidean, Manhattan, Hamming, or edit distance. Specifically, unless the Strong Exponential Time Hypothesis (SETH) is false, for every $\delta>0$ there exists a constant $\epsilon>0$ such that computing a $(1+\epsilon)$-approximation to the Bichromatic Closest Pair requires $n^\{2-\delta\}$ time. In particular, this implies a near-linear query time for Approximate Nearest Neighbor search with polynomial preprocessing time. Our reduction uses the Distributed PCP framework of [ARW'17], but obtains improved efficiency using Algebraic Geometry (AG) codes. Efficient PCPs from AG codes have been constructed in other settings before [BKKMS'16, BCGRS'17], but our construction is the first to yield new hardness results.
