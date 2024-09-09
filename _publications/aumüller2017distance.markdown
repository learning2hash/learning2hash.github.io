---
layout: publication
title: "Distance-Sensitive hashing"
authors: Aumüller Martin, Christiani Tobias, Pagh Rasmus, Silvestri Francesco
conference: Arxiv
year: 2017
bibkey: aumüller2017distance
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.07867"}
tags: ['ARXIV', 'LSH']
---
Locality-sensitive hashing (LSH) is an important tool for managing high-dimensional noisy or uncertain data, for example in connection with data cleaning (similarity join) and noise-robust search (similarity search). However, for a number of problems the LSH framework is not known to yield good solutions, and instead ad hoc solutions have been designed for particular similarity and distance measures. For example, this is true for output-sensitive similarity search/join, and for indexes supporting annulus queries that aim to report a point close to a certain given distance from the query point. In this paper we initiate the study of distance-sensitive hashing (DSH), a generalization of LSH that seeks a family of hash functions such that the probability of two points having the same hash value is a given function of the distance between them. More precisely, given a distance space $(X, \text\{dist\})$ and a "collision probability function" (CPF) $f\colon \mathbb\{R\}\rightarrow [0,1]$ we seek a distribution over pairs of functions $(h,g)$ such that for every pair of points $x, y \in X$ the collision probability is $\Pr[h(x)=g(y)] = f(\text\{dist\}(x,y))$. Locality-sensitive hashing is the study of how fast a CPF can decrease as the distance grows. For many spaces, $f$ can be made exponentially decreasing even if we restrict attention to the symmetric case where $g=h$. We show that the asymmetry achieved by having a pair of functions makes it possible to achieve CPFs that are, for example, increasing or unimodal, and show how this leads to principled solutions to problems not addressed by the LSH framework. This includes a novel application to privacy-preserving distance estimation. We believe that the DSH framework will find further applications in high-dimensional data management.