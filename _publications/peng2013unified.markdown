---
layout: publication
title: A Unified Framework For Representation-based Subspace Clustering Of Out-of-sample
  And Large-scale Data
authors: Xi Peng, Huajin Tang, Lei Zhang, Zhang Yi, Shijie Xiao
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2015
bibkey: peng2013unified
citations: 141
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1309.6487'}]
tags: []
short_authors: Peng et al.
---
Under the framework of spectral clustering, the key of subspace clustering is
building a similarity graph which describes the neighborhood relations among
data points. Some recent works build the graph using sparse, low-rank, and
\\(ℓ₂\\)-norm-based representation, and have achieved state-of-the-art
performance. However, these methods have suffered from the following two
limitations. First, the time complexities of these methods are at least
proportional to the cube of the data size, which make those methods inefficient
for solving large-scale problems. Second, they cannot cope with out-of-sample
data that are not used to construct the similarity graph. To cluster each
out-of-sample datum, the methods have to recalculate the similarity graph and
the cluster membership of the whole data set. In this paper, we propose a
unified framework which makes representation-based subspace clustering
algorithms feasible to cluster both out-of-sample and large-scale data. Under
our framework, the large-scale problem is tackled by converting it as
out-of-sample problem in the manner of "sampling, clustering, coding, and
classifying". Furthermore, we give an estimation for the error bounds by
treating each subspace as a point in a hyperspace. Extensive experimental
results on various benchmark data sets show that our methods outperform several
recently-proposed scalable methods in clustering large-scale data set.