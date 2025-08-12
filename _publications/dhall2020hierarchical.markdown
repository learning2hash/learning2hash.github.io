---
layout: publication
title: Hierarchical Image Classification Using Entailment Cone Embeddings
authors: Ankit Dhall, Anastasia Makarova, Octavian Ganea, Dario Pavllo, Michael Greeff,
  Andreas Krause
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: dhall2020hierarchical
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.03459'}]
tags: ["CVPR"]
short_authors: Dhall et al.
---
Image classification has been studied extensively, but there has been limited
work in using unconventional, external guidance other than traditional
image-label pairs for training. We present a set of methods for leveraging
information about the semantic hierarchy embedded in class labels. We first
inject label-hierarchy knowledge into an arbitrary CNN-based classifier and
empirically show that availability of such external semantic information in
conjunction with the visual semantics from images boosts overall performance.
Taking a step further in this direction, we model more explicitly the
label-label and label-image interactions using order-preserving embeddings
governed by both Euclidean and hyperbolic geometries, prevalent in natural
language, and tailor them to hierarchical image classification and
representation learning. We empirically validate all the models on the
hierarchical ETHEC dataset.