---
layout: publication
title: 'Nm-net: Mining Reliable Neighbors For Robust Feature Correspondences'
authors: Chen Zhao, Zhiguo Cao, Chi Li, Xin Li, Jiaqi Yang
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: zhao2019nm
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.00320'}]
tags: ["CVPR", "Datasets", "Evaluation", "Robustness"]
short_authors: Zhao et al.
---
Feature correspondence selection is pivotal to many feature-matching based
tasks in computer vision. Searching for spatially k-nearest neighbors is a
common strategy for extracting local information in many previous works.
However, there is no guarantee that the spatially k-nearest neighbors of
correspondences are consistent because the spatial distribution of false
correspondences is often irregular. To address this issue, we present a
compatibility-specific mining method to search for consistent neighbors.
Moreover, in order to extract and aggregate more reliable features from
neighbors, we propose a hierarchical network named NM-Net with a series of
convolution layers taking the generated graph as input, which is insensitive to
the order of correspondences. Our experimental results have shown the proposed
method achieves the state-of-the-art performance on four datasets with various
inlier ratios and varying numbers of feature consistencies.