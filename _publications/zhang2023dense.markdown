---
layout: publication
title: Dense Distinct Query For End-to-end Object Detection
authors: Shilong Zhang, Xinjiang Wang, Jiaqi Wang, Jiangmiao Pang, Chengqi Lyu, Wenwei
  Zhang, Ping Luo, Kai Chen
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: zhang2023dense
citations: 114
additional_links: [{name: Code, url: 'https://github.com/jshilong/DDQ'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.12776'}]
tags: ["CVPR"]
short_authors: Zhang et al.
---
One-to-one label assignment in object detection has successfully obviated the
need for non-maximum suppression (NMS) as postprocessing and makes the pipeline
end-to-end. However, it triggers a new dilemma as the widely used sparse
queries cannot guarantee a high recall, while dense queries inevitably bring
more similar queries and encounter optimization difficulties. As both sparse
and dense queries are problematic, then what are the expected queries in
end-to-end object detection? This paper shows that the solution should be Dense
Distinct Queries (DDQ). Concretely, we first lay dense queries like traditional
detectors and then select distinct ones for one-to-one assignments. DDQ blends
the advantages of traditional and recent end-to-end detectors and significantly
improves the performance of various detectors including FCN, R-CNN, and DETRs.
Most impressively, DDQ-DETR achieves 52.1 AP on MS-COCO dataset within 12
epochs using a ResNet-50 backbone, outperforming all existing detectors in the
same setting. DDQ also shares the benefit of end-to-end detectors in crowded
scenes and achieves 93.8 AP on CrowdHuman. We hope DDQ can inspire researchers
to consider the complementarity between traditional methods and end-to-end
detectors. The source code can be found at
https://github.com/jshilong/DDQ.