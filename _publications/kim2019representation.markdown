---
layout: publication
title: Representation Learning With Weighted Inner Product For Universal Approximation
  Of General Similarities
authors: Geewook Kim, Akifumi Okuno, Kazuki Fukui, Hidetoshi Shimodaira
conference: Proceedings of the Twenty-Eighth International Joint Conference on Artificial
  Intelligence
year: 2019
bibkey: kim2019representation
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.10409'}]
tags: [IJCAI, Evaluation, AAAI, Distance Metric Learning, Datasets]
short_authors: Kim et al.
---
We propose \(\textit\{weighted inner product similarity\}\) (WIPS) for neural
network-based graph embedding. In addition to the parameters of neural
networks, we optimize the weights of the inner product by allowing positive and
negative values. Despite its simplicity, WIPS can approximate arbitrary general
similarities including positive definite, conditionally positive definite, and
indefinite kernels. WIPS is free from similarity model selection, since it can
learn any similarity models such as cosine similarity, negative Poincar\'e
distance and negative Wasserstein distance. Our experiments show that the
proposed method can learn high-quality distributed representations of nodes
from real datasets, leading to an accurate approximation of similarities as
well as high performance in inductive tasks.