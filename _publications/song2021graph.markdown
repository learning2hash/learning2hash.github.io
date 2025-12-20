---
layout: publication
title: Graph Attention Collaborative Similarity Embedding For Recommender System
authors: Jinbo Song, Chao Chang, Fei Sun, Zhenyang Chen, Guoyong Hu, Peng Jiang
conference: Lecture Notes in Computer Science
year: 2021
bibkey: song2021graph
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.03135'}]
tags: ["Evaluation", "Graph Based ANN", "Recommender Systems", "Tools & Libraries"]
short_authors: Song et al.
---
We present Graph Attention Collaborative Similarity Embedding (GACSE), a new
recommendation framework that exploits collaborative information in the
user-item bipartite graph for representation learning. Our framework consists
of two parts: the first part is to learn explicit graph collaborative filtering
information such as user-item association through embedding propagation with
attention mechanism, and the second part is to learn implicit graph
collaborative information such as user-user similarities and item-item
similarities through auxiliary loss. We design a new loss function that
combines BPR loss with adaptive margin and similarity loss for the similarities
learning. Extensive experiments on three benchmarks show that our model is
consistently better than the latest state-of-the-art models.