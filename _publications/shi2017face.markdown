---
layout: publication
title: 'Face Clustering: Representation And Pairwise Constraints'
authors: Yichun Shi, Charles Otto, Anil K. Jain
conference: IEEE Transactions on Information Forensics and Security
year: 2018
bibkey: shi2017face
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.05067'}]
tags: [Datasets, Supervised, Evaluation]
short_authors: Yichun Shi, Charles Otto, Anil K. Jain
---
Clustering face images according to their identity has two important
applications: (i) grouping a collection of face images when no external labels
are associated with images, and (ii) indexing for efficient large scale face
retrieval. The clustering problem is composed of two key parts: face
representation and choice of similarity for grouping faces. We first propose a
representation based on ResNet, which has been shown to perform very well in
image classification problems. Given this representation, we design a
clustering algorithm, Conditional Pairwise Clustering (ConPaC), which directly
estimates the adjacency matrix only based on the similarity between face
images. This allows a dynamic selection of number of clusters and retains
pairwise similarity between faces. ConPaC formulates the clustering problem as
a Conditional Random Field (CRF) model and uses Loopy Belief Propagation to
find an approximate solution for maximizing the posterior probability of the
adjacency matrix. Experimental results on two benchmark face datasets (LFW and
IJB-B) show that ConPaC outperforms well known clustering algorithms such as
k-means, spectral clustering and approximate rank-order. Additionally, our
algorithm can naturally incorporate pairwise constraints to obtain a
semi-supervised version that leads to improved clustering performance. We also
propose an k-NN variant of ConPaC, which has a linear time complexity given a
k-NN graph, suitable for large datasets.