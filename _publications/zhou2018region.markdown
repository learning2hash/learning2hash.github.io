---
layout: publication
title: Region Convolutional Features For Multi-label Remote Sensing Image Retrieval
authors: Zhou Weixun, Deng Xueqing, Shao Zhenfeng
conference: International Journal of Intelligent Engineering and Systems
year: 2018
bibkey: zhou2018region
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.08634'}]
tags: [Image Retrieval]
---
Conventional remote sensing image retrieval (RSIR) systems usually perform
single-label retrieval where each image is annotated by a single label
representing the most significant semantic content of the image. This
assumption, however, ignores the complexity of remote sensing images, where an
image might have multiple classes (i.e., multiple labels), thus resulting in
worse retrieval performance. We therefore propose a novel multi-label RSIR
approach with fully convolutional networks (FCN). In our approach, we first
train a FCN model using a pixel-wise labeled dataset,and the trained FCN is
then used to predict the segmentation maps of each image in the considered
archive. We finally extract region convolutional features of each image based
on its segmentation map.The region features can be either used to perform
region-based retrieval or further post-processed to obtain a feature vector for
similarity measure. The experimental results show that our approach achieves
state-of-the-art performance in contrast to conventional single-label and
recent multi-label RSIR approaches.