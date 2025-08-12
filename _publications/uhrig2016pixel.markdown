---
layout: publication
title: Pixel-level Encoding And Depth Layering For Instance-level Semantic Labeling
authors: Jonas Uhrig, Marius Cordts, Uwe Franke, Thomas Brox
conference: Lecture Notes in Computer Science
year: 2016
bibkey: uhrig2016pixel
citations: 159
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.05096'}]
tags: []
short_authors: Uhrig et al.
---
Recent approaches for instance-aware semantic labeling have augmented
convolutional neural networks (CNNs) with complex multi-task architectures or
computationally expensive graphical models. We present a method that leverages
a fully convolutional network (FCN) to predict semantic labels, depth and an
instance-based encoding using each pixel's direction towards its corresponding
instance center. Subsequently, we apply low-level computer vision techniques to
generate state-of-the-art instance segmentation on the street scene datasets
KITTI and Cityscapes. Our approach outperforms existing works by a large margin
and can additionally predict absolute distances of individual instances from a
monocular image as well as a pixel-level semantic labeling.