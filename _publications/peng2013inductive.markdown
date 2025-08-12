---
layout: publication
title: Inductive Sparse Subspace Clustering
authors: Xi Peng, Lei Zhang, Zhang Yi
conference: Electronics Letters
year: 2013
bibkey: peng2013inductive
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1303.0362'}]
tags: []
short_authors: Xi Peng, Lei Zhang, Zhang Yi
---
Sparse Subspace Clustering (SSC) has achieved state-of-the-art clustering
quality by performing spectral clustering over a \(\ell^\{1\}\)-norm based
similarity graph. However, SSC is a transductive method which does not handle
with the data not used to construct the graph (out-of-sample data). For each
new datum, SSC requires solving \(n\) optimization problems in O(n) variables for
performing the algorithm over the whole data set, where \(n\) is the number of
data points. Therefore, it is inefficient to apply SSC in fast online
clustering and scalable graphing. In this letter, we propose an inductive
spectral clustering algorithm, called inductive Sparse Subspace Clustering
(iSSC), which makes SSC feasible to cluster out-of-sample data. iSSC adopts the
assumption that high-dimensional data actually lie on the low-dimensional
manifold such that out-of-sample data could be grouped in the embedding space
learned from in-sample data. Experimental results show that iSSC is promising
in clustering out-of-sample data.