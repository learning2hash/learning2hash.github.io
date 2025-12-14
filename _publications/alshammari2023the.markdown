---
layout: publication
title: The Effect Of Points Dispersion On The \(k\)-nn Search In Random Projection
  Forests
authors: Mashaan Alshammari, John Stavrakakis, Adel F. Ahmed, Masahiro Takatsuka
conference: IEEE Access
year: 2023
bibkey: alshammari2023the
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.13160'}]
tags: [Scalability, Locality Sensitive Hashing, Datasets, Quantization]
short_authors: Alshammari et al.
---
Partitioning trees are efficient data structures for \(k\)-nearest neighbor
search. Machine learning libraries commonly use a special type of partitioning
trees called \(k\)d-trees to perform \(k\)-nn search. Unfortunately, \(k\)d-trees can
be ineffective in high dimensions because they need more tree levels to
decrease the vector quantization (VQ) error. Random projection trees rpTrees
solve this scalability problem by using random directions to split the data. A
collection of rpTrees is called rpForest. \(k\)-nn search in an rpForest is
influenced by two factors: 1) the dispersion of points along the random
direction and 2) the number of rpTrees in the rpForest. In this study, we
investigate how these two factors affect the \(k\)-nn search with varying \(k\)
values and different datasets. We found that with larger number of trees, the
dispersion of points has a very limited effect on the \(k\)-nn search. One should
use the original rpTree algorithm by picking a random direction regardless of
the dispersion of points.