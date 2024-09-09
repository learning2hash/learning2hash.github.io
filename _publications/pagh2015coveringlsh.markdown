---
layout: publication
title: "CoveringLSH: Locality-sensitive Hashing without False Negatives"
authors: Pagh Rasmus
conference: Arxiv
year: 2015
bibkey: pagh2015coveringlsh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.03225"}
tags: ['ARXIV', 'LSH']
---
We consider a new construction of locality-sensitive hash functions for Hamming space that is \emph{covering} in the sense that is it guaranteed to produce a collision for every pair of vectors within a given radius $r$. The construction is \emph{efficient} in the sense that the expected number of hash collisions between vectors at distance~$cr$, for a given $c>1$, comes close to that of the best possible data independent LSH without the covering guarantee, namely, the seminal LSH construction of Indyk and Motwani (STOC '98). The efficiency of the new construction essentially \emph{matches} their bound when the search radius is not too large --- e.g., when $cr = o(\log(n)/\log\log n)$, where $n$ is the number of points in the data set, and when $cr = \log(n)/k$ where $k$ is an integer constant. In general, it differs by at most a factor $\ln(4)$ in the exponent of the time bounds. As a consequence, LSH-based similarity search in Hamming space can avoid the problem of false negatives at little or no cost in efficiency.