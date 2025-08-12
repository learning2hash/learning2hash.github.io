---
layout: publication
title: Levenshtein Distance Embedding With Poisson Regression For DNA Storage
authors: Xiang Wei, Alan J. X. Guo, Sihan Sun, Mengyi Wei, Wei Yu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: wei2023levenshtein
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.07931'}]
tags: ["AAAI"]
short_authors: Wei et al.
---
Efficient computation or approximation of Levenshtein distance, a widely-used
metric for evaluating sequence similarity, has attracted significant attention
with the emergence of DNA storage and other biological applications. Sequence
embedding, which maps Levenshtein distance to a conventional distance between
embedding vectors, has emerged as a promising solution. In this paper, a novel
neural network-based sequence embedding technique using Poisson regression is
proposed. We first provide a theoretical analysis of the impact of embedding
dimension on model performance and present a criterion for selecting an
appropriate embedding dimension. Under this embedding dimension, the Poisson
regression is introduced by assuming the Levenshtein distance between sequences
of fixed length following a Poisson distribution, which naturally aligns with
the definition of Levenshtein distance. Moreover, from the perspective of the
distribution of embedding distances, Poisson regression approximates the
negative log likelihood of the chi-squared distribution and offers advancements
in removing the skewness. Through comprehensive experiments on real DNA storage
data, we demonstrate the superior performance of the proposed method compared
to state-of-the-art approaches.