---
layout: publication
title: 'Devil''s In The Details: Aligning Visual Clues For Conditional Embedding In
  Person Re-identification'
authors: Fufu Yu, Xinyang Jiang, Yifei Gong, Shizhen Zhao, Xiaowei Guo, Wei-Shi Zheng,
  Feng Zheng, Xing Sun
conference: Arxiv
year: 2020
bibkey: yu2020devil
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.05250'}]
tags: []
short_authors: Yu et al.
---
Although Person Re-Identification has made impressive progress, difficult
cases like occlusion, change of view-pointand similar clothing still bring
great challenges. Besides overall visual features, matching and comparing
detailed information is also essential for tackling these challenges. This
paper proposes two key recognition patterns to better utilize the detail
information of pedestrian images, that most of the existing methods are unable
to satisfy. Firstly, Visual Clue Alignment requires the model to select and
align decisive regions pairs from two images for pair-wise comparison, while
existing methods only align regions with predefined rules like high feature
similarity or same semantic labels. Secondly, the Conditional Feature Embedding
requires the overall feature of a query image to be dynamically adjusted based
on the gallery image it matches, while most of the existing methods ignore the
reference images. By introducing novel techniques including correspondence
attention module and discrepancy-based GCN, we propose an end-to-end ReID
method that integrates both patterns into a unified framework, called
CACE-Net((C)lue(A)lignment and (C)onditional (E)mbedding). The experiments show
that CACE-Net achieves state-of-the-art performance on three public datasets.