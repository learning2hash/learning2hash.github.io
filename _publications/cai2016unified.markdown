---
layout: publication
title: A Unified Multi-scale Deep Convolutional Neural Network For Fast Object Detection
authors: Zhaowei Cai, Quanfu Fan, Rogerio S. Feris, Nuno Vasconcelos
conference: Lecture Notes in Computer Science
year: 2016
bibkey: cai2016unified
citations: 1592
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.07155'}]
tags: []
short_authors: Cai et al.
---
A unified deep neural network, denoted the multi-scale CNN (MS-CNN), is
proposed for fast multi-scale object detection. The MS-CNN consists of a
proposal sub-network and a detection sub-network. In the proposal sub-network,
detection is performed at multiple output layers, so that receptive fields
match objects of different scales. These complementary scale-specific detectors
are combined to produce a strong multi-scale object detector. The unified
network is learned end-to-end, by optimizing a multi-task loss. Feature
upsampling by deconvolution is also explored, as an alternative to input
upsampling, to reduce the memory and computation costs. State-of-the-art object
detection performance, at up to 15 fps, is reported on datasets, such as KITTI
and Caltech, containing a substantial number of small objects.