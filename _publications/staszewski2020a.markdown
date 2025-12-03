---
layout: publication
title: A New Approach To Descriptors Generation For Image Retrieval By Analyzing Activations
  Of Deep Neural Network Layers
authors: "Pawe\u0142 Staszewski, MacIej Jaworski, Jinde Cao, Leszek Rutkowski"
conference: Arxiv
year: 2020
bibkey: staszewski2020a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.06624'}]
tags: ["Datasets", "Image Retrieval"]
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