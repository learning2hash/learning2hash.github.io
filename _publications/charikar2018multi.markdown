---
layout: publication
title: Multi-Resolution Hashing for Fast Pairwise Summations
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018multi
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.07635"}
tags: ['ARXIV', 'FOCS']
---
A basic computational primitive in the analysis of massive datasets is summing simple functions over a large number of objects. Modern applications pose an additional challenge in that such functions often depend on a parameter vector y (query) that is unknown a priori. Given a set of points X\subset ^d and a pairwise function w^d\times ^d\to [0,1], we study the problem of designing a data-structure that enables sublinear-time approximation of the summation Z_w(y)=|X|\sum_x\in Xw(x,y) for any query y\in ^d. By combining ideas from Harmonic Analysis (partitions of unity and approximation theory) with Hashing-Based-Estimators [Charikar, Siminelakis FOCS'17], we provide a general framework for designing such data structures through hashing that reaches far beyond what previous techniques allowed. A key design principle is a collection of T\geq 1 hashing schemes with collision probabilities p_1,\ldots, p_T such that \sup_t\in [T]\p_t(x,y)\ = \Theta(). This leads to a data-structure that approximates Z_w(y) using a sub-linear number of samples from each hash family. Using this new framework along with Distance Sensitive Hashing [Aumuller, Christiani, Pagh, Silvestri PODS'18], we show that such a collection can be constructed and evaluated efficiently for any log-convex function w(x,y)=e^\phi(\langle x,y\rangle) of the inner product on the unit sphere x,y\in ^d-1. Our method leads to data structures with sub-linear query time that significantly improve upon random sampling and can be used for Kernel Density or Partition Function Estimation. We provide extensions of our result from the sphere to ^d and from scalar functions to vector functions.
