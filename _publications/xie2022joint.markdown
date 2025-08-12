---
layout: publication
title: 'Joint Distribution Matters: Deep Brownian Distance Covariance For Few-shot
  Classification'
authors: Jiangtao Xie, Fei Long, Jiaming Lv, Qilong Wang, Peihua Li
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: xie2022joint
citations: 173
additional_links: [{name: Code, url: 'http://www.peihuali.org/DeepBDC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2204.04567'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Xie et al.
---
Few-shot classification is a challenging problem as only very few training
examples are given for each new task. One of the effective research lines to
address this challenge focuses on learning deep representations driven by a
similarity measure between a query image and few support images of some class.
Statistically, this amounts to measure the dependency of image features, viewed
as random vectors in a high-dimensional embedding space. Previous methods
either only use marginal distributions without considering joint distributions,
suffering from limited representation capability, or are computationally
expensive though harnessing joint distributions. In this paper, we propose a
deep Brownian Distance Covariance (DeepBDC) method for few-shot classification.
The central idea of DeepBDC is to learn image representations by measuring the
discrepancy between joint characteristic functions of embedded features and
product of the marginals. As the BDC metric is decoupled, we formulate it as a
highly modular and efficient layer. Furthermore, we instantiate DeepBDC in two
different few-shot classification frameworks. We make experiments on six
standard few-shot image benchmarks, covering general object recognition,
fine-grained categorization and cross-domain classification. Extensive
evaluations show our DeepBDC significantly outperforms the counterparts, while
establishing new state-of-the-art results. The source code is available at
http://www.peihuali.org/DeepBDC