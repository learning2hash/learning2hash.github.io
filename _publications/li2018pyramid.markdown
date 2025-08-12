---
layout: publication
title: Pyramid Attention Network For Semantic Segmentation
authors: Hanchao Li, Pengfei Xiong, Jie An, Lingxue Wang
conference: Arxiv
year: 2018
bibkey: li2018pyramid
citations: 565
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.10180'}]
tags: []
short_authors: Li et al.
---
A Pyramid Attention Network(PAN) is proposed to exploit the impact of global
contextual information in semantic segmentation. Different from most existing
works, we combine attention mechanism and spatial pyramid to extract precise
dense features for pixel labeling instead of complicated dilated convolution
and artificially designed decoder networks. Specifically, we introduce a
Feature Pyramid Attention module to perform spatial pyramid attention structure
on high-level output and combining global pooling to learn a better feature
representation, and a Global Attention Upsample module on each decoder layer to
provide global context as a guidance of low-level features to select category
localization details. The proposed approach achieves state-of-the-art
performance on PASCAL VOC 2012 and Cityscapes benchmarks with a new record of
mIoU accuracy 84.0% on PASCAL VOC 2012, while training without COCO dataset.