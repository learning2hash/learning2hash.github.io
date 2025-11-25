---
layout: publication
title: 'Modalink: Unifying Modalities For Efficient Image-to-pointcloud Place Recognition'
authors: Weidong Xie, Lun Luo, Nanfei Ye, Yi Ren, Shaoyi Du, Minhang Wang, Jintao
  Xu, Rui Ai, Weihao Gu, Xieyuanli Chen
conference: 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2024
bibkey: xie2024modalink
citations: 6
additional_links: [{name: Code, url: 'https://github.com/haomo-ai/ModaLink.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.18762'}]
tags: ["Efficiency", "IROS", "Multimodal Retrieval"]
short_authors: Xie et al.
---
Place recognition is an important task for robots and autonomous cars to
localize themselves and close loops in pre-built maps. While single-modal
sensor-based methods have shown satisfactory performance, cross-modal place
recognition that retrieving images from a point-cloud database remains a
challenging problem. Current cross-modal methods transform images into 3D
points using depth estimation for modality conversion, which are usually
computationally intensive and need expensive labeled data for depth
supervision. In this work, we introduce a fast and lightweight framework to
encode images and point clouds into place-distinctive descriptors. We propose
an effective Field of View (FoV) transformation module to convert point clouds
into an analogous modality as images. This module eliminates the necessity for
depth estimation and helps subsequent modules achieve real-time performance. We
further design a non-negative factorization-based encoder to extract mutually
consistent semantic features between point clouds and images. This encoder
yields more distinctive global descriptors for retrieval. Experimental results
on the KITTI dataset show that our proposed methods achieve state-of-the-art
performance while running in real time. Additional evaluation on the HAOMO
dataset covering a 17 km trajectory further shows the practical generalization
capabilities. We have released the implementation of our methods as open source
at: https://github.com/haomo-ai/ModaLink.git.