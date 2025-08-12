---
layout: publication
title: 'Cut-thumbnail: A Novel Data Augmentation For Convolutional Neural Network'
authors: Tianshu Xie, Xuan Cheng, Minghui Liu, Jiali Deng, Xiaomin Wang, Ming Liu
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: xie2021cut
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.05342'}]
tags: []
short_authors: Xie et al.
---
In this paper, we propose a novel data augmentation strategy named
Cut-Thumbnail, that aims to improve the shape bias of the network. We reduce an
image to a certain size and replace the random region of the original image
with the reduced image. The generated image not only retains most of the
original image information but also has global information in the reduced
image. We call the reduced image as thumbnail. Furthermore, we find that the
idea of thumbnail can be perfectly integrated with Mixed Sample Data
Augmentation, so we put one image's thumbnail on another image while the ground
truth labels are also mixed, making great achievements on various computer
vision tasks. Extensive experiments show that Cut-Thumbnail works better than
state-of-the-art augmentation strategies across classification, fine-grained
image classification, and object detection. On ImageNet classification,
ResNet-50 architecture with our method achieves 79.21% accuracy, which is more
than 2.8% improvement on the baseline.