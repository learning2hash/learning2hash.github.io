---
layout: publication
title: Asymmetric Hashing For Fast Ranking Via Neural Network Measures
authors: Khoa Doan, Shulong Tan, Weijie Zhao, Ping Li
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: doan2022asymmetric
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.00619'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Recommender Systems", "SIGIR", "Similarity Search"]
short_authors: Doan et al.
---
Fast item ranking is an important task in recommender systems. In previous
works, graph-based Approximate Nearest Neighbor (ANN) approaches have
demonstrated good performance on item ranking tasks with generic
searching/matching measures (including complex measures such as neural network
measures). However, since these ANN approaches must go through the neural
measures several times during ranking, the computation is not practical if the
neural measure is a large network. On the other hand, fast item ranking using
existing hashing-based approaches, such as Locality Sensitive Hashing (LSH),
only works with a limited set of measures. Previous learning-to-hash approaches
are also not suitable to solve the fast item ranking problem since they can
take a significant amount of time and computation to train the hash functions.
Hashing approaches, however, are attractive because they provide a principle
and efficient way to retrieve candidate items. In this paper, we propose a
simple and effective learning-to-hash approach for the fast item ranking
problem that can be used for any type of measure, including neural network
measures. Specifically, we solve this problem with an asymmetric hashing
framework based on discrete inner product fitting. We learn a pair of related
hash functions that map heterogeneous objects (e.g., users and items) into a
common discrete space where the inner product of their binary codes reveals
their true similarity defined via the original searching measure. The fast
ranking problem is reduced to an ANN search via this asymmetric hashing scheme.
Then, we propose a sampling strategy to efficiently select relevant and
contrastive samples to train the hashing model. We empirically validate the
proposed method against the existing state-of-the-art fast item ranking methods
in several combinations of non-linear searching functions and prominent
datasets.