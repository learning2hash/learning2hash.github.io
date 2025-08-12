---
layout: publication
title: 'Picie: Unsupervised Semantic Segmentation Using Invariance And Equivariance
  In Clustering'
authors: Jang Hyun Cho, Utkarsh Mall, Kavita Bala, Bharath Hariharan
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: cho2021picie
citations: 100
additional_links: [{name: Code, url: 'https://github.com/janghyuncho/PiCIE'}, {name: Paper,
    url: 'https://arxiv.org/abs/2103.17070'}]
tags: ["CVPR", "Unsupervised"]
short_authors: Cho et al.
---
We present a new framework for semantic segmentation without annotations via
clustering. Off-the-shelf clustering methods are limited to curated,
single-label, and object-centric images yet real-world data are dominantly
uncurated, multi-label, and scene-centric. We extend clustering from images to
pixels and assign separate cluster membership to different instances within
each image. However, solely relying on pixel-wise feature similarity fails to
learn high-level semantic concepts and overfits to low-level visual cues. We
propose a method to incorporate geometric consistency as an inductive bias to
learn invariance and equivariance for photometric and geometric variations.
With our novel learning objective, our framework can learn high-level semantic
concepts. Our method, PiCIE (Pixel-level feature Clustering using Invariance
and Equivariance), is the first method capable of segmenting both things and
stuff categories without any hyperparameter tuning or task-specific
pre-processing. Our method largely outperforms existing baselines on COCO and
Cityscapes with +17.5 Acc. and +4.5 mIoU. We show that PiCIE gives a better
initialization for standard supervised training. The code is available at
https://github.com/janghyuncho/PiCIE.