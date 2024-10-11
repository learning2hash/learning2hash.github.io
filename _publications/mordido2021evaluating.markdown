---
layout: publication
title: Evaluating Post-training Compression In Gans Using Locality-sensitive Hashing
authors: Mordido Gonçalo, Yang Haojin, Meinel Christoph
conference: "Arxiv"
year: 2021
bibkey: mordido2021evaluating
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2103.11912"}
tags: ['ARXIV', 'Independent', 'LSH', 'Quantisation']
---
The analysis of the compression effects in generative adversarial networks (GANs) after training, i.e. without any fine-tuning, remains an unstudied, albeit important, topic with the increasing trend of their computation and memory requirements. While existing works discuss the difficulty of compressing GANs during training, requiring novel methods designed with the instability of GANs training in mind, we show that existing compression methods (namely clipping and quantization) may be directly applied to compress GANs post-training, without any additional changes. High compression levels may distort the generated set, likely leading to an increase of outliers that may negatively affect the overall assessment of existing k-nearest neighbor (KNN) based metrics. We propose two new precision and recall metrics based on locality-sensitive hashing (LSH), which, on top of increasing the outlier robustness, decrease the complexity of assessing an evaluation sample against $n$ reference samples from $O(n)$ to $O(\log(n))$, if using LSH and KNN, and to $O(1)$, if only applying LSH. We show that low-bit compression of several pre-trained GANs on multiple datasets induces a trade-off between precision and recall, retaining sample quality while sacrificing sample diversity.
