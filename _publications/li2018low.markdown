---
layout: publication
title: Low-rank Embedding Of Kernels In Convolutional Neural Networks Under Random
  Shuffling
authors: Chao Li, Zhun Sun, Jinshi Yu, Ming Hou, Qibin Zhao
conference: ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2019
bibkey: li2018low
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.13098'}]
tags: ["ICASSP"]
short_authors: Li et al.
---
Although the convolutional neural networks (CNNs) have become popular for
various image processing and computer vision task recently, it remains a
challenging problem to reduce the storage cost of the parameters for
resource-limited platforms. In the previous studies, tensor decomposition (TD)
has achieved promising compression performance by embedding the kernel of a
convolutional layer into a low-rank subspace. However the employment of TD is
naively on the kernel or its specified variants. Unlike the conventional
approaches, this paper shows that the kernel can be embedded into more general
or even random low-rank subspaces. We demonstrate this by compressing the
convolutional layers via randomly-shuffled tensor decomposition (RsTD) for a
standard classification task using CIFAR-10. In addition, we analyze how the
spatial similarity of the training data influences the low-rank structure of
the kernels. The experimental results show that the CNN can be significantly
compressed even if the kernels are randomly shuffled. Furthermore, the
RsTD-based method yields more stable classification accuracy than the
conventional TD-based methods in a large range of compression ratios.