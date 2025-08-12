---
layout: publication
title: Dimensionality Reduced Clustered Data And Order Partition And Stepwise Dimensionality
  Increasing Indices
authors: Alexander Thomasian
conference: Arxiv
year: 2024
bibkey: thomasian2024dimensionality
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.02858'}]
tags: ["Scalability"]
short_authors: Alexander Thomasian
---
One of the goals of NASA funded project at IBM T. J. Watson Research Center
was to build an index for similarity searching satellite images, which were
characterized by high-dimensional feature image texture vectors. Reviewed is
our effort on data clustering, dimensionality reduction via Singular Value
Decomposition - SVD and indexing to build a smaller index and more efficient
k-Nearest Neighbor - k-NN query processing for similarity search. k-NN queries
based on scanning of the feature vectors of all images is obviously too costly
for ever-increasing number of images. The ubiquitous multidimensional R-tree
index and its extensions were not an option given their limited scalability
dimension-wise. The cost of processing k-NN queries was further reduced by
building memory resident Ordered Partition indices on dimensionality reduced
clusters. Further research in a university setting included the following: (1)
Clustered SVD was extended to yield exact k-NN queries by issuing appropriate
less costly range queries, (2) Stepwise Dimensionality Increasing - SDI index
outperformed other known indices, (3) selection of optimal number of dimensions
to reduce query processing cost, (4) two methods to make the OP-trees
persistent and loadable as a single file access.