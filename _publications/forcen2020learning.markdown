---
layout: publication
title: Learning Ordered Pooling Weights In Image Classification
authors: J. I. Forcen, Miguel Pagola, Edurne Barrenechea, Humberto Bustince
conference: Neurocomputing
year: 2020
bibkey: forcen2020learning
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.01243'}]
tags: []
short_authors: Forcen et al.
---
Spatial pooling is an important step in computer vision systems like
Convolutional Neural Networks or the Bag-of-Words method. The spatial pooling
purpose is to combine neighbouring descriptors to obtain a single descriptor
for a given region (local or global). The resultant combined vector must be as
discriminant as possible, in other words, must contain relevant information,
while removing irrelevant and confusing details. Maximum and average are the
most common aggregation functions used in the pooling step. To improve the
aggregation of relevant information without degrading their discriminative
power for image classification, we introduce a simple but effective scheme
based on Ordered Weighted Average (OWA) aggregation operators. We present a
method to learn the weights of the OWA aggregation operator in a Bag-of-Words
framework and in Convolutional Neural Networks, and provide an extensive
evaluation showing that OWA based pooling outperforms classical aggregation
operators.