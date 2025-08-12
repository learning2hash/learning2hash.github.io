---
layout: publication
title: Heterogeneous Semantic Transfer For Multi-label Recognition With Partial Labels
authors: Tianshui Chen, Tao Pu, Lingbo Liu, Yukai Shi, Zhijing Yang, Liang Lin
conference: International Journal of Computer Vision
year: 2024
bibkey: chen2022heterogeneous
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.11131'}]
tags: []
short_authors: Chen et al.
---
Multi-label image recognition with partial labels (MLR-PL), in which some
labels are known while others are unknown for each image, may greatly reduce
the cost of annotation and thus facilitate large-scale MLR. We find that strong
semantic correlations exist within each image and across different images, and
these correlations can help transfer the knowledge possessed by the known
labels to retrieve the unknown labels and thus improve the performance of the
MLR-PL task (see Figure 1). In this work, we propose a novel heterogeneous
semantic transfer (HST) framework that consists of two complementary transfer
modules that explore both within-image and cross-image semantic correlations to
transfer the knowledge possessed by known labels to generate pseudo labels for
the unknown labels. Specifically, an intra-image semantic transfer (IST) module
learns an image-specific label co-occurrence matrix for each image and maps the
known labels to complement the unknown labels based on these matrices.
Additionally, a cross-image transfer (CST) module learns category-specific
feature-prototype similarities and then helps complement the unknown labels
that have high degrees of similarity with the corresponding prototypes.
Finally, both the known and generated pseudo labels are used to train MLR
models. Extensive experiments conducted on the Microsoft COCO, Visual Genome,
and Pascal VOC 2007 datasets show that the proposed HST framework achieves
superior performance to that of current state-of-the-art algorithms.
Specifically, it obtains mean average precision (mAP) improvements of 1.4%,
3.3%, and 0.4% on the three datasets over the results of the best-performing
previously developed algorithm.