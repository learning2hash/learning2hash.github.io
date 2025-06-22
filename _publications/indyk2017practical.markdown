---
layout: publication
title: Practical Data-dependent Metric Compression With Provable Guarantees
authors: Piotr Indyk, Ilya Razenshteyn, Tal Wagner
conference: Neural Information Processing Systems
year: 2017
citations: 3
bibkey: indyk2017practical
additional_links: [{name: Paper, url: 'https://papers.nips.cc/paper/2017/hash/49b8b4f95f02e055801da3b4f58e28b7-Abstract.html'}]
tags: [NEURIPS, Quantisation, Efficiency and Optimization]
---
We introduce a new distance-preserving compact representation of multi-dimensional point-sets. Given n points in a d-dimensional space where each coordinate is represented using B bits (i.e., dB bits per point), it produces  a representation of size O( d log(d B/epsilon) +log n) bits per point from which one can approximate the distances up to a factor of 1 + epsilon. Our algorithm almost matches the recent bound of Indyk et al, 2017\} while being much simpler. We compare our algorithm to Product Quantization (PQ) (Jegou et al, 2011) a state of the art heuristic metric compression method. We evaluate both algorithms on several data sets: SIFT, MNIST, New York City taxi time series and a synthetic one-dimensional data set embedded in a high-dimensional space. Our algorithm produces representations that are comparable to or better than those produced by PQ, while having provable guarantees on its performance.