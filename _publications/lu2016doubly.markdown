---
layout: publication
title: Doubly Stochastic Neighbor Embedding On Spheres
authors: Yao Lu, Jukka Corander, Zhirong Yang
conference: Pattern Recognition Letters
year: 2019
bibkey: lu2016doubly
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.01977'}]
tags: ["Datasets"]
short_authors: Yao Lu, Jukka Corander, Zhirong Yang
---
Stochastic Neighbor Embedding (SNE) methods minimize the divergence between
the similarity matrix of a high-dimensional data set and its counterpart from a
low-dimensional embedding, leading to widely applied tools for data
visualization. Despite their popularity, the current SNE methods experience a
crowding problem when the data include highly imbalanced similarities. This
implies that the data points with higher total similarity tend to get crowded
around the display center. To solve this problem, we introduce a fast
normalization method and normalize the similarity matrix to be doubly
stochastic such that all the data points have equal total similarities.
Furthermore, we show empirically and theoretically that the doubly
stochasticity constraint often leads to embeddings which are approximately
spherical. This suggests replacing a flat space with spheres as the embedding
space. The spherical embedding eliminates the discrepancy between the center
and the periphery in visualization, which efficiently resolves the crowding
problem. We compared the proposed method (DOSNES) with the state-of-the-art SNE
method on three real-world datasets and the results clearly indicate that our
method is more favorable in terms of visualization quality.