---
layout: publication
title: 'Catdet: Cascaded Tracked Detector For Efficient Object Detection From Video'
authors: Huizi Mao, Taeyoung Kong, William J. Dally
conference: Arxiv
year: 2018
bibkey: mao2018catdet
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.00434'}]
tags: ["Efficiency"]
short_authors: Huizi Mao, Taeyoung Kong, William J. Dally
---
Detecting objects in a video is a compute-intensive task. In this paper we
propose CaTDet, a system to speedup object detection by leveraging the temporal
correlation in video. CaTDet consists of two DNN models that form a cascaded
detector, and an additional tracker to predict regions of interests based on
historic detections. We also propose a new metric, mean Delay(mD), which is
designed for latency-critical video applications. Experiments on the KITTI
dataset show that CaTDet reduces operation count by 5.1-8.7x with the same mean
Average Precision(mAP) as the single-model Faster R-CNN detector and incurs
additional delay of 0.3 frame. On CityPersons dataset, CaTDet achieves 13.0x
reduction in operations with 0.8% mAP loss.