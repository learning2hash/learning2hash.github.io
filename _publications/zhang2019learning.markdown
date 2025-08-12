---
layout: publication
title: Learning Semantics-aware Distance Map With Semantics Layering Network For Amodal
  Instance Segmentation
authors: Ziheng Zhang, Anpei Chen, Ling Xie, Jingyi Yu, Shenghua Gao
conference: Proceedings of the 27th ACM International Conference on Multimedia
year: 2019
bibkey: zhang2019learning
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12898'}]
tags: []
short_authors: Zhang et al.
---
In this work, we demonstrate yet another approach to tackle the amodal
segmentation problem. Specifically, we first introduce a new representation,
namely a semantics-aware distance map (sem-dist map), to serve as our target
for amodal segmentation instead of the commonly used masks and heatmaps. The
sem-dist map is a kind of level-set representation, of which the different
regions of an object are placed into different levels on the map according to
their visibility. It is a natural extension of masks and heatmaps, where modal,
amodal segmentation, as well as depth order information, are all
well-described. Then we also introduce a novel convolutional neural network
(CNN) architecture, which we refer to as semantic layering network, to estimate
sem-dist maps layer by layer, from the global-level to the instance-level, for
all objects in an image. Extensive experiments on the COCOA and D2SA datasets
have demonstrated that our framework can predict amodal segmentation, occlusion
and depth order with state-of-the-art performance.