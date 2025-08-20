---
layout: publication
title: Efficient Point-to-subspace Query In \(\ell^1\) With Application To Robust
  Object Instance Recognition
authors: Ju Sun, Yuqian Zhang, John Wright
conference: SIAM Journal on Imaging Sciences
year: 2014
bibkey: sun2012efficient
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1208.0432'}]
tags: [Scalability]
short_authors: Ju Sun, Yuqian Zhang, John Wright
---
Motivated by vision tasks such as robust face and object recognition, we
consider the following general problem: given a collection of low-dimensional
linear subspaces in a high-dimensional ambient (image) space, and a query point
(image), efficiently determine the nearest subspace to the query in \\(\ell^1\\)
distance. In contrast to the naive exhaustive search which entails large-scale
linear programs, we show that the computational burden can be cut down
significantly by a simple two-stage algorithm: (1) projecting the query and
data-base subspaces into lower-dimensional space by random Cauchy matrix, and
solving small-scale distance evaluations (linear programs) in the projection
space to locate candidate nearest; (2) with few candidates upon independent
repetition of (1), getting back to the high-dimensional space and performing
exhaustive search. To preserve the identity of the nearest subspace with
nontrivial probability, the projection dimension typically is low-order
polynomial of the subspace dimension multiplied by logarithm of number of the
subspaces (Theorem 2.1). The reduced dimensionality and hence complexity
renders the proposed algorithm particularly relevant to vision application such
as robust face and object instance recognition that we investigate empirically.