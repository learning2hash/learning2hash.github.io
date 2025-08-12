---
layout: publication
title: 'Nerd: Neural Field-based Demosaicking'
authors: Tomas Kerepecky, Filip Sroubek, Adam Novozamsky, Jan Flusser
conference: 2023 IEEE International Conference on Image Processing (ICIP)
year: 2023
bibkey: kerepecky2023nerd
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.06566'}]
tags: []
short_authors: Kerepecky et al.
---
We introduce NeRD, a new demosaicking method for generating full-color images
from Bayer patterns. Our approach leverages advancements in neural fields to
perform demosaicking by representing an image as a coordinate-based neural
network with sine activation functions. The inputs to the network are spatial
coordinates and a low-resolution Bayer pattern, while the outputs are the
corresponding RGB values. An encoder network, which is a blend of ResNet and
U-net, enhances the implicit neural representation of the image to improve its
quality and ensure spatial consistency through prior learning. Our experimental
results demonstrate that NeRD outperforms traditional and state-of-the-art
CNN-based methods and significantly closes the gap to transformer-based
methods.