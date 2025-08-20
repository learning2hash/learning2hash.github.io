---
layout: publication
title: 'Spatial Semantic Embedding Network: Fast 3D Instance Segmentation With Deep
  Metric Learning'
authors: Dongsu Zhang, Junha Chun, Sang Kyun Cha, Young Min Kim
conference: Arxiv
year: 2020
bibkey: zhang2020spatial
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.03169'}]
tags: [Evaluation, Distance Metric Learning, Re-ranking, Scalability]
short_authors: Zhang et al.
---
We propose spatial semantic embedding network (SSEN), a simple, yet efficient
algorithm for 3D instance segmentation using deep metric learning. The raw 3D
reconstruction of an indoor environment suffers from occlusions, noise, and is
produced without any meaningful distinction between individual entities. For
high-level intelligent tasks from a large scale scene, 3D instance segmentation
recognizes individual instances of objects. We approach the instance
segmentation by simply learning the correct embedding space that maps
individual instances of objects into distinct clusters that reflect both
spatial and semantic information. Unlike previous approaches that require
complex pre-processing or post-processing, our implementation is compact and
fast with competitive performance, maintaining scalability on large scenes with
high resolution voxels. We demonstrate the state-of-the-art performance of our
algorithm in the ScanNet 3D instance segmentation benchmark on AP score.