---
layout: publication
title: 'DEANN: Speeding Up Kernel-density Estimation Using Approximate Nearest Neighbor Search'
authors: Matti Karppa, Martin Aumüller, Rasmus Pagh
conference: "Arxiv"
year: 2021
citations: 2
bibkey: karppa2021speeding
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2107.02736'}
tags: ['Hashing Methods', 'Approximate Nearest Neighbor Search', 'Tools and Libraries', 'ANN Search', 'Hashing Fundamentals']
---
Kernel Density Estimation (KDE) is a nonparametric method for estimating the
shape of a density function, given a set of samples from the distribution.
Recently, locality-sensitive hashing, originally proposed as a tool for nearest
neighbor search, has been shown to enable fast KDE data structures. However,
these approaches do not take advantage of the many other advances that have
been made in algorithms for nearest neighbor algorithms. We present an
algorithm called Density Estimation from Approximate Nearest Neighbors (DEANN)
where we apply Approximate Nearest Neighbor (ANN) algorithms as a black box
subroutine to compute an unbiased KDE. The idea is to find points that have a
large contribution to the KDE using ANN, compute their contribution exactly,
and approximate the remainder with Random Sampling (RS). We present a
theoretical argument that supports the idea that an ANN subroutine can speed up
the evaluation. Furthermore, we provide a C++ implementation with a Python
interface that can make use of an arbitrary ANN implementation as a subroutine
for kernel density estimation. We show empirically that our implementation
outperforms state of the art implementations in all high dimensional datasets
we considered, and matches the performance of RS in cases where the ANN yield
no gains in performance.
