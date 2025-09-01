---
layout: publication
title: Graph Convolutional Neural Networks For Web-scale Recommender Systems
authors: Rex Ying, Ruining He, Kaifeng Chen, Pong Eksombatchai, William L. Hamilton,
  Jure Leskovec
conference: Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2018
bibkey: ying2018graph
citations: 3197
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.01973'}]
tags: ["Evaluation", "Graph Based ANN", "KDD", "Large Scale Search", "Neural Hashing", "Recommender Systems", "Robustness", "Scalability"]
short_authors: Ying et al.
---
Recent advancements in deep neural networks for graph-structured data have
led to state-of-the-art performance on recommender system benchmarks. However,
making these methods practical and scalable to web-scale recommendation tasks
with billions of items and hundreds of millions of users remains a challenge.
Here we describe a large-scale deep recommendation engine that we developed and
deployed at Pinterest. We develop a data-efficient Graph Convolutional Network
(GCN) algorithm PinSage, which combines efficient random walks and graph
convolutions to generate embeddings of nodes (i.e., items) that incorporate
both graph structure as well as node feature information. Compared to prior GCN
approaches, we develop a novel method based on highly efficient random walks to
structure the convolutions and design a novel training strategy that relies on
harder-and-harder training examples to improve robustness and convergence of
the model. We also develop an efficient MapReduce model inference algorithm to
generate embeddings using a trained model. We deploy PinSage at Pinterest and
train it on 7.5 billion examples on a graph with 3 billion nodes representing
pins and boards, and 18 billion edges. According to offline metrics, user
studies and A/B tests, PinSage generates higher-quality recommendations than
comparable deep learning and graph-based alternatives. To our knowledge, this
is the largest application of deep graph embeddings to date and paves the way
for a new generation of web-scale recommender systems based on graph
convolutional architectures.