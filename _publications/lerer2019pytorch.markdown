---
layout: publication
title: 'Pytorch-biggraph: A Large-scale Graph Embedding System'
authors: Adam Lerer, Ledell Wu, Jiajun Shen, Timothee Lacroix, Luca Wehrstedt, Abhijit
  Bose, Alex Peysakhovich
conference: Proceedings of The Conference on Systems and Machine Learning 2019
year: 2019
bibkey: lerer2019pytorch
citations: 196
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.12287'}]
tags: ["Scalability"]
short_authors: Lerer et al.
---
Graph embedding methods produce unsupervised node features from graphs that
can then be used for a variety of machine learning tasks. Modern graphs,
particularly in industrial applications, contain billions of nodes and
trillions of edges, which exceeds the capability of existing embedding systems.
We present PyTorch-BigGraph (PBG), an embedding system that incorporates
several modifications to traditional multi-relation embedding systems that
allow it to scale to graphs with billions of nodes and trillions of edges. PBG
uses graph partitioning to train arbitrarily large embeddings on either a
single machine or in a distributed environment. We demonstrate comparable
performance with existing embedding systems on common benchmarks, while
allowing for scaling to arbitrarily large graphs and parallelization on
multiple machines. We train and evaluate embeddings on several large social
network graphs as well as the full Freebase dataset, which contains over 100
million nodes and 2 billion edges.