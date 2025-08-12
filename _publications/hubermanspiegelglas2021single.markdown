---
layout: publication
title: Single Image Object Counting And Localizing Using Active-learning
authors: Inbar Huberman-spiegelglas, Raanan Fattal
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2022
bibkey: hubermanspiegelglas2021single
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.08383'}]
tags: ["Datasets", "Evaluation"]
short_authors: Inbar Huberman-spiegelglas, Raanan Fattal
---
The need to count and localize repeating objects in an image arises in
different scenarios, such as biological microscopy studies, production lines
inspection, and surveillance recordings analysis. The use of supervised
Convoutional Neural Networks (CNNs) achieves accurate object detection when
trained over large class-specific datasets. The labeling effort in this
approach does not pay-off when the counting is required over few images of a
unique object class.
  We present a new method for counting and localizing repeating objects in
single-image scenarios, assuming no pre-trained classifier is available. Our
method trains a CNN over a small set of labels carefully collected from the
input image in few active-learning iterations. At each iteration, the latent
space of the network is analyzed to extract a minimal number of user-queries
that strives to both sample the in-class manifold as thoroughly as possible as
well as avoid redundant labels.
  Compared with existing user-assisted counting methods, our active-learning
iterations achieve state-of-the-art performance in terms of counting and
localizing accuracy, number of user mouse clicks, and running-time. This
evaluation was performed through a large user study over a wide range of image
classes with diverse conditions of illumination and occlusions.