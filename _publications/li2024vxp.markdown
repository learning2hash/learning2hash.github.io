---
layout: publication
title: 'VXP: Voxel-cross-pixel Large-scale Image-lidar Place Recognition'
authors: Yun-Jin Li, Mariia Gladkova, Yan Xia, Rui Wang, Daniel Cremers
conference: Arxiv
year: 2024
bibkey: li2024vxp
citations: 4
additional_links: [{name: Other, url: 'https://yunjinli.github.io/projects-vxp/'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.14594'}]
tags: ["Evaluation", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Li et al.
---
Cross-modal place recognition methods are flexible GPS-alternatives under
varying environment conditions and sensor setups. However, this task is
non-trivial since extracting consistent and robust global descriptors from
different modalities is challenging. To tackle this issue, we propose
Voxel-Cross-Pixel (VXP), a novel camera-to-LiDAR place recognition framework
that enforces local similarities in a self-supervised manner and effectively
brings global context from images and LiDAR scans into a shared feature space.
Specifically, VXP is trained in three stages: first, we deploy a visual
transformer to compactly represent input images. Secondly, we establish local
correspondences between image-based and point cloud-based feature spaces using
our novel geometric alignment module. We then aggregate local similarities into
an expressive shared latent space. Extensive experiments on the three
benchmarks (Oxford RobotCar, ViViD++ and KITTI) demonstrate that our method
surpasses the state-of-the-art cross-modal retrieval by a large margin. Our
evaluations show that the proposed method is accurate, efficient and
light-weight. Our project page is available at:
https://yunjinli.github.io/projects-vxp/