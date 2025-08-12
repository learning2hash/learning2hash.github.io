---
layout: publication
title: Training Of Convolutional Networks On Multiple Heterogeneous Datasets For Street
  Scene Semantic Segmentation
authors: Panagiotis Meletis, Gijs Dubbelman
conference: 2018 IEEE Intelligent Vehicles Symposium (IV)
year: 2018
bibkey: meletis2018training
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.05675'}]
tags: ["Datasets"]
short_authors: Panagiotis Meletis, Gijs Dubbelman
---
We propose a convolutional network with hierarchical classifiers for
per-pixel semantic segmentation, which is able to be trained on multiple,
heterogeneous datasets and exploit their semantic hierarchy. Our network is the
first to be simultaneously trained on three different datasets from the
intelligent vehicles domain, i.e. Cityscapes, GTSDB and Mapillary Vistas, and
is able to handle different semantic level-of-detail, class imbalances, and
different annotation types, i.e. dense per-pixel and sparse bounding-box
labels. We assess our hierarchical approach, by comparing against flat,
non-hierarchical classifiers and we show improvements in mean pixel accuracy of
13.0% for Cityscapes classes and 2.4% for Vistas classes and 32.3% for GTSDB
classes. Our implementation achieves inference rates of 17 fps at a resolution
of 520x706 for 108 classes running on a GPU.