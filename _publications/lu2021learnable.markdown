---
layout: publication
title: "Learnable Locality-Sensitive Hashing for Video Anomaly Detection"
authors: Lu Yue, Cao Congqi, Zhang Yanning
conference: "Arxiv"
year: 2021
bibkey: lu2021learnable
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2111.07839"}
tags: ['ARXIV', 'LSH']
---
Video anomaly detection (VAD) mainly refers to identifying anomalous events that
have not occurred in the training set where only normal samples are available.
Existing works usually formulate VAD as a reconstruction or prediction problem.
However, the adaptability and scalability of these methods are limited. In this
paper, we propose a novel distance-based VAD method to take advantage of all the
available normal data efficiently and flexibly. In our method, the smaller the
distance between a testing sample and normal samples, the higher the probability
that the testing sample is normal. Specifically, we propose to use locality-
sensitive hashing (LSH) to map samples whose similarity exceeds a certain
threshold into the same bucket in advance. In this manner, the complexity of
near neighbor search is cut down significantly. To make the samples that are
semantically similar get closer and samples not similar get further apart, we
propose a novel learnable version of LSH that embeds LSH into a neural network
and optimizes the hash functions with contrastive learning strategy. The
proposed method is robust to data imbalance and can handle the large intra-class
variations in normal data flexibly. Besides, it has a good ability of
scalability. Extensive experiments demonstrate the superiority of our method,
which achieves new state-of-the-art results on VAD benchmarks.
