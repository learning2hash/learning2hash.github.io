---
layout: publication
title: Patchnet -- Short-range Template Matching For Efficient Video Processing
authors: Huizi Mao, Sibo Zhu, Song Han, William J. Dally
conference: Arxiv
year: 2021
bibkey: mao2021patchnet
citations: 2
additional_links: [{name: Code, url: 'https://github.com/RalphMao/PatchNet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2103.07371'}]
tags: []
short_authors: Mao et al.
---
Object recognition is a fundamental problem in many video processing tasks,
accurately locating seen objects at low computation cost paves the way for
on-device video recognition. We propose PatchNet, an efficient convolutional
neural network to match objects in adjacent video frames. It learns the
patchwise correlation features instead of pixel features. PatchNet is very
compact, running at just 58MFLOPs, \(5\times\) simpler than MobileNetV2. We
demonstrate its application on two tasks, video object detection and visual
object tracking. On ImageNet VID, PatchNet reduces the flops of R-FCN
ResNet-101 by 5x and EfficientDet-D0 by 3.4x with less than 1% mAP loss. On
OTB2015, PatchNet reduces SiamFC and SiamRPN by 2.5x with no accuracy loss.
Experiments on Jetson Nano further demonstrate 2.8x to 4.3x speed-ups
associated with flops reduction. Code is open sourced at
https://github.com/RalphMao/PatchNet.