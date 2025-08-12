---
layout: publication
title: Instance Segmentation By Jointly Optimizing Spatial Embeddings And Clustering
  Bandwidth
authors: Davy Neven, Bert de Brabandere, Marc Proesmans, Luc van Gool
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: neven2019instance
citations: 263
additional_links: [{name: Code, url: 'https://github.com/davyneven/SpatialEmbeddings'},
  {name: Paper, url: 'https://arxiv.org/abs/1906.11109'}]
tags: ["CVPR"]
short_authors: Neven et al.
---
Current state-of-the-art instance segmentation methods are not suited for
real-time applications like autonomous driving, which require fast execution
times at high accuracy. Although the currently dominant proposal-based methods
have high accuracy, they are slow and generate masks at a fixed and low
resolution. Proposal-free methods, by contrast, can generate masks at high
resolution and are often faster, but fail to reach the same accuracy as the
proposal-based methods. In this work we propose a new clustering loss function
for proposal-free instance segmentation. The loss function pulls the spatial
embeddings of pixels belonging to the same instance together and jointly learns
an instance-specific clustering bandwidth, maximizing the
intersection-over-union of the resulting instance mask. When combined with a
fast architecture, the network can perform instance segmentation in real-time
while maintaining a high accuracy. We evaluate our method on the challenging
Cityscapes benchmark and achieve top results (5% improvement over Mask R-CNN)
at more than 10 fps on 2MP images. Code will be available at
https://github.com/davyneven/SpatialEmbeddings .