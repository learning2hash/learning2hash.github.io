---
layout: publication
title: 'Stampnet: Unsupervised Multi-class Object Discovery'
authors: Joost Visser, Alessandro Corbetta, Vlado Menkovski, Federico Toschi
conference: 2019 IEEE International Conference on Image Processing (ICIP)
year: 2019
bibkey: visser2019stampnet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.02693'}]
tags: ["Unsupervised"]
short_authors: Visser et al.
---
Unsupervised object discovery in images involves uncovering recurring
patterns that define objects and discriminates them against the background.
This is more challenging than image clustering as the size and the location of
the objects are not known: this adds additional degrees of freedom and
increases the problem complexity. In this work, we propose StampNet, a novel
autoencoding neural network that localizes shapes (objects) over a simple
background in images and categorizes them simultaneously. StampNet consists of
a discrete latent space that is used to categorize objects and to determine the
location of the objects. The object categories are formed during the training,
resulting in the discovery of a fixed set of objects. We present a set of
experiments that demonstrate that StampNet is able to localize and cluster
multiple overlapping shapes with varying complexity including the digits from
the MNIST dataset. We also present an application of StampNet in the
localization of pedestrians in overhead depth-maps.