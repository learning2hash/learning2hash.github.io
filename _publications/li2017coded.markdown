---
layout: publication
title: Coded Terasort
authors: Songze Li, Sucha Supittayapornpong, Mohammad Ali Maddah-Ali, A. Salman Avestimehr
conference: Arxiv
year: 2017
bibkey: li2017coded
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.04850'}]
tags: []
short_authors: Li et al.
---
We focus on sorting, which is the building block of many machine learning
algorithms, and propose a novel distributed sorting algorithm, named Coded
TeraSort, which substantially improves the execution time of the TeraSort
benchmark in Hadoop MapReduce. The key idea of Coded TeraSort is to impose
structured redundancy in data, in order to enable in-network coding
opportunities that overcome the data shuffling bottleneck of TeraSort. We
empirically evaluate the performance of CodedTeraSort algorithm on Amazon EC2
clusters, and demonstrate that it achieves 1.97x - 3.39x speedup, compared with
TeraSort, for typical settings of interest.