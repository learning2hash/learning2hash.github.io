---
layout: publication
title: Fracking Deep Convolutional Image Descriptors
authors: Edgar Simo-serra, Eduard Trulls, Luis Ferraz, Iasonas Kokkinos, Francesc
  Moreno-noguer
conference: Arxiv
year: 2014
bibkey: simoserra2014fracking
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.6537'}]
tags: []
short_authors: Simo-serra et al.
---
In this paper we propose a novel framework for learning local image
descriptors in a discriminative manner. For this purpose we explore a siamese
architecture of Deep Convolutional Neural Networks (CNN), with a Hinge
embedding loss on the L2 distance between descriptors. Since a siamese
architecture uses pairs rather than single image patches to train, there exist
a large number of positive samples and an exponential number of negative
samples. We propose to explore this space with a stochastic sampling of the
training set, in combination with an aggressive mining strategy over both the
positive and negative samples which we denote as "fracking". We perform a
thorough evaluation of the architecture hyper-parameters, and demonstrate large
performance gains compared to both standard CNN learning strategies,
hand-crafted image descriptors like SIFT, and the state-of-the-art on learned
descriptors: up to 2.5x vs SIFT and 1.5x vs the state-of-the-art in terms of
the area under the curve (AUC) of the Precision-Recall curve.