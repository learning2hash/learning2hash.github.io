---
layout: publication
title: Hashing-based Non-maximum Suppression For Crowded Object Detection
authors: Wang Jianfeng, Yin Xi, Wang Lijuan, Zhang Lei
conference: "Arxiv"
year: 2020
bibkey: wang2020hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.11426"}
  - {name: "Code", url: "https://github.com/microsoft/hnms.git}"}
tags: ['ARXIV', 'Has Code']
---
In this paper, we propose an algorithm, named hashing-based non-maximum suppression (HNMS) to efficiently suppress the non-maximum boxes for object detection. Non-maximum suppression (NMS) is an essential component to suppress the boxes at closely located locations with similar shapes. The time cost tends to be huge when the number of boxes becomes large, especially for crowded scenes. The basic idea of HNMS is to firstly map each box to a discrete code (hash cell) and then remove the boxes with lower confidences if they are in the same cell. Considering the intersection-over-union (IoU) as the metric, we propose a simple yet effective hashing algorithm, named IoUHash, which guarantees that the boxes within the same cell are close enough by a lower IoU bound. For two-stage detectors, we replace NMS in region proposal network with HNMS, and observe significant speed-up with comparable accuracy. For one-stage detectors, HNMS is used as a pre-filter to speed up the suppression with a large margin. Extensive experiments are conducted on CARPK, SKU-110K, CrowdHuman datasets to demonstrate the efficiency and effectiveness of HNMS. Code is released at \url{https://github.com/microsoft/hnms.git}.
