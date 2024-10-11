---
layout: publication
title: On The Problem Of p_1^-1 In Locality-sensitive Hashing
authors: Ahle Thomas Dybdahl
conference: "Arxiv"
year: 2020
bibkey: ahle2020problem
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.12065"}
tags: ['ARXIV', 'Independent', 'LSH']
---
A Locality-Sensitive Hash (LSH) function is called $(r,cr,p\_1,p\_2)$-sensitive, if two data-points with a distance less than $r$ collide with probability at least $p\_1$ while data points with a distance greater than $cr$ collide with probability at most $p\_2$. These functions form the basis of the successful Indyk-Motwani algorithm (STOC 1998) for nearest neighbour problems. In particular one may build a $c$-approximate nearest neighbour data structure with query time $\tilde O(n^\rho/p\_1)$ where $\rho=\frac\{\log1/p\_1\}\{\log1/p\_2\}\in(0,1)$. That is, sub-linear time, as long as $p\_1$ is not too small. This is significant since most high dimensional nearest neighbour problems suffer from the curse of dimensionality, and can't be solved exact, faster than a brute force linear-time scan of the database. Unfortunately, the best LSH functions tend to have very low collision probabilities, $p\_1$ and $p\_2$. Including the best functions for Cosine and Jaccard Similarity. This means that the $n^\rho/p\_1$ query time of LSH is often not sub-linear after all, even for approximate nearest neighbours! In this paper, we improve the general Indyk-Motwani algorithm to reduce the query time of LSH to $\tilde O(n^\rho/p\_1^\{1-\rho\})$ (and the space usage correspondingly.) Since $n^\rho p\_1^\{\rho-1\} < n \Leftrightarrow p\_1 > n^\{-1\}$, our algorithm always obtains sublinear query time, for any collision probabilities at least $1/n$. For $p\_1$ and $p\_2$ small enough, our improvement over all previous methods can be \emph\{up to a factor $n$\} in both query time and space. The improvement comes from a simple change to the Indyk-Motwani algorithm, which can easily be implemented in existing software packages.
