---
layout: publication
title: Multi-Resolution Hashing for Fast Pairwise Summations
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018multiresolution
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.07635"}
tags: ['ARXIV', 'FOCS']
---
A basic computational primitive in the analysis of massive datasets is summing simple functions over a large number of objects. Modern applications pose an additional challenge in that such functions often depend on a parameter vector y (query) that is unknown a priori. Given a set of points Xsubset ^d and a pairwise function w^dtimes ^dto 01 we study the problem of designing a data-structure that enables sublinear-time approximation of the summation Z_w(y)=Xsum_xin Xw(xy) for any query yin ^d. By combining ideas from Harmonic Analysis (partitions of unity and approximation theory) with Hashing-Based-Estimators Charikar Siminelakis FOCS17 we provide a general framework for designing such data structures through hashing that reaches far beyond what previous techniques allowed. A key design principle is a collection of Tgeq 1 hashing schemes with collision probabilities p_1ldots p_T such that sup_tin Tp_t(xy) = Theta(). This leads to a data-structure that approximates Z_w(y) using a sub-linear number of samples from each hash family. Using this new framework along with Distance Sensitive Hashing Aumuller Christiani Pagh Silvestri PODS18 we show that such a collection can be constructed and evaluated efficiently for any log-convex function w(xy)=e^phi(langle xyrangle) of the inner product on the unit sphere xyin ^d-1. Our method leads to data structures with sub-linear query time that significantly improve upon random sampling and can be used for Kernel Density or Partition Function Estimation. We provide extensions of our result from the sphere to ^d and from scalar functions to vector functions.
