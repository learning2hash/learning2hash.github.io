---
layout: publication
title: Joint Debiased Representation Learning And Imbalanced Data Clustering
authors: Mina Rezaei, Emilio Dorigatti, David Ruegamer, Bernd Bischl
conference: 2022 IEEE International Conference on Data Mining Workshops (ICDMW)
year: 2022
bibkey: rezaei2021joint
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.05232'}]
tags: ["Unsupervised"]
short_authors: Rezaei et al.
---
One of the most promising approaches for unsupervised learning is combining
deep representation learning and deep clustering. Some recent works propose to
simultaneously learn representation using deep neural networks and perform
clustering by defining a clustering loss on top of embedded features. However,
these approaches are sensitive to imbalanced data and out-of-distribution
samples. As a consequence, these methods optimize clustering by pushing data
close to randomly initialized cluster centers. This is problematic when the
number of instances varies largely in different classes or a cluster with few
samples has less chance to be assigned a good centroid. To overcome these
limitations, we introduce a new unsupervised framework for joint debiased
representation learning and image clustering. We simultaneously train two deep
learning models, a deep representation network that captures the data
distribution, and a deep clustering network that learns embedded features and
performs clustering. Specifically, the clustering network and learning
representation network both take advantage of our proposed statistics pooling
block that represents mean, variance, and cardinality to handle the
out-of-distribution samples and class imbalance. Our experiments show that
using these representations, one can considerably improve results on imbalanced
image clustering across a variety of image datasets. Moreover, the learned
representations generalize well when transferred to the out-of-distribution
dataset.