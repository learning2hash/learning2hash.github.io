---
layout: publication
title: 'Patch-drosonet: Classifying Image Partitions With Fly-inspired Models For
  Lightweight Visual Place Recognition'
authors: Bruno Arcanjo, Bruno Ferrarini, Michael Milford, Klaus D. McDonald-Maier,
  Shoaib Ehsan
conference: Arxiv
year: 2023
bibkey: arcanjo2023patch
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05256'}]
tags: []
short_authors: Arcanjo et al.
---
Visual place recognition (VPR) enables autonomous systems to localize
themselves within an environment using image information. While Convolution
Neural Networks (CNNs) currently dominate state-of-the-art VPR performance,
their high computational requirements make them unsuitable for platforms with
budget or size constraints. This has spurred the development of lightweight
algorithms, such as DrosoNet, which employs a voting system based on multiple
bio-inspired units. In this paper, we present a novel training approach for
DrosoNet, wherein separate models are trained on distinct regions of a
reference image, allowing them to specialize in the visual features of that
specific section. Additionally, we introduce a convolutional-like prediction
method, in which each DrosoNet unit generates a set of place predictions for
each portion of the query image. These predictions are then combined using the
previously introduced voting system. Our approach significantly improves upon
the VPR performance of previous work while maintaining an extremely compact and
lightweight algorithm, making it suitable for resource-constrained platforms.