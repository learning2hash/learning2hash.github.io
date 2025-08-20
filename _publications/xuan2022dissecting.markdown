---
layout: publication
title: Dissecting The Impact Of Different Loss Functions With Gradient Surgery
authors: Hong Xuan, Robert Pless
conference: Arxiv
year: 2022
bibkey: xuan2022dissecting
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.11307'}]
tags: [Distance Metric Learning, Datasets, Image Retrieval]
short_authors: Hong Xuan, Robert Pless
---
Pair-wise loss is an approach to metric learning that learns a semantic
embedding by optimizing a loss function that encourages images from the same
semantic class to be mapped closer than images from different classes. The
literature reports a large and growing set of variations of the pair-wise loss
strategies. Here we decompose the gradient of these loss functions into
components that relate to how they push the relative feature positions of the
anchor-positive and anchor-negative pairs. This decomposition allows the
unification of a large collection of current pair-wise loss functions.
Additionally, explicitly constructing pair-wise gradient updates to separate
out these effects gives insights into which have the biggest impact, and leads
to a simple algorithm that beats the state of the art for image retrieval on
the CAR, CUB and Stanford Online products datasets.