---
layout: publication
title: Curvature Regularization To Prevent Distortion In Graph Embedding
authors: Hongbin Pei, Bingzhe Wei, Kevin Chen-Chuan Chang, Chunxu Zhang, Bo Yang
conference: Arxiv
year: 2020
bibkey: pei2020curvature
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.14211'}]
tags: []
short_authors: Pei et al.
---
Recent research on graph embedding has achieved success in various
applications. Most graph embedding methods preserve the proximity in a graph
into a manifold in an embedding space. We argue an important but neglected
problem about this proximity-preserving strategy: Graph topology patterns,
while preserved well into an embedding manifold by preserving proximity, may
distort in the ambient embedding Euclidean space, and hence to detect them
becomes difficult for machine learning models. To address the problem, we
propose curvature regularization, to enforce flatness for embedding manifolds,
thereby preventing the distortion. We present a novel angle-based sectional
curvature, termed ABS curvature, and accordingly three kinds of curvature
regularization to induce flat embedding manifolds during graph embedding. We
integrate curvature regularization into five popular proximity-preserving
embedding methods, and empirical results in two applications show significant
improvements on a wide range of open graph datasets.