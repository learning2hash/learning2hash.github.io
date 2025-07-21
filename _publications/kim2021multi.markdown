---
layout: publication
title: Multi-level Distance Regularization for Deep Metric Learning
authors: Kim Yonghyun, Park Wonpyo
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: kim2021multi
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04223'}]
tags: ["AAAI", "Distance-Metric-Learning"]
---
We propose a novel distance-based regularization method for deep metric
learning called Multi-level Distance Regularization (MDR). MDR explicitly
disturbs a learning procedure by regularizing pairwise distances between
embedding vectors into multiple levels that represents a degree of similarity
between a pair. In the training stage, the model is trained with both MDR and
an existing loss function of deep metric learning, simultaneously; the two
losses interfere with the objective of each other, and it makes the learning
process difficult. Moreover, MDR prevents some examples from being ignored or
overly influenced in the learning process. These allow the parameters of the
embedding network to be settle on a local optima with better generalization.
Without bells and whistles, MDR with simple Triplet loss achieves
the-state-of-the-art performance in various benchmark datasets: CUB-200-2011,
Cars-196, Stanford Online Products, and In-Shop Clothes Retrieval. We
extensively perform ablation studies on its behaviors to show the effectiveness
of MDR. By easily adopting our MDR, the previous approaches can be improved in
performance and generalization ability.