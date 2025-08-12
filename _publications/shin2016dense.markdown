---
layout: publication
title: Dense Image Representation With Spatial Pyramid VLAD Coding Of CNN For Locally
  Robust Captioning
authors: Andrew Shin, Masataka Yamaguchi, Katsunori Ohnishi, Tatsuya Harada
conference: Arxiv
year: 2016
bibkey: shin2016dense
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.09046'}]
tags: ["Compact Codes", "Hashing Methods", "Image Retrieval", "Locality Sensitive Hashing", "Quantization"]
short_authors: Shin et al.
---
The workflow of extracting features from images using convolutional neural
networks (CNN) and generating captions with recurrent neural networks (RNN) has
become a de-facto standard for image captioning task. However, since CNN
features are originally designed for classification task, it is mostly
concerned with the main conspicuous element of the image, and often fails to
correctly convey information on local, secondary elements. We propose to
incorporate coding with vector of locally aggregated descriptors (VLAD) on
spatial pyramid for CNN features of sub-regions in order to generate image
representations that better reflect the local information of the images. Our
results show that our method of compact VLAD coding can match CNN features with
as little as 3% of dimensionality and, when combined with spatial pyramid, it
results in image captions that more accurately take local elements into
account.