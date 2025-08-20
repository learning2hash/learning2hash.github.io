---
layout: publication
title: Deep Metric Learning Using Similarities From Nonlinear Rank Approximations
authors: Konstantin Schall, Kai Uwe Barthel, Nico Hezel, Klaus Jung
conference: 2019 IEEE 21st International Workshop on Multimedia Signal Processing
  (MMSP)
year: 2019
bibkey: schall2019deep
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09427'}]
tags: [Distance Metric Learning, Similarity Search]
short_authors: Schall et al.
---
In recent years, deep metric learning has achieved promising results in
learning high dimensional semantic feature embeddings where the spatial
relationships of the feature vectors match the visual similarities of the
images. Similarity search for images is performed by determining the vectors
with the smallest distances to a query vector. However, high retrieval quality
does not depend on the actual distances of the feature vectors, but rather on
the ranking order of the feature vectors from similar images. In this paper, we
introduce a metric learning algorithm that focuses on identifying and modifying
those feature vectors that most strongly affect the retrieval quality. We
compute normalized approximated ranks and convert them to similarities by
applying a nonlinear transfer function. These similarities are used in a newly
proposed loss function that better contracts similar and disperses dissimilar
samples. Experiments demonstrate significant improvement over existing deep
feature embedding methods on the CUB-200-2011, Cars196, and Stanford Online
Products data sets for all embedding sizes.