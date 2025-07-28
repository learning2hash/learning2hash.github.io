---
layout: publication
title: Object Category Learning And Retrieval With Weak Supervision
authors: Steven Hickson, Anelia Angelova, Irfan Essa, Rahul Sukthankar
conference: Arxiv
year: 2018
bibkey: hickson2018object
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.08985'}]
tags: []
short_authors: Hickson et al.
---
We consider the problem of retrieving objects from image data and learning to
classify them into meaningful semantic categories with minimal supervision. To
that end, we propose a fully differentiable unsupervised deep clustering
approach to learn semantic classes in an end-to-end fashion without individual
class labeling using only unlabeled object proposals. The key contributions of
our work are 1) a kmeans clustering objective where the clusters are learned as
parameters of the network and are represented as memory units, and 2)
simultaneously building a feature representation, or embedding, while learning
to cluster it. This approach shows promising results on two popular computer
vision datasets: on CIFAR10 for clustering objects, and on the more complex and
challenging Cityscapes dataset for semantically discovering classes which
visually correspond to cars, people, and bicycles. Currently, the only
supervision provided is segmentation objectness masks, but this method can be
extended to use an unsupervised objectness-based object generation mechanism
which will make the approach completely unsupervised.