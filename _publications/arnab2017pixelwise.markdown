---
layout: publication
title: Pixelwise Instance Segmentation With A Dynamically Instantiated Network
authors: Anurag Arnab, Philip H. S Torr
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: arnab2017pixelwise
citations: 248
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.02386'}]
tags: ["CVPR"]
short_authors: Anurag Arnab, Philip H. S Torr
---
Semantic segmentation and object detection research have recently achieved
rapid progress. However, the former task has no notion of different instances
of the same object, and the latter operates at a coarse, bounding-box level. We
propose an Instance Segmentation system that produces a segmentation map where
each pixel is assigned an object class and instance identity label. Most
approaches adapt object detectors to produce segments instead of boxes. In
contrast, our method is based on an initial semantic segmentation module, which
feeds into an instance subnetwork. This subnetwork uses the initial
category-level segmentation, along with cues from the output of an object
detector, within an end-to-end CRF to predict instances. This part of our model
is dynamically instantiated to produce a variable number of instances per
image. Our end-to-end approach requires no post-processing and considers the
image holistically, instead of processing independent proposals. Therefore,
unlike some related work, a pixel cannot belong to multiple instances.
Furthermore, far more precise segmentations are achieved, as shown by our
state-of-the-art results (particularly at high IoU thresholds) on the Pascal
VOC and Cityscapes datasets.