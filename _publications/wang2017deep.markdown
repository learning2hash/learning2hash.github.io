---
layout: publication
title: Deep Collaborative Learning For Visual Recognition
authors: Yan Wang, Lingxi Xie, Ya Zhang, Wenjun Zhang, Alan Yuille
conference: Arxiv
year: 2017
bibkey: wang2017deep
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.01229'}]
tags: [Datasets]
short_authors: Wang et al.
---
Deep neural networks are playing an important role in state-of-the-art visual
recognition. To represent high-level visual concepts, modern networks are
equipped with large convolutional layers, which use a large number of filters
and contribute significantly to model complexity. For example, more than half
of the weights of AlexNet are stored in the first fully-connected layer (4,096
filters).
  We formulate the function of a convolutional layer as learning a large visual
vocabulary, and propose an alternative way, namely Deep Collaborative Learning
(DCL), to reduce the computational complexity. We replace a convolutional layer
with a two-stage DCL module, in which we first construct a couple of smaller
convolutional layers individually, and then fuse them at each spatial position
to consider feature co-occurrence. In mathematics, DCL can be explained as an
efficient way of learning compositional visual concepts, in which the
vocabulary size increases exponentially while the model complexity only
increases linearly. We evaluate DCL on a wide range of visual recognition
tasks, including a series of multi-digit number classification datasets, and
some generic image classification datasets such as SVHN, CIFAR and ILSVRC2012.
We apply DCL to several state-of-the-art network structures, improving the
recognition accuracy meanwhile reducing the number of parameters (16.82% fewer
in AlexNet).