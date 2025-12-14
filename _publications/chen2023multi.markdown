---
layout: publication
title: Multi-content Interaction Network For Few-shot Segmentation
authors: Hao Chen, Yunlong Yu, Yonghan Dong, Zheming Lu, Yingming Li, Zhongfei Zhang
conference: Arxiv
year: 2023
bibkey: chen2023multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.06304'}]
tags: [Evaluation, Few-shot & Zero-shot, Datasets]
short_authors: Chen et al.
---
Few-Shot Segmentation (FSS) is challenging for limited support images and
large intra-class appearance discrepancies. Most existing approaches focus on
extracting high-level representations of the same layers for support-query
correlations, neglecting the shift issue between different layers and scales,
due to the huge difference between support and query samples. In this paper, we
propose a Multi-Content Interaction Network (MCINet) to remedy this issue by
fully exploiting and interacting with the multi-scale contextual information
contained in the support-query pairs to supplement the same-layer correlations.
Specifically, MCINet improves FSS from the perspectives of boosting the query
representations by incorporating the low-level structural information from
another query branch into the high-level semantic features, enhancing the
support-query correlations by exploiting both the same-layer and adjacent-layer
features, and refining the predicted results by a multi-scale mask prediction
strategy, with which the different scale contents have bidirectionally
interacted. Experiments on two benchmarks demonstrate that our approach reaches
SOTA performances and outperforms the best competitors with many desirable
advantages, especially on the challenging COCO dataset.