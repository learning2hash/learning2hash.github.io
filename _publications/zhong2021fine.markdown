---
layout: publication
title: Fine-grained Data Distribution Alignment For Post-training Quantization
authors: Yunshan Zhong, Mingbao Lin, Mengzhao Chen, Ke Li, Yunhang Shen, Fei Chao,
  Yongjian Wu, Rongrong Ji
conference: Lecture Notes in Computer Science
year: 2022
bibkey: zhong2021fine
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04186'}]
tags: ["Quantization"]
short_authors: Zhong et al.
---
While post-training quantization receives popularity mostly due to its
evasion in accessing the original complete training dataset, its poor
performance also stems from scarce images. To alleviate this limitation, in
this paper, we leverage the synthetic data introduced by zero-shot quantization
with calibration dataset and propose a fine-grained data distribution alignment
(FDDA) method to boost the performance of post-training quantization. The
method is based on two important properties of batch normalization statistics
(BNS) we observed in deep layers of the trained network, (i.e.), inter-class
separation and intra-class incohesion. To preserve this fine-grained
distribution information: 1) We calculate the per-class BNS of the calibration
dataset as the BNS centers of each class and propose a BNS-centralized loss to
force the synthetic data distributions of different classes to be close to
their own centers. 2) We add Gaussian noise into the centers to imitate the
incohesion and propose a BNS-distorted loss to force the synthetic data
distribution of the same class to be close to the distorted centers. By
utilizing these two fine-grained losses, our method manifests the
state-of-the-art performance on ImageNet, especially when both the first and
last layers are quantized to the low-bit. Code is at
https://github.com/zysxmu/FDDA.