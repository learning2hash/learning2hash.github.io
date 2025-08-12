---
layout: publication
title: Fine-grained Object Classification Via Self-supervised Pose Alignment
authors: Xuhui Yang, Yaowei Wang, Ke Chen, Yong Xu, Yonghong Tian
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: yang2022fine
citations: 56
additional_links: [{name: Code, url: 'https://github.com/yangxh11/P2P-Net'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.15987'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Yang et al.
---
Semantic patterns of fine-grained objects are determined by subtle appearance
difference of local parts, which thus inspires a number of part-based methods.
However, due to uncontrollable object poses in images, distinctive details
carried by local regions can be spatially distributed or even self-occluded,
leading to a large variation on object representation. For discounting pose
variations, this paper proposes to learn a novel graph based object
representation to reveal a global configuration of local parts for
self-supervised pose alignment across classes, which is employed as an
auxiliary feature regularization on a deep representation learning
network.Moreover, a coarse-to-fine supervision together with the proposed
pose-insensitive constraint on shallow-to-deep sub-networks encourages
discriminative features in a curriculum learning manner. We evaluate our method
on three popular fine-grained object classification benchmarks, consistently
achieving the state-of-the-art performance. Source codes are available at
https://github.com/yangxh11/P2P-Net.