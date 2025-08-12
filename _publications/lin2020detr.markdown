---
layout: publication
title: DETR For Crowd Pedestrian Detection
authors: Matthieu Lin, Chuming Li, Xingyuan Bu, Ming Sun, Chen Lin, Junjie Yan, Wanli
  Ouyang, Zhidong Deng
conference: Arxiv
year: 2020
bibkey: lin2020detr
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.06785'}]
tags: []
short_authors: Lin et al.
---
Pedestrian detection in crowd scenes poses a challenging problem due to the
heuristic defined mapping from anchors to pedestrians and the conflict between
NMS and highly overlapped pedestrians. The recently proposed end-to-end
detectors(ED), DETR and deformable DETR, replace hand designed components such
as NMS and anchors using the transformer architecture, which gets rid of
duplicate predictions by computing all pairwise interactions between queries.
Inspired by these works, we explore their performance on crowd pedestrian
detection. Surprisingly, compared to Faster-RCNN with FPN, the results are
opposite to those obtained on COCO. Furthermore, the bipartite match of ED
harms the training efficiency due to the large ground truth number in crowd
scenes. In this work, we identify the underlying motives driving ED's poor
performance and propose a new decoder to address them. Moreover, we design a
mechanism to leverage the less occluded visible parts of pedestrian
specifically for ED, and achieve further improvements. A faster bipartite match
algorithm is also introduced to make ED training on crowd dataset more
practical. The proposed detector PED(Pedestrian End-to-end Detector)
outperforms both previous EDs and the baseline Faster-RCNN on CityPersons and
CrowdHuman. It also achieves comparable performance with state-of-the-art
pedestrian detection methods. Code will be released soon.