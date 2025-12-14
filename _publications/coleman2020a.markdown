---
layout: publication
title: A One-pass Private Sketch For Most Machine Learning Tasks
authors: Benjamin Coleman, Anshumali Shrivastava
conference: Arxiv
year: 2020
bibkey: coleman2020a
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.09352'}]
tags: [Privacy & Security, Datasets, Scalability, Hashing Methods, Locality Sensitive
    Hashing]
short_authors: Benjamin Coleman, Anshumali Shrivastava
---
Differential privacy (DP) is a compelling privacy definition that explains
the privacy-utility tradeoff via formal, provable guarantees. Inspired by
recent progress toward general-purpose data release algorithms, we propose a
private sketch, or small summary of the dataset, that supports a multitude of
machine learning tasks including regression, classification, density
estimation, near-neighbor search, and more. Our sketch consists of randomized
contingency tables that are indexed with locality-sensitive hashing and
constructed with an efficient one-pass algorithm. We prove competitive error
bounds for DP kernel density estimation. Existing methods for DP kernel density
estimation scale poorly, often exponentially slower with an increase in
dimensions. In contrast, our sketch can quickly run on large, high-dimensional
datasets in a single pass. Exhaustive experiments show that our generic sketch
delivers a similar privacy-utility tradeoff when compared to existing DP
methods at a fraction of the computation cost. We expect that our sketch will
enable differential privacy in distributed, large-scale machine learning
settings.