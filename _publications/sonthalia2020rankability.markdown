---
layout: publication
title: On the rankability of visual embeddings
authors: Sonthalia Ankit, Uselis Arnas, Oh Seong Joon
conference: Neurocomputing
year: 2020
bibkey: sonthalia2020rankability
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.03683'}]
tags: []
---
We study whether visual embedding models capture continuous, ordinal attributes along linear directions, which we term _rank axes_. We define a model as _rankable_ for an attribute if projecting embeddings onto such an axis preserves the attribute's order. Across 7 popular encoders and 9 datasets with attributes like age, crowd count, head pose, aesthetics, and recency, we find that many embeddings are inherently rankable. Surprisingly, a small number of samples, or even just two extreme examples, often suffice to recover meaningful rank axes, without full-scale supervision. These findings open up new use cases for image ranking in vector databases and motivate further study into the structure and learning of rankable embeddings. Our code is available at https://github.com/aktsonthalia/rankable-vision-embeddings.