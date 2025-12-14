---
layout: publication
title: Mutual Information Guided Optimal Transport For Unsupervised Visible-infrared
  Person Re-identification
authors: Zhizhong Zhang, Jiangming Wang, Xin Tan, Yanyun Qu, Junping Wang, Yong Xie,
  Yuan Xie
conference: Arxiv
year: 2024
bibkey: zhang2024mutual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.12758'}]
tags: [Self-Supervised, Supervised, Unsupervised, Evaluation]
short_authors: Zhang et al.
---
Unsupervised visible infrared person re-identification (USVI-ReID) is a
challenging retrieval task that aims to retrieve cross-modality pedestrian
images without using any label information. In this task, the large
cross-modality variance makes it difficult to generate reliable cross-modality
labels, and the lack of annotations also provides additional difficulties for
learning modality-invariant features. In this paper, we first deduce an
optimization objective for unsupervised VI-ReID based on the mutual information
between the model's cross-modality input and output. With equivalent
derivation, three learning principles, i.e., "Sharpness" (entropy
minimization), "Fairness" (uniform label distribution), and "Fitness" (reliable
cross-modality matching) are obtained. Under their guidance, we design a loop
iterative training strategy alternating between model training and
cross-modality matching. In the matching stage, a uniform prior guided optimal
transport assignment ("Fitness", "Fairness") is proposed to select matched
visible and infrared prototypes. In the training stage, we utilize this
matching information to introduce prototype-based contrastive learning for
minimizing the intra- and cross-modality entropy ("Sharpness"). Extensive
experimental results on benchmarks demonstrate the effectiveness of our method,
e.g., 60.6% and 90.3% of Rank-1 accuracy on SYSU-MM01 and RegDB without any
annotations.