---
layout: publication
title: Using Dimensionality Reduction To Optimize T-sne
authors: Rikhav Shah, Sandeep Silwal
conference: Arxiv
year: 2019
bibkey: shah2019using
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01098'}]
tags: ["Unsupervised"]
short_authors: Rikhav Shah, Sandeep Silwal
---
t-SNE is a popular tool for embedding multi-dimensional datasets into two or
three dimensions. However, it has a large computational cost, especially when
the input data has many dimensions. Many use t-SNE to embed the output of a
neural network, which is generally of much lower dimension than the original
data. This limits the use of t-SNE in unsupervised scenarios. We propose using
\textit\{random\} projections to embed high dimensional datasets into relatively
few dimensions, and then using t-SNE to obtain a two dimensional embedding. We
show that random projections preserve the desirable clustering achieved by
t-SNE, while dramatically reducing the runtime of finding the embedding.