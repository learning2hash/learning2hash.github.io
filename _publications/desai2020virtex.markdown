---
layout: publication
title: 'Virtex: Learning Visual Representations From Textual Annotations'
authors: Karan Desai, Justin Johnson
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: desai2020virtex
citations: 280
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.06666'}]
tags: ["CVPR"]
short_authors: Karan Desai, Justin Johnson
---
The de-facto approach to many vision tasks is to start from pretrained visual
representations, typically learned via supervised training on ImageNet. Recent
methods have explored unsupervised pretraining to scale to vast quantities of
unlabeled images. In contrast, we aim to learn high-quality visual
representations from fewer images. To this end, we revisit supervised
pretraining, and seek data-efficient alternatives to classification-based
pretraining. We propose VirTex -- a pretraining approach using semantically
dense captions to learn visual representations. We train convolutional networks
from scratch on COCO Captions, and transfer them to downstream recognition
tasks including image classification, object detection, and instance
segmentation. On all tasks, VirTex yields features that match or exceed those
learned on ImageNet -- supervised or unsupervised -- despite using up to ten
times fewer images.