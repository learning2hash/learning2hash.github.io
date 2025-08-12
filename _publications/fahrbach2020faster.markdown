---
layout: publication
title: Faster Graph Embeddings Via Coarsening
authors: Matthew Fahrbach, Gramoz Goranci, Richard Peng, Sushant Sachdeva, Chi Wang
conference: Proceedings of the 37th International Conference on Machine Learning (ICML
  2020) 2953-2963
year: 2020
bibkey: fahrbach2020faster
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.02817'}]
tags: ["ICML"]
short_authors: Fahrbach et al.
---
Graph embeddings are a ubiquitous tool for machine learning tasks, such as
node classification and link prediction, on graph-structured data. However,
computing the embeddings for large-scale graphs is prohibitively inefficient
even if we are interested only in a small subset of relevant vertices. To
address this, we present an efficient graph coarsening approach, based on Schur
complements, for computing the embedding of the relevant vertices. We prove
that these embeddings are preserved exactly by the Schur complement graph that
is obtained via Gaussian elimination on the non-relevant vertices. As computing
Schur complements is expensive, we give a nearly-linear time algorithm that
generates a coarsened graph on the relevant vertices that provably matches the
Schur complement in expectation in each iteration. Our experiments involving
prediction tasks on graphs demonstrate that computing embeddings on the
coarsened graph, rather than the entire graph, leads to significant time
savings without sacrificing accuracy.