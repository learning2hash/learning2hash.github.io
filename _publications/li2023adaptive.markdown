---
layout: publication
title: An Adaptive Plug-and-play Network For Few-shot Learning
authors: Hao Li, Li Li, Yunmeng Huang, Ning Li, Yongtao Zhang
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: li2023adaptive
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.09326'}]
tags: ["Few Shot & Zero Shot", "ICASSP"]
short_authors: Li et al.
---
Few-shot learning (FSL) requires a model to classify new samples after
learning from only a few samples. While remarkable results are achieved in
existing methods, the performance of embedding and metrics determines the upper
limit of classification accuracy in FSL. The bottleneck is that deep networks
and complex metrics tend to induce overfitting in FSL, making it difficult to
further improve the performance. Towards this, we propose plug-and-play
model-adaptive resizer (MAR) and adaptive similarity metric (ASM) without any
other losses. MAR retains high-resolution details to alleviate the overfitting
problem caused by data scarcity, and ASM decouples the relationship between
different metrics and then fuses them into an advanced one. Extensive
experiments show that the proposed method could boost existing methods on two
standard dataset and a fine-grained datasets, and achieve state-of-the-art
results on mini-ImageNet and tiered-ImageNet.