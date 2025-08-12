---
layout: publication
title: Kernel Normalized Convolutional Networks
authors: Reza Nasirigerdeh, Reihaneh Torkzadehmahani, Daniel Rueckert, Georgios Kaissis
conference: Transactions on Machine Learning Research (TMLR) 2024
year: 2022
bibkey: nasirigerdeh2022kernel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.10089'}]
tags: []
short_authors: Nasirigerdeh et al.
---
Existing convolutional neural network architectures frequently rely upon
batch normalization (BatchNorm) to effectively train the model. BatchNorm,
however, performs poorly with small batch sizes, and is inapplicable to
differential privacy. To address these limitations, we propose the kernel
normalization (KernelNorm) and kernel normalized convolutional layers, and
incorporate them into kernel normalized convolutional networks (KNConvNets) as
the main building blocks. We implement KNConvNets corresponding to the
state-of-the-art ResNets while forgoing the BatchNorm layers. Through extensive
experiments, we illustrate that KNConvNets achieve higher or competitive
performance compared to the BatchNorm counterparts in image classification and
semantic segmentation. They also significantly outperform their
batch-independent competitors including those based on layer and group
normalization in non-private and differentially private training. Given that,
KernelNorm combines the batch-independence property of layer and group
normalization with the performance advantage of BatchNorm.