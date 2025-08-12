---
layout: publication
title: Edge Augmentation For Large-scale Sketch Recognition Without Sketches
authors: Nikos Efthymiadis, Giorgos Tolias, Ondrej Chum
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: efthymiadis2022edge
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.13164'}]
tags: ["Scalability"]
short_authors: Nikos Efthymiadis, Giorgos Tolias, Ondrej Chum
---
This work addresses scaling up the sketch classification task into a large
number of categories. Collecting sketches for training is a slow and tedious
process that has so far precluded any attempts to large-scale sketch
recognition. We overcome the lack of training sketch data by exploiting labeled
collections of natural images that are easier to obtain. To bridge the domain
gap we present a novel augmentation technique that is tailored to the task of
learning sketch recognition from a training set of natural images.
Randomization is introduced in the parameters of edge detection and edge
selection. Natural images are translated to a pseudo-novel domain called
"randomized Binary Thin Edges" (rBTE), which is used as a training domain
instead of natural images. The ability to scale up is demonstrated by training
CNN-based sketch recognition of more than 2.5 times larger number of categories
than used previously. For this purpose, a dataset of natural images from 874
categories is constructed by combining a number of popular computer vision
datasets. The categories are selected to be suitable for sketch recognition. To
estimate the performance, a subset of 393 categories with sketches is also
collected.