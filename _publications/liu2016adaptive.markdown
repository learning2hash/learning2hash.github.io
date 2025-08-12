---
layout: publication
title: Adaptive Deep Pyramid Matching For Remote Sensing Scene Classification
authors: Qingshan Liu, Renlong Hang, Huihui Song, Fuping Zhu, Javier Plaza, Antonio
  Plaza
conference: Arxiv
year: 2016
bibkey: liu2016adaptive
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.03589'}]
tags: ["Evaluation"]
short_authors: Liu et al.
---
Convolutional neural networks (CNNs) have attracted increasing attention in
the remote sensing community. Most CNNs only take the last fully-connected
layers as features for the classification of remotely sensed images, discarding
the other convolutional layer features which may also be helpful for
classification purposes. In this paper, we propose a new adaptive deep pyramid
matching (ADPM) model that takes advantage of the features from all of the
convolutional layers for remote sensing image classification. To this end, the
optimal fusing weights for different convolutional layers are learned from the
data itself. In remotely sensed scenes, the objects of interest exhibit
different scales in distinct scenes, and even a single scene may contain
objects with different sizes. To address this issue, we select the CNN with
spatial pyramid pooling (SPP-net) as the basic deep network, and further
construct a multi-scale ADPM model to learn complementary information from
multi-scale images. Our experiments have been conducted using two widely used
remote sensing image databases, and the results show that the proposed method
significantly improves the performance when compared to other state-of-the-art
methods.