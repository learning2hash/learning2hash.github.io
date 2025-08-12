---
layout: publication
title: Parallel Computation Of Graph Embeddings
authors: Chi Thang Duong, Hongzhi Yin, Thanh Dat Hoang, Truong Giang Le Ba, Matthias
  Weidlich, Quoc Viet Hung Nguyen, Karl Aberer
conference: Arxiv
year: 2019
bibkey: duong2019parallel
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.02977'}]
tags: []
short_authors: Duong et al.
---
Graph embedding aims at learning a vector-based representation of vertices
that incorporates the structure of the graph. This representation then enables
inference of graph properties. Existing graph embedding techniques, however, do
not scale well to large graphs. We therefore propose a framework for parallel
computation of a graph embedding using a cluster of compute nodes with resource
constraints. We show how to distribute any existing embedding technique by
first splitting a graph for any given set of constrained compute nodes and then
reconciling the embedding spaces derived for these subgraphs. We also propose a
new way to evaluate the quality of graph embeddings that is independent of a
specific inference task. Based thereon, we give a formal bound on the
difference between the embeddings derived by centralised and parallel
computation. Experimental results illustrate that our approach for parallel
computation scales well, while largely maintaining the embedding quality.