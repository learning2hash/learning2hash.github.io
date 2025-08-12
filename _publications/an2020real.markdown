---
layout: publication
title: Real-time Universal Style Transfer On High-resolution Images Via Zero-channel
  Pruning
authors: Jie An, Tao Li, Haozhi Huang, Li Shen, Xuan Wang, Yongyi Tang, Jinwen Ma,
  Wei Liu, Jiebo Luo
conference: Arxiv
year: 2020
bibkey: an2020real
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.09029'}]
tags: ["Efficiency"]
short_authors: An et al.
---
Extracting effective deep features to represent content and style information
is the key to universal style transfer. Most existing algorithms use VGG19 as
the feature extractor, which incurs a high computational cost and impedes
real-time style transfer on high-resolution images. In this work, we propose a
lightweight alternative architecture - ArtNet, which is based on GoogLeNet, and
later pruned by a novel channel pruning method named Zero-channel Pruning
specially designed for style transfer approaches. Besides, we propose a
theoretically sound sandwich swap transform (S2) module to transfer deep
features, which can create a pleasing holistic appearance and good local
textures with an improved content preservation ability. By using ArtNet and S2,
our method is 2.3 to 107.4 times faster than state-of-the-art approaches. The
comprehensive experiments demonstrate that ArtNet can achieve universal,
real-time, and high-quality style transfer on high-resolution images
simultaneously, (68.03 FPS on 512 times 512 images).