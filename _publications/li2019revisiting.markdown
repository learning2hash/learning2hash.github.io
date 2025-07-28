---
layout: publication
title: Revisiting Metric Learning For Few-shot Image Classification
authors: Xiaomeng Li, Lequan Yu, Chi-wing Fu, Meng Fang, Pheng-ann Heng
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: li2019revisiting
citations: 574
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.03123'}]
tags: ["CVPR", "Distance Metric Learning", "Few Shot & Zero Shot"]
short_authors: Li et al.
---
The goal of few-shot learning is to recognize new visual concepts with just a
few amount of labeled samples in each class. Recent effective metric-based
few-shot approaches employ neural networks to learn a feature similarity
comparison between query and support examples. However, the importance of
feature embedding, i.e., exploring the relationship among training samples, is
neglected. In this work, we present a simple yet powerful baseline for few-shot
classification by emphasizing the importance of feature embedding.
Specifically, we revisit the classical triplet network from deep metric
learning, and extend it into a deep K-tuplet network for few-shot learning,
utilizing the relationship among the input samples to learn a general
representation learning via episode-training. Once trained, our network is able
to extract discriminative features for unseen novel categories and can be
seamlessly incorporated with a non-linear distance metric function to
facilitate the few-shot classification. Our result on the miniImageNet
benchmark outperforms other metric-based few-shot classification methods. More
importantly, when evaluated on completely different datasets (Caltech-101,
CUB-200, Stanford Dogs and Cars) using the model trained with miniImageNet, our
method significantly outperforms prior methods, demonstrating its superior
capability to generalize to unseen classes.