---
layout: publication
title: Generalized Relative Neighborhood Graph (GRNG) For Similarity Search
authors: Cole Foster, Berk Sevilmis, Benjamin Kimia
conference: Lecture Notes in Computer Science
year: 2022
bibkey: foster2022generalized
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.10022'}]
tags: [Graph-based ANN, Datasets, Similarity Search]
short_authors: Cole Foster, Berk Sevilmis, Benjamin Kimia
---
Similarity search is a fundamental building block for information retrieval
on a variety of datasets. The notion of a neighbor is often based on binary
considerations, such as the k nearest neighbors. However, considering that data
is often organized as a manifold with low intrinsic dimension, the notion of a
neighbor must recognize higher-order relationship, to capture neighbors in all
directions. Proximity graphs, such as the Relative Neighbor Graphs (RNG), use
trinary relationships which capture the notion of direction and have been
successfully used in a number of applications. However, the current algorithms
for computing the RNG, despite widespread use, are approximate and not
scalable. This paper proposes a novel type of graph, the Generalized Relative
Neighborhood Graph (GRNG) for use in a pivot layer that then guides the
efficient and exact construction of the RNG of a set of exemplars. It also
shows how to extend this to a multi-layer hierarchy which significantly
improves over the state-of-the-art methods which can only construct an
approximate RNG.