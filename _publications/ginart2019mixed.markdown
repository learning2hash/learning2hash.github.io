---
layout: publication
title: Mixed Dimension Embeddings With Application To Memory-efficient Recommendation
  Systems
authors: Antonio Ginart, Maxim Naumov, Dheevatsa Mudigere, Jiyan Yang, James Zou
conference: Arxiv
year: 2019
bibkey: ginart2019mixed
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.11810'}]
tags: [Scalability, Memory Efficiency, Datasets, Recommender Systems, Evaluation]
short_authors: Ginart et al.
---
Embedding representations power machine intelligence in many applications,
including recommendation systems, but they are space intensive -- potentially
occupying hundreds of gigabytes in large-scale settings. To help manage this
outsized memory consumption, we explore mixed dimension embeddings, an
embedding layer architecture in which a particular embedding vector's dimension
scales with its query frequency. Through theoretical analysis and systematic
experiments, we demonstrate that using mixed dimensions can drastically reduce
the memory usage, while maintaining and even improving the ML performance.
Empirically, we show that the proposed mixed dimension layers improve accuracy
by 0.1% using half as many parameters or maintain it using 16X fewer parameters
for click-through rate prediction task on the Criteo Kaggle dataset.