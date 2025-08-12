---
layout: publication
title: Fast Exact Shortest-path Distance Queries On Large Networks By Pruned Landmark
  Labeling
authors: Takuya Akiba, Yoichi Iwata, Yuichi Yoshida
conference: Proceedings of the 2013 ACM SIGMOD International Conference on Management
  of Data
year: 2013
bibkey: akiba2013fast
citations: 349
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1304.4661'}]
tags: ["Efficiency", "Scalability"]
short_authors: Takuya Akiba, Yoichi Iwata, Yuichi Yoshida
---
We propose a new exact method for shortest-path distance queries on
large-scale networks. Our method precomputes distance labels for vertices by
performing a breadth-first search from every vertex. Seemingly too obvious and
too inefficient at first glance, the key ingredient introduced here is pruning
during breadth-first searches. While we can still answer the correct distance
for any pair of vertices from the labels, it surprisingly reduces the search
space and sizes of labels. Moreover, we show that we can perform 32 or 64
breadth-first searches simultaneously exploiting bitwise operations. We
experimentally demonstrate that the combination of these two techniques is
efficient and robust on various kinds of large-scale real-world networks. In
particular, our method can handle social networks and web graphs with hundreds
of millions of edges, which are two orders of magnitude larger than the limits
of previous exact methods, with comparable query time to those of previous
methods.