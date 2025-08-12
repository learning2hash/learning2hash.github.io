---
layout: publication
title: Unsupervised Representation Learning By Predicting Random Distances
authors: Hu Wang, Guansong Pang, Chunhua Shen, Congbo Ma
conference: Proceedings of the Twenty-Ninth International Joint Conference on Artificial
  Intelligence
year: 2020
bibkey: wang2019unsupervised
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.12186'}]
tags: ["IJCAI", "Unsupervised"]
short_authors: Wang et al.
---
Deep neural networks have gained tremendous success in a broad range of
machine learning tasks due to its remarkable capability to learn semantic-rich
features from high-dimensional data. However, they often require large-scale
labelled data to successfully learn such features, which significantly hinders
their adaption into unsupervised learning tasks, such as anomaly detection and
clustering, and limits their applications into critical domains where obtaining
massive labelled data is prohibitively expensive. To enable unsupervised
learning on those domains, in this work we propose to learn features without
using any labelled data by training neural networks to predict data distances
in a randomly projected space. Random mapping is a theoretically proven
approach to obtain approximately preserved distances. To well predict these
random distances, the representation learner is optimised to learn genuine
class structures that are implicitly embedded in the randomly projected space.
Empirical results on 19 real-world datasets show that our learned
representations substantially outperform a few state-of-the-art competing
methods in both anomaly detection and clustering tasks. Code is available at
https://git.io/RDP