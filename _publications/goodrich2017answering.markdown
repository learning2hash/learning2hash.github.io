---
layout: publication
title: Answering Spatial Multiple-set Intersection Queries Using 2-3 Cuckoo Hash-filters
authors: Michael T. Goodrich
conference: Arxiv
year: 2017
bibkey: goodrich2017answering
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.09059'}]
tags: ["Evaluation"]
short_authors: Michael T. Goodrich
---
We show how to answer spatial multiple-set intersection queries in O(n(log
w)/w + kt) expected time, where n is the total size of the t sets involved in
the query, w is the number of bits in a memory word, k is the output size, and
c is any fixed constant. This improves the asymptotic performance over previous
solutions and is based on an interesting data structure, known as 2-3 cuckoo
hash-filters. Our results apply in the word-RAM model (or practical RAM model),
which allows for constant-time bit-parallel operations, such as bitwise AND,
OR, NOT, and MSB (most-significant 1-bit), as exist in modern CPUs and GPUs.
Our solutions apply to any multiple-set intersection queries in spatial data
sets that can be reduced to one-dimensional range queries, such as spatial join
queries for one-dimensional points or sets of points stored along space-filling
curves, which are used in GIS applications.