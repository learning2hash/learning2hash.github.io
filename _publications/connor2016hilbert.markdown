---
layout: publication
title: 'Hilbert Exclusion: Improved Metric Search Through Finite Isometric Embeddings'
authors: Richard Connor, Franco Alberto Cardillo, Lucia Vadicamo, Fausto Rabitti
conference: "ACM Transactions on Information Systems (TOIS) 35 3 Article 17 (2016)"
year: 2016
citations: 18
bibkey: connor2016hilbert
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1604.08640'}
tags: ['Cross-Modal', 'Quantisation', 'Retrieval Models', 'Shallow', 'Vector Indexing']
---
Most research into similarity search in metric spaces relies upon the
triangle inequality property. This property allows the space to be arranged
according to relative distances to avoid searching some subspaces. We show that
many common metric spaces, notably including those using Euclidean and
Jensen-Shannon distances, also have a stronger property, sometimes called the
four-point property: in essence, these spaces allow an isometric embedding of
any four points in three-dimensional Euclidean space, as well as any three
points in two-dimensional Euclidean space. In fact, we show that any space
which is isometrically embeddable in Hilbert space has the stronger property.
This property gives stronger geometric guarantees, and one in particular, which
we name the Hilbert Exclusion property, allows any indexing mechanism which
uses hyperplane partitioning to perform better. One outcome of this observation
is that a number of state-of-the-art indexing mechanisms over high dimensional
spaces can be easily extended to give a significant increase in performance;
furthermore, the improvement given is greater in higher dimensions. This
therefore leads to a significant improvement in the cost of metric search in
these spaces.
