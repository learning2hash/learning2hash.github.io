---
layout: publication
title: Wavelet Convolutional Neural Networks For Texture Classification
authors: Shin Fujieda, Kohei Takayama, Toshiya Hachisuka
conference: Arxiv
year: 2017
bibkey: fujieda2017wavelet
citations: 95
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07394'}]
tags: []
short_authors: Shin Fujieda, Kohei Takayama, Toshiya Hachisuka
---
Texture classification is an important and challenging problem in many image
processing applications. While convolutional neural networks (CNNs) achieved
significant successes for image classification, texture classification remains
a difficult problem since textures usually do not contain enough information
regarding the shape of object. In image processing, texture classification has
been traditionally studied well with spectral analyses which exploit repeated
structures in many textures. Since CNNs process images as-is in the spatial
domain whereas spectral analyses process images in the frequency domain, these
models have different characteristics in terms of performance. We propose a
novel CNN architecture, wavelet CNNs, which integrates a spectral analysis into
CNNs. Our insight is that the pooling layer and the convolution layer can be
viewed as a limited form of a spectral analysis. Based on this insight, we
generalize both layers to perform a spectral analysis with wavelet transform.
Wavelet CNNs allow us to utilize spectral information which is lost in
conventional CNNs but useful in texture classification. The experiments
demonstrate that our model achieves better accuracy in texture classification
than existing models. We also show that our model has significantly fewer
parameters than CNNs, making our model easier to train with less memory.