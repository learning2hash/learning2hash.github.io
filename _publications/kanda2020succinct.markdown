---
layout: publication
title: Succinct Trit-array Trie for Scalable Trajectory Similarity Search
authors: Kanda et al.
conference: Proceedings of the 28th International Conference on Advances in Geographic
  Information Systems
year: 2020
bibkey: kanda2020succinct
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.10917'}]
tags: [Similarity Search]
---
Massive datasets of spatial trajectories representing the mobility of a
diversity of moving objects are ubiquitous in research and industry. Similarity
search of a large collection of trajectories is indispensable for turning these
datasets into knowledge. Locality sensitive hashing (LSH) is a powerful
technique for fast similarity searches. Recent methods employ LSH and attempt
to realize an efficient similarity search of trajectories; however, those
methods are inefficient in terms of search time and memory when applied to
massive datasets. To address this problem, we present the trajectory-indexing
succinct trit-array trie (tSTAT), which is a scalable method leveraging LSH for
trajectory similarity searches. tSTAT quickly performs the search on a tree
data structure called trie. We also present two novel techniques that enable to
dramatically enhance the memory efficiency of tSTAT. One is a node reduction
technique that substantially omits redundant trie nodes while maintaining the
time performance. The other is a space-efficient representation that leverages
the idea behind succinct data structures (i.e., a compressed data structure
supporting fast data operations). We experimentally test tSTAT on its ability
to retrieve similar trajectories for a query from large collections of
trajectories and show that tSTAT performs superiorly in comparison to
state-of-the-art similarity search methods.