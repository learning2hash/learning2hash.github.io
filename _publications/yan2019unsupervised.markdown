---
layout: publication
title: Unsupervised Learning Framework Of Interest Point Via Properties Optimization
authors: Pei Yan, Yihua Tan, Yuan Xiao, Yuan Tai, Cai Wen
conference: Arxiv
year: 2019
bibkey: yan2019unsupervised
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.11375'}]
tags: ["Unsupervised"]
short_authors: Yan et al.
---
This paper presents an entirely unsupervised interest point training
framework by jointly learning detector and descriptor, which takes an image as
input and outputs a probability and a description for every image point. The
objective of the training framework is formulated as joint probability
distribution of the properties of the extracted points. The essential
properties are selected as sparsity, repeatability and discriminability which
are formulated by the probabilities. To maximize the objective efficiently,
latent variable is introduced to represent the probability of that a point
satisfies the required properties. Therefore, original maximization can be
optimized with Expectation Maximization algorithm (EM). Considering high
computation cost of EM on large scale image set, we implement the optimization
process with an efficient strategy as Mini-Batch approximation of EM (MBEM). In
the experiments both detector and descriptor are instantiated with fully
convolutional network which is named as Property Network (PN). The experiments
demonstrate that PN outperforms state-of-the-art methods on a number of image
matching benchmarks without need of retraining. PN also reveals that the
proposed training framework has high flexibility to adapt to diverse types of
scenes.