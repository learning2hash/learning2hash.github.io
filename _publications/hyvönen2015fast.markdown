---
layout: publication
title: Fast K-nn Search
authors: "Ville Hyv\xF6nen et al."
conference: IEEE International Conference on Big Data 2016 p. 881-888
year: 2015
citations: 0
bibkey: "hyv\xF6nen2015fast"
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.06957'}]
tags: [ANN Search, Indexing, Applications, Hashing Methods]
---
Efficient index structures for fast approximate nearest neighbor queries are
required in many applications such as recommendation systems. In
high-dimensional spaces, many conventional methods suffer from excessive usage
of memory and slow response times. We propose a method where multiple random
projection trees are combined by a novel voting scheme. The key idea is to
exploit the redundancy in a large number of candidate sets obtained by
independently generated random projections in order to reduce the number of
expensive exact distance evaluations. The method is straightforward to
implement using sparse projections which leads to a reduced memory footprint
and fast index construction. Furthermore, it enables grouping of the required
computations into big matrix multiplications, which leads to additional savings
due to cache effects and low-level parallelization. We demonstrate by extensive
experiments on a wide variety of data sets that the method is faster than
existing partitioning tree or hashing based approaches, making it the fastest
available technique on high accuracy levels.