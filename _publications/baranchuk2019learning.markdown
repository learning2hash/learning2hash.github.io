---
layout: publication
title: Learning To Route In Similarity Graphs
authors: Baranchuk et al.
conference: Arxiv
year: 2019
bibkey: baranchuk2019learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.10987'}]
tags: [Tree Based ANN, Locality Sensitive Hashing, Evaluation]
---
Recently similarity graphs became the leading paradigm for efficient nearest
neighbor search, outperforming traditional tree-based and LSH-based methods.
Similarity graphs perform the search via greedy routing: a query traverses the
graph and in each vertex moves to the adjacent vertex that is the closest to
this query. In practice, similarity graphs are often susceptible to local
minima, when queries do not reach its nearest neighbors, getting stuck in
suboptimal vertices. In this paper we propose to learn the routing function
that overcomes local minima via incorporating information about the graph
global structure. In particular, we augment the vertices of a given graph with
additional representations that are learned to provide the optimal routing from
the start vertex to the query nearest neighbor. By thorough experiments, we
demonstrate that the proposed learnable routing successfully diminishes the
local minima problem and significantly improves the overall search performance.