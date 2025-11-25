---
layout: publication
title: Scalable Solution For Approximate Nearest Subspace Search
authors: Masakazu Iwamura, Masataka Konishi, Koichi Kise
conference: Arxiv
year: 2016
bibkey: iwamura2016scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.08810'}]
tags: ["Large Scale Search", "Scalability", "Similarity Search"]
short_authors: Masakazu Iwamura, Masataka Konishi, Koichi Kise
---
Finding the nearest subspace is a fundamental problem and influential to many
applications. In particular, a scalable solution that is fast and accurate for
a large problem has a great impact. The existing methods for the problem are,
however, useless in a large-scale problem with a large number of subspaces and
high dimensionality of the feature space. A cause is that they are designed
based on the traditional idea to represent a subspace by a single point. In
this paper, we propose a scalable solution for the approximate nearest subspace
search (ANSS) problem. Intuitively, the proposed method represents a subspace
by multiple points unlike the existing methods. This makes a large-scale ANSS
problem tractable. In the experiment with 3036 subspaces in the
1024-dimensional space, we confirmed that the proposed method was 7.3 times
faster than the previous state-of-the-art without loss of accuracy.