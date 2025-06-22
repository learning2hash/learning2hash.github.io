---
layout: publication
title: 'The Superm-tree: Indexing Metric Spaces With Sized Objects'
authors: "J\xF6rg P. Bachmann"
conference: Arxiv
year: 2019
citations: 2
bibkey: bachmann2019superm
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.11453'}]
tags: [Applications, Indexing, ANN Search]
---
A common approach to implementing similarity search applications is the usage
of distance functions, where small distances indicate high similarity. In the
case of metric distance functions, metric index structures can be used to
accelerate nearest neighbor queries. On the other hand, many applications ask
for approximate subsequences or subsets, e.g. searching for a similar partial
sequence of a gene, for a similar scene in a movie, or for a similar object in
a picture which is represented by a set of multidimensional features. Metric
index structures such as the M-Tree cannot be utilized for these tasks because
of the symmetry of the metric distance functions. In this work, we propose the
SuperM-Tree as an extension of the M-Tree where approximate subsequence and
subset queries become nearest neighbor queries. In order to do this, we
introduce metric subset spaces as a generalized concept of metric spaces.
Various metric distance functions can be extended to metric subset distance
functions, e.g. the Euclidean distance (on windows), the Hausdorff distance (on
subsets), the Edit distance and the Dog-Keeper distance (on subsequences). We
show that these examples subsume the applications mentioned above.