---
layout: publication
title: 'Deep Affinity Net: Instance Segmentation Via Affinity'
authors: Xingqian Xu, Mang Tik Chiu, Thomas S. Huang, Honghui Shi
conference: Arxiv
year: 2020
bibkey: xu2020deep
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.06849'}]
tags: []
short_authors: Xu et al.
---
Most of the modern instance segmentation approaches fall into two categories:
region-based approaches in which object bounding boxes are detected first and
later used in cropping and segmenting instances; and keypoint-based approaches
in which individual instances are represented by a set of keypoints followed by
a dense pixel clustering around those keypoints. Despite the maturity of these
two paradigms, we would like to report an alternative affinity-based paradigm
where instances are segmented based on densely predicted affinities and graph
partitioning algorithms. Such affinity-based approaches indicate that
high-level graph features other than regions or keypoints can be directly
applied in the instance segmentation task. In this work, we propose Deep
Affinity Net, an effective affinity-based approach accompanied with a new graph
partitioning algorithm Cascade-GAEC. Without bells and whistles, our end-to-end
model results in 32.4% AP on Cityscapes val and 27.5% AP on test. It achieves
the best single-shot result as well as the fastest running time among all
affinity-based models. It also outperforms the region-based method Mask R-CNN.