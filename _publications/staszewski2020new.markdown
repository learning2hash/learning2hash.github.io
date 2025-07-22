---
layout: publication
title: A new approach to descriptors generation for image retrieval by analyzing activations
  of deep neural network layers
authors: "Staszewski Pawe\u0142, Jaworski Maciej, Cao Jinde, Rutkowski Leszek"
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2021
bibkey: staszewski2020new
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.06624'}]
tags: ["Datasets", "Image-Retrieval"]
short_authors: Staszewski et al.
---
In this paper, we consider the problem of descriptors construction for the
task of content-based image retrieval using deep neural networks. The idea of
neural codes, based on fully connected layers activations, is extended by
incorporating the information contained in convolutional layers. It is known
that the total number of neurons in the convolutional part of the network is
large and the majority of them have little influence on the final
classification decision. Therefore, in the paper we propose a novel algorithm
that allows us to extract the most significant neuron activations and utilize
this information to construct effective descriptors. The descriptors consisting
of values taken from both the fully connected and convolutional layers
perfectly represent the whole image content. The images retrieved using these
descriptors match semantically very well to the query image, and also they are
similar in other secondary image characteristics, like background, textures or
color distribution. These features of the proposed descriptors are verified
experimentally based on the IMAGENET1M dataset using the VGG16 neural network.