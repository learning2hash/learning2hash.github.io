---
layout: publication
title: 'NCL-CIR: Noise-aware Contrastive Learning For Composed Image Retrieval'
authors: Peng Gao, Yujian Lee, Zailong Chen, Hui Zhang, Xubo Liu, Yiyang Hu, Guquang
  Jing
conference: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2025
bibkey: gao2025ncl
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.04339'}]
tags: [Evaluation, ICASSP, Image Retrieval, Self-Supervised, Datasets]
short_authors: Gao et al.
---
Composed Image Retrieval (CIR) seeks to find a target image using a
multi-modal query, which combines an image with modification text to pinpoint
the target. While recent CIR methods have shown promise, they mainly focus on
exploring relationships between the query pairs (image and text) through data
augmentation or model design. These methods often assume perfect alignment
between queries and target images, an idealized scenario rarely encountered in
practice. In reality, pairs are often partially or completely mismatched due to
issues like inaccurate modification texts, low-quality target images, and
annotation errors. Ignoring these mismatches leads to numerous False Positive
Pair (FFPs) denoted as noise pairs in the dataset, causing the model to overfit
and ultimately reducing its performance. To address this problem, we propose
the Noise-aware Contrastive Learning for CIR (NCL-CIR), comprising two key
components: the Weight Compensation Block (WCB) and the Noise-pair Filter Block
(NFB). The WCB coupled with diverse weight maps can ensure more stable token
representations of multi-modal queries and target images. Meanwhile, the NFB,
in conjunction with the Gaussian Mixture Model (GMM) predicts noise pairs by
evaluating loss distributions, and generates soft labels correspondingly,
allowing for the design of the soft-label based Noise Contrastive Estimation
(NCE) loss function. Consequently, the overall architecture helps to mitigate
the influence of mismatched and partially matched samples, with experimental
results demonstrating that NCL-CIR achieves exceptional performance on the
benchmark datasets.