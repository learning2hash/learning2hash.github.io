---
layout: publication
title: Online Adaptive Mahalanobis Distance Estimation
authors: Lianke Qin, Aravind Reddy, Zhao Song
conference: 2023 IEEE International Conference on Big Data (BigData)
year: 2023
bibkey: qin2023online
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01030'}]
tags: [Uncategorized]
short_authors: Lianke Qin, Aravind Reddy, Zhao Song
---
Mahalanobis metrics are widely used in machine learning in conjunction with
methods like \(k\)-nearest neighbors, \(k\)-means clustering, and \(k\)-medians
clustering. Despite their importance, there has not been any prior work on
applying sketching techniques to speed up algorithms for Mahalanobis metrics.
In this paper, we initiate the study of dimension reduction for Mahalanobis
metrics. In particular, we provide efficient data structures for solving the
Approximate Distance Estimation (ADE) problem for Mahalanobis distances. We
first provide a randomized Monte Carlo data structure. Then, we show how we can
adapt it to provide our main data structure which can handle sequences of
\textit\{adaptive\} queries and also online updates to both the Mahalanobis
metric matrix and the data points, making it amenable to be used in conjunction
with prior algorithms for online learning of Mahalanobis metrics.