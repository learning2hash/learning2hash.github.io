---
layout: publication
title: Codes With Locality In The Rank And Subspace Metrics
authors: Swanand Kadhe, Salim El Rouayheb, Iwan Duursma, Alex Sprintson
conference: Arxiv
year: 2017
bibkey: kadhe2017codes
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05944'}]
tags: ["Compact Codes", "Distance Metric Learning", "Locality Sensitive Hashing"]
short_authors: Kadhe et al.
---
We extend the notion of locality from the Hamming metric to the rank and
subspace metrics. Our main contribution is to construct a class of array codes
with locality constraints in the rank metric. Our motivation for constructing
such codes stems from designing codes for efficient data recovery from
correlated and/or mixed (i.e., complete and partial) failures in distributed
storage systems. Specifically, the proposed local rank-metric codes can recover
locally from 'crisscross errors and erasures', which affect a limited number of
rows and/or columns of the storage system. We also derive a Singleton-like
upper bound on the minimum rank distance of (linear) codes with 'rank-locality'
constraints. Our proposed construction achieves this bound for a broad range of
parameters. The construction builds upon Tamo and Barg's method for
constructing locally repairable codes with optimal minimum Hamming distance.
Finally, we construct a class of constant-dimension subspace codes (also known
as Grassmannian codes) with locality constraints in the subspace metric. The
key idea is to show that a Grassmannian code with locality can be easily
constructed from a rank-metric code with locality by using the lifting method
proposed by Silva et al. We present an application of such codes for
distributed storage systems, wherein nodes are connected over a network that
can introduce errors and erasures.