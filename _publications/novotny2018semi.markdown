---
layout: publication
title: Semi-convolutional Operators For Instance Segmentation
authors: David Novotny, Samuel Albanie, Diane Larlus, Andrea Vedaldi
conference: Lecture Notes in Computer Science
year: 2018
bibkey: novotny2018semi
citations: 96
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.10712'}]
tags: []
short_authors: Novotny et al.
---
Object detection and instance segmentation are dominated by region-based
methods such as Mask RCNN. However, there is a growing interest in reducing
these problems to pixel labeling tasks, as the latter could be more efficient,
could be integrated seamlessly in image-to-image network architectures as used
in many other tasks, and could be more accurate for objects that are not well
approximated by bounding boxes. In this paper we show theoretically and
empirically that constructing dense pixel embeddings that can separate object
instances cannot be easily achieved using convolutional operators. At the same
time, we show that simple modifications, which we call semi-convolutional, have
a much better chance of succeeding at this task. We use the latter to show a
connection to Hough voting as well as to a variant of the bilateral kernel that
is spatially steered by a convolutional network. We demonstrate that these
operators can also be used to improve approaches such as Mask RCNN,
demonstrating better segmentation of complex biological shapes and PASCAL VOC
categories than achievable by Mask RCNN alone.