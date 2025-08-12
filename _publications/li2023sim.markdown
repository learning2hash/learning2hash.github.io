---
layout: publication
title: 'SIM: Semantic-aware Instance Mask Generation For Box-supervised Instance Segmentation'
authors: Ruihuang Li, Chenhang He, Yabin Zhang, Shuai Li, Liyi Chen, Lei Zhang
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: li2023sim
citations: 13
additional_links: [{name: Code, url: 'https://github.com/lslrh/SIM'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.08578'}]
tags: ["CVPR", "Supervised"]
short_authors: Li et al.
---
Weakly supervised instance segmentation using only bounding box annotations
has recently attracted much research attention. Most of the current efforts
leverage low-level image features as extra supervision without explicitly
exploiting the high-level semantic information of the objects, which will
become ineffective when the foreground objects have similar appearances to the
background or other objects nearby. We propose a new box-supervised instance
segmentation approach by developing a Semantic-aware Instance Mask (SIM)
generation paradigm. Instead of heavily relying on local pair-wise affinities
among neighboring pixels, we construct a group of category-wise feature
centroids as prototypes to identify foreground objects and assign them
semantic-level pseudo labels. Considering that the semantic-aware prototypes
cannot distinguish different instances of the same semantics, we propose a
self-correction mechanism to rectify the falsely activated regions while
enhancing the correct ones. Furthermore, to handle the occlusions between
objects, we tailor the Copy-Paste operation for the weakly-supervised instance
segmentation task to augment challenging training data. Extensive experimental
results demonstrate the superiority of our proposed SIM approach over other
state-of-the-art methods. The source code: https://github.com/lslrh/SIM.