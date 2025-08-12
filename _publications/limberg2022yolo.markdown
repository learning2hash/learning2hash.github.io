---
layout: publication
title: YOLO -- You Only Look 10647 Times
authors: Christian Limberg, Andrew Melnik, Augustin Harter, Helge Ritter
conference: Proceedings of the 18th International Joint Conference on Computer Vision,
  Imaging and Computer Graphics Theory and Applications
year: 2023
bibkey: limberg2022yolo
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.06159'}]
tags: ["CVPR", "ECCV", "ICCV"]
short_authors: Limberg et al.
---
With this work we are explaining the "You Only Look Once" (YOLO) single-stage
object detection approach as a parallel classification of 10647 fixed region
proposals. We support this view by showing that each of YOLOs output pixel is
attentive to a specific sub-region of previous layers, comparable to a local
region proposal. This understanding reduces the conceptual gap between
YOLO-like single-stage object detection models, RCNN-like two-stage region
proposal based models, and ResNet-like image classification models. In
addition, we created interactive exploration tools for a better visual
understanding of the YOLO information processing streams:
https://limchr.github.io/yolo_visualization