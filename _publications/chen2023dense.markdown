---
layout: publication
title: Dense Affinity Matching For Few-shot Segmentation
authors: Hao Chen, Yonghan Dong, Zheming Lu, Yunlong Yu, Yingming Li, Jungong Han,
  Zhongfei Zhang
conference: Neurocomputing
year: 2024
bibkey: chen2023dense
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.08434'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Few-Shot Segmentation (FSS) aims to segment the novel class images with a few
annotated samples. In this paper, we propose a dense affinity matching (DAM)
framework to exploit the support-query interaction by densely capturing both
the pixel-to-pixel and pixel-to-patch relations in each support-query pair with
the bidirectional 3D convolutions. Different from the existing methods that
remove the support background, we design a hysteretic spatial filtering module
(HSFM) to filter the background-related query features and retain the
foreground-related query features with the assistance of the support
background, which is beneficial for eliminating interference objects in the
query background. We comprehensively evaluate our DAM on ten benchmarks under
cross-category, cross-dataset, and cross-domain FSS tasks. Experimental results
demonstrate that DAM performs very competitively under different settings with
only 0.68M parameters, especially under cross-domain FSS tasks, showing its
effectiveness and efficiency.