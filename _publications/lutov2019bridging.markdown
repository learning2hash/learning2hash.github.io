---
layout: publication
title: 'Bridging The Gap Between Community And Node Representations: Graph Embedding
  Via Community Detection'
authors: "Artem Lutov, Dingqi Yang, Philippe Cudr\xE9-Mauroux"
conference: 2019 IEEE International Conference on Big Data (Big Data)
year: 2019
bibkey: lutov2019bridging
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08808'}]
tags: ["Distance Metric Learning"]
short_authors: "Artem Lutov, Dingqi Yang, Philippe Cudr\xE9-Mauroux"
---
Graph embedding has become a key component of many data mining and analysis
systems. Current graph embedding approaches either sample a large number of
node pairs from a graph to learn node embeddings via stochastic optimization or
factorize a high-order proximity/adjacency matrix of the graph via
computationally expensive matrix factorization techniques. These approaches
typically require significant resources for the learning process and rely on
multiple parameters, which limits their applicability in practice. Moreover,
most of the existing graph embedding techniques operate effectively in one
specific metric space only (e.g., the one produced with cosine similarity), do
not preserve higher-order structural features of the input graph and cannot
automatically determine a meaningful number of embedding dimensions. Typically,
the produced embeddings are not easily interpretable, which complicates further
analyses and limits their applicability. To address these issues, we propose
DAOR, a highly efficient and parameter-free graph embedding technique producing
metric space-robust, compact and interpretable embeddings without any manual
tuning. Compared to a dozen state-of-the-art graph embedding algorithms, DAOR
yields competitive results on both node classification (which benefits form
high-order proximity) and link prediction (which relies on low-order proximity
mostly). Unlike existing techniques, however, DAOR does not require any
parameter tuning and improves the embeddings generation speed by several orders
of magnitude. Our approach has hence the ambition to greatly simplify and speed
up data analysis tasks involving graph representation learning.