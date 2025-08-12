---
layout: publication
title: Information-theoretical Label Embeddings For Large-scale Image Classification
authors: "Fran\xE7ois Chollet"
conference: Arxiv
year: 2016
bibkey: chollet2016information
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.05691'}]
tags: ["Scalability"]
short_authors: "Fran\xE7ois Chollet"
---
We present a method for training multi-label, massively multi-class image
classification models, that is faster and more accurate than supervision via a
sigmoid cross-entropy loss (logistic regression). Our method consists in
embedding high-dimensional sparse labels onto a lower-dimensional dense sphere
of unit-normed vectors, and treating the classification problem as a cosine
proximity regression problem on this sphere. We test our method on a dataset of
300 million high-resolution images with 17,000 labels, where it yields
considerably faster convergence, as well as a 7% higher mean average precision
compared to logistic regression.