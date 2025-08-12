---
layout: publication
title: 'IDEA: Increasing Text Diversity Via Online Multi-label Recognition For Vision-language
  Pre-training'
authors: Xinyu Huang, Youcai Zhang, Ying Cheng, Weiwei Tian, Ruiwei Zhao, Rui Feng,
  Yuejie Zhang, Yaqian Li, Yandong Guo, Xiaobo Zhang
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: huang2022idea
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05333'}]
tags: []
short_authors: Huang et al.
---
Vision-Language Pre-training (VLP) with large-scale image-text pairs has
demonstrated superior performance in various fields. However, the image-text
pairs co-occurrent on the Internet typically lack explicit alignment
information, which is suboptimal for VLP. Existing methods proposed to adopt an
off-the-shelf object detector to utilize additional image tag information.
However, the object detector is time-consuming and can only identify the
pre-defined object categories, limiting the model capacity. Inspired by the
observation that the texts incorporate incomplete fine-grained image
information, we introduce IDEA, which stands for increasing text diversity via
online multi-label recognition for VLP. IDEA shows that multi-label learning
with image tags extracted from the texts can be jointly optimized during VLP.
Moreover, IDEA can identify valuable image tags online to provide more explicit
textual supervision. Comprehensive experiments demonstrate that IDEA can
significantly boost the performance on multiple downstream datasets with a
small extra computational cost.