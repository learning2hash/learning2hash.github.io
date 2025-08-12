---
layout: publication
title: Knowledge Graph Convolutional Networks For Recommender Systems
authors: Hongwei Wang, Miao Zhao, Xing Xie, Wenjie Li, Minyi Guo
conference: The World Wide Web Conference
year: 2019
bibkey: wang2019knowledge
citations: 897
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.12575'}]
tags: ["Recommender Systems"]
short_authors: Wang et al.
---
To alleviate sparsity and cold start problem of collaborative filtering based
recommender systems, researchers and engineers usually collect attributes of
users and items, and design delicate algorithms to exploit these additional
information. In general, the attributes are not isolated but connected with
each other, which forms a knowledge graph (KG). In this paper, we propose
Knowledge Graph Convolutional Networks (KGCN), an end-to-end framework that
captures inter-item relatedness effectively by mining their associated
attributes on the KG. To automatically discover both high-order structure
information and semantic information of the KG, we sample from the neighbors
for each entity in the KG as their receptive field, then combine neighborhood
information with bias when calculating the representation of a given entity.
The receptive field can be extended to multiple hops away to model high-order
proximity information and capture users' potential long-distance interests.
Moreover, we implement the proposed KGCN in a minibatch fashion, which enables
our model to operate on large datasets and KGs. We apply the proposed model to
three datasets about movie, book, and music recommendation, and experiment
results demonstrate that our approach outperforms strong recommender baselines.