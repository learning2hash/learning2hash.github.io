---
layout: publication
title: Scalable Similarity Learning Using Large Margin Neighborhood Embedding
authors: Wang Zhaowen, Yang Jianchao, Lin Zhe, Brandt Jonathan, Chang Shiyu, Huang
  Thomas
conference: 2015 IEEE Winter Conference on Applications of Computer Vision
year: 2015
bibkey: wang2014scalable
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1404.6272'}]
tags: ["Efficiency", "Evaluation", "Distance-Metric-Learning", "Scalability"]
short_authors: Wang et al.
---
Classifying large-scale image data into object categories is an important
problem that has received increasing research attention. Given the huge amount
of data, non-parametric approaches such as nearest neighbor classifiers have
shown promising results, especially when they are underpinned by a learned
distance or similarity measurement. Although metric learning has been well
studied in the past decades, most existing algorithms are impractical to handle
large-scale data sets. In this paper, we present an image similarity learning
method that can scale well in both the number of images and the dimensionality
of image descriptors. To this end, similarity comparison is restricted to each
sample's local neighbors and a discriminative similarity measure is induced
from large margin neighborhood embedding. We also exploit the ensemble of
projections so that high-dimensional features can be processed in a set of
lower-dimensional subspaces in parallel without much performance compromise.
The similarity function is learned online using a stochastic gradient descent
algorithm in which the triplet sampling strategy is customized for quick
convergence of classification performance. The effectiveness of our proposed
model is validated on several data sets with scales varying from tens of
thousands to one million images. Recognition accuracies competitive with the
state-of-the-art performance are achieved with much higher efficiency and
scalability.