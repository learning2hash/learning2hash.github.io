---
layout: publication
title: A Self-encoder For Learning Nearest Neighbors
authors: Boschin Armand, Bonald Thomas, Jeanmougin Marc
conference: Arxiv
year: 2023
bibkey: boschin2023self
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14257'}]
tags: ["Supervised", "Self-Supervised", "Efficiency"]
short_authors: Boschin Armand, Bonald Thomas, Jeanmougin Marc
---
We present the self-encoder, a neural network trained to guess the identity
of each data sample. Despite its simplicity, it learns a very useful
representation of data, in a self-supervised way. Specifically, the
self-encoder learns to distribute the data samples in the embedding space so
that they are linearly separable from one another. This induces a geometry
where two samples are close in the embedding space when they are not easy to
differentiate. The self-encoder can then be combined with a nearest-neighbor
classifier or regressor for any subsequent supervised task. Unlike regular
nearest neighbors, the predictions resulting from this encoding of data are
invariant to any scaling of features, making any preprocessing like min-max
scaling not necessary. The experiments show the efficiency of the approach,
especially on heterogeneous data mixing numerical features and categorical
features.