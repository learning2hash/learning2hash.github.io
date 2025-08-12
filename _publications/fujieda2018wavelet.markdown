---
layout: publication
title: Wavelet Convolutional Neural Networks
authors: Shin Fujieda, Kohei Takayama, Toshiya Hachisuka
conference: Arxiv
year: 2018
bibkey: fujieda2018wavelet
citations: 100
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.08620'}]
tags: []
short_authors: Shin Fujieda, Kohei Takayama, Toshiya Hachisuka
---
Spatial and spectral approaches are two major approaches for image processing
tasks such as image classification and object recognition. Among many such
algorithms, convolutional neural networks (CNNs) have recently achieved
significant performance improvement in many challenging tasks. Since CNNs
process images directly in the spatial domain, they are essentially spatial
approaches. Given that spatial and spectral approaches are known to have
different characteristics, it will be interesting to incorporate a spectral
approach into CNNs. We propose a novel CNN architecture, wavelet CNNs, which
combines a multiresolution analysis and CNNs into one model. Our insight is
that a CNN can be viewed as a limited form of a multiresolution analysis. Based
on this insight, we supplement missing parts of the multiresolution analysis
via wavelet transform and integrate them as additional components in the entire
architecture. Wavelet CNNs allow us to utilize spectral information which is
mostly lost in conventional CNNs but useful in most image processing tasks. We
evaluate the practical performance of wavelet CNNs on texture classification
and image annotation. The experiments show that wavelet CNNs can achieve better
accuracy in both tasks than existing models while having significantly fewer
parameters than conventional CNNs.