---
layout: publication
title: Compressing Deep Cnns Using Basis Representation And Spectral Fine-tuning
authors: Muhammad Tayyab, Fahad Ahmad Khan, Abhijit Mahalanobis
conference: 2021 IEEE International Conference on Image Processing (ICIP)
year: 2021
bibkey: tayyab2021compressing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.10436'}]
tags: []
short_authors: Muhammad Tayyab, Fahad Ahmad Khan, Abhijit Mahalanobis
---
We propose an efficient and straightforward method for compressing deep
convolutional neural networks (CNNs) that uses basis filters to represent the
convolutional layers, and optimizes the performance of the compressed network
directly in the basis space. Specifically, any spatial convolution layer of the
CNN can be replaced by two successive convolution layers: the first is a set of
three-dimensional orthonormal basis filters, followed by a layer of
one-dimensional filters that represents the original spatial filters in the
basis space. We jointly fine-tune both the basis and the filter representation
to directly mitigate any performance loss due to the truncation. Generality of
the proposed approach is demonstrated by applying it to several well known deep
CNN architectures and data sets for image classification and object detection.
We also present the execution time and power usage at different compression
levels on the Xavier Jetson AGX processor.