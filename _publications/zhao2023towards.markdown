---
layout: publication
title: Towards Diverse Binary Segmentation Via A Simple Yet General Gated Network
authors: Xiaoqi Zhao, Youwei Pang, Lihe Zhang, Huchuan Lu, Lei Zhang
conference: International Journal of Computer Vision
year: 2024
bibkey: zhao2023towards
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.10396'}]
tags: []
short_authors: Zhao et al.
---
In many binary segmentation tasks, most CNNs-based methods use a U-shape
encoder-decoder network as their basic structure. They ignore two key problems
when the encoder exchanges information with the decoder: one is the lack of
interference control mechanism between them, the other is without considering
the disparity of the contributions from different encoder levels. In this work,
we propose a simple yet general gated network (GateNet) to tackle them all at
once. With the help of multi-level gate units, the valuable context information
from the encoder can be selectively transmitted to the decoder. In addition, we
design a gated dual branch structure to build the cooperation among the
features of different levels and improve the discrimination ability of the
network. Furthermore, we introduce a "Fold" operation to improve the atrous
convolution and form a novel folded atrous convolution, which can be flexibly
embedded in ASPP or DenseASPP to accurately localize foreground objects of
various scales. GateNet can be easily generalized to many binary segmentation
tasks, including general and specific object segmentation and multi-modal
segmentation. Without bells and whistles, our network consistently performs
favorably against the state-of-the-art methods under 10 metrics on 33 datasets
of 10 binary segmentation tasks.