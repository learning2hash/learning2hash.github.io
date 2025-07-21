---
layout: publication
title: Lattice-based Locality Sensitive Hashing is Optimal
authors: Chandrasekaran et al.
conference: Proceedings of the IEEE
year: 2017
bibkey: chandrasekaran2017lattice
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.08558'}]
tags: ["Hashing Methods", "Locality Sensitive Hashing"]
---
Locality sensitive hashing (LSH) was introduced by Indyk and Motwani (STOC
`98) to give the first sublinear time algorithm for the c-approximate nearest
neighbor (ANN) problem using only polynomial space. At a high level, an LSH
family hashes "nearby" points to the same bucket and "far away" points to
different buckets. The quality of measure of an LSH family is its LSH exponent,
which helps determine both query time and space usage.
  In a seminal work, Andoni and Indyk (FOCS `06) constructed an LSH family
based on random ball partitioning of space that achieves an LSH exponent of
1/c^2 for the l_2 norm, which was later shown to be optimal by Motwani, Naor
and Panigrahy (SIDMA `07) and O'Donnell, Wu and Zhou (TOCT `14). Although
optimal in the LSH exponent, the ball partitioning approach is computationally
expensive. So, in the same work, Andoni and Indyk proposed a simpler and more
practical hashing scheme based on Euclidean lattices and provided computational
results using the 24-dimensional Leech lattice. However, no theoretical
analysis of the scheme was given, thus leaving open the question of finding the
exponent of lattice based LSH.
  In this work, we resolve this question by showing the existence of lattices
achieving the optimal LSH exponent of 1/c^2 using techniques from the geometry
of numbers. At a more conceptual level, our results show that optimal LSH space
partitions can have periodic structure. Understanding the extent to which
additional structure can be imposed on these partitions, e.g. to yield low
space and query complexity, remains an important open problem.