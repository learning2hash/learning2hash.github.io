---
layout: publication
title: Affinity Derivation And Graph Merge For Instance Segmentation
authors: Yiding Liu, Siyu Yang, Bin Li, Wengang Zhou, Jizheng Xu, Houqiang Li, Yan
  Lu
conference: Lecture Notes in Computer Science
year: 2018
bibkey: liu2018affinity
citations: 120
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.10870'}]
tags: []
short_authors: Liu et al.
---
We present an instance segmentation scheme based on pixel affinity
information, which is the relationship of two pixels belonging to a same
instance. In our scheme, we use two neural networks with similar structure. One
is to predict pixel level semantic score and the other is designed to derive
pixel affinities.
  Regarding pixels as the vertexes and affinities as edges, we then propose a
simple yet effective graph merge algorithm to cluster pixels into instances.
Experimental results show that our scheme can generate fine-grained instance
mask.
  With Cityscapes training data, the proposed scheme achieves 27.3 AP on test
set.