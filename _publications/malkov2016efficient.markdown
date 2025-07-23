---
layout: publication
title: Efficient And Robust Approximate Nearest Neighbor Search Using Hierarchical
  Navigable Small World Graphs
authors: Malkov Yu. A., Yashunin D. A.
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: malkov2016efficient
citations: 1091
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.09320'}]
tags: ["Efficiency", "Graph-based ANN", "Large-Scale Search", "Robustness", "Similarity Search"]
short_authors: Malkov Yu. A., Yashunin D. A.
---
We present a new approach for the approximate K-nearest neighbor search based
on navigable small world graphs with controllable hierarchy (Hierarchical NSW,
HNSW). The proposed solution is fully graph-based, without any need for
additional search structures, which are typically used at the coarse search
stage of the most proximity graph techniques. Hierarchical NSW incrementally
builds a multi-layer structure consisting from hierarchical set of proximity
graphs (layers) for nested subsets of the stored elements. The maximum layer in
which an element is present is selected randomly with an exponentially decaying
probability distribution. This allows producing graphs similar to the
previously studied Navigable Small World (NSW) structures while additionally
having the links separated by their characteristic distance scales. Starting
search from the upper layer together with utilizing the scale separation boosts
the performance compared to NSW and allows a logarithmic complexity scaling.
Additional employment of a heuristic for selecting proximity graph neighbors
significantly increases performance at high recall and in case of highly
clustered data. Performance evaluation has demonstrated that the proposed
general metric space search index is able to strongly outperform previous
opensource state-of-the-art vector-only approaches. Similarity of the algorithm
to the skip list structure allows straightforward balanced distributed
implementation.