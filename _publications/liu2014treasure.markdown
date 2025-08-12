---
layout: publication
title: 'The Treasure Beneath Convolutional Layers: Cross-convolutional-layer Pooling
  For Image Classification'
authors: Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: liu2014treasure
citations: 177
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1411.7466'}]
tags: ["CVPR"]
short_authors: Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
---
A number of recent studies have shown that a Deep Convolutional Neural
Network (DCNN) pretrained on a large dataset can be adopted as a universal
image description which leads to astounding performance in many visual
classification tasks. Most of these studies, if not all, adopt activations of
the fully-connected layer of a DCNN as the image or region representation and
it is believed that convolutional layer activations are less discriminative.
  This paper, however, advocates that if used appropriately convolutional layer
activations can be turned into a powerful image representation which enjoys
many advantages over fully-connected layer activations. This is achieved by
adopting a new technique proposed in this paper called
cross-convolutional-layer pooling. More specifically, it extracts subarrays of
feature maps of one convolutional layer as local features and pools the
extracted features with the guidance of feature maps of the successive
convolutional layer. Compared with exising methods that apply DCNNs in the
local feature setting, the proposed method is significantly faster since it
requires much fewer times of DCNN forward computation. Moreover, it avoids the
domain mismatch issue which is usually encountered when applying fully
connected layer activations to describe local regions. By applying our method
to four popular visual classification tasks, it is demonstrated that the
proposed method can achieve comparable or in some cases significantly better
performance than existing fully-connected layer based image representations
while incurring much lower computational cost.