---
layout: publication
title: Identifying Reliable Annotations For Large Scale Image Segmentation
authors: Alexander Kolesnikov, Christoph H. Lampert
conference: Arxiv
year: 2015
bibkey: kolesnikov2015identifying
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1504.07460'}]
tags: ["Datasets"]
short_authors: Alexander Kolesnikov, Christoph H. Lampert
---
Challenging computer vision tasks, in particular semantic image segmentation,
require large training sets of annotated images. While obtaining the actual
images is often unproblematic, creating the necessary annotation is a tedious
and costly process. Therefore, one often has to work with unreliable annotation
sources, such as Amazon Mechanical Turk or (semi-)automatic algorithmic
techniques. In this work, we present a Gaussian process (GP) based technique
for simultaneously identifying which images of a training set have unreliable
annotation and learning a segmentation model in which the negative effect of
these images is suppressed. Alternatively, the model can also just be used to
identify the most reliably annotated images from the training set, which can
then be used for training any other segmentation method. By relying on "deep
features" in combination with a linear covariance function, our GP can be
learned and its hyperparameter determined efficiently using only matrix
operations and gradient-based optimization. This makes our method scalable even
to large datasets with several million training instances.