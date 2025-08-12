---
layout: publication
title: Attention-aware Multi-stroke Style Transfer
authors: Yuan Yao, Jianqiang Ren, Xuansong Xie, Weidong Liu, Yong-Jin Liu, Jun Wang
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: yao2019attention
citations: 166
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.05127'}]
tags: ["CVPR"]
short_authors: Yao et al.
---
Neural style transfer has drawn considerable attention from both academic and
industrial field. Although visual effect and efficiency have been significantly
improved, existing methods are unable to coordinate spatial distribution of
visual attention between the content image and stylized image, or render
diverse level of detail via different brush strokes. In this paper, we tackle
these limitations by developing an attention-aware multi-stroke style transfer
model. We first propose to assemble self-attention mechanism into a
style-agnostic reconstruction autoencoder framework, from which the attention
map of a content image can be derived. By performing multi-scale style swap on
content features and style features, we produce multiple feature maps
reflecting different stroke patterns. A flexible fusion strategy is further
presented to incorporate the salient characteristics from the attention map,
which allows integrating multiple stroke patterns into different spatial
regions of the output image harmoniously. We demonstrate the effectiveness of
our method, as well as generate comparable stylized images with multiple stroke
patterns against the state-of-the-art methods.