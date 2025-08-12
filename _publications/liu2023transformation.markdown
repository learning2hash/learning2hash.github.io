---
layout: publication
title: Transformation-invariant Network For Few-shot Object Detection In Remote Sensing
  Images
authors: Nanqing Liu, Xun Xu, Turgay Celik, Zongxin Gan, Heng-Chao Li
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2023
bibkey: liu2023transformation
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.06817'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Object detection in remote sensing images relies on a large amount of labeled
data for training. However, the increasing number of new categories and class
imbalance make exhaustive annotation impractical. Few-shot object detection
(FSOD) addresses this issue by leveraging meta-learning on seen base classes
and fine-tuning on novel classes with limited labeled samples. Nonetheless, the
substantial scale and orientation variations of objects in remote sensing
images pose significant challenges to existing few-shot object detection
methods. To overcome these challenges, we propose integrating a feature pyramid
network and utilizing prototype features to enhance query features, thereby
improving existing FSOD methods. We refer to this modified FSOD approach as a
Strong Baseline, which has demonstrated significant performance improvements
compared to the original baselines. Furthermore, we tackle the issue of spatial
misalignment caused by orientation variations between the query and support
images by introducing a Transformation-Invariant Network (TINet). TINet ensures
geometric invariance and explicitly aligns the features of the query and
support branches, resulting in additional performance gains while maintaining
the same inference speed as the Strong Baseline. Extensive experiments on three
widely used remote sensing object detection datasets, i.e., NWPU VHR-10.v2,
DIOR, and HRRSD demonstrated the effectiveness of the proposed method.