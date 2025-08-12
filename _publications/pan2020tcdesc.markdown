---
layout: publication
title: 'Tcdesc: Learning Topology Consistent Descriptors'
authors: Honghu Pan, Fanyang Meng, Zhenyu He, Yongsheng Liang, Wei Liu
conference: Arxiv
year: 2020
bibkey: pan2020tcdesc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.03254'}]
tags: ["Distance Metric Learning"]
short_authors: Pan et al.
---
Triplet loss is widely used for learning local descriptors from image patch.
However, triplet loss only minimizes the Euclidean distance between matching
descriptors and maximizes that between the non-matching descriptors, which
neglects the topology similarity between two descriptor sets. In this paper, we
propose topology measure besides Euclidean distance to learn topology
consistent descriptors by considering kNN descriptors of positive sample. First
we establish a novel topology vector for each descriptor followed by Locally
Linear Embedding (LLE) to indicate the topological relation among the
descriptor and its kNN descriptors. Then we define topology distance between
descriptors as the difference of their topology vectors. Last we employ the
dynamic weighting strategy to fuse Euclidean distance and topology distance of
matching descriptors and take the fusion result as the positive sample distance
in the triplet loss. Experimental results on several benchmarks show that our
method performs better than state-of-the-arts results and effectively improves
the performance of triplet loss.