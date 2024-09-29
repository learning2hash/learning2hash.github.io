---
layout: publication
title: Multi45;resolution Hashing For Fast Pairwise Summations
authors: Charikar Moses, Siminelakis Paris
conference: "Arxiv"
year: 2018
bibkey: charikar2018hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.07635"}
tags: ['ARXIV', 'Independent']
---
A basic computational primitive in the analysis of massive datasets is summing simple functions over a large number of objects. Modern applications pose an additional challenge in that such functions often depend on a parameter vector y (query) that is unknown a priori. Given a set of points X⊂ R^123;d125; and a pairwise function wR^123;d125;× R^123;d125;to 01 we study the problem of designing a data45;structure that enables sublinear45;time approximation of the summation Z95;123;w125;(y)=frac123;1125;123;X125;∑95;123;xin X125;w(xy) for any query yin R^123;d125;. By combining ideas from Harmonic Analysis (partitions of unity and approximation theory) with Hashing45;Based45;Estimators Charikar Siminelakis FOCS17 we provide a general framework for designing such data structures through hashing that reaches far beyond what previous techniques allowed. A key design principle is a collection of T≥ 1 hashing schemes with collision probabilities p95;123;1125;ldots p95;123;T125; such that sup95;123;tin T125;123;p95;123;t125;(xy)125; = Theta(sqrt123;w(xy)125;). This leads to a data45;structure that approximates Z95;123;w125;(y) using a sub45;linear number of samples from each hash family. Using this new framework along with Distance Sensitive Hashing Aumuller Christiani Pagh Silvestri PODS18 we show that such a collection can be constructed and evaluated efficiently for any log45;convex function w(xy)=e^123;φ(langle xyrangle)125; of the inner product on the unit sphere xyin mathcal123;S125;^123;d45;1125;. Our method leads to data structures with sub45;linear query time that significantly improve upon random sampling and can be used for Kernel Density or Partition Function Estimation. We provide extensions of our result from the sphere to R^123;d125; and from scalar functions to vector functions.
