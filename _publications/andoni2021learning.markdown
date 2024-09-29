---
layout: publication
title: Learning To Hash Robustly Guaranteed
authors: Andoni Alexandr, Beaglehole Daniel
conference: "Arxiv"
year: 2021
bibkey: andoni2021learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2108.05433"}
tags: ['ARXIV', 'Independent', 'LSH']
---
The indexing algorithms for the high45;dimensional nearest neighbor search (NNS) with the best worst45;case guarantees are based on the randomized Locality Sensitive Hashing (LSH) and its derivatives. In practice many heuristic approaches exist to learn the best indexing method in order to speed45;up NNS crucially adapting to the structure of the given dataset. Oftentimes these heuristics outperform the LSH45;based algorithms on real datasets but almost always come at the cost of losing the guarantees of either correctness or robust performance on adversarial queries or apply to datasets with an assumed extra structure/model. In this paper we design an NNS algorithm for the Hamming space that has worst45;case guarantees essentially matching that of theoretical algorithms while optimizing the hashing to the structure of the dataset (think instance45;optimal algorithms) for performance on the minimum45;performing query. We evaluate the algorithms ability to optimize for a given dataset both theoretically and practically. On the theoretical side we exhibit a natural setting (dataset model) where our algorithm is much better than the standard theoretical one. On the practical side we run experiments that show that our algorithm has a 1.8x and 2.1x better recall on the worst45;performing queries to the MNIST and ImageNet datasets.
