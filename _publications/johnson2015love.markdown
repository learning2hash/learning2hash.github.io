---
layout: publication
title: 'Love Thy Neighbors: Image Annotation By Exploiting Image Metadata'
authors: Justin Johnson, Lamberto Ballan, Fei-Fei Li
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: johnson2015love
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1508.07647'}]
tags: ["ICCV"]
short_authors: Justin Johnson, Lamberto Ballan, Fei-Fei Li
---
Some images that are difficult to recognize on their own may become more
clear in the context of a neighborhood of related images with similar
social-network metadata. We build on this intuition to improve multilabel image
annotation. Our model uses image metadata nonparametrically to generate
neighborhoods of related images using Jaccard similarities, then uses a deep
neural network to blend visual information from the image and its neighbors.
Prior work typically models image metadata parametrically, in contrast, our
nonparametric treatment allows our model to perform well even when the
vocabulary of metadata changes between training and testing. We perform
comprehensive experiments on the NUS-WIDE dataset, where we show that our model
outperforms state-of-the-art methods for multilabel image annotation even when
our model is forced to generalize to new types of metadata.