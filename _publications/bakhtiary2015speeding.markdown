---
layout: publication
title: Speeding Up Neural Networks For Large Scale Classification Using WTA Hashing
authors: Amir H. Bakhtiary, Agata Lapedriza, David Masip
conference: Arxiv
year: 2015
citations: 2
bibkey: bakhtiary2015speeding
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1504.07488'}]
tags: [Hashing Methods]
---
In this paper we propose to use the Winner Takes All hashing technique to
speed up forward propagation and backward propagation in fully connected layers
in convolutional neural networks. The proposed technique reduces significantly
the computational complexity, which in turn, allows us to train layers with a
large number of kernels with out the associated time penalty.
  As a consequence we are able to train convolutional neural network on a very
large number of output classes with only a small increase in the computational
cost. To show the effectiveness of the technique we train a new output layer on
a pretrained network using both the regular multiplicative approach and our
proposed hashing methodology. Our results showed no drop in performance and
demonstrate, with our implementation, a 7 fold speed up during the training.