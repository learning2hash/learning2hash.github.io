---
layout: publication
title: Weakly-supervised Multi-class Object Localization Using Only Object Counts
  As Labels
authors: Kyle Mills, Isaac Tamblyn
conference: Arxiv
year: 2021
bibkey: mills2021weakly
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.11743'}]
tags: []
short_authors: Kyle Mills, Isaac Tamblyn
---
We demonstrate the use of an extensive deep neural network to localize
instances of objects in images. The EDNN is naturally able to accurately
perform multi-class counting using only ground truth count values as labels.
Without providing any conceptual information, object annotations, or pixel
segmentation information, the neural network is able to formulate its own
conceptual representation of the items in the image. Using images labelled with
only the counts of the objects present,the structure of the extensive deep
neural network can be exploited to perform localization of the objects within
the visual field. We demonstrate that a trained EDNN can be used to count
objects in images much larger than those on which it was trained. In order to
demonstrate our technique, we introduce seven new data sets: five progressively
harder MNIST digit-counting data sets, and two datasets of 3d-rendered rubber
ducks in various situations. On most of these datasets, the EDNN achieves
greater than 99% test set accuracy in counting objects.