---
layout: publication
title: Revisiting the Inverted Indices for Billion-Scale Approximate Nearest Neighbors
authors: Baranchuk Dmitry, Babenko Artem, Malkov Yury
conference: Lecture Notes in Computer Science
year: 2018
bibkey: baranchuk2018revisiting
citations: 67
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.02422'}]
tags: ["Large Scale Search", "Scalability"]
---
This work addresses the problem of billion-scale nearest neighbor search. The
state-of-the-art retrieval systems for billion-scale databases are currently
based on the inverted multi-index, the recently proposed generalization of the
inverted index structure. The multi-index provides a very fine-grained
partition of the feature space that allows extracting concise and accurate
short-lists of candidates for the search queries. In this paper, we argue that
the potential of the simple inverted index was not fully exploited in previous
works and advocate its usage both for the highly-entangled deep descriptors and
relatively disentangled SIFT descriptors. We introduce a new retrieval system
that is based on the inverted index and outperforms the multi-index by a large
margin for the same memory consumption and construction complexity. For
example, our system achieves the state-of-the-art recall rates several times
faster on the dataset of one billion deep descriptors compared to the efficient
implementation of the inverted multi-index from the FAISS library.