---
layout: publication
title: Sharp Load Thresholds For Cuckoo Hashing
authors: Fountoulakis Nikolaos, Panagiotou Konstantinos
conference: "Arxiv"
year: 2009
bibkey: fountoulakis2009sharp
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/0910.5147"}
tags: ['ARXIV', 'Graph', 'Independent']
---
The paradigm of many choices has influenced significantly the design of
efficient data structures and, most notably, hash tables. Cuckoo hashing is a
technique that extends this concept. There,we are given a table with \{n\}
locations, and we assume that each location can hold one item. Each item to be
inserted chooses randomly k>1 locations and has to be placed in any one of
them. How much load can cuckoo hashing handle before collisions prevent the
successful assignment of the available items to the chosen locations? Practical
evaluations of this method have shown that one can allocate a number of
elements that is a large proportion of the size of the table, being very close
to 1 even for small values of k such as 4 or 5.
  In this paper we show that there is a critical value for this proportion:
with high probability, when the amount of available items is below this value,
then these can be allocated successfully, but when it exceeds this value, the
allocation becomes impossible. We give explicitly for each k>1 this critical
value. This answers an open question posed by Mitzenmacher (ESA '09) and
underpins theoretically the experimental results. Our proofs are based on the
translation of the question into a hypergraph setting, and the study of the
related typical properties of random k-uniform hypergraphs.
