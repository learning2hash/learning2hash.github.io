---
layout: publication
title: 'Onepose: One-shot Object Pose Estimation Without CAD Models'
authors: Jiaming Sun, Zihao Wang, Siyu Zhang, Xingyi He, Hongcheng Zhao, Guofeng Zhang,
  Xiaowei Zhou
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: sun2022onepose
citations: 87
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.12257'}]
tags: ["CVPR"]
short_authors: Sun et al.
---
We propose a new method named OnePose for object pose estimation. Unlike
existing instance-level or category-level methods, OnePose does not rely on CAD
models and can handle objects in arbitrary categories without instance- or
category-specific network training. OnePose draws the idea from visual
localization and only requires a simple RGB video scan of the object to build a
sparse SfM model of the object. Then, this model is registered to new query
images with a generic feature matching network. To mitigate the slow runtime of
existing visual localization methods, we propose a new graph attention network
that directly matches 2D interest points in the query image with the 3D points
in the SfM model, resulting in efficient and robust pose estimation. Combined
with a feature-based pose tracker, OnePose is able to stably detect and track
6D poses of everyday household objects in real-time. We also collected a
large-scale dataset that consists of 450 sequences of 150 objects.