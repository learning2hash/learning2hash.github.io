---
layout: publication
title: Multi-scale Convolutions For Learning Context Aware Feature Representations
authors: "Nikolai Ufer, Kam To Lui, Katja Schwarz, Paul Warkentin, Bj\xF6rn Ommer"
conference: Arxiv
year: 2019
bibkey: ufer2019multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.06978'}]
tags: []
short_authors: Ufer et al.
---
Finding semantic correspondences is a challenging problem. With the
breakthrough of CNNs stronger features are available for tasks like
classification but not specifically for the requirements of semantic matching.
In the following we present a weakly supervised metric learning approach which
generates stronger features by encoding far more context than previous methods.
First, we generate more suitable training data using a geometrically informed
correspondence mining method which is less prone to spurious matches and
requires only image category labels as supervision. Second, we introduce a new
convolutional layer which is a learned mixture of differently strided
convolutions and allows the network to encode implicitly more context while
preserving matching accuracy at the same time. The strong geometric encoding on
the feature side enables us to learn a semantic flow network, which generates
more natural deformations than parametric transformation based models and is
able to jointly predict foreground regions at the same time. Our semantic flow
network outperforms current state-of-the-art on several semantic matching
benchmarks and the learned features show astonishing performance regarding
simple nearest neighbor matching.