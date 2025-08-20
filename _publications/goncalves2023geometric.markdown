---
layout: publication
title: Geometric Covering Using Random Fields
authors: Felipe Goncalves, Daniel Keren, Amit Shahar, Gal Yehuda
conference: Arxiv
year: 2023
bibkey: goncalves2023geometric
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.14082'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Goncalves et al.
---
A set of vectors \(S \subseteq \mathbb\{R\}^d\) is
\((k_1,\epsilon)\)-clusterable if there are \(k_1\) balls of radius
\(\epsilon\) that cover \(S\). A set of vectors \(S \subseteq \mathbb\{R\}^d\) is
\((k_2,\delta)\)-far from being clusterable if there are at least \(k_2\) vectors
in \(S\), with all pairwise distances at least \(\delta\). We propose a
probabilistic algorithm to distinguish between these two cases. Our algorithm
reaches a decision by only looking at the extreme values of a scalar valued
hash function, defined by a random field, on \(S\); hence, it is especially
suitable in distributed and online settings. An important feature of our method
is that the algorithm is oblivious to the number of vectors: in the online
setting, for example, the algorithm stores only a constant number of scalars,
which is independent of the stream length.
  We introduce random field hash functions, which are a key ingredient in our
paradigm. Random field hash functions generalize locality-sensitive hashing
(LSH). In addition to the LSH requirement that ``nearby vectors are hashed to
similar values", our hash function also guarantees that the ``hash values are
(nearly) independent random variables for distant vectors". We formulate
necessary conditions for the kernels which define the random fields applied to
our problem, as well as a measure of kernel optimality, for which we provide a
bound. Then, we propose a method to construct kernels which approximate the
optimal one.