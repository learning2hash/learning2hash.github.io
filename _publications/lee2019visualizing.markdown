---
layout: publication
title: Visualizing Image Content To Explain Novel Image Discovery
authors: Jake H. Lee, Kiri L. Wagstaff
conference: Data Mining and Knowledge Discovery
year: 2020
bibkey: lee2019visualizing
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05006'}]
tags: ["Image Retrieval", "KDD"]
short_authors: Jake H. Lee, Kiri L. Wagstaff
---
The initial analysis of any large data set can be divided into two phases:
(1) the identification of common trends or patterns and (2) the identification
of anomalies or outliers that deviate from those trends. We focus on the goal
of detecting observations with novel content, which can alert us to artifacts
in the data set or, potentially, the discovery of previously unknown phenomena.
To aid in interpreting and diagnosing the novel aspect of these selected
observations, we recommend the use of novelty detection methods that generate
explanations. In the context of large image data sets, these explanations
should highlight what aspect of a given image is new (color, shape, texture,
content) in a human-comprehensible form. We propose DEMUD-VIS, the first method
for providing visual explanations of novel image content by employing a
convolutional neural network (CNN) to extract image features, a method that
uses reconstruction error to detect novel content, and an up-convolutional
network to convert CNN feature representations back into image space. We
demonstrate this approach on diverse images from ImageNet, freshwater streams,
and the surface of Mars.