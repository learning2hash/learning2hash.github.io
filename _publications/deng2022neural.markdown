---
layout: publication
title: Neural Eigenfunctions Are Structured Representation Learners
authors: Zhijie Deng, Jiaxin Shi, Hao Zhang, Peng Cui, Cewu Lu, Jun Zhu
conference: Arxiv
year: 2022
bibkey: deng2022neural
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.12637'}]
tags: ["Image Retrieval", "Self-Supervised"]
short_authors: Deng et al.
---
This paper introduces a structured, adaptive-length deep representation
called Neural Eigenmap. Unlike prior spectral methods such as Laplacian
Eigenmap that operate in a nonparametric manner, Neural Eigenmap leverages
NeuralEF to parametrically model eigenfunctions using a neural network. We show
that, when the eigenfunction is derived from positive relations in a data
augmentation setup, applying NeuralEF results in an objective function that
resembles those of popular self-supervised learning methods, with an additional
symmetry-breaking property that leads to *structured* representations
where features are ordered by importance. We demonstrate using such
representations as adaptive-length codes in image retrieval systems. By
truncation according to feature importance, our method requires up to
\(16\times\) shorter representation length than leading self-supervised learning
ones to achieve similar retrieval performance. We further apply our method to
graph data and report strong results on a node representation learning
benchmark with more than one million nodes.