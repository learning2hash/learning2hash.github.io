---
layout: publication
title: 'Transposer: Universal Texture Synthesis Using Feature Maps As Transposed Convolution
  Filter'
authors: Guilin Liu, Rohan Taori, Ting-Chun Wang, Zhiding Yu, Shiqiu Liu, Fitsum A.
  Reda, Karan Sapra, Andrew Tao, Bryan Catanzaro
conference: Arxiv
year: 2020
bibkey: liu2020transposer
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.07243'}]
tags: []
short_authors: Liu et al.
---
Conventional CNNs for texture synthesis consist of a sequence of
(de)-convolution and up/down-sampling layers, where each layer operates locally
and lacks the ability to capture the long-term structural dependency required
by texture synthesis. Thus, they often simply enlarge the input texture, rather
than perform reasonable synthesis. As a compromise, many recent methods
sacrifice generalizability by training and testing on the same single (or fixed
set of) texture image(s), resulting in huge re-training time costs for unseen
images. In this work, based on the discovery that the assembling/stitching
operation in traditional texture synthesis is analogous to a transposed
convolution operation, we propose a novel way of using transposed convolution
operation. Specifically, we directly treat the whole encoded feature map of the
input texture as transposed convolution filters and the features'
self-similarity map, which captures the auto-correlation information, as input
to the transposed convolution. Such a design allows our framework, once
trained, to be generalizable to perform synthesis of unseen textures with a
single forward pass in nearly real-time. Our method achieves state-of-the-art
texture synthesis quality based on various metrics. While self-similarity helps
preserve the input textures' regular structural patterns, our framework can
also take random noise maps for irregular input textures instead of
self-similarity maps as transposed convolution inputs. It allows to get more
diverse results as well as generate arbitrarily large texture outputs by
directly sampling large noise maps in a single pass as well.