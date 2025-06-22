---
layout: publication
title: Optimizing Ranking Measures For Compact Binary Code Learning
authors: Guosheng Lin, Chunhua Shen, Jianxin Wu
conference: Arxiv
year: 2014
citations: 13
bibkey: lin2014optimizing
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.1151'}]
tags: [Applications, Hashing Methods, Loss Functions]
---
Hashing has proven a valuable tool for large-scale information retrieval.
Despite much success, existing hashing methods optimize over simple objectives
such as the reconstruction error or graph Laplacian related loss functions,
instead of the performance evaluation criteria of interest---multivariate
performance measures such as the AUC and NDCG. Here we present a general
framework (termed StructHash) that allows one to directly optimize multivariate
performance measures. The resulting optimization problem can involve
exponentially or infinitely many variables and constraints, which is more
challenging than standard structured output learning. To solve the StructHash
optimization problem, we use a combination of column generation and
cutting-plane techniques. We demonstrate the generality of StructHash by
applying it to ranking prediction and image retrieval, and show that it
outperforms a few state-of-the-art hashing methods.