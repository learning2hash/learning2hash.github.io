---
layout: publication
title: 'SOAR: Improved Indexing For Approximate Nearest Neighbor Search'
authors: Philip Sun, David Simcha, Dave Dopson, Ruiqi Guo, Sanjiv Kumar
conference: Advances in Neural Information Processing Systems 36 (2023) 3189-3204
year: 2024
citations: 1
bibkey: sun2024improved
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.00774'}]
tags: [Indexing, ANN Search, Evaluation Metrics]
---
This paper introduces SOAR: Spilling with Orthogonality-Amplified Residuals,
a novel data indexing technique for approximate nearest neighbor (ANN) search.
SOAR extends upon previous approaches to ANN search, such as spill trees, that
utilize multiple redundant representations while partitioning the data to
reduce the probability of missing a nearest neighbor during search. Rather than
training and computing these redundant representations independently, however,
SOAR uses an orthogonality-amplified residual loss, which optimizes each
representation to compensate for cases where other representations perform
poorly. This drastically improves the overall index quality, resulting in
state-of-the-art ANN benchmark performance while maintaining fast indexing
times and low memory consumption.