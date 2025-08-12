---
layout: publication
title: Exploring Cross-image Pixel Contrast For Semantic Segmentation
authors: Wenguan Wang, Tianfei Zhou, Fisher Yu, Jifeng Dai, Ender Konukoglu, Luc van
  Gool
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: wang2021exploring
citations: 449
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.11939'}]
tags: ["ICCV"]
short_authors: Wang et al.
---
Current semantic segmentation methods focus only on mining "local" context,
i.e., dependencies between pixels within individual images, by
context-aggregation modules (e.g., dilated convolution, neural attention) or
structure-aware optimization criteria (e.g., IoU-like loss). However, they
ignore "global" context of the training data, i.e., rich semantic relations
between pixels across different images. Inspired by the recent advance in
unsupervised contrastive representation learning, we propose a pixel-wise
contrastive framework for semantic segmentation in the fully supervised
setting. The core idea is to enforce pixel embeddings belonging to a same
semantic class to be more similar than embeddings from different classes. It
raises a pixel-wise metric learning paradigm for semantic segmentation, by
explicitly exploring the structures of labeled pixels, which were rarely
explored before. Our method can be effortlessly incorporated into existing
segmentation frameworks without extra overhead during testing. We
experimentally show that, with famous segmentation models (i.e., DeepLabV3,
HRNet, OCR) and backbones (i.e., ResNet, HR-Net), our method brings consistent
performance improvements across diverse datasets (i.e., Cityscapes,
PASCAL-Context, COCO-Stuff, CamVid). We expect this work will encourage our
community to rethink the current de facto training paradigm in fully supervised
semantic segmentation.