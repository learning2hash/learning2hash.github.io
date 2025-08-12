---
layout: publication
title: 'Densenet: Implementing Efficient Convnet Descriptor Pyramids'
authors: Forrest Iandola, Matt Moskewicz, Sergey Karayev, Ross Girshick, Trevor Darrell,
  Kurt Keutzer
conference: Arxiv
year: 2014
bibkey: iandola2014densenet
citations: 615
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1404.1869'}]
tags: ["Efficiency"]
short_authors: Iandola et al.
---
Convolutional Neural Networks (CNNs) can provide accurate object
classification. They can be extended to perform object detection by iterating
over dense or selected proposed object regions. However, the runtime of such
detectors scales as the total number and/or area of regions to examine per
image, and training such detectors may be prohibitively slow. However, for some
CNN classifier topologies, it is possible to share significant work among
overlapping regions to be classified. This paper presents DenseNet, an open
source system that computes dense, multiscale features from the convolutional
layers of a CNN based object classifier. Future work will involve training
efficient object detectors with DenseNet feature descriptors.