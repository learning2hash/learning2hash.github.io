---
layout: publication
title: Interest-aware Message-passing GCN For Recommendation
authors: Fan Liu, Zhiyong Cheng, Lei Zhu, Zan Gao, Liqiang Nie
conference: Proceedings of the Web Conference 2021
year: 2021
bibkey: liu2021interest
citations: 264
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.10044'}]
tags: [Evaluation, Supervised, Graph-based ANN, Datasets, Scalability, Unsupervised,
  Recommender Systems]
short_authors: Liu et al.
---
Graph Convolution Networks (GCNs) manifest great potential in recommendation.
This is attributed to their capability on learning good user and item
embeddings by exploiting the collaborative signals from the high-order
neighbors. Like other GCN models, the GCN based recommendation models also
suffer from the notorious over-smoothing problem - when stacking more layers,
node embeddings become more similar and eventually indistinguishable, resulted
in performance degradation. The recently proposed LightGCN and LR-GCN alleviate
this problem to some extent, however, we argue that they overlook an important
factor for the over-smoothing problem in recommendation, that is, high-order
neighboring users with no common interests of a user can be also involved in
the user's embedding learning in the graph convolution operation. As a result,
the multi-layer graph convolution will make users with dissimilar interests
have similar embeddings. In this paper, we propose a novel Interest-aware
Message-Passing GCN (IMP-GCN) recommendation model, which performs high-order
graph convolution inside subgraphs. The subgraph consists of users with similar
interests and their interacted items. To form the subgraphs, we design an
unsupervised subgraph generation module, which can effectively identify users
with common interests by exploiting both user feature and graph structure. To
this end, our model can avoid propagating negative information from high-order
neighbors into embedding learning. Experimental results on three large-scale
benchmark datasets show that our model can gain performance improvement by
stacking more layers and outperform the state-of-the-art GCN-based
recommendation models significantly.