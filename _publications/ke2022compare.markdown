---
layout: publication
title: 'Compare Learning: Bi-attention Network For Few-shot Learning'
authors: Ke et al.
conference: ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: ke2022compare
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13487'}]
tags: [ICASSP, Evaluation, Distance Metric Learning]
---
Learning with few labeled data is a key challenge for visual recognition, as
deep neural networks tend to overfit using a few samples only. One of the
Few-shot learning methods called metric learning addresses this challenge by
first learning a deep distance metric to determine whether a pair of images
belong to the same category, then applying the trained metric to instances from
other test set with limited labels. This method makes the most of the few
samples and limits the overfitting effectively. However, extant metric networks
usually employ Linear classifiers or Convolutional neural networks (CNN) that
are not precise enough to globally capture the subtle differences between
vectors. In this paper, we propose a novel approach named Bi-attention network
to compare the instances, which can measure the similarity between embeddings
of instances precisely, globally and efficiently. We verify the effectiveness
of our model on two benchmarks. Experiments show that our approach achieved
improved accuracy and convergence speed over baseline models.