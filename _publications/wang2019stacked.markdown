---
layout: publication
title: Stacked Semantic-guided Network For Zero-shot Sketch-based Image Retrieval
authors: Hao Wang, Cheng Deng, Xinxu Xu, Wei Liu, Xinbo Gao, Dacheng Tao
conference: Arxiv
year: 2019
bibkey: wang2019stacked
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.01971'}]
tags: [Scalability, Datasets, Image Retrieval, Few-shot & Zero-shot, Evaluation]
short_authors: Wang et al.
---
Zero-shot sketch-based image retrieval (ZS-SBIR) is a task of cross-domain
image retrieval from a natural image gallery with free-hand sketch under a
zero-shot scenario. Previous works mostly focus on a generative approach that
takes a highly abstract and sparse sketch as input and then synthesizes the
corresponding natural image. However, the intrinsic visual sparsity and large
intra-class variance of the sketch make the learning of the conditional decoder
more difficult and hence achieve unsatisfactory retrieval performance. In this
paper, we propose a novel stacked semantic-guided network to address the unique
characteristics of sketches in ZS-SBIR. Specifically, we devise multi-layer
feature fusion networks that incorporate different intermediate feature
representation information in a deep neural network to alleviate the intrinsic
sparsity of sketches. In order to improve visual knowledge transfer from seen
to unseen classes, we elaborate a coarse-to-fine conditional decoder that
generates coarse-grained category-specific corresponding features first (taking
auxiliary semantic information as conditional input) and then generates
fine-grained instance-specific corresponding features (taking sketch
representation as conditional input). Furthermore, regression loss and
classification loss are utilized to preserve the semantic and discriminative
information of the synthesized features respectively. Extensive experiments on
the large-scale Sketchy dataset and TU-Berlin dataset demonstrate that our
proposed approach outperforms state-of-the-art methods by more than 20% in
retrieval performance.