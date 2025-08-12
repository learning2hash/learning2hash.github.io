---
layout: publication
title: On Extended Concentration Inequalities For Fast JL Embeddings Of Infinite Sets
authors: Edem Boahen, March T. Boedihardjo, Rafael Chiclana, Mark Iwen
conference: Arxiv
year: 2025
bibkey: boahen2025extended
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.14010'}]
tags: ["Distance Metric Learning"]
short_authors: Boahen et al.
---
The Johnson-Lindenstrauss (JL) lemma allows subsets of a high-dimensional
space to be embedded into a lower-dimensional space while approximately
preserving all pairwise Euclidean distances. This important result has inspired
an extensive literature, with a significant portion dedicated to constructing
structured random matrices with fast matrix-vector multiplication algorithms
that generate such embeddings for finite point sets. In this paper, we briefly
consider fast JL embedding matrices for \{\it infinite\} subsets of
\(\mathbb\{R\}^d\). Prior work in this direction such as \cite\{oymak2018isometric,
mendelson2023column\} has focused on constructing fast JL matrices \(HD \in
\mathbb\{R\}^\{k \times d\}\) by multiplying structured matrices with RIP(-like)
properties \(H \in \mathbb\{R\}^\{k \times d\}\) against a random diagonal matrix \(D
\in \mathbb\{R\}^\{d \times d\}\). However, utilizing RIP(-like) matrices \(H\) in
this fashion necessarily has the unfortunate side effect that the resulting
embedding dimension \(k\) must depend on the ambient dimension \(d\) no matter how
simple the infinite set is that one aims to embed. Motivated by this, we
explore an alternate strategy for removing this \(d\)-dependence from \(k\) herein:
Extending a concentration inequality proven by Ailon and Liberty
\cite\{Ailon2008fast\} in the hope of later utilizing it in a chaining argument
to obtain a near-optimal result for infinite sets. %, and \((ii)\) utilizing a
simple secondary Gaussian embedding of an initial fast JL embedding of a given
infinite set.
  Though this strategy ultimately fails to provide the near-optimal embedding
dimension we seek, along the way we obtain a stronger-than-sub-exponential
extension of the concentration inequality in \cite\{Ailon2008fast\} which may be
of independent interest.