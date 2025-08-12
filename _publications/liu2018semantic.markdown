---
layout: publication
title: Semantic Edge Detection With Diverse Deep Supervision
authors: Yun Liu, Ming-ming Cheng, Deng-ping Fan, Le Zhang, Jiawang Bian, Dacheng
  Tao
conference: International Journal of Computer Vision
year: 2021
bibkey: liu2018semantic
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.02864'}]
tags: []
short_authors: Liu et al.
---
Semantic edge detection (SED), which aims at jointly extracting edges as well
as their category information, has far-reaching applications in domains such as
semantic segmentation, object proposal generation, and object recognition. SED
naturally requires achieving two distinct supervision targets: locating fine
detailed edges and identifying high-level semantics. Our motivation comes from
the hypothesis that such distinct targets prevent state-of-the-art SED methods
from effectively using deep supervision to improve results. To this end, we
propose a novel fully convolutional neural network using diverse deep
supervision (DDS) within a multi-task framework where bottom layers aim at
generating category-agnostic edges, while top layers are responsible for the
detection of category-aware semantic edges. To overcome the hypothesized
supervision challenge, a novel information converter unit is introduced, whose
effectiveness has been extensively evaluated on SBD and Cityscapes datasets.