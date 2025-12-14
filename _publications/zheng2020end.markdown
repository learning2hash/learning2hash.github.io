---
layout: publication
title: End-to-end Object Detection With Adaptive Clustering Transformer
authors: Minghang Zheng, Peng Gao, Renrui Zhang, Kunchang Li, Xiaogang Wang, Hongsheng
  Li, Hao Dong
conference: British Machine Vision Conference 2021
year: 2020
bibkey: zheng2020end
citations: 13
additional_links: [{name: Code, url: 'https://github.com/gaopengcuhk/SMCA-DETR/'},
  {name: Paper, url: 'https://arxiv.org/abs/2011.09315'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Evaluation, Transformer-based
    ANN]
short_authors: Zheng et al.
---
End-to-end Object Detection with Transformer (DETR)proposes to perform object
detection with Transformer and achieve comparable performance with two-stage
object detection like Faster-RCNN. However, DETR needs huge computational
resources for training and inference due to the high-resolution spatial input.
In this paper, a novel variant of transformer named Adaptive Clustering
Transformer(ACT) has been proposed to reduce the computation cost for
high-resolution input. ACT cluster the query features adaptively using Locality
Sensitive Hashing (LSH) and ap-proximate the query-key interaction using the
prototype-key interaction. ACT can reduce the quadratic O(N2) complexity inside
self-attention into O(NK) where K is the number of prototypes in each layer.
ACT can be a drop-in module replacing the original self-attention module
without any training. ACT achieves a good balance between accuracy and
computation cost (FLOPs). The code is available as supplementary for the ease
of experiment replication and verification. Code is released at
https://github.com/gaopengcuhk/SMCA-DETR/