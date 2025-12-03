---
layout: publication
title: 'DSC: Deep Scan Context Descriptor For Large-scale Place Recognition'
authors: Jiafeng Cui, Tengfei Huang, Yingfeng Cai, Junqiao Zhao, Lu Xiong, Zhuoping
  Yu
conference: Arxiv
year: 2021
bibkey: cui2021dsc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.13838'}]
tags: ["Datasets", "Scalability"]
short_authors: Cui et al.
---
LiDAR-based place recognition is an essential and challenging task both in
loop closure detection and global relocalization. We propose Deep Scan Context
(DSC), a general and discriminative global descriptor that captures the
relationship among segments of a point cloud. Unlike previous methods that
utilize either semantics or a sequence of adjacent point clouds for better
place recognition, we only use raw point clouds to get competitive results.
Concretely, we first segment the point cloud egocentrically to acquire
centroids and eigenvalues of the segments. Then, we introduce a graph neural
network to aggregate these features into an embedding representation. Extensive
experiments conducted on the KITTI dataset show that DSC is robust to scene
variants and outperforms existing methods.