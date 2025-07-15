---
layout: publication
title: Efficient Training Of Very Deep Neural Networks For Supervised Hashing
authors: Zhang Ziming, Chen, Saligrama
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: zhang2025efficient
citations: 111
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.04524'}]
tags: [Datasets, Alt, Evaluation, HASHING Methods, Efficiency And Optimization, CVPR]
---
In this paper, we propose training very deep neural networks (DNNs) for supervised learning of hash codes. Existing methods in this context train relatively "shallow" networks limited by the issues arising in back propagation (e.e. vanishing gradients) as well as computational efficiency. We propose a novel and efficient training algorithm inspired by alternating direction method of multipliers (ADMM) that overcomes some of these limitations. Our method decomposes the training process into independent layer-wise local updates through auxiliary variables. Empirically we observe that our training algorithm always converges and its computational complexity is linearly proportional to the number of edges in the networks. Empirically we manage to train DNNs with 64 hidden layers and 1024 nodes per layer for supervised hashing in about 3 hours using a single GPU. Our proposed very deep supervised hashing (VDSH) method significantly outperforms the state-of-the-art on several benchmark datasets.