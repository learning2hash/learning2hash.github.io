---
layout: publication
title: Linear-time Approximation Scheme For K-means Clustering Of Affine Subspaces
authors: Kyungjin Cho, Eunjin Oh
conference: Computational Geometry
year: 2023
bibkey: cho2021linear
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.14176'}]
tags: ["Efficiency", "Unsupervised"]
short_authors: Kyungjin Cho, Eunjin Oh
---
In this paper, we present a linear-time approximation scheme for \\(k\\)-means
clustering of *incomplete* data points in \\(d\\)-dimensional Euclidean space.
An *incomplete* data point with \\(\Delta>0\\) unspecified entries is
represented as an axis-parallel affine subspaces of dimension \\(\Delta\\). The
distance between two incomplete data points is defined as the Euclidean
distance between two closest points in the axis-parallel affine subspaces
corresponding to the data points. We present an algorithm for \\(k\\)-means
clustering of axis-parallel affine subspaces of dimension \\(\Delta\\) that yields
an \\((1+\epsilon)\\)-approximate solution in \\(O(nd)\\) time. The constants hidden
behind \\(O(\cdot)\\) depend only on \\(\Delta, \epsilon\\) and \\(k\\). This improves the
\\(O(n^2 d)\\)-time algorithm by Eiben et al.[SODA'21] by a factor of \\(n\\).