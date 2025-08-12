---
layout: publication
title: 'Fresada: A French Satire Data Set For Cross-domain Satire Detection'
authors: Radu Tudor Ionescu, Adrian Gabriel Chifu
conference: 2021 International Joint Conference on Neural Networks (IJCNN)
year: 2021
bibkey: ionescu2021fresada
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.04828'}]
tags: []
short_authors: Radu Tudor Ionescu, Adrian Gabriel Chifu
---
In this paper, we introduce FreSaDa, a French Satire Data Set, which is
composed of 11,570 articles from the news domain. In order to avoid reporting
unreasonably high accuracy rates due to the learning of characteristics
specific to publication sources, we divided our samples into training,
validation and test, such that the training publication sources are distinct
from the validation and test publication sources. This gives rise to a
cross-domain (cross-source) satire detection task. We employ two classification
methods as baselines for our new data set, one based on low-level features
(character n-grams) and one based on high-level features (average of CamemBERT
word embeddings). As an additional contribution, we present an unsupervised
domain adaptation method based on regarding the pairwise similarities (given by
the dot product) between the training samples and the validation samples as
features. By including these domain-specific features, we attain significant
improvements for both character n-grams and CamemBERT embeddings.