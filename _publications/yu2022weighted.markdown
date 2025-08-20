---
layout: publication
title: Weighted Contrastive Hashing
authors: Jiaguo Yu, Huming Qiu, Dubing Chen, Haofeng Zhang
conference: Lecture Notes in Computer Science
year: 2023
bibkey: yu2022weighted
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.14099'}]
tags: [Hashing Methods, Unsupervised, Datasets, Supervised, Neural Hashing, Self-Supervised,
  Evaluation]
short_authors: Yu et al.
---
The development of unsupervised hashing is advanced by the recent popular
contrastive learning paradigm. However, previous contrastive learning-based
works have been hampered by (1) insufficient data similarity mining based on
global-only image representations, and (2) the hash code semantic loss caused
by the data augmentation. In this paper, we propose a novel method, namely
Weighted Contrative Hashing (WCH), to take a step towards solving these two
problems. We introduce a novel mutual attention module to alleviate the problem
of information asymmetry in network features caused by the missing image
structure during contrative augmentation. Furthermore, we explore the
fine-grained semantic relations between images, i.e., we divide the images into
multiple patches and calculate similarities between patches. The aggregated
weighted similarities, which reflect the deep image relations, are distilled to
facilitate the hash codes learning with a distillation loss, so as to obtain
better retrieval performance. Extensive experiments show that the proposed WCH
significantly outperforms existing unsupervised hashing methods on three
benchmark datasets.