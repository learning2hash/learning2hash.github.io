---
layout: publication
title: Adaptive Additive Classification-based Loss For Deep Metric Learning
authors: Istvan Fehervari, Ives Macedo
conference: Arxiv
year: 2020
bibkey: fehervari2020adaptive
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.14693'}]
tags: ["Distance Metric Learning"]
short_authors: Istvan Fehervari, Ives Macedo
---
Recent works have shown that deep metric learning algorithms can benefit from
weak supervision from another input modality. This additional modality can be
incorporated directly into the popular triplet-based loss function as
distances. Also recently, classification loss and proxy-based metric learning
have been observed to lead to faster convergence as well as better retrieval
results, all the while without requiring complex and costly sampling
strategies. In this paper we propose an extension to the existing adaptive
margin for classification-based deep metric learning. Our extension introduces
a separate margin for each negative proxy per sample. These margins are
computed during training from precomputed distances of the classes in the other
modality. Our results set a new state-of-the-art on both on the Amazon fashion
retrieval dataset as well as on the public DeepFashion dataset. This was
observed with both fastText- and BERT-based embeddings for the additional
textual modality. Our results were achieved with faster convergence and lower
code complexity than the prior state-of-the-art.