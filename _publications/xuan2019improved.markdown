---
layout: publication
title: Improved Embeddings With Easy Positive Triplet Mining
authors: Hong Xuan, Abby Stylianou, Robert Pless
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: xuan2019improved
citations: 131
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.04370'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: Hong Xuan, Abby Stylianou, Robert Pless
---
Deep metric learning seeks to define an embedding where semantically similar
images are embedded to nearby locations, and semantically dissimilar images are
embedded to distant locations. Substantial work has focused on loss functions
and strategies to learn these embeddings by pushing images from the same class
as close together in the embedding space as possible. In this paper, we propose
an alternative, loosened embedding strategy that requires the embedding
function only map each training image to the most similar examples from the
same class, an approach we call "Easy Positive" mining. We provide a collection
of experiments and visualizations that highlight that this Easy Positive mining
leads to embeddings that are more flexible and generalize better to new unseen
data. This simple mining strategy yields recall performance that exceeds state
of the art approaches (including those with complicated loss functions and
ensemble methods) on image retrieval datasets including CUB, Stanford Online
Products, In-Shop Clothes and Hotels-50K.