---
layout: publication
title: On-sensor Binarized Fully Convolutional Neural Network With A Pixel Processor
  Array
authors: Yanan Liu, Laurie Bose, Yao Lu, Piotr Dudek, Walterio Mayol-Cuevas
conference: Arxiv
year: 2022
bibkey: liu2022sensor
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.00836'}]
tags: []
short_authors: Liu et al.
---
This work presents a method to implement fully convolutional neural networks
(FCNs) on Pixel Processor Array (PPA) sensors, and demonstrates coarse
segmentation and object localisation tasks. We design and train binarized FCN
for both binary weights and activations using batchnorm, group convolution, and
learnable threshold for binarization, producing networks small enough to be
embedded on the focal plane of the PPA, with limited local memory resources,
and using parallel elementary add/subtract, shifting, and bit operations only.
We demonstrate the first implementation of an FCN on a PPA device, performing
three convolution layers entirely in the pixel-level processors. We use this
architecture to demonstrate inference generating heat maps for object
segmentation and localisation at over 280 FPS using the SCAMP-5 PPA vision
chip.