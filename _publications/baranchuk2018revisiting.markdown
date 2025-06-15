---
layout: publication
title: 'Revisiting The Inverted Indices For Billion-scale Approximate Nearest Neighbors'
authors: Dmitry Baranchuk, Artem Babenko, Yury Malkov
conference: "Arxiv"
year: 2018
citations: 47
bibkey: baranchuk2018revisiting
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1802.02422'}
tags: ['Approximate Nearest Neighbor Search', 'Evaluation Metrics', 'Indexing', 'Tools and Libraries', 'ANN Search']
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
