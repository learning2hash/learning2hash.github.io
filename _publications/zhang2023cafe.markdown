---
layout: publication
title: 'CAFE: Towards Compact, Adaptive, And Fast Embedding For Large-scale Recommendation
  Models'
authors: Hailin Zhang, Zirui Liu, Boxuan Chen, Yikai Zhao, Tong Zhao, Tong Yang, Bin
  Cui
conference: Proceedings of the ACM on Management of Data
year: 2023
bibkey: zhang2023cafe
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.03256'}]
tags: ["Efficiency", "Memory Efficiency", "Recommender Systems"]
short_authors: Zhang et al.
---
Recently, the growing memory demands of embedding tables in Deep Learning
Recommendation Models (DLRMs) pose great challenges for model training and
deployment. Existing embedding compression solutions cannot simultaneously meet
three key design requirements: memory efficiency, low latency, and adaptability
to dynamic data distribution. This paper presents CAFE, a Compact, Adaptive,
and Fast Embedding compression framework that addresses the above requirements.
The design philosophy of CAFE is to dynamically allocate more memory resources
to important features (called hot features), and allocate less memory to
unimportant ones. In CAFE, we propose a fast and lightweight sketch data
structure, named HotSketch, to capture feature importance and report hot
features in real time. For each reported hot feature, we assign it a unique
embedding. For the non-hot features, we allow multiple features to share one
embedding by using hash embedding technique. Guided by our design philosophy,
we further propose a multi-level hash embedding framework to optimize the
embedding tables of non-hot features. We theoretically analyze the accuracy of
HotSketch, and analyze the model convergence against deviation. Extensive
experiments show that CAFE significantly outperforms existing embedding
compression methods, yielding 3.92% and 3.68% superior testing AUC on Criteo
Kaggle dataset and CriteoTB dataset at a compression ratio of 10000x. The
source codes of CAFE are available at GitHub.