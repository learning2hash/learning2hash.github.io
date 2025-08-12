---
layout: publication
title: Label Embedding Via Low-coherence Matrices
authors: Jianxin Zhang, Clayton Scott
conference: Arxiv
year: 2023
bibkey: zhang2023label
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.19470'}]
tags: []
short_authors: Jianxin Zhang, Clayton Scott
---
Label embedding is a framework for multiclass classification problems where
each label is represented by a distinct vector of some fixed dimension, and
training involves matching model output to the vector representing the correct
label. While label embedding has been successfully applied in extreme
classification and zero-shot learning, and offers both computational and
statistical advantages, its theoretical foundations remain poorly understood.
This work presents an analysis of label embedding in the context of extreme
multiclass classification, where the number of classes \(C\) is very large. We
present an excess risk bound that reveals a trade-off between computational and
statistical efficiency, quantified via the coherence of the embedding matrix.
We further show that under the Massart noise condition, the statistical penalty
for label embedding vanishes with sufficiently low coherence. Our analysis
supports an algorithm that is simple, scalable, and easily parallelizable, and
experimental results demonstrate its effectiveness in large-scale applications.