---
layout: publication
title: Work-efficient Parallel Non-maximum Suppression Kernels
authors: "David Oro, Carles Fern\xE1ndez, Xavier Martorell, Javier Hernando"
conference: The Computer Journal
year: 2020
bibkey: oro2020work
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.00535'}]
tags: []
short_authors: Oro et al.
---
In the context of object detection, sliding-window classifiers and
single-shot Convolutional Neural Network (CNN) meta-architectures typically
yield multiple overlapping candidate windows with similar high scores around
the true location of a particular object. Non-Maximum Suppression (NMS) is the
process of selecting a single representative candidate within this cluster of
detections, so as to obtain a unique detection per object appearing on a given
picture. In this paper, we present a highly scalable NMS algorithm for embedded
GPU architectures that is designed from scratch to handle workloads featuring
thousands of simultaneous detections on a given picture. Our kernels are
directly applicable to other sequential NMS algorithms such as FeatureNMS,
Soft-NMS or AdaptiveNMS that share the inner workings of the classic greedy NMS
method. The obtained performance results show that our parallel NMS algorithm
is capable of clustering 1024 simultaneous detected objects per frame in
roughly 1 ms on both NVIDIA Tegra X1 and NVIDIA Tegra X2 on-die GPUs, while
taking 2 ms on NVIDIA Tegra K1. Furthermore, our proposed parallel greedy NMS
algorithm yields a 14x-40x speed up when compared to state-of-the-art NMS
methods that require learning a CNN from annotated data.