---
layout: publication
title: 'FINGER: Fast Inference For Graph-based Approximate Nearest Neighbor Search'
authors: Patrick H. Chen, Chang Wei-Cheng, Yu Hsiang-Fu, Inderjit S. Dhillon, Hsieh
  Cho-Jui
conference: 'WWW ''23: The ACM Web Conference 2023'
year: 2022
bibkey: chen2022finger
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.11408'}]
tags: ["Datasets", "Evaluation", "Graph Based ANN", "Neural Hashing"]
short_authors: Chen et al.
---
Approximate K-Nearest Neighbor Search (AKNNS) has now become ubiquitous in
modern applications, for example, as a fast search procedure with two tower
deep learning models. Graph-based methods for AKNNS in particular have received
great attention due to their superior performance. These methods rely on greedy
graph search to traverse the data points as embedding vectors in a database.
Under this greedy search scheme, we make a key observation: many distance
computations do not influence search updates so these computations can be
approximated without hurting performance. As a result, we propose FINGER, a
fast inference method to achieve efficient graph search. FINGER approximates
the distance function by estimating angles between neighboring residual vectors
with low-rank bases and distribution matching. The approximated distance can be
used to bypass unnecessary computations, which leads to faster searches.
Empirically, accelerating a popular graph-based method named HNSW by FINGER is
shown to outperform existing graph-based methods by 20%-60% across different
benchmark datasets.