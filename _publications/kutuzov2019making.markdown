---
layout: publication
title: Making Fast Graph-based Algorithms With Graph Metric Embeddings
authors: Andrey Kutuzov, Mohammad Dorgham, Oleksiy Oliynyk, Chris Biemann, Alexander
  Panchenko
conference: Proceedings of the 57th Annual Meeting of the Association for Computational
  Linguistics
year: 2019
bibkey: kutuzov2019making
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.07040'}]
tags: []
short_authors: Kutuzov et al.
---
The computation of distance measures between nodes in graphs is inefficient
and does not scale to large graphs. We explore dense vector representations as
an effective way to approximate the same information: we introduce a simple yet
efficient and effective approach for learning graph embeddings. Instead of
directly operating on the graph structure, our method takes structural measures
of pairwise node similarities into account and learns dense node
representations reflecting user-defined graph distance measures, such as
e.g.the shortest path distance or distance measures that take information
beyond the graph structure into account. We demonstrate a speed-up of several
orders of magnitude when predicting word similarity by vector operations on our
embeddings as opposed to directly computing the respective path-based measures,
while outperforming various other graph embeddings on semantic similarity and
word sense disambiguation tasks and show evaluations on the WordNet graph and
two knowledge base graphs.