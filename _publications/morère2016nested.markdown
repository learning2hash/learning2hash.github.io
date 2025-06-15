---
layout: publication
title: 'Nested Invariance Pooling And RBM Hashing For Image Instance Retrieval'
authors: Olivier Morère, Jie Lin, Antoine Veillard, Vijay Chandrasekhar, Tomaso Poggio
conference: "Arxiv"
year: 2016
citations: 12
bibkey: morère2016nested
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1603.04595'}
tags: ['Cross-Modal', 'Deep', 'Retrieval Models', 'Evaluation', 'Datasets', 'Vector Indexing', 'Supervised', 'Hashing']
---
The goal of this work is the computation of very compact binary hashes for
image instance retrieval. Our approach has two novel contributions. The first
one is Nested Invariance Pooling (NIP), a method inspired from i-theory, a
mathematical theory for computing group invariant transformations with
feed-forward neural networks. NIP is able to produce compact and
well-performing descriptors with visual representations extracted from
convolutional neural networks. We specifically incorporate scale, translation
and rotation invariances but the scheme can be extended to any arbitrary sets
of transformations. We also show that using moments of increasing order
throughout nesting is important. The NIP descriptors are then hashed to the
target code size (32-256 bits) with a Restricted Boltzmann Machine with a novel
batch-level regularization scheme specifically designed for the purpose of
hashing (RBMH). A thorough empirical evaluation with state-of-the-art shows
that the results obtained both with the NIP descriptors and the NIP+RBMH hashes
are consistently outstanding across a wide range of datasets.
