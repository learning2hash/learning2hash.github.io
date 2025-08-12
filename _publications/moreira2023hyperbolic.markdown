---
layout: publication
title: 'Hyperbolic Vs Euclidean Embeddings In Few-shot Learning: Two Sides Of The
  Same Coin'
authors: "Gabriel Moreira, Manuel Marques, Jo\xE3o Paulo Costeira, Alexander Hauptmann"
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: moreira2023hyperbolic
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.10013'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Moreira et al.
---
Recent research in representation learning has shown that hierarchical data
lends itself to low-dimensional and highly informative representations in
hyperbolic space. However, even if hyperbolic embeddings have gathered
attention in image recognition, their optimization is prone to numerical
hurdles. Further, it remains unclear which applications stand to benefit the
most from the implicit bias imposed by hyperbolicity, when compared to
traditional Euclidean features. In this paper, we focus on prototypical
hyperbolic neural networks. In particular, the tendency of hyperbolic
embeddings to converge to the boundary of the Poincar\'e ball in high
dimensions and the effect this has on few-shot classification. We show that the
best few-shot results are attained for hyperbolic embeddings at a common
hyperbolic radius. In contrast to prior benchmark results, we demonstrate that
better performance can be achieved by a fixed-radius encoder equipped with the
Euclidean metric, regardless of the embedding dimension.