---
layout: publication
title: A Survey On Deep Hashing For Image Retrieval
authors: Zhang Xiaopeng
conference: "Arxiv"
year: 2020
bibkey: zhang2020survey
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2006.05627"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised', 'Survey Paper']
---
Hashing has been widely used in approximate nearest search for large-scale database retrieval for its computation and storage efficiency. Deep hashing which devises convolutional neural network architecture to exploit and extract the semantic information or feature of images has received increasing attention recently. In this survey several deep supervised hashing methods for image retrieval are evaluated and I conclude three main different directions for deep supervised hashing methods. Several comments are made at the end. Moreover to break through the bottleneck of the existing hashing methods I propose a Shadow Recurrent Hashing(SRH) method as a try. Specifically I devise a CNN architecture to extract the semantic features of images and design a loss function to encourage similar images projected close. To this end I propose a concept shadow of the CNN output. During optimization process the CNN output and its shadow are guiding each other so as to achieve the optimal solution as much as possible. Several experiments on dataset CIFAR-10 show the satisfying performance of SRH.
