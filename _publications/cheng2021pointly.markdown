---
layout: publication
title: Pointly-supervised Instance Segmentation
authors: Bowen Cheng, Omkar Parkhi, Alexander Kirillov
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: cheng2021pointly
citations: 106
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.06404'}]
tags: ["CVPR", "Evaluation", "Supervised"]
short_authors: Bowen Cheng, Omkar Parkhi, Alexander Kirillov
---
We propose an embarrassingly simple point annotation scheme to collect weak
supervision for instance segmentation. In addition to bounding boxes, we
collect binary labels for a set of points uniformly sampled inside each
bounding box. We show that the existing instance segmentation models developed
for full mask supervision can be seamlessly trained with point-based
supervision collected via our scheme. Remarkably, Mask R-CNN trained on COCO,
PASCAL VOC, Cityscapes, and LVIS with only 10 annotated random points per
object achieves 94%--98% of its fully-supervised performance, setting a strong
baseline for weakly-supervised instance segmentation. The new point annotation
scheme is approximately 5 times faster than annotating full object masks,
making high-quality instance segmentation more accessible in practice.
  Inspired by the point-based annotation form, we propose a modification to
PointRend instance segmentation module. For each object, the new architecture,
called Implicit PointRend, generates parameters for a function that makes the
final point-level mask prediction. Implicit PointRend is more straightforward
and uses a single point-level mask loss. Our experiments show that the new
module is more suitable for the point-based supervision.