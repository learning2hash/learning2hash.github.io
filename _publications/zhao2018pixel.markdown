---
layout: publication
title: Pixel-level Semantics Guided Image Colorization
authors: Jiaojiao Zhao, Li Liu, Cees G. M. Snoek, Jungong Han, Ling Shao
conference: Arxiv
year: 2018
bibkey: zhao2018pixel
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01597'}]
tags: ["Image Retrieval"]
short_authors: Zhao et al.
---
While many image colorization algorithms have recently shown the capability
of producing plausible color versions from gray-scale photographs, they still
suffer from the problems of context confusion and edge color bleeding. To
address context confusion, we propose to incorporate the pixel-level object
semantics to guide the image colorization. The rationale is that human beings
perceive and distinguish colors based on the object's semantic categories. We
propose a hierarchical neural network with two branches. One branch learns what
the object is while the other branch learns the object's colors. The network
jointly optimizes a semantic segmentation loss and a colorization loss. To
attack edge color bleeding we generate more continuous color maps with sharp
edges by adopting a joint bilateral upsamping layer at inference. Our network
is trained on PASCAL VOC2012 and COCO-stuff with semantic segmentation labels
and it produces more realistic and finer results compared to the colorization
state-of-the-art.