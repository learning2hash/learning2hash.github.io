---
layout: publication
title: Efficient Approximate Nearest Neighbor Search For Multiple Weighted \(l_{p\leq2}\)
  Distance Functions
authors: Huan Hu, Jianzhong Li
conference: Arxiv
year: 2020
citations: 0
bibkey: hu2020efficient
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.11907'}]
tags: [ANN Search, Hashing Methods, Applications]
---
Nearest neighbor search is fundamental to a wide range of applications. Since
the exact nearest neighbor search suffers from the "curse of dimensionality",
approximate approaches, such as Locality-Sensitive Hashing (LSH), are widely
used to trade a little query accuracy for a much higher query efficiency. In
many scenarios, it is necessary to perform nearest neighbor search under
multiple weighted distance functions in high-dimensional spaces. This paper
considers the important problem of supporting efficient approximate nearest
neighbor search for multiple weighted distance functions in high-dimensional
spaces. To the best of our knowledge, prior work can only solve the problem for
the \\(l_2\\) distance. However, numerous studies have shown that the \\(l_p\\)
distance with \\(p\in(0,2)\\) could be more effective than the \\(l_2\\) distance in
high-dimensional spaces. We propose a novel method, WLSH, to address the
problem for the \\(l_p\\) distance for \\(p\in(0,2]\\). WLSH takes the LSH approach and
can theoretically guarantee both the efficiency of processing queries and the
accuracy of query results while minimizing the required total number of hash
tables. We conduct extensive experiments on synthetic and real data sets, and
the results show that WLSH achieves high performance in terms of query
efficiency, query accuracy and space consumption.