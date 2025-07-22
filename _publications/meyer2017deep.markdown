---
layout: publication
title: Deep Metric Learning and Image Classification with Nearest Neighbour Gaussian
  Kernels
authors: Meyer Benjamin J., Harwood Ben, Drummond Tom
conference: 2018 25th IEEE International Conference on Image Processing (ICIP)
year: 2018
bibkey: meyer2017deep
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.09780'}]
tags: ["Similarity-Search", "Distance-Metric-Learning", "Datasets"]
short_authors: Meyer Benjamin J., Harwood Ben, Drummond Tom
---
We present a Gaussian kernel loss function and training algorithm for
convolutional neural networks that can be directly applied to both distance
metric learning and image classification problems. Our method treats all
training features from a deep neural network as Gaussian kernel centres and
computes loss by summing the influence of a feature's nearby centres in the
feature embedding space. Our approach is made scalable by treating it as an
approximate nearest neighbour search problem. We show how to make end-to-end
learning feasible, resulting in a well formed embedding space, in which
semantically related instances are likely to be located near one another,
regardless of whether or not the network was trained on those classes. Our
approach outperforms state-of-the-art deep metric learning approaches on
embedding learning challenges, as well as conventional softmax classification
on several datasets.