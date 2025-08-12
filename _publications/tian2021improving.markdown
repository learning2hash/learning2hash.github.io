---
layout: publication
title: Improving Apparel Detection With Category Grouping And Multi-grained Branches
authors: Qing Tian, Sampath Chanda, K C Amit Kumar, Douglas Gray
conference: Multimedia Tools and Applications
year: 2022
bibkey: tian2021improving
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.06770'}]
tags: ["Evaluation"]
short_authors: Tian et al.
---
Training an accurate object detector is expensive and time-consuming. One
main reason lies in the laborious labeling process, i.e., annotating category
and bounding box information for all instances in every image. In this paper,
we examine ways to improve performance of deep object detectors without extra
labeling. We first explore to group existing categories of high visual and
semantic similarities together as one super category (or, a superclass). Then,
we study how this knowledge of hierarchical categories can be exploited to
better detect object using multi-grained RCNN top branches. Experimental
results on DeepFashion2 and OpenImagesV4-Clothing reveal that the proposed
detection heads with multi-grained branches can boost the overall performance
by 2.3 mAP for DeepFashion2 and 2.5 mAP for OpenImagesV4-Clothing with no
additional time-consuming annotations. More importantly, classes that have
fewer training samples tend to benefit more from the proposed multi-grained
heads with superclass grouping. In particular, we improve the mAP for last 30%
categories (in terms of training sample number) by 2.6 and 4.6 for DeepFashion2
and OpenImagesV4-Clothing, respectively.