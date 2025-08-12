---
layout: publication
title: Multi-scale Matching Networks For Semantic Correspondence
authors: Dongyang Zhao, Ziyang Song, Zhenghao Ji, Gangming Zhao, Weifeng Ge, Yizhou
  Yu
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: zhao2021multi
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.00211'}]
tags: ["ICCV"]
short_authors: Zhao et al.
---
Deep features have been proven powerful in building accurate dense semantic
correspondences in various previous works. However, the multi-scale and
pyramidal hierarchy of convolutional neural networks has not been well studied
to learn discriminative pixel-level features for semantic correspondence. In
this paper, we propose a multi-scale matching network that is sensitive to tiny
semantic differences between neighboring pixels. We follow the coarse-to-fine
matching strategy and build a top-down feature and matching enhancement scheme
that is coupled with the multi-scale hierarchy of deep convolutional neural
networks. During feature enhancement, intra-scale enhancement fuses
same-resolution feature maps from multiple layers together via local
self-attention and cross-scale enhancement hallucinates higher-resolution
feature maps along the top-down hierarchy. Besides, we learn complementary
matching details at different scales thus the overall matching score is refined
by features of different semantic levels gradually. Our multi-scale matching
network can be trained end-to-end easily with few additional learnable
parameters. Experimental results demonstrate that the proposed method achieves
state-of-the-art performance on three popular benchmarks with high
computational efficiency.