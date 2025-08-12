---
layout: publication
title: Point Cloud Classification Using Content-based Transformer Via Clustering In
  Feature Space
authors: Yahui Liu, Bin Tian, Yisheng Lv, Lingxi Li, Feiyue Wang
conference: IEEE/CAA Journal of Automatica Sinica
year: 2023
bibkey: liu2023point
citations: 51
additional_links: [{name: Code, url: 'https://github.com/yahuiliu99/PointConT'}, {
    name: Paper, url: 'https://arxiv.org/abs/2303.04599'}]
tags: ["Evaluation"]
short_authors: Liu et al.
---
Recently, there have been some attempts of Transformer in 3D point cloud
classification. In order to reduce computations, most existing methods focus on
local spatial attention, but ignore their content and fail to establish
relationships between distant but relevant points. To overcome the limitation
of local spatial attention, we propose a point content-based Transformer
architecture, called PointConT for short. It exploits the locality of points in
the feature space (content-based), which clusters the sampled points with
similar features into the same class and computes the self-attention within
each class, thus enabling an effective trade-off between capturing long-range
dependencies and computational complexity. We further introduce an Inception
feature aggregator for point cloud classification, which uses parallel
structures to aggregate high-frequency and low-frequency information in each
branch separately. Extensive experiments show that our PointConT model achieves
a remarkable performance on point cloud shape classification. Especially, our
method exhibits 90.3% Top-1 accuracy on the hardest setting of ScanObjectNN.
Source code of this paper is available at
https://github.com/yahuiliu99/PointConT.