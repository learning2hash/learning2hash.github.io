---
layout: publication
title: 'Multimodal Transfer: A Hierarchical Deep Convolutional Neural Network For
  Fast Artistic Style Transfer'
authors: Xin Wang, Geoffrey Oxholm, da Zhang, Yuan-fang Wang
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: wang2016multimodal
citations: 174
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.01895'}]
tags: ["CVPR"]
short_authors: Wang et al.
---
Transferring artistic styles onto everyday photographs has become an
extremely popular task in both academia and industry. Recently, offline
training has replaced on-line iterative optimization, enabling nearly real-time
stylization. When those stylization networks are applied directly to
high-resolution images, however, the style of localized regions often appears
less similar to the desired artistic style. This is because the transfer
process fails to capture small, intricate textures and maintain correct texture
scales of the artworks. Here we propose a multimodal convolutional neural
network that takes into consideration faithful representations of both color
and luminance channels, and performs stylization hierarchically with multiple
losses of increasing scales. Compared to state-of-the-art networks, our network
can also perform style transfer in nearly real-time by conducting much more
sophisticated training offline. By properly handling style and texture cues at
multiple scales using several modalities, we can transfer not just large-scale,
obvious style cues but also subtle, exquisite ones. That is, our scheme can
generate results that are visually pleasing and more similar to multiple
desired artistic styles with color and texture cues at multiple scales.