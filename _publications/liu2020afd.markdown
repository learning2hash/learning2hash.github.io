---
layout: publication
title: 'Afd-net: Adaptive Fully-dual Network For Few-shot Object Detection'
authors: Longyao Liu, Bo Ma, Yulin Zhang, Xin Yi, Haozhi Li
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: liu2020afd
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.14667'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot object detection (FSOD) aims at learning a detector that can fast
adapt to previously unseen objects with scarce annotated examples, which is
challenging and demanding. Existing methods solve this problem by performing
subtasks of classification and localization utilizing a shared component (e.g.,
RoI head) in the detector, yet few of them take the distinct preferences of two
subtasks towards feature embedding into consideration. In this paper, we
carefully analyze the characteristics of FSOD, and present that a general
few-shot detector should consider the explicit decomposition of two subtasks,
as well as leveraging information from both of them to enhance feature
representations. To the end, we propose a simple yet effective Adaptive
Fully-Dual Network (AFD-Net). Specifically, we extend Faster R-CNN by
introducing Dual Query Encoder and Dual Attention Generator for separate
feature extraction, and Dual Aggregator for separate model reweighting.
Spontaneously, separate state estimation is achieved by the R-CNN detector.
Besides, for the acquisition of enhanced feature representations, we further
introduce Adaptive Fusion Mechanism to adaptively perform feature fusion in
different subtasks. Extensive experiments on PASCAL VOC and MS COCO in various
settings show that, our method achieves new state-of-the-art performance by a
large margin, demonstrating its effectiveness and generalization ability.