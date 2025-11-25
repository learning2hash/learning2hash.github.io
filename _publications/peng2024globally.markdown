---
layout: publication
title: Globally Correlation-aware Hard Negative Generation
authors: Wenjie Peng, Hongxiang Huang, Tianshui Chen, Quhui Ke, Gang Dai, Shuangping
  Huang
conference: International Journal of Computer Vision
year: 2024
bibkey: peng2024globally
citations: 2
additional_links: [{name: Code, url: 'https://github.com/PWenJay/GCA-HNG'}, {name: Paper,
    url: 'https://arxiv.org/abs/2411.13145'}]
tags: ["Distance Metric Learning", "Image Retrieval"]
short_authors: Peng et al.
---
Hard negative generation aims to generate informative negative samples that
help to determine the decision boundaries and thus facilitate advancing deep
metric learning. Current works select pair/triplet samples, learn their
correlations, and fuse them to generate hard negatives. However, these works
merely consider the local correlations of selected samples, ignoring global
sample correlations that would provide more significant information to generate
more informative negatives. In this work, we propose a Globally
Correlation-Aware Hard Negative Generation (GCA-HNG) framework, which first
learns sample correlations from a global perspective and exploits these
correlations to guide generating hardness-adaptive and diverse negatives.
Specifically, this approach begins by constructing a structured graph to model
sample correlations, where each node represents a specific sample and each edge
represents the correlations between corresponding samples. Then, we introduce
an iterative graph message propagation to propagate the messages of node and
edge through the whole graph and thus learn the sample correlations globally.
Finally, with the guidance of the learned global correlations, we propose a
channel-adaptive manner to combine an anchor and multiple negatives for HNG.
Compared to current methods, GCA-HNG allows perceiving sample correlations with
numerous negatives from a global and comprehensive perspective and generates
the negatives with better hardness and diversity. Extensive experiment results
demonstrate that the proposed GCA-HNG is superior to related methods on four
image retrieval benchmark datasets. Codes and trained models are available at
https://github.com/PWenJay/GCA-HNG.