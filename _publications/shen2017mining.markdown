---
layout: publication
title: Mining Point Cloud Local Structures By Kernel Correlation And Graph Pooling
authors: Yiru Shen, Chen Feng, Yaoqing Yang, Dong Tian
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: shen2017mining
citations: 566
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.06760'}]
tags: ["CVPR"]
short_authors: Shen et al.
---
Unlike on images, semantic learning on 3D point clouds using a deep network
is challenging due to the naturally unordered data structure. Among existing
works, PointNet has achieved promising results by directly learning on point
sets. However, it does not take full advantage of a point's local neighborhood
that contains fine-grained structural information which turns out to be helpful
towards better semantic learning. In this regard, we present two new operations
to improve PointNet with a more efficient exploitation of local structures. The
first one focuses on local 3D geometric structures. In analogy to a convolution
kernel for images, we define a point-set kernel as a set of learnable 3D points
that jointly respond to a set of neighboring data points according to their
geometric affinities measured by kernel correlation, adapted from a similar
technique for point cloud registration. The second one exploits local
high-dimensional feature structures by recursive feature aggregation on a
nearest-neighbor-graph computed from 3D positions. Experiments show that our
network can efficiently capture local information and robustly achieve better
performances on major datasets. Our code is available at
http://www.merl.com/research/license%23KCNet