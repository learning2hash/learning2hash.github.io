---
layout: publication
title: A Multilabel Classification Framework For Approximate Nearest Neighbor Search
authors: "Ville Hyv\xF6nen, Elias J\xE4\xE4saari, Teemu Roos"
conference: Arxiv
year: 2019
bibkey: "hyv\xF6nen2019a"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.08322'}]
tags: [Vector Indexing, Supervised, Tools & Libraries, Unsupervised, Similarity Search,
  Evaluation]
short_authors: "Ville Hyv\xF6nen, Elias J\xE4\xE4saari, Teemu Roos"
---
Both supervised and unsupervised machine learning algorithms have been used
to learn partition-based index structures for approximate nearest neighbor
(ANN) search. Existing supervised algorithms formulate the learning task as
finding a partition in which the nearest neighbors of a training set point
belong to the same partition element as the point itself, so that the nearest
neighbor candidates can be retrieved by naive lookup or backtracking search. We
formulate candidate set selection in ANN search directly as a multilabel
classification problem where the labels correspond to the nearest neighbors of
the query point, and interpret the partitions as partitioning classifiers for
solving this task. Empirical results suggest that the natural classifier based
on this interpretation leads to strictly improved performance when combined
with any unsupervised or supervised partitioning strategy. We also prove a
sufficient condition for consistency of a partitioning classifier for ANN
search, and illustrate the result by verifying this condition for chronological
\(k\)-d trees.