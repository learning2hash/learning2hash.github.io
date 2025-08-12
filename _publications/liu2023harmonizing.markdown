---
layout: publication
title: 'Harmonizing Base And Novel Classes: A Class-contrastive Approach For Generalized
  Few-shot Segmentation'
authors: Weide Liu, Zhonghua Wu, Yang Zhao, Yuming Fang, Chuan-Sheng Foo, Jun Cheng,
  Guosheng Lin
conference: International Journal of Computer Vision
year: 2023
bibkey: liu2023harmonizing
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.13724'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Current methods for few-shot segmentation (FSSeg) have mainly focused on
improving the performance of novel classes while neglecting the performance of
base classes. To overcome this limitation, the task of generalized few-shot
semantic segmentation (GFSSeg) has been introduced, aiming to predict
segmentation masks for both base and novel classes. However, the current
prototype-based methods do not explicitly consider the relationship between
base and novel classes when updating prototypes, leading to a limited
performance in identifying true categories. To address this challenge, we
propose a class contrastive loss and a class relationship loss to regulate
prototype updates and encourage a large distance between prototypes from
different classes, thus distinguishing the classes from each other while
maintaining the performance of the base classes. Our proposed approach achieves
new state-of-the-art performance for the generalized few-shot segmentation task
on PASCAL VOC and MS COCO datasets.