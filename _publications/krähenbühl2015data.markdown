---
layout: publication
title: Data-dependent Initializations Of Convolutional Neural Networks
authors: "Philipp Kr\xE4henb\xFChl, Carl Doersch, Jeff Donahue, Trevor Darrell"
conference: Arxiv
year: 2015
bibkey: "kr\xE4henb\xFChl2015data"
citations: 124
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.06856'}]
tags: []
short_authors: "Kr\xE4henb\xFChl et al."
---
Convolutional Neural Networks spread through computer vision like a wildfire,
impacting almost all visual tasks imaginable. Despite this, few researchers
dare to train their models from scratch. Most work builds on one of a handful
of ImageNet pre-trained models, and fine-tunes or adapts these for specific
tasks. This is in large part due to the difficulty of properly initializing
these networks from scratch. A small miscalibration of the initial weights
leads to vanishing or exploding gradients, as well as poor convergence
properties. In this work we present a fast and simple data-dependent
initialization procedure, that sets the weights of a network such that all
units in the network train at roughly the same rate, avoiding vanishing or
exploding gradients. Our initialization matches the current state-of-the-art
unsupervised or self-supervised pre-training methods on standard computer
vision tasks, such as image classification and object detection, while being
roughly three orders of magnitude faster. When combined with pre-training
methods, our initialization significantly outperforms prior work, narrowing the
gap between supervised and unsupervised pre-training.