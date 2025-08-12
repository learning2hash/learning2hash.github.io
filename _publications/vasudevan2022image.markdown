---
layout: publication
title: Image Classification Using Graph Neural Network And Multiscale Wavelet Superpixels
authors: Varun Vasudevan, Maxime Bassenne, Md Tauhidul Islam, Lei Xing
conference: Pattern Recognition Letters
year: 2023
bibkey: vasudevan2022image
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.12633'}]
tags: []
short_authors: Vasudevan et al.
---
Prior studies using graph neural networks (GNNs) for image classification
have focused on graphs generated from a regular grid of pixels or similar-sized
superpixels. In the latter, a single target number of superpixels is defined
for an entire dataset irrespective of differences across images and their
intrinsic multiscale structure. On the contrary, this study investigates image
classification using graphs generated from an image-specific number of
multiscale superpixels. We propose WaveMesh, a new wavelet-based superpixeling
algorithm, where the number and sizes of superpixels in an image are
systematically computed based on its content. WaveMesh superpixel graphs are
structurally different from similar-sized superpixel graphs. We use SplineCNN,
a state-of-the-art network for image graph classification, to compare WaveMesh
and similar-sized superpixels. Using SplineCNN, we perform extensive
experiments on three benchmark datasets under three local-pooling settings: 1)
no pooling, 2) GraclusPool, and 3) WavePool, a novel spatially heterogeneous
pooling scheme tailored to WaveMesh superpixels. Our experiments demonstrate
that SplineCNN learns from multiscale WaveMesh superpixels on-par with
similar-sized superpixels. In all WaveMesh experiments, GraclusPool performs
poorer than no pooling / WavePool, indicating that poor choice of pooling can
result in inferior performance while learning from multiscale superpixels.