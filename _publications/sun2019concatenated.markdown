---
layout: publication
title: Concatenated Feature Pyramid Network For Instance Segmentation
authors: Yongqing Sun, Pranav Shenoy K P, Jun Shimamura, Atsushi Sagata
conference: 2019 IEEE Fifth International Conference on Multimedia Big Data (BigMM)
year: 2019
bibkey: sun2019concatenated
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.00768'}]
tags: []
short_authors: Sun et al.
---
Low level features like edges and textures play an important role in
accurately localizing instances in neural networks. In this paper, we propose
an architecture which improves feature pyramid networks commonly used instance
segmentation networks by incorporating low level features in all layers of the
pyramid in an optimal and efficient way. Specifically, we introduce a new layer
which learns new correlations from feature maps of multiple feature pyramid
levels holistically and enhances the semantic information of the feature
pyramid to improve accuracy. Our architecture is simple to implement in
instance segmentation or object detection frameworks to boost accuracy. Using
this method in Mask RCNN, our model achieves consistent improvement in
precision on COCO Dataset with the computational overhead compared to the
original feature pyramid network.