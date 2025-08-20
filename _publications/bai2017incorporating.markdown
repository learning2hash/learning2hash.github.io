---
layout: publication
title: Incorporating Intra-class Variance To Fine-grained Visual Recognition
authors: Yan Bai, Feng Gao, Yihang Lou, Shiqi Wang, Tiejun Huang, Ling-Yu Duan
conference: 2017 IEEE International Conference on Multimedia and Expo (ICME)
year: 2017
bibkey: bai2017incorporating
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.00196'}]
tags: [Distance Metric Learning, Datasets, Evaluation]
short_authors: Bai et al.
---
Fine-grained visual recognition aims to capture discriminative
characteristics amongst visually similar categories. The state-of-the-art
research work has significantly improved the fine-grained recognition
performance by deep metric learning using triplet network. However, the impact
of intra-category variance on the performance of recognition and robust feature
representation has not been well studied. In this paper, we propose to leverage
intra-class variance in metric learning of triplet network to improve the
performance of fine-grained recognition. Through partitioning training images
within each category into a few groups, we form the triplet samples across
different categories as well as different groups, which is called Group
Sensitive TRiplet Sampling (GS-TRS). Accordingly, the triplet loss function is
strengthened by incorporating intra-class variance with GS-TRS, which may
contribute to the optimization objective of triplet network. Extensive
experiments over benchmark datasets CompCar and VehicleID show that the
proposed GS-TRS has significantly outperformed state-of-the-art approaches in
both classification and retrieval tasks.