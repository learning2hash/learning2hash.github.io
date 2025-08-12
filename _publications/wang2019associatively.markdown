---
layout: publication
title: Associatively Segmenting Instances And Semantics In Point Clouds
authors: Xinlong Wang, Shu Liu, Xiaoyong Shen, Chunhua Shen, Jiaya Jia
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: wang2019associatively
citations: 269
additional_links: [{name: Code, url: 'https://github.com/WXinlong/ASIS'}, {name: Paper,
    url: 'https://arxiv.org/abs/1902.09852'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
A 3D point cloud describes the real scene precisely and intuitively.To date
how to segment diversified elements in such an informative 3D scene is rarely
discussed. In this paper, we first introduce a simple and flexible framework to
segment instances and semantics in point clouds simultaneously. Then, we
propose two approaches which make the two tasks take advantage of each other,
leading to a win-win situation. Specifically, we make instance segmentation
benefit from semantic segmentation through learning semantic-aware point-level
instance embedding. Meanwhile, semantic features of the points belonging to the
same instance are fused together to make more accurate per-point semantic
predictions. Our method largely outperforms the state-of-the-art method in 3D
instance segmentation along with a significant improvement in 3D semantic
segmentation. Code has been made available at:
https://github.com/WXinlong/ASIS.