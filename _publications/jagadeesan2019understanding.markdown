---
layout: publication
title: Understanding Sparse JL For Feature Hashing
authors: Meena Jagadeesan
conference: "Neural Information Processing Systems"
year: 2019
bibkey: jagadeesan2019understanding
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2019/hash/502cc2c94be1a7c4ca7ef25b8b50bc04-Abstract.html"}
tags: ['ICML', 'Independent', 'NEURIPS']
---
Feature hashing and other random projection schemes are commonly used to reduce the dimensionality of feature vectors. The goal is to efficiently project a high-dimensional feature vector living in R^n into a much lower-dimensional space R^m, while approximately preserving Euclidean norm. These schemes can be constructed using sparse random projections, for example using a sparse Johnson-Lindenstrauss (JL) transform. A line of work introduced by Weinberger et. al (ICML '09) analyzes the accuracy of sparse JL with sparsity 1 on feature vectors with small linfinity-to-l2 norm ratio. Recently, Freksen, Kamma, and Larsen (NeurIPS '18) closed this line of work by proving a tight tradeoff between linfinity-to-l2 norm ratio and accuracy for sparse JL with sparsity 1. In this paper, we demonstrate the benefits of using sparsity s greater than 1 in sparse JL on feature vectors. Our main result is a tight tradeoff between linfinity-to-l2 norm ratio and accuracy for a general sparsity s, that significantly generalizes the result of Freksen et. al. Our result theoretically demonstrates that sparse JL with s > 1 can have significantly better norm-preservation properties on feature vectors than sparse JL with s = 1; we also empirically demonstrate this finding.
