---
layout: publication
title: A Debiased Nearest Neighbors Framework For Multi-label Text Classification
authors: Zifeng Cheng, Zhiwei Jiang, Yafeng Yin, Zhaoling Chen, Cong Wang, Shiping
  Ge, Qiguo Huang, Qing Gu
conference: Arxiv
year: 2024
bibkey: cheng2024a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.03202'}]
tags: ["Datasets", "Evaluation", "Self-Supervised"]
short_authors: Cheng et al.
---
Multi-Label Text Classification (MLTC) is a practical yet challenging task
that involves assigning multiple non-exclusive labels to each document.
Previous studies primarily focus on capturing label correlations to assist
label prediction by introducing special labeling schemes, designing specific
model structures, or adding auxiliary tasks. Recently, the \(k\) Nearest Neighbor
(\(k\)NN) framework has shown promise by retrieving labeled samples as references
to mine label co-occurrence information in the embedding space. However, two
critical biases, namely embedding alignment bias and confidence estimation
bias, are often overlooked, adversely affecting prediction performance. In this
paper, we introduce a DEbiased Nearest Neighbors (DENN) framework for MLTC,
specifically designed to mitigate these biases. To address embedding alignment
bias, we propose a debiased contrastive learning strategy, enhancing neighbor
consistency on label co-occurrence. For confidence estimation bias, we present
a debiased confidence estimation strategy, improving the adaptive combination
of predictions from \(k\)NN and inductive binary classifications. Extensive
experiments conducted on four public benchmark datasets (i.e., AAPD, RCV1-V2,
Amazon-531, and EUR-LEX57K) showcase the effectiveness of our proposed method.
Besides, our method does not introduce any extra parameters.