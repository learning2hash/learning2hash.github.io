---
layout: publication
title: 'Hscnet++: Hierarchical Scene Coordinate Classification And Regression For
  Visual Localization With Transformer'
authors: Shuzhe Wang, Zakaria Laskar, Iaroslav Melekhov, Xiaotian Li, Yi Zhao, Giorgos
  Tolias, Juho Kannala
conference: International Journal of Computer Vision
year: 2024
bibkey: wang2023hscnet
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03595'}]
tags: []
short_authors: Wang et al.
---
Visual localization is critical to many applications in computer vision and
robotics. To address single-image RGB localization, state-of-the-art
feature-based methods match local descriptors between a query image and a
pre-built 3D model. Recently, deep neural networks have been exploited to
regress the mapping between raw pixels and 3D coordinates in the scene, and
thus the matching is implicitly performed by the forward pass through the
network. However, in a large and ambiguous environment, learning such a
regression task directly can be difficult for a single network. In this work,
we present a new hierarchical scene coordinate network to predict pixel scene
coordinates in a coarse-to-fine manner from a single RGB image. The proposed
method, which is an extension of HSCNet, allows us to train compact models
which scale robustly to large environments. It sets a new state-of-the-art for
single-image localization on the 7-Scenes, 12 Scenes, Cambridge Landmarks
datasets, and the combined indoor scenes.