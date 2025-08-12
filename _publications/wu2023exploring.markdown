---
layout: publication
title: Exploring The Sharpened Cosine Similarity
authors: Skyler Wu, Fred Lu, Edward Raff, James Holt
conference: Arxiv
year: 2023
bibkey: wu2023exploring
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.13855'}]
tags: ["Distance Metric Learning"]
short_authors: Wu et al.
---
Convolutional layers have long served as the primary workhorse for image
classification. Recently, an alternative to convolution was proposed using the
Sharpened Cosine Similarity (SCS), which in theory may serve as a better
feature detector. While multiple sources report promising results, there has
not been to date a full-scale empirical analysis of neural network performance
using these new layers. In our work, we explore SCS's parameter behavior and
potential as a drop-in replacement for convolutions in multiple CNN
architectures benchmarked on CIFAR-10. We find that while SCS may not yield
significant increases in accuracy, it may learn more interpretable
representations. We also find that, in some circumstances, SCS may confer a
slight increase in adversarial robustness.