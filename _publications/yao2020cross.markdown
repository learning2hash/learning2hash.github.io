---
layout: publication
title: Cross-dataset Training For Class Increasing Object Detection
authors: Yongqiang Yao, Yan Wang, Yu Guo, Jiaojiao Lin, Hongwei Qin, Junjie Yan
conference: Arxiv
year: 2020
bibkey: yao2020cross
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.04621'}]
tags: ["Datasets"]
short_authors: Yao et al.
---
We present a conceptually simple, flexible and general framework for
cross-dataset training in object detection. Given two or more already labeled
datasets that target for different object classes, cross-dataset training aims
to detect the union of the different classes, so that we do not have to label
all the classes for all the datasets. By cross-dataset training, existing
datasets can be utilized to detect the merged object classes with a single
model. Further more, in industrial applications, the object classes usually
increase on demand. So when adding new classes, it is quite time-consuming if
we label the new classes on all the existing datasets. While using
cross-dataset training, we only need to label the new classes on the new
dataset. We experiment on PASCAL VOC, COCO, WIDER FACE and WIDER Pedestrian
with both solo and cross-dataset settings. Results show that our cross-dataset
pipeline can achieve similar impressive performance simultaneously on these
datasets compared with training independently.