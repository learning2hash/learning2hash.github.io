---
layout: publication
title: Revisiting SVD To Generate Powerful Node Embeddings For Recommendation Systems
authors: Amar Budhiraja
conference: Arxiv
year: 2021
bibkey: budhiraja2021revisiting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.03665'}]
tags: ["Datasets", "Evaluation", "Recommender Systems"]
short_authors: Amar Budhiraja
---
Graph Representation Learning (GRL) is an upcoming and promising area in
recommendation systems. In this paper, we revisit the Singular Value
Decomposition (SVD) of adjacency matrix for embedding generation of users and
items and use a two-layer neural network on top of these embeddings to learn
relevance between user-item pairs. Inspired by the success of higher-order
learning in GRL, we further propose an extension of this method to include
two-hop neighbors for SVD through the second order of the adjacency matrix and
demonstrate improved performance compared with the simple SVD method which only
uses one-hop neighbors. Empirical validation on three publicly available
datasets of recommendation system demonstrates that the proposed methods,
despite being simple, beat many state-of-the-art methods and for two of three
datasets beats all of them up to a margin of 10%. Through our research, we want
to shed light on the effectiveness of matrix factorization approaches,
specifically SVD, in the deep learning era and show that these methods still
contribute as important baselines in recommendation systems.