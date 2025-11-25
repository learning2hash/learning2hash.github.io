---
layout: publication
title: A Scalable Solution To The Nearest Neighbor Search Problem Through Local-search
  Methods On Neighbor Graphs
authors: Eric S. Tellez, Guillermo Ruiz, Edgar Chavez, Mario Graff
conference: Pattern Analysis and Applications
year: 2017
bibkey: tellez2017a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10351'}]
tags: ["Evaluation", "Graph Based ANN", "Memory Efficiency"]
short_authors: Tellez et al.
---
Near neighbor search (NNS) is a powerful abstraction for data access;
however, data indexing is troublesome even for approximate indexes. For
intrinsically high-dimensional data, high-quality fast searches demand either
indexes with impractically large memory usage or preprocessing time.
  In this paper, we introduce an algorithm to solve a nearest-neighbor query
\(q\) by minimizing a kernel function defined by the distance from \(q\) to each
object in the database. The minimization is performed using metaheuristics to
solve the problem rapidly; even when some methods in the literature use this
strategy behind the scenes, our approach is the first one using it explicitly.
We also provide two approaches to select edges in the graph's construction
stage that limit memory footprint and reduce the number of free parameters
simultaneously.
  We carry out a thorough experimental comparison with state-of-the-art indexes
through synthetic and real-world datasets; we found out that our contributions
achieve competitive performances regarding speed, accuracy, and memory in
almost any of our benchmarks.