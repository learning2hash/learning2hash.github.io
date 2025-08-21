---
layout: publication
title: Adaptive Local-component-aware Graph Convolutional Network For One-shot Skeleton-based
  Action Recognition
authors: Anqi Zhu, Qiuhong Ke, Mingming Gong, James Bailey
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: zhu2022adaptive
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.10073'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Zhu et al.
---
Skeleton-based action recognition receives increasing attention because the
skeleton representations reduce the amount of training data by eliminating
visual information irrelevant to actions. To further improve the sample
efficiency, meta-learning-based one-shot learning solutions were developed for
skeleton-based action recognition. These methods find the nearest neighbor
according to the similarity between instance-level global average embedding.
However, such measurement holds unstable representativity due to inadequate
generalized learning on local invariant and noisy features, while intuitively,
more fine-grained recognition usually relies on determining key local body
movements. To address this limitation, we present the Adaptive
Local-Component-aware Graph Convolutional Network, which replaces the
comparison metric with a focused sum of similarity measurements on aligned
local embedding of action-critical spatial/temporal segments. Comprehensive
one-shot experiments on the public benchmark of NTU-RGB+D 120 indicate that our
method provides a stronger representation than the global embedding and helps
our model reach state-of-the-art.