---
layout: publication
title: Image Completion On CIFAR-10
authors: Mason Swofford
conference: Arxiv
year: 2018
bibkey: swofford2018image
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.03213'}]
tags: ["Datasets"]
short_authors: Mason Swofford
---
This project performed image completion on CIFAR-10, a dataset of 60,000
32x32 RGB images, using three different neural network architectures: fully
convolutional networks, convolutional networks with fully connected layers, and
encoder-decoder convolutional networks. The highest performing model was a deep
fully convolutional network, which was able to achieve a mean squared error of
.015 when comparing the original image pixel values with the predicted pixel
values. As well, this network was able to output in-painted images which
appeared real to the human eye.