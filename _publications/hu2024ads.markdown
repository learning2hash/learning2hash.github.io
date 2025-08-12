---
layout: publication
title: 'ADS: Approximate Densest Subgraph For Novel Image Discovery'
authors: Shanfeng Hu
conference: Arxiv
year: 2024
bibkey: hu2024ads
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.08743'}]
tags: []
short_authors: Shanfeng Hu
---
The volume of image repositories continues to grow. Despite the availability
of content-based addressing, we still lack a lightweight tool that allows us to
discover images of distinct characteristics from a large collection. In this
paper, we propose a fast and training-free algorithm for novel image discovery.
The key of our algorithm is formulating a collection of images as a perceptual
distance-weighted graph, within which our task is to locate the K-densest
subgraph that corresponds to a subset of the most unique images. While solving
this problem is not just NP-hard but also requires a full computation of the
potentially huge distance matrix, we propose to relax it into a K-sparse
eigenvector problem that we can efficiently solve using stochastic gradient
descent (SGD) without explicitly computing the distance matrix. We compare our
algorithm against state-of-the-arts on both synthetic and real datasets,
showing that it is considerably faster to run with a smaller memory footprint
while able to mine novel images more accurately.