---
layout: publication
title: Unsupervised High-level Feature Learning By Ensemble Projection For Semi-supervised
  Image Classification And Image Clustering
authors: Dengxin Dai, Luc van Gool
conference: Arxiv
year: 2016
bibkey: dai2016unsupervised
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.00955'}]
tags: ["Unsupervised"]
short_authors: Dengxin Dai, Luc van Gool
---
This paper investigates the problem of image classification with limited or
no annotations, but abundant unlabeled data. The setting exists in many tasks
such as semi-supervised image classification, image clustering, and image
retrieval. Unlike previous methods, which develop or learn sophisticated
regularizers for classifiers, our method learns a new image representation by
exploiting the distribution patterns of all available data for the task at
hand. Particularly, a rich set of visual prototypes are sampled from all
available data, and are taken as surrogate classes to train discriminative
classifiers; images are projected via the classifiers; the projected values,
similarities to the prototypes, are stacked to build the new feature vector.
The training set is noisy. Hence, in the spirit of ensemble learning we create
a set of such training sets which are all diverse, leading to diverse
classifiers. The method is dubbed Ensemble Projection (EP). EP captures not
only the characteristics of individual images, but also the relationships among
images. It is conceptually simple and computationally efficient, yet effective
and flexible. Experiments on eight standard datasets show that: (1) EP
outperforms previous methods for semi-supervised image classification; (2) EP
produces promising results for self-taught image classification, where
unlabeled samples are a random collection of images rather than being from the
same distribution as the labeled ones; and (3) EP improves over the original
features for image clustering. The code of the method is available on the
project page.