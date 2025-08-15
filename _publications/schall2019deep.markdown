---
layout: publication
title: Deep Aggregation Of Regional Convolutional Activations For Content Based Image
  Retrieval
authors: Konstantin Schall, Kai Uwe Barthel, Nico Hezel, Klaus Jung
conference: 2019 IEEE 21st International Workshop on Multimedia Signal Processing
  (MMSP)
year: 2019
bibkey: schall2019deep
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.09420'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Supervised"]
short_authors: Schall et al.
---
One of the key challenges of deep learning based image retrieval remains in
aggregating convolutional activations into one highly representative feature
vector. Ideally, this descriptor should encode semantic, spatial and low level
information. Even though off-the-shelf pre-trained neural networks can already
produce good representations in combination with aggregation methods,
appropriate fine tuning for the task of image retrieval has shown to
significantly boost retrieval performance. In this paper, we present a simple
yet effective supervised aggregation method built on top of existing regional
pooling approaches. In addition to the maximum activation of a given region, we
calculate regional average activations of extracted feature maps. Subsequently,
weights for each of the pooled feature vectors are learned to perform a
weighted aggregation to a single feature vector. Furthermore, we apply our
newly proposed NRA loss function for deep metric learning to fine tune the
backbone neural network and to learn the aggregation weights. Our method
achieves state-of-the-art results for the INRIA Holidays data set and
competitive results for the Oxford Buildings and Paris data sets while reducing
the training time significantly.