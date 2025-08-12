---
layout: publication
title: Learning Stixel-based Instance Segmentation
authors: Monty Santarossa, Lukas Schneider, Claudius Zelenka, Lars Schmarje, Reinhard
  Koch, Uwe Franke
conference: Arxiv
year: 2021
bibkey: santarossa2021learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.03070'}]
tags: []
short_authors: Santarossa et al.
---
Stixels have been successfully applied to a wide range of vision tasks in
autonomous driving, recently including instance segmentation. However, due to
their sparse occurrence in the image, until now Stixels seldomly served as
input for Deep Learning algorithms, restricting their utility for such
approaches. In this work we present StixelPointNet, a novel method to perform
fast instance segmentation directly on Stixels. By regarding the Stixel
representation as unstructured data similar to point clouds, architectures like
PointNet are able to learn features from Stixels. We use a bounding box
detector to propose candidate instances, for which the relevant Stixels are
extracted from the input image. On these Stixels, a PointNet models learns
binary segmentations, which we then unify throughout the whole image in a final
selection step. StixelPointNet achieves state-of-the-art performance on
Stixel-level, is considerably faster than pixel-based segmentation methods, and
shows that with our approach the Stixel domain can be introduced to many new 3D
Deep Learning tasks.