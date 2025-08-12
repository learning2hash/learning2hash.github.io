---
layout: publication
title: 'Spnet: Multi-shell Kernel Convolution For Point Cloud Semantic Segmentation'
authors: Yuyan Li, Chuanmao Fan, Xu Wang, Ye Duan
conference: Lecture Notes in Computer Science
year: 2021
bibkey: li2021spnet
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.11610'}]
tags: []
short_authors: Li et al.
---
Feature encoding is essential for point cloud analysis. In this paper, we
propose a novel point convolution operator named Shell Point Convolution
(SPConv) for shape encoding and local context learning. Specifically, SPConv
splits 3D neighborhood space into shells, aggregates local features on manually
designed kernel points, and performs convolution on the shells. Moreover,
SPConv incorporates a simple yet effective attention module that enhances local
feature aggregation. Based upon SPConv, a deep neural network named SPNet is
constructed to process large-scale point clouds. Poisson disk sampling and
feature propagation are incorporated in SPNet for better efficiency and
accuracy. We provided details of the shell design and conducted extensive
experiments on challenging large-scale point cloud datasets. Experimental
results show that SPConv is effective in local shape encoding, and our SPNet is
able to achieve top-ranking performances in semantic segmentation tasks.