---
layout: publication
title: Joint Learning of Deep Retrieval Model and Product Quantization based Embedding
  Index
authors: Zhang et al.
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: zhang2021joint
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.03933'}]
tags: ["Quantization", "SIGIR"]
---
Embedding index that enables fast approximate nearest neighbor(ANN) search,
serves as an indispensable component for state-of-the-art deep retrieval
systems. Traditional approaches, often separating the two steps of embedding
learning and index building, incur additional indexing time and decayed
retrieval accuracy. In this paper, we propose a novel method called Poeem,
which stands for product quantization based embedding index jointly trained
with deep retrieval model, to unify the two separate steps within an end-to-end
training, by utilizing a few techniques including the gradient straight-through
estimator, warm start strategy, optimal space decomposition and Givens
rotation. Extensive experimental results show that the proposed method not only
improves retrieval accuracy significantly but also reduces the indexing time to
almost none. We have open sourced our approach for the sake of comparison and
reproducibility.