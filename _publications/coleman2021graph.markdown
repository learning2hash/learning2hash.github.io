---
layout: publication
title: Graph Reordering For Cache-efficient Near Neighbor Search
authors: Benjamin Coleman, Santiago Segarra, Anshumali Shrivastava, Alex Smola
conference: Arxiv
year: 2021
bibkey: coleman2021graph
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.03221'}]
tags: [Evaluation, Graph-based ANN, Efficiency]
short_authors: Coleman et al.
---
Graph search is one of the most successful algorithmic trends in near
neighbor search. Several of the most popular and empirically successful
algorithms are, at their core, a simple walk along a pruned near neighbor
graph. Such algorithms consistently perform at the top of industrial speed
benchmarks for applications such as embedding search. However, graph traversal
applications often suffer from poor memory access patterns, and near neighbor
search is no exception to this rule. Our measurements show that popular search
indices such as the hierarchical navigable small-world graph (HNSW) can have
poor cache miss performance. To address this problem, we apply graph reordering
algorithms to near neighbor graphs. Graph reordering is a memory layout
optimization that groups commonly-accessed nodes together in memory. We present
exhaustive experiments applying several reordering algorithms to a leading
graph-based near neighbor method based on the HNSW index. We find that
reordering improves the query time by up to 40%, and we demonstrate that the
time needed to reorder the graph is negligible compared to the time required to
construct the index.