---
layout: publication
title: Sample Efficient Semantic Segmentation Using Rotation Equivariant Convolutional
  Networks
authors: Jasper Linmans, Jim Winkens, Bastiaan S. Veeling, Taco S. Cohen, Max Welling
conference: Arxiv
year: 2018
bibkey: linmans2018sample
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.00583'}]
tags: ["Efficiency"]
short_authors: Linmans et al.
---
We propose a semantic segmentation model that exploits rotation and
reflection symmetries. We demonstrate significant gains in sample efficiency
due to increased weight sharing, as well as improvements in robustness to
symmetry transformations. The group equivariant CNN framework is extended for
segmentation by introducing a new equivariant (G->Z2)-convolution that
transforms feature maps on a group to planar feature maps. Also, equivariant
transposed convolution is formulated for up-sampling in an encoder-decoder
network. To demonstrate improvements in sample efficiency we evaluate on
multiple data regimes of a rotation-equivariant segmentation task: cancer
metastases detection in histopathology images. We further show the
effectiveness of exploiting more symmetries by varying the size of the group.