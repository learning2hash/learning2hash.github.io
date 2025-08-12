---
layout: publication
title: Detecting Recolored Image By Spatial Correlation
authors: Yushu Zhang, Nuo Chen, Shuren Qi, Mingfu Xue, Xiaochun Cao
conference: Arxiv
year: 2022
bibkey: zhang2022detecting
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.10973'}]
tags: []
short_authors: Zhang et al.
---
Image forensics, aiming to ensure the authenticity of the image, has made
great progress in dealing with common image manipulation such as copy-move,
splicing, and inpainting in the past decades. However, only a few researchers
pay attention to an emerging editing technique called image recoloring, which
can manipulate the color values of an image to give it a new style. To prevent
it from being used maliciously, the previous approaches address the
conventional recoloring from the perspective of inter-channel correlation and
illumination consistency. In this paper, we try to explore a solution from the
perspective of the spatial correlation, which exhibits the generic detection
capability for both conventional and deep learning-based recoloring. Through
theoretical and numerical analysis, we find that the recoloring operation will
inevitably destroy the spatial correlation between pixels, implying a new prior
of statistical discriminability. Based on such fact, we generate a set of
spatial correlation features and learn the informative representation from the
set via a convolutional neural network. To train our network, we use three
recoloring methods to generate a large-scale and high-quality data set.
Extensive experimental results in two recoloring scenes demonstrate that the
spatial correlation features are highly discriminative. Our method achieves the
state-of-the-art detection accuracy on multiple benchmark datasets and exhibits
well generalization for unknown types of recoloring methods.