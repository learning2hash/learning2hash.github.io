---
layout: publication
title: 'Tencent Ml-images: A Large-scale Multi-label Image Database For Visual Representation
  Learning'
authors: Baoyuan Wu, Weidong Chen, Yanbo Fan, Yong Zhang, Jinlong Hou, Jie Liu, Tong
  Zhang
conference: IEEE Access
year: 2019
bibkey: wu2019tencent
citations: 76
additional_links: [{name: Code, url: 'https://github.com/Tencent/tencent-ml-images'},
  {name: Paper, url: 'https://arxiv.org/abs/1901.01703'}]
tags: ["Scalability", "Tools & Libraries"]
short_authors: Wu et al.
---
In existing visual representation learning tasks, deep convolutional neural
networks (CNNs) are often trained on images annotated with single tags, such as
ImageNet. However, a single tag cannot describe all important contents of one
image, and some useful visual information may be wasted during training. In
this work, we propose to train CNNs from images annotated with multiple tags,
to enhance the quality of visual representation of the trained CNN model. To
this end, we build a large-scale multi-label image database with 18M images and
11K categories, dubbed Tencent ML-Images. We efficiently train the ResNet-101
model with multi-label outputs on Tencent ML-Images, taking 90 hours for 60
epochs, based on a large-scale distributed deep learning framework,i.e.,TFplus.
The good quality of the visual representation of the Tencent ML-Images
checkpoint is verified through three transfer learning tasks, including
single-label image classification on ImageNet and Caltech-256, object detection
on PASCAL VOC 2007, and semantic segmentation on PASCAL VOC 2012. The Tencent
ML-Images database, the checkpoints of ResNet-101, and all the training
codehave been released at https://github.com/Tencent/tencent-ml-images. It is
expected to promote other vision tasks in the research and industry community.