---
layout: publication
title: A Lightweight Clustering Framework For Unsupervised Semantic Segmentation
authors: Yau Shing Jonathan Cheung, Xi Chen, Lihe Yang, Hengshuang Zhao
conference: Arxiv
year: 2023
bibkey: cheung2023lightweight
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.18628'}]
tags: ["Unsupervised"]
short_authors: Cheung et al.
---
Unsupervised semantic segmentation aims to categorize each pixel in an image
into a corresponding class without the use of annotated data. It is a widely
researched area as obtaining labeled datasets is expensive. While previous
works in the field have demonstrated a gradual improvement in model accuracy,
most required neural network training. This made segmentation equally
expensive, especially when dealing with large-scale datasets. We thus propose a
lightweight clustering framework for unsupervised semantic segmentation. We
discovered that attention features of the self-supervised Vision Transformer
exhibit strong foreground-background differentiability. Therefore, clustering
can be employed to effectively separate foreground and background image
patches. In our framework, we first perform multilevel clustering across the
Dataset-level, Category-level, and Image-level, and maintain consistency
throughout. Then, the binary patch-level pseudo-masks extracted are upsampled,
refined and finally labeled. Furthermore, we provide a comprehensive analysis
of the self-supervised Vision Transformer features and a detailed comparison
between DINO and DINOv2 to justify our claims. Our framework demonstrates great
promise in unsupervised semantic segmentation and achieves state-of-the-art
results on PASCAL VOC and MS COCO datasets.