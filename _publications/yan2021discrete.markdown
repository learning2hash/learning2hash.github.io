---
layout: publication
title: Discrete-continuous Action Space Policy Gradient-based Attention For Image-text
  Matching
authors: Shiyang Yan, Li Yu, Yuan Xie
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: yan2021discrete
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.10406'}]
tags: ["CVPR", "Datasets", "Supervised"]
short_authors: Shiyang Yan, Li Yu, Yuan Xie
---
Image-text matching is an important multi-modal task with massive
applications. It tries to match the image and the text with similar semantic
information. Existing approaches do not explicitly transform the different
modalities into a common space. Meanwhile, the attention mechanism which is
widely used in image-text matching models does not have supervision. We propose
a novel attention scheme which projects the image and text embedding into a
common space and optimises the attention weights directly towards the
evaluation metrics. The proposed attention scheme can be considered as a kind
of supervised attention and requiring no additional annotations. It is trained
via a novel Discrete-continuous action space policy gradient algorithm, which
is more effective in modelling complex action space than previous continuous
action space policy gradient. We evaluate the proposed methods on two
widely-used benchmark datasets: Flickr30k and MS-COCO, outperforming the
previous approaches by a large margin.