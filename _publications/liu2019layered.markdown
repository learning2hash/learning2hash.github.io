---
layout: publication
title: Layered Embeddings For Amodal Instance Segmentation
authors: "Yanfeng Liu, Eric Psota, Lance P\xE9rez"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: liu2019layered
citations: 3
additional_links: [{name: Code, url: 'https://github.com/yanfengliu/layered_embeddings'},
  {name: Paper, url: 'https://arxiv.org/abs/2002.06264'}]
tags: []
short_authors: "Yanfeng Liu, Eric Psota, Lance P\xE9rez"
---
The proposed method extends upon the representational output of semantic
instance segmentation by explicitly including both visible and occluded parts.
A fully convolutional network is trained to produce consistent pixel-level
embedding across two layers such that, when clustered, the results convey the
full spatial extent and depth ordering of each instance. Results demonstrate
that the network can accurately estimate complete masks in the presence of
occlusion and outperform leading top-down bounding-box approaches. Source code
available at https://github.com/yanfengliu/layered_embeddings