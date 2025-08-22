---
layout: publication
title: Finding Original Image Of A Sub Image Using Cnns
authors: Raja Asim
conference: Arxiv
year: 2018
bibkey: asim2018finding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.08078'}]
tags: ["Supervised", "Unsupervised"]
short_authors: Raja Asim
---
Convolututional Neural Networks have achieved state of the art in image
classification, object detection and other image related tasks. In this paper I
present another use of CNNs i.e. if given a set of images and then giving a
single test image the network identifies that the test image is part of which
image from the images given before. This is a task somehow similar to measuring
image similarity and can be done using a simple CNN. Doing this task manually
by looping can be quite a time consuming problem and won't be a generalizable
solution. The task is quite similar to doing object detection but for that lots
training data should be given or in the case of sliding window it takes lot of
time and my algorithm can work with much fewer examples, is totally
unsupervised and works much efficiently. Also, I explain that how unsupervised
algorithm like K-Means or supervised algorithm like K-NN are not good enough to
perform this task. The basic idea is that image encodings are collected for
each image from a CNN, when a test image comes it is replaced by a part of
original image, the encoding is generated using the same network, the frobenius
norm is calculated and if it comes under a tolerance level then the test image
is said to be the part of the original image.