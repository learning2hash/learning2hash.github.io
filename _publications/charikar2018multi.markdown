---
layout: publication
title: Multi-resolution Hashing For Fast Pairwise Summations
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018multi
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.07635"}
tags: ['ARXIV', 'Independent']
---
A basic computational primitive in the analysis of massive datasets is summing simple functions over a large number of objects. Modern applications pose an additional challenge in that such functions often depend on a parameter vector y (query) that is unknown a priori. Given a set of points X(subset) (mathbbR)^d and a pairwise function w(mathbbR)^d(times) (mathbbR)^d(to) 01 we study the problem of designing a data-structure that enables sublinear-time approximation of the summation Z_w(y)=(frac1)X(sum)_x(in) Xw(xy) for any query y(in) (mathbbR)^d. By combining ideas from Harmonic Analysis (partitions of unity and approximation theory) with Hashing-Based-Estimators Charikar Siminelakis FOCS17 we provide a general framework for designing such data structures through hashing that reaches far beyond what previous techniques allowed. A key design principle is a collection of T(geq) 1 hashing schemes with collision probabilities p_1(ldots) p_T such that (sup)_t(in) Tp_t(xy) = (Theta)((sqrt)w(xy)). This leads to a data-structure that approximates Z_w(y) using a sub-linear number of samples from each hash family. Using this new framework along with Distance Sensitive Hashing Aumuller Christiani Pagh Silvestri PODS18 we show that such a collection can be constructed and evaluated efficiently for any log-convex function w(xy)=e^(phi)((langle) xy(rangle)) of the inner product on the unit sphere xy(in) (mathcalS)^d-1. Our method leads to data structures with sub-linear query time that significantly improve upon random sampling and can be used for Kernel Density or Partition Function Estimation. We provide extensions of our result from the sphere to (mathbbR)^d and from scalar functions to vector functions.
