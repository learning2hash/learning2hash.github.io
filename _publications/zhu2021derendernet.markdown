---
layout: publication
title: 'Derendernet: Intrinsic Image Decomposition Of Urban Scenes With Shape-(in)dependent
  Shading Rendering'
authors: Yongjie Zhu, Jiajun Tang, Si Li, Boxin Shi
conference: 2021 IEEE International Conference on Computational Photography (ICCP)
year: 2021
bibkey: zhu2021derendernet
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.13602'}]
tags: []
short_authors: Zhu et al.
---
We propose DeRenderNet, a deep neural network to decompose the albedo and
latent lighting, and render shape-(in)dependent shadings, given a single image
of an outdoor urban scene, trained in a self-supervised manner. To achieve this
goal, we propose to use the albedo maps extracted from scenes in videogames as
direct supervision and pre-compute the normal and shadow prior maps based on
the depth maps provided as indirect supervision. Compared with state-of-the-art
intrinsic image decomposition methods, DeRenderNet produces shadow-free albedo
maps with clean details and an accurate prediction of shadows in the
shape-independent shading, which is shown to be effective in re-rendering and
improving the accuracy of high-level vision tasks for urban scenes.