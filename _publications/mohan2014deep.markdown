---
layout: publication
title: Deep Deconvolutional Networks For Scene Parsing
authors: Rahul Mohan
conference: Arxiv
year: 2014
bibkey: mohan2014deep
citations: 53
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1411.4101'}]
tags: []
short_authors: Rahul Mohan
---
Scene parsing is an important and challenging prob- lem in computer vision.
It requires labeling each pixel in an image with the category it belongs to.
Tradition- ally, it has been approached with hand-engineered features from
color information in images. Recently convolutional neural networks (CNNs),
which automatically learn hierar- chies of features, have achieved record
performance on the task. These approaches typically include a post-processing
technique, such as superpixels, to produce the final label- ing. In this paper,
we propose a novel network architecture that combines deep deconvolutional
neural networks with CNNs. Our experiments show that deconvolutional neu- ral
networks are capable of learning higher order image structure beyond edge
primitives in comparison to CNNs. The new network architecture is employed for
multi-patch training, introduced as part of this work. Multi-patch train- ing
makes it possible to effectively learn spatial priors from scenes. The proposed
approach yields state-of-the-art per- formance on four scene parsing datasets,
namely Stanford Background, SIFT Flow, CamVid, and KITTI. In addition, our
system has the added advantage of having a training system that can be
completely automated end-to-end with- out requiring any post-processing.