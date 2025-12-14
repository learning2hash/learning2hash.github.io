---
layout: publication
title: 'Nformer: Robust Person Re-identification With Neighbor Transformer'
authors: Haochen Wang, Jiayi Shen, Yongtuo Liu, Yan Gao, Efstratios Gavves
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: wang2022nformer
citations: 144
additional_links: [{name: Code, url: 'https://github.com/haochenheheda/NFormer'},
  {name: Paper, url: 'https://arxiv.org/abs/2204.09331'}]
tags: [Scalability, Evaluation, CVPR, Datasets]
short_authors: Wang et al.
---
Person re-identification aims to retrieve persons in highly varying settings
across different cameras and scenarios, in which robust and discriminative
representation learning is crucial. Most research considers learning
representations from single images, ignoring any potential interactions between
them. However, due to the high intra-identity variations, ignoring such
interactions typically leads to outlier features. To tackle this issue, we
propose a Neighbor Transformer Network, or NFormer, which explicitly models
interactions across all input images, thus suppressing outlier features and
leading to more robust representations overall. As modelling interactions
between enormous amount of images is a massive task with lots of distractors,
NFormer introduces two novel modules, the Landmark Agent Attention, and the
Reciprocal Neighbor Softmax. Specifically, the Landmark Agent Attention
efficiently models the relation map between images by a low-rank factorization
with a few landmarks in feature space. Moreover, the Reciprocal Neighbor
Softmax achieves sparse attention to relevant -- rather than all -- neighbors
only, which alleviates interference of irrelevant representations and further
relieves the computational burden. In experiments on four large-scale datasets,
NFormer achieves a new state-of-the-art. The code is released at
https://github.com/haochenheheda/NFormer.