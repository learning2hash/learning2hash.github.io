---
layout: publication
title: Piecewise-linear Manifolds For Deep Metric Learning
authors: Shubhang Bhatnagar, Narendra Ahuja
conference: Arxiv
year: 2024
bibkey: bhatnagar2024piecewise
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.14977'}]
tags: [Datasets, Supervised, Unsupervised, Evaluation, Distance Metric Learning, Few-shot
    & Zero-shot, Image Retrieval]
short_authors: Shubhang Bhatnagar, Narendra Ahuja
---
Unsupervised deep metric learning (UDML) focuses on learning a semantic
representation space using only unlabeled data. This challenging problem
requires accurately estimating the similarity between data points, which is
used to supervise a deep network. For this purpose, we propose to model the
high-dimensional data manifold using a piecewise-linear approximation, with
each low-dimensional linear piece approximating the data manifold in a small
neighborhood of a point. These neighborhoods are used to estimate similarity
between data points. We empirically show that this similarity estimate
correlates better with the ground truth than the similarity estimates of
current state-of-the-art techniques. We also show that proxies, commonly used
in supervised metric learning, can be used to model the piecewise-linear
manifold in an unsupervised setting, helping improve performance. Our method
outperforms existing unsupervised metric learning approaches on standard
zero-shot image retrieval benchmarks.