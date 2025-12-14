---
layout: publication
title: 'Deeptrax: Embedding Graphs Of Financial Transactions'
authors: C. Bayan Bruss, Anish Khazane, Jonathan Rider, Richard Serpe, Antonia Gogoglou,
  Keegan E. Hines
conference: 2019 18th IEEE International Conference On Machine Learning And Applications
  (ICMLA)
year: 2019
bibkey: bruss2019deeptrax
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.07225'}]
tags: [ICML, Graph-based ANN, Tools & Libraries, Datasets]
short_authors: Bruss et al.
---
Financial transactions can be considered edges in a heterogeneous graph
between entities sending money and entities receiving money. For financial
institutions, such a graph is likely large (with millions or billions of edges)
while also sparsely connected. It becomes challenging to apply machine learning
to such large and sparse graphs. Graph representation learning seeks to embed
the nodes of a graph into a Euclidean vector space such that graph topological
properties are preserved after the transformation. In this paper, we present a
novel application of representation learning to bipartite graphs of credit card
transactions in order to learn embeddings of account and merchant entities. Our
framework is inspired by popular approaches in graph embeddings and is trained
on two internal transaction datasets. This approach yields highly effective
embeddings, as quantified by link prediction AUC and F1 score. Further, the
resulting entity vectors retain intuitive semantic similarity that is explored
through visualizations and other qualitative analyses. Finally, we show how
these embeddings can be used as features in downstream machine learning
business applications such as fraud detection.