---
layout: publication
title: Generalized Max Pooling
authors: Naila Murray, Florent Perronnin
conference: 2014 IEEE Conference on Computer Vision and Pattern Recognition
year: 2014
bibkey: murray2014generalized
citations: 204
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1406.0312'}]
tags: ["CVPR"]
short_authors: Naila Murray, Florent Perronnin
---
State-of-the-art patch-based image representations involve a pooling
operation that aggregates statistics computed from local descriptors. Standard
pooling operations include sum- and max-pooling. Sum-pooling lacks
discriminability because the resulting representation is strongly influenced by
frequent yet often uninformative descriptors, but only weakly influenced by
rare yet potentially highly-informative ones. Max-pooling equalizes the
influence of frequent and rare descriptors but is only applicable to
representations that rely on count statistics, such as the bag-of-visual-words
(BOV) and its soft- and sparse-coding extensions. We propose a novel pooling
mechanism that achieves the same effect as max-pooling but is applicable beyond
the BOV and especially to the state-of-the-art Fisher Vector -- hence the name
Generalized Max Pooling (GMP). It involves equalizing the similarity between
each patch and the pooled representation, which is shown to be equivalent to
re-weighting the per-patch statistics. We show on five public image
classification benchmarks that the proposed GMP can lead to significant
performance gains with respect to heuristic alternatives.