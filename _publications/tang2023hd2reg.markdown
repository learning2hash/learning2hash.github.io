---
layout: publication
title: 'Hd2reg: Hierarchical Descriptors And Detectors For Point Cloud Registration'
authors: Canhui Tang, Yiheng Li, Shaoyi Du, Guofa Wang, Zhiqiang Tian
conference: 2023 IEEE Intelligent Vehicles Symposium (IV)
year: 2023
bibkey: tang2023hd2reg
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03487'}]
tags: []
short_authors: Tang et al.
---
Feature Descriptors and Detectors are two main components of feature-based
point cloud registration. However, little attention has been drawn to the
explicit representation of local and global semantics in the learning of
descriptors and detectors. In this paper, we present a framework that
explicitly extracts dual-level descriptors and detectors and performs
coarse-to-fine matching with them. First, to explicitly learn local and global
semantics, we propose a hierarchical contrastive learning strategy, training
the robust matching ability of high-level descriptors, and refining the local
feature space using low-level descriptors. Furthermore, we propose to learn
dual-level saliency maps that extract two groups of keypoints in two different
senses. To overcome the weak supervision of binary matchability labels, we
propose a ranking strategy to label the significance ranking of keypoints, and
thus provide more fine-grained supervision signals. Finally, we propose a
global-to-local matching scheme to obtain robust and accurate correspondences
by leveraging the complementary dual-level features.Quantitative experiments on
3DMatch and KITTI odometry datasets show that our method achieves robust and
accurate point cloud registration and outperforms recent keypoint-based
methods.