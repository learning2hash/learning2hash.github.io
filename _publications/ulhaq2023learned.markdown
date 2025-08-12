---
layout: publication
title: Learned Point Cloud Compression For Classification
authors: "Mateen Ulhaq, Ivan V. Baji\u0107"
conference: 2023 IEEE 25th International Workshop on Multimedia Signal Processing
  (MMSP)
year: 2023
bibkey: ulhaq2023learned
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.05959'}]
tags: []
short_authors: "Mateen Ulhaq, Ivan V. Baji\u0107"
---
Deep learning is increasingly being used to perform machine vision tasks such
as classification, object detection, and segmentation on 3D point cloud data.
However, deep learning inference is computationally expensive. The limited
computational capabilities of end devices thus necessitate a codec for
transmitting point cloud data over the network for server-side processing. Such
a codec must be lightweight and capable of achieving high compression ratios
without sacrificing accuracy. Motivated by this, we present a novel point cloud
codec that is highly specialized for the machine task of classification. Our
codec, based on PointNet, achieves a significantly better rate-accuracy
trade-off in comparison to alternative methods. In particular, it achieves a
94% reduction in BD-bitrate over non-specialized codecs on the ModelNet40
dataset. For low-resource end devices, we also propose two lightweight
configurations of our encoder that achieve similar BD-bitrate reductions of 93%
and 92% with 3% and 5% drops in top-1 accuracy, while consuming only 0.470 and
0.048 encoder-side kMACs/point, respectively. Our codec demonstrates the
potential of specialized codecs for machine analysis of point clouds, and
provides a basis for extension to more complex tasks and datasets in the
future.