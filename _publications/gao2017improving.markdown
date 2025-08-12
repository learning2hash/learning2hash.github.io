---
layout: publication
title: Improving Object Detection With Region Similarity Learning
authors: Feng Gao, Yihang Lou, Yan Bai, Shiqi Wang, Tiejun Huang, Ling-Yu Duan
conference: 2017 IEEE International Conference on Multimedia and Expo (ICME)
year: 2017
bibkey: gao2017improving
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.00234'}]
tags: []
short_authors: Gao et al.
---
Object detection aims to identify instances of semantic objects of a certain
class in images or videos. The success of state-of-the-art approaches is
attributed to the significant progress of object proposal and convolutional
neural networks (CNNs). Most promising detectors involve multi-task learning
with an optimization objective of softmax loss and regression loss. The first
is for multi-class categorization, while the latter is for improving
localization accuracy. However, few of them attempt to further investigate the
hardness of distinguishing different sorts of distracting background regions
(i.e., negatives) from true object regions (i.e., positives). To improve the
performance of classifying positive object regions vs. a variety of negative
background regions, we propose to incorporate triplet embedding into learning
objective. The triplet units are formed by assigning each negative region to a
meaningful object class and establishing class- specific negatives, followed by
triplets construction. Over the benchmark PASCAL VOC 2007, the proposed triplet
em- bedding has improved the performance of well-known FastRCNN model with a
mAP gain of 2.1%. In particular, the state-of-the-art approach OHEM can benefit
from the triplet embedding and has achieved a mAP improvement of 1.2%.