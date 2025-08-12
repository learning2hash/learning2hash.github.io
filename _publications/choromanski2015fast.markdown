---
layout: publication
title: Fast Online Clustering With Randomized Skeleton Sets
authors: Krzysztof Choromanski, Sanjiv Kumar, Xiaofeng Liu
conference: Arxiv
year: 2015
bibkey: choromanski2015fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.03425'}]
tags: []
short_authors: Krzysztof Choromanski, Sanjiv Kumar, Xiaofeng Liu
---
We present a new fast online clustering algorithm that reliably recovers
arbitrary-shaped data clusters in high throughout data streams. Unlike the
existing state-of-the-art online clustering methods based on k-means or
k-medoid, it does not make any restrictive generative assumptions. In addition,
in contrast to existing nonparametric clustering techniques such as DBScan or
DenStream, it gives provable theoretical guarantees. To achieve fast
clustering, we propose to represent each cluster by a skeleton set which is
updated continuously as new data is seen. A skeleton set consists of weighted
samples from the data where weights encode local densities. The size of each
skeleton set is adapted according to the cluster geometry. The proposed
technique automatically detects the number of clusters and is robust to
outliers. The algorithm works for the infinite data stream where more than one
pass over the data is not feasible. We provide theoretical guarantees on the
quality of the clustering and also demonstrate its advantage over the existing
state-of-the-art on several datasets.