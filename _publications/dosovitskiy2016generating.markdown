---
layout: publication
title: Generating Images With Perceptual Similarity Metrics Based On Deep Networks
authors: Alexey Dosovitskiy, Thomas Brox
conference: Arxiv
year: 2016
bibkey: dosovitskiy2016generating
citations: 690
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.02644'}]
tags: ["Distance Metric Learning"]
short_authors: Alexey Dosovitskiy, Thomas Brox
---
Image-generating machine learning models are typically trained with loss
functions based on distance in the image space. This often leads to
over-smoothed results. We propose a class of loss functions, which we call deep
perceptual similarity metrics (DeePSiM), that mitigate this problem. Instead of
computing distances in the image space, we compute distances between image
features extracted by deep neural networks. This metric better reflects
perceptually similarity of images and thus leads to better results. We show
three applications: autoencoder training, a modification of a variational
autoencoder, and inversion of deep convolutional networks. In all cases, the
generated images look sharp and resemble natural images.