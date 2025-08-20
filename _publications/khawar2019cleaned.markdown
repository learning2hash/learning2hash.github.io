---
layout: publication
title: Cleaned Similarity For Better Memory-based Recommenders
authors: Farhan Khawar, Nevin L. Zhang
conference: Proceedings of the 42nd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2019
bibkey: khawar2019cleaned
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.07370'}]
tags: [Recommender Systems, Distance Metric Learning, SIGIR, Evaluation]
short_authors: Farhan Khawar, Nevin L. Zhang
---
Memory-based collaborative filtering methods like user or item k-nearest
neighbors (kNN) are a simple yet effective solution to the recommendation
problem. The backbone of these methods is the estimation of the empirical
similarity between users/items. In this paper, we analyze the spectral
properties of the Pearson and the cosine similarity estimators, and we use
tools from random matrix theory to argue that they suffer from noise and
eigenvalues spreading. We argue that, unlike the Pearson correlation, the
cosine similarity naturally possesses the desirable property of eigenvalue
shrinkage for large eigenvalues. However, due to its zero-mean assumption, it
overestimates the largest eigenvalues. We quantify this overestimation and
present a simple re-scaling and noise cleaning scheme. This results in better
performance of the memory-based methods compared to their vanilla counterparts.