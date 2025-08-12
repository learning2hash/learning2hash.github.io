---
layout: publication
title: Efficient Dataset Distillation Through Low-rank Space Sampling
authors: Hangyang Kong, Wenbo Zhou, Xuxiang He, Xiaotong Tu, Xinghao Ding
conference: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2025
bibkey: kong2025efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.07998'}]
tags: ["Datasets", "ICASSP"]
short_authors: Kong et al.
---
Huge amount of data is the key of the success of deep learning, however,
redundant information impairs the generalization ability of the model and
increases the burden of calculation. Dataset Distillation (DD) compresses the
original dataset into a smaller but representative subset for high-quality data
and efficient training strategies. Existing works for DD generate synthetic
images by treating each image as an independent entity, thereby overlooking the
common features among data. This paper proposes a dataset distillation method
based on Matching Training Trajectories with Low-rank Space Sampling(MTT-LSS),
which uses low-rank approximations to capture multiple low-dimensional manifold
subspaces of the original data. The synthetic data is represented by basis
vectors and shared dimension mappers from these subspaces, reducing the cost of
generating individual data points while effectively minimizing information
redundancy. The proposed method is tested on CIFAR-10, CIFAR-100, and SVHN
datasets, and outperforms the baseline methods by an average of 9.9%.