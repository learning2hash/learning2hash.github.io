---
layout: publication
title: Unified Loss Of Pair Similarity Optimization For Vision-language Retrieval
authors: Zheng Li, Caili Guo, Xin Wang, Zerun Feng, Jenq-Neng Hwang, Zhongtian Du
conference: Arxiv
year: 2022
bibkey: li2022unified
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.13869'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Li et al.
---
There are two popular loss functions used for vision-language retrieval,
i.e., triplet loss and contrastive learning loss, both of them essentially
minimize the difference between the similarities of negative pairs and positive
pairs. More specifically, Triplet loss with Hard Negative mining (Triplet-HN),
which is widely used in existing retrieval models to improve the discriminative
ability, is easy to fall into local minima in training. On the other hand,
Vision-Language Contrastive learning loss (VLC), which is widely used in the
vision-language pre-training, has been shown to achieve significant performance
gains on vision-language retrieval, but the performance of fine-tuning with VLC
on small datasets is not satisfactory. This paper proposes a unified loss of
pair similarity optimization for vision-language retrieval, providing a
powerful tool for understanding existing loss functions. Our unified loss
includes the hard sample mining strategy of VLC and introduces the margin used
by the triplet loss for better similarity separation. It is shown that both
Triplet-HN and VLC are special forms of our unified loss. Compared with the
Triplet-HN, our unified loss has a fast convergence speed. Compared with the
VLC, our unified loss is more discriminative and can provide better
generalization in downstream fine-tuning tasks. Experiments on image-text and
video-text retrieval benchmarks show that our unified loss can significantly
improve the performance of the state-of-the-art retrieval models.