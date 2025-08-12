---
layout: publication
title: 'Multisiam: Self-supervised Multi-instance Siamese Representation Learning
  For Autonomous Driving'
authors: Kai Chen, Lanqing Hong, Hang Xu, Zhenguo Li, Dit-Yan Yeung
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: chen2021multisiam
citations: 26
additional_links: [{name: Code, url: 'https://github.com/KaiChen1998/MultiSiam'},
  {name: Paper, url: 'https://arxiv.org/abs/2108.12178'}]
tags: ["ICCV", "Self-Supervised"]
short_authors: Chen et al.
---
Autonomous driving has attracted much attention over the years but turns out
to be harder than expected, probably due to the difficulty of labeled data
collection for model training. Self-supervised learning (SSL), which leverages
unlabeled data only for representation learning, might be a promising way to
improve model performance. Existing SSL methods, however, usually rely on the
single-centric-object guarantee, which may not be applicable for multi-instance
datasets such as street scenes. To alleviate this limitation, we raise two
issues to solve: (1) how to define positive samples for cross-view consistency
and (2) how to measure similarity in multi-instance circumstances. We first
adopt an IoU threshold during random cropping to transfer global-inconsistency
to local-consistency. Then, we propose two feature alignment methods to enable
2D feature maps for multi-instance similarity measurement. Additionally, we
adopt intra-image clustering with self-attention for further mining intra-image
similarity and translation-invariance. Experiments show that, when pre-trained
on Waymo dataset, our method called Multi-instance Siamese Network (MultiSiam)
remarkably improves generalization ability and achieves state-of-the-art
transfer performance on autonomous driving benchmarks, including Cityscapes and
BDD100K, while existing SSL counterparts like MoCo, MoCo-v2, and BYOL show
significant performance drop. By pre-training on SODA10M, a large-scale
autonomous driving dataset, MultiSiam exceeds the ImageNet pre-trained MoCo-v2,
demonstrating the potential of domain-specific pre-training. Code will be
available at https://github.com/KaiChen1998/MultiSiam.