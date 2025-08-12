---
layout: publication
title: Double Similarity Distillation For Semantic Image Segmentation
authors: Yingchao Feng, Xian Sun, Wenhui Diao, Jihao Li, Xin Gao
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: feng2021double
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.08591'}]
tags: []
short_authors: Feng et al.
---
The balance between high accuracy and high speed has always been a
challenging task in semantic image segmentation. Compact segmentation networks
are more widely used in the case of limited resources, while their performances
are constrained. In this paper, motivated by the residual learning and global
aggregation, we propose a simple yet general and effective knowledge
distillation framework called double similarity distillation (DSD) to improve
the classification accuracy of all existing compact networks by capturing the
similarity knowledge in pixel and category dimensions, respectively.
Specifically, we propose a pixel-wise similarity distillation (PSD) module that
utilizes residual attention maps to capture more detailed spatial dependencies
across multiple layers. Compared with exiting methods, the PSD module greatly
reduces the amount of calculation and is easy to expand. Furthermore,
considering the differences in characteristics between semantic segmentation
task and other computer vision tasks, we propose a category-wise similarity
distillation (CSD) module, which can help the compact segmentation network
strengthen the global category correlation by constructing the correlation
matrix. Combining these two modules, DSD framework has no extra parameters and
only a minimal increase in FLOPs. Extensive experiments on four challenging
datasets, including Cityscapes, CamVid, ADE20K, and Pascal VOC 2012, show that
DSD outperforms current state-of-the-art methods, proving its effectiveness and
generality. The code and models will be publicly available.