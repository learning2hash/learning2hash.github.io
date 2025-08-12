---
layout: publication
title: 'DGC-GNN: Leveraging Geometry And Color Cues For Visual Descriptor-free 2D-3D
  Matching'
authors: Shuzhe Wang, Juho Kannala, Daniel Barath
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: wang2023dgc
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.12547'}]
tags: ["CVPR"]
short_authors: Shuzhe Wang, Juho Kannala, Daniel Barath
---
Matching 2D keypoints in an image to a sparse 3D point cloud of the scene
without requiring visual descriptors has garnered increased interest due to its
low memory requirements, inherent privacy preservation, and reduced need for
expensive 3D model maintenance compared to visual descriptor-based methods.
However, existing algorithms often compromise on performance, resulting in a
significant deterioration compared to their descriptor-based counterparts. In
this paper, we introduce DGC-GNN, a novel algorithm that employs a
global-to-local Graph Neural Network (GNN) that progressively exploits
geometric and color cues to represent keypoints, thereby improving matching
accuracy. Our procedure encodes both Euclidean and angular relations at a
coarse level, forming the geometric embedding to guide the point matching. We
evaluate DGC-GNN on both indoor and outdoor datasets, demonstrating that it not
only doubles the accuracy of the state-of-the-art visual descriptor-free
algorithm but also substantially narrows the performance gap between
descriptor-based and descriptor-free methods.