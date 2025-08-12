---
layout: publication
title: Nearest Neighbor Based Clustering Algorithm For Large Data Sets
authors: Pankaj Kumar Yadav, Sriniwas Pandey, Sraban Kumar Mohanty
conference: Advances in Intelligent Systems and Computing
year: 2018
bibkey: yadav2015nearest
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.05962'}]
tags: []
short_authors: Pankaj Kumar Yadav, Sriniwas Pandey, Sraban Kumar Mohanty
---
Clustering is an unsupervised learning technique in which data or objects are
grouped into sets based on some similarity measure. Most of the clustering
algorithms assume that the main memory is infinite and can accommodate the set
of patterns. In reality many applications give rise to a large set of patterns
which does not fit in the main memory. When the data set is too large, much of
the data is stored in the secondary memory. Input/Outputs (I/O) from the disk
are the major bottleneck in designing efficient clustering algorithms for large
data sets. Different designing techniques have been used to design clustering
algorithms for large data sets. External memory algorithms are one class of
algorithms which can be used for large data sets. These algorithms exploit the
hierarchical memory structure of the computers by incorporating locality of
reference directly in the algorithm. This paper makes some contribution towards
designing clustering algorithms in the external memory model (Proposed by
Aggarwal and Vitter 1988) to make the algorithms scalable. In this paper, it is
shown that the Shared near neighbors algorithm is not very I/O efficient since
the computational complexity is same as the I/O complexity. The algorithm is
designed in the external memory model and I/O complexity is reduced. The
computational complexity remains same. We substantiate the theoretical analysis
by showing the performance of the algorithms with their traditional counterpart
by implementing in STXXL library.