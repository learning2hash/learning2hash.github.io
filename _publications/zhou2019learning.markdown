---
layout: publication
title: Learning To Reconstruct 3D Manhattan Wireframes From A Single Image
authors: Yichao Zhou, Haozhi Qi, Yuexiang Zhai, Qi Sun, Zhili Chen, Li-Yi Wei, Yi
  Ma
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: zhou2019learning
citations: 18
additional_links: [{name: Code, url: 'https://github.com/zhou13/shapeunity'}, {name: Paper,
    url: 'https://arxiv.org/abs/1905.07482'}]
tags: ["CVPR"]
short_authors: Zhou et al.
---
In this paper, we propose a method to obtain a compact and accurate 3D
wireframe representation from a single image by effectively exploiting global
structural regularities. Our method trains a convolutional neural network to
simultaneously detect salient junctions and straight lines, as well as predict
their 3D depth and vanishing points. Compared with the state-of-the-art
learning-based wireframe detection methods, our network is simpler and more
unified, leading to better 2D wireframe detection. With global structural
priors from parallelism, our method further reconstructs a full 3D wireframe
model, a compact vector representation suitable for a variety of high-level
vision tasks such as AR and CAD. We conduct extensive evaluations on a large
synthetic dataset of urban scenes as well as real images. Our code and datasets
have been made public at https://github.com/zhou13/shapeunity.