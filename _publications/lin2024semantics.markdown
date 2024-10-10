---
layout: publication
title: Semantics-preserving Hashing For Cross-view Retrieval
authors: Lin Zijia, Ding, Wang
conference: "Arxiv"
year: 2024
bibkey: lin2024semantics
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/lin2015semantics"}
tags: ['ARXIV', 'Cross Modal', 'Supervised']
---
With benefits of low storage costs and high query speeds hashing methods are widely researched for efficiently retrieving large-scale data which commonly contains multiple views e.g. a news report with images videos and texts. In this paper we study the problem of cross-view retrieval and propose an effective Semantics-Preserving Hashing method termed SePH. Given semantic affinities of training data as supervised information SePH transforms them into a probability distribution and approximates it with tobe-learnt hash codes in Hamming space via minimizing the Kullback-Leibler divergence. Then kernel logistic regression with a sampling strategy is utilized to learn the nonlinear projections from features in each view to the learnt hash codes. And for any unseen instance predicted hash codes and their corresponding output probabilities from observed views are utilized to determine its unified hash code using a novel probabilistic approach. Extensive experiments conducted on three benchmark datasets well demonstrate the effectiveness and reasonableness of SePH.
