---
layout: publication
title: 'Tcdesc: Learning Topology Consistent Descriptors For Image Matching'
authors: Honghu Pan, Fanyang Meng, Nana Fan, Zhenyu He
conference: Arxiv
year: 2020
bibkey: pan2020tcdesc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.07036'}]
tags: ["Distance Metric Learning"]
short_authors: Pan et al.
---
The constraint of neighborhood consistency or local consistency is widely
used for robust image matching. In this paper, we focus on learning
neighborhood topology consistent descriptors (TCDesc), while former works of
learning descriptors, such as HardNet and DSM, only consider point-to-point
Euclidean distance among descriptors and totally neglect neighborhood
information of descriptors. To learn topology consistent descriptors, first we
propose the linear combination weights to depict the topological relationship
between center descriptor and its kNN descriptors, where the difference between
center descriptor and the linear combination of its kNN descriptors is
minimized. Then we propose the global mapping function which maps the local
linear combination weights to the global topology vector and define the
topology distance of matching descriptors as l1 distance between their topology
vectors. Last we employ adaptive weighting strategy to jointly minimize
topology distance and Euclidean distance, which automatically adjust the weight
or attention of two distances in triplet loss. Our method has the following two
advantages: (1) We are the first to consider neighborhood information of
descriptors, while former works mainly focus on neighborhood consistency of
feature points; (2) Our method can be applied in any former work of learning
descriptors by triplet loss. Experimental results verify the generalization of
our method: We can improve the performances of both HardNet and DSM on several
benchmarks.