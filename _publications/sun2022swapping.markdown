---
layout: publication
title: Swapping Semantic Contents For Mixing Images
authors: "R\xE9my Sun, Cl\xE9ment Masson, Gilles H\xE9naff, Nicolas Thome, Matthieu\
  \ Cord"
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: sun2022swapping
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.10158'}]
tags: []
short_authors: Sun et al.
---
Deep architecture have proven capable of solving many tasks provided a
sufficient amount of labeled data. In fact, the amount of available labeled
data has become the principal bottleneck in low label settings such as
Semi-Supervised Learning. Mixing Data Augmentations do not typically yield new
labeled samples, as indiscriminately mixing contents creates between-class
samples. In this work, we introduce the SciMix framework that can learn to
generator to embed a semantic style code into image backgrounds, we obtain new
mixing scheme for data augmentation. We then demonstrate that SciMix yields
novel mixed samples that inherit many characteristics from their non-semantic
parents. Afterwards, we verify those samples can be used to improve the
performance semi-supervised frameworks like Mean Teacher or Fixmatch, and even
fully supervised learning on a small labeled dataset.