---
layout: publication
title: Semantic Instance Annotation Of Street Scenes By 3D To 2D Label Transfer
authors: Jun Xie, Martin Kiefel, Ming-ting Sun, Andreas Geiger
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: xie2015semantic
citations: 156
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.03240'}]
tags: ["CVPR", "Datasets"]
short_authors: Xie et al.
---
Semantic annotations are vital for training models for object recognition,
semantic segmentation or scene understanding. Unfortunately, pixelwise
annotation of images at very large scale is labor-intensive and only little
labeled data is available, particularly at instance level and for street
scenes. In this paper, we propose to tackle this problem by lifting the
semantic instance labeling task from 2D into 3D. Given reconstructions from
stereo or laser data, we annotate static 3D scene elements with rough bounding
primitives and develop a model which transfers this information into the image
domain. We leverage our method to obtain 2D labels for a novel suburban video
dataset which we have collected, resulting in 400k semantic and instance image
annotations. A comparison of our method to state-of-the-art label transfer
baselines reveals that 3D information enables more efficient annotation while
at the same time resulting in improved accuracy and time-coherent labels.