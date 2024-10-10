---
layout: publication
title: Reverse Nearest Neighbors Search In High Dimensions Using Locality-sensitive Hashing
authors: Arthur David, Oudot Steve Y.
conference: "Arxiv"
year: 2010
bibkey: arthur2010reverse
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1011.4955"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We investigate the problem of finding reverse nearest neighbors efficiently. Although provably good solutions exist for this problem in low or fixed dimensions to this date the methods proposed in high dimensions are mostly heuristic. We introduce a method that is both provably correct and efficient in all dimensions based on a reduction of the problem to one instance of (e)-nearest neighbor search plus a controlled number of instances of em exhaustive (r)-pleb a variant of em Point Location among Equal Balls where all the (r)-balls centered at the data points that contain the query point are sought for not just one. The former problem has been extensively studied and elegantly solved in high dimensions using Locality-Sensitive Hashing (LSH) techniques. By contrast the latter problem has a complexity that is still not fully understood. We revisit the analysis of the LSH scheme for exhaustive (r)-pleb using a somewhat refined notion of locality-sensitive family of hash function which brings out a meaningful output-sensitive term in the complexity of the problem. Our analysis combined with a non-isometric lifting of the data enables us to answer exhaustive (r)-pleb queries (and down the road reverse nearest neighbors queries) efficiently. Along the way we obtain a simple algorithm for answering exact nearest neighbor queries whose complexity is parametrized by some em condition number measuring the inherent difficulty of a given instance of the problem.
