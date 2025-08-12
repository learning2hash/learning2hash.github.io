---
layout: publication
title: 'Cuts3d: Cutting Semantics In 3D For 2D Unsupervised Instance Segmentation'
authors: Leon Sick, Dominik Engel, Sebastian Hartwig, Pedro Hermosilla, Timo Ropinski
conference: Arxiv
year: 2024
bibkey: sick2024cuts3d
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.16319'}]
tags: ["Unsupervised"]
short_authors: Sick et al.
---
Traditionally, algorithms that learn to segment object instances in 2D images
have heavily relied on large amounts of human-annotated data. Only recently,
novel approaches have emerged tackling this problem in an unsupervised fashion.
Generally, these approaches first generate pseudo-masks and then train a
class-agnostic detector. While such methods deliver the current state of the
art, they often fail to correctly separate instances overlapping in 2D image
space since only semantics are considered. To tackle this issue, we instead
propose to cut the semantic masks in 3D to obtain the final 2D instances by
utilizing a point cloud representation of the scene. Furthermore, we derive a
Spatial Importance function, which we use to resharpen the semantics along the
3D borders of instances. Nevertheless, these pseudo-masks are still subject to
mask ambiguity. To address this issue, we further propose to augment the
training of a class-agnostic detector with three Spatial Confidence components
aiming to isolate a clean learning signal. With these contributions, our
approach outperforms competing methods across multiple standard benchmarks for
unsupervised instance segmentation and object detection.