---
layout: publication
title: A Multilabel Classification Framework For Approximate Nearest Neighbor Search
authors: Ville Hyvönen, Elias Jääsaari, Teemu Roos
conference: "Neural Information Processing Systems"
year: 2022
bibkey: hyvönen2022multilabel
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper_files/paper/2022/hash/e8752f3e51f33a2e06daf044c40ce412-Abstract-Conference.html"}
tags: ['NEURIPS', 'Unsupervised']
---
Both supervised and unsupervised machine learning algorithms have been used to learn partition-based index structures for approximate nearest neighbor (ANN) search. Existing supervised algorithms formulate the learning task as finding a partition in which the nearest neighbors of a training set point belong to the same partition element as the point itself, so that the nearest neighbor candidates can be retrieved by naive lookup or backtracking search. We formulate candidate set selection in ANN search directly as a multilabel classification problem where the labels correspond to the nearest neighbors of the query point, and interpret the partitions as partitioning classifiers for solving this task. Empirical results suggest that the natural classifier based on this interpretation leads to strictly improved performance when combined with any unsupervised or supervised partitioning strategy. We also prove a sufficient condition for consistency of a partitioning classifier for ANN search, and illustrate the result by verifying this condition for chronological $k$-d trees.
