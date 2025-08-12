---
layout: publication
title: Deep Kernel Learning For Clustering
authors: Chieh Wu, Zulqarnain Khan, Yale Chang, Stratis Ioannidis, Jennifer Dy
conference: Proceedings of the 2020 SIAM International Conference on Data Mining
year: 2020
bibkey: wu2019deep
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.03515'}]
tags: []
short_authors: Wu et al.
---
We propose a deep learning approach for discovering kernels tailored to
identifying clusters over sample data. Our neural network produces sample
embeddings that are motivated by--and are at least as expressive as--spectral
clustering. Our training objective, based on the Hilbert Schmidt Information
Criterion, can be optimized via gradient adaptations on the Stiefel manifold,
leading to significant acceleration over spectral methods relying on
eigendecompositions. Finally, our trained embedding can be directly applied to
out-of-sample data. We show experimentally that our approach outperforms
several state-of-the-art deep clustering methods, as well as traditional
approaches such as \\(k\\)-means and spectral clustering over a broad array of
real-life and synthetic datasets.