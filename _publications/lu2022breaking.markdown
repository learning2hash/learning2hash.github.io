---
layout: publication
title: 'Breaking Immutable: Information-coupled Prototype Elaboration For Few-shot
  Object Detection'
authors: Xiaonan Lu, Wenhui Diao, Yongqiang Mao, Junxi Li, Peijin Wang, Xian Sun,
  Kun Fu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: lu2022breaking
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.14782'}]
tags: ["AAAI"]
short_authors: Lu et al.
---
Few-shot object detection, expecting detectors to detect novel classes with a
few instances, has made conspicuous progress. However, the prototypes extracted
by existing meta-learning based methods still suffer from insufficient
representative information and lack awareness of query images, which cannot be
adaptively tailored to different query images. Firstly, only the support images
are involved for extracting prototypes, resulting in scarce perceptual
information of query images. Secondly, all pixels of all support images are
treated equally when aggregating features into prototype vectors, thus the
salient objects are overwhelmed by the cluttered background. In this paper, we
propose an Information-Coupled Prototype Elaboration (ICPE) method to generate
specific and representative prototypes for each query image. Concretely, a
conditional information coupling module is introduced to couple information
from the query branch to the support branch, strengthening the query-perceptual
information in support features. Besides, we design a prototype dynamic
aggregation module that dynamically adjusts intra-image and inter-image
aggregation weights to highlight the salient information useful for detecting
query images. Experimental results on both Pascal VOC and MS COCO demonstrate
that our method achieves state-of-the-art performance in almost all settings.