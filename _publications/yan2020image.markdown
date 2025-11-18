---
layout: publication
title: Image Retrieval For Structure-from-motion Via Graph Convolutional Network
authors: Shen Yan, Yang Pen, Shiming Lai, Yu Liu, Maojun Zhang
conference: Information Sciences
year: 2020
bibkey: yan2020image
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.08049'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Yan et al.
---
Conventional image retrieval techniques for Structure-from-Motion (SfM)
suffer from the limit of effectively recognizing repetitive patterns and cannot
guarantee to create just enough match pairs with high precision and high
recall. In this paper, we present a novel retrieval method based on Graph
Convolutional Network (GCN) to generate accurate pairwise matches without
costly redundancy. We formulate image retrieval task as a node binary
classification problem in graph data: a node is marked as positive if it shares
the scene overlaps with the query image. The key idea is that we find that the
local context in feature space around a query image contains rich information
about the matchable relation between this image and its neighbors. By
constructing a subgraph surrounding the query image as input data, we adopt a
learnable GCN to exploit whether nodes in the subgraph have overlapping regions
with the query photograph. Experiments demonstrate that our method performs
remarkably well on the challenging dataset of highly ambiguous and duplicated
scenes. Besides, compared with state-of-the-art matchable retrieval methods,
the proposed approach significantly reduces useless attempted matches without
sacrificing the accuracy and completeness of reconstruction.