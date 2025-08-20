---
layout: publication
title: Visual Place Recognition Using Landmark Distribution Descriptors
authors: Pilailuck Panphattarasap, Andrew Calway
conference: Lecture Notes in Computer Science
year: 2017
bibkey: panphattarasap2017visual
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.04274'}]
tags: [Datasets, Evaluation]
short_authors: Pilailuck Panphattarasap, Andrew Calway
---
Recent work by Suenderhauf et al. [1] demonstrated improved visual place
recognition using proposal regions coupled with features from convolutional
neural networks (CNN) to match landmarks between views. In this work we extend
the approach by introducing descriptors built from landmark features which also
encode the spatial distribution of the landmarks within a view. Matching
descriptors then enforces consistency of the relative positions of landmarks
between views. This has a significant impact on performance. For example, in
experiments on 10 image-pair datasets, each consisting of 200 urban locations
with significant differences in viewing positions and conditions, we recorded
average precision of around 70% (at 100% recall), compared with 58% obtained
using whole image CNN features and 50% for the method in [1].