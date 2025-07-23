---
layout: publication
title: Efficient Neural Ranking Using Forward Indexes
authors: Leonhardt Jurek, Rudra Koustav, Khosla Megha, Anand Abhijit, Anand Avishek
conference: Proceedings of the ACM Web Conference 2022
year: 2022
bibkey: leonhardt2021efficient
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.06051'}]
tags: ["Efficiency", "Evaluation", "Hybrid ANN Methods", "Neural Hashing", "Scalability", "Similarity Search"]
short_authors: Leonhardt et al.
---
Neural document ranking approaches, specifically transformer models, have
achieved impressive gains in ranking performance. However, query processing
using such over-parameterized models is both resource and time intensive. In
this paper, we propose the Fast-Forward index -- a simple vector forward index
that facilitates ranking documents using interpolation of lexical and semantic
scores -- as a replacement for contextual re-rankers and dense indexes based on
nearest neighbor search. Fast-Forward indexes rely on efficient sparse models
for retrieval and merely look up pre-computed dense transformer-based vector
representations of documents and passages in constant time for fast CPU-based
semantic similarity computation during query processing. We propose index
pruning and theoretically grounded early stopping techniques to improve the
query processing throughput. We conduct extensive large-scale experiments on
TREC-DL datasets and show improvements over hybrid indexes in performance and
query processing efficiency using only CPUs. Fast-Forward indexes can provide
superior ranking performance using interpolation due to the complementary
benefits of lexical and semantic similarities.