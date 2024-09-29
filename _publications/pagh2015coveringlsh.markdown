---
layout: publication
title: Coveringlsh Locality45;sensitive Hashing Without False Negatives
authors: Pagh Rasmus
conference: "Arxiv"
year: 2015
bibkey: pagh2015coveringlsh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1507.03225"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We consider a new construction of locality45;sensitive hash functions for Hamming space that is emph123;covering125; in the sense that is it guaranteed to produce a collision for every pair of vectors within a given radius r. The construction is emph123;efficient125; in the sense that the expected number of hash collisions between vectors at distance~cr for a given c1 comes close to that of the best possible data independent LSH without the covering guarantee namely the seminal LSH construction of Indyk and Motwani (STOC 98). The efficiency of the new construction essentially emph123;matches125; their bound when the search radius is not too large 45;45;45; e.g. when cr = o(log(n)/loglog n) where n is the number of points in the data set and when cr = log(n)/k where k is an integer constant. In general it differs by at most a factor ln(4) in the exponent of the time bounds. As a consequence LSH45;based similarity search in Hamming space can avoid the problem of false negatives at little or no cost in efficiency.
