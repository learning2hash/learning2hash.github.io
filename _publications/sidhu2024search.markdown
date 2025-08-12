---
layout: publication
title: 'Search And Detect: Training-free Long Tail Object Detection Via Web-image
  Retrieval'
authors: Mankeerat Sidhu, Hetarth Chopra, Ansel Blume, Jeonghwan Kim, Revanth Gangi
  Reddy, Heng Ji
conference: Arxiv
year: 2024
bibkey: sidhu2024search
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.18733'}]
tags: []
short_authors: Sidhu et al.
---
In this paper, we introduce SearchDet, a training-free long-tail object
detection framework that significantly enhances open-vocabulary object
detection performance. SearchDet retrieves a set of positive and negative
images of an object to ground, embeds these images, and computes an input
image-weighted query which is used to detect the desired concept in the image.
Our proposed method is simple and training-free, yet achieves over 48.7% mAP
improvement on ODinW and 59.1% mAP improvement on LVIS compared to
state-of-the-art models such as GroundingDINO. We further show that our
approach of basing object detection on a set of Web-retrieved exemplars is
stable with respect to variations in the exemplars, suggesting a path towards
eliminating costly data annotation and training procedures.