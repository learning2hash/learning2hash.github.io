---
layout: publication
title: 'Discovering Data Structures: Nearest Neighbor Search And Beyond'
authors: Omar Salemohamed, Laurent Charlin, Shivam Garg, Vatsal Sharan, Gregory Valiant
conference: Arxiv
year: 2024
citations: 0
bibkey: salemohamed2024discovering
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.03253'}]
tags: [Tools and Libraries, ANN Search, Hashing Methods]
---
We propose a general framework for end-to-end learning of data structures.
Our framework adapts to the underlying data distribution and provides
fine-grained control over query and space complexity. Crucially, the data
structure is learned from scratch, and does not require careful initialization
or seeding with candidate data structures/algorithms. We first apply this
framework to the problem of nearest neighbor search. In several settings, we
are able to reverse-engineer the learned data structures and query algorithms.
For 1D nearest neighbor search, the model discovers optimal distribution
(in)dependent algorithms such as binary search and variants of interpolation
search. In higher dimensions, the model learns solutions that resemble k-d
trees in some regimes, while in others, they have elements of
locality-sensitive hashing. The model can also learn useful representations of
high-dimensional data and exploit them to design effective data structures. We
also adapt our framework to the problem of estimating frequencies over a data
stream, and believe it could also be a powerful discovery tool for new
problems.