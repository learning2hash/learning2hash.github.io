---
layout: publication
title: Product-based Neural Networks For User Response Prediction
authors: Yanru Qu, Han Cai, Kan Ren, Weinan Zhang, Yong Yu, Ying Wen, Jun Wang
conference: 2016 IEEE 16th International Conference on Data Mining (ICDM)
year: 2016
bibkey: qu2016product
citations: 627
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.00144'}]
tags: ["Recommender Systems"]
short_authors: Qu et al.
---
Predicting user responses, such as clicks and conversions, is of great
importance and has found its usage in many Web applications including
recommender systems, web search and online advertising. The data in those
applications is mostly categorical and contains multiple fields; a typical
representation is to transform it into a high-dimensional sparse binary feature
representation via one-hot encoding. Facing with the extreme sparsity,
traditional models may limit their capacity of mining shallow patterns from the
data, i.e. low-order feature combinations. Deep models like deep neural
networks, on the other hand, cannot be directly applied for the
high-dimensional input because of the huge feature space. In this paper, we
propose a Product-based Neural Networks (PNN) with an embedding layer to learn
a distributed representation of the categorical data, a product layer to
capture interactive patterns between inter-field categories, and further fully
connected layers to explore high-order feature interactions. Our experimental
results on two large-scale real-world ad click datasets demonstrate that PNNs
consistently outperform the state-of-the-art models on various metrics.