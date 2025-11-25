---
layout: publication
title: Deep Metric Learning For Multi-labelled Radiographs
authors: Mauro Annarumma, Giovanni Montana
conference: Proceedings of the 33rd Annual ACM Symposium on Applied Computing
year: 2017
bibkey: annarumma2017deep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.07682'}]
tags: ["Distance Metric Learning", "Image Retrieval"]
short_authors: Mauro Annarumma, Giovanni Montana
---
Many radiological studies can reveal the presence of several co-existing
abnormalities, each one represented by a distinct visual pattern. In this
article we address the problem of learning a distance metric for plain
radiographs that captures a notion of "radiological similarity": two chest
radiographs are considered to be similar if they share similar abnormalities.
Deep convolutional neural networks (DCNs) are used to learn a low-dimensional
embedding for the radiographs that is equipped with the desired metric. Two
loss functions are proposed to deal with multi-labelled images and potentially
noisy labels. We report on a large-scale study involving over 745,000 chest
radiographs whose labels were automatically extracted from free-text
radiological reports through a natural language processing system. Using 4,500
validated exams, we demonstrate that the methodology performs satisfactorily on
clustering and image retrieval tasks. Remarkably, the learned metric separates
normal exams from those having radiological abnormalities.