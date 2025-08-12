---
layout: publication
title: Cross-convolutional-layer Pooling For Image Recognition
authors: Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2016
bibkey: liu2015cross
citations: 89
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1510.00921'}]
tags: []
short_authors: Lingqiao Liu, Chunhua Shen, Anton van Den Hengel
---
Recent studies have shown that a Deep Convolutional Neural Network (DCNN)
pretrained on a large image dataset can be used as a universal image
descriptor, and that doing so leads to impressive performance for a variety of
image classification tasks. Most of these studies adopt activations from a
single DCNN layer, usually the fully-connected layer, as the image
representation. In this paper, we proposed a novel way to extract image
representations from two consecutive convolutional layers: one layer is
utilized for local feature extraction and the other serves as guidance to pool
the extracted features. By taking different viewpoints of convolutional layers,
we further develop two schemes to realize this idea. The first one directly
uses convolutional layers from a DCNN. The second one applies the pretrained
CNN on densely sampled image regions and treats the fully-connected activations
of each image region as convolutional feature activations. We then train
another convolutional layer on top of that as the pooling-guidance
convolutional layer. By applying our method to three popular visual
classification tasks, we find our first scheme tends to perform better on the
applications which need strong discrimination on subtle object patterns within
small regions while the latter excels in the cases that require discrimination
on category-level patterns. Overall, the proposed method achieves superior
performance over existing ways of extracting image representations from a DCNN.