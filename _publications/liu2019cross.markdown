---
layout: publication
title: Cross-modal Zero-shot Hashing
authors: Liu Xuanwu, Li Zhao, Wang Jun, Yu Guoxian, Domeniconi Carlotta, Zhang Xiangliang
conference: 2019 IEEE International Conference on Data Mining (ICDM)
year: 2019
bibkey: liu2019cross
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.07388'}]
tags: ["Hashing-Methods", "Datasets", "Few-Shot-&-Zero-Shot", "Evaluation"]
short_authors: Liu et al.
---
Hashing has been widely studied for big data retrieval due to its low storage
cost and fast query speed. Zero-shot hashing (ZSH) aims to learn a hashing
model that is trained using only samples from seen categories, but can
generalize well to samples of unseen categories. ZSH generally uses category
attributes to seek a semantic embedding space to transfer knowledge from seen
categories to unseen ones. As a result, it may perform poorly when labeled data
are insufficient. ZSH methods are mainly designed for single-modality data,
which prevents their application to the widely spread multi-modal data. On the
other hand, existing cross-modal hashing solutions assume that all the
modalities share the same category labels, while in practice the labels of
different data modalities may be different. To address these issues, we propose
a general Cross-modal Zero-shot Hashing (CZHash) solution to effectively
leverage unlabeled and labeled multi-modality data with different label spaces.
CZHash first quantifies the composite similarity between instances using label
and feature information. It then defines an objective function to achieve deep
feature learning compatible with the composite similarity preserving, category
attribute space learning, and hashing coding function learning. CZHash further
introduces an alternative optimization procedure to jointly optimize these
learning objectives. Experiments on benchmark multi-modal datasets show that
CZHash significantly outperforms related representative hashing approaches both
on effectiveness and adaptability.