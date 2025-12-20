---
layout: publication
title: Embedding Geometries Of Contrastive Language-image Pre-training
authors: Jason Chuan-Chih Chou, Nahid Alam
conference: Arxiv
year: 2024
bibkey: chou2024embedding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.13079'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Jason Chuan-Chih Chou, Nahid Alam
---
Since the publication of CLIP, the approach of using InfoNCE loss for
contrastive pre-training has become widely popular for bridging two or more
modalities. Despite its wide adoption, CLIP's original design choices of L2
normalization and cosine similarity logit have rarely been revisited. We have
systematically experimented with alternative geometries and softmax logits for
language-image pre-training and identified that variants with intuitive
Euclidean geometry, Euclidean CLIP (EuCLIP), match or exceed the performance of
CLIP and support hierarchical relationships at least as well as more
complicated hyperbolic alternative.