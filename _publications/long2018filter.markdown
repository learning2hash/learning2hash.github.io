---
layout: publication
title: 'A Filter Of Minhash For Image Similarity Measures'
authors: Jun Long, Qunfeng Liu, Xinpan Yuan, Chengyuan Zhang, Junfeng Liu
conference: "Arxiv"
year: 2018
citations: 1
bibkey: long2018filter
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1807.02895'}
tags: ['Hashing Methods', 'Applications', 'Tools and Libraries', 'ANN Search', 'Hashing Fundamentals']
---
Image similarity measures play an important role in nearest neighbor search
and duplicate detection for large-scale image datasets. Recently, Minwise
Hashing (or Minhash) and its related hashing algorithms have achieved great
performances in large-scale image retrieval systems. However, there are a large
number of comparisons for image pairs in these applications, which may spend a
lot of computation time and affect the performance. In order to quickly obtain
the pairwise images that theirs similarities are higher than the specific
threshold T (e.g., 0.5), we propose a dynamic threshold filter of Minwise
Hashing for image similarity measures. It greatly reduces the calculation time
by terminating the unnecessary comparisons in advance. We also find that the
filter can be extended to other hashing algorithms, on when the estimator
satisfies the binomial distribution, such as b-Bit Minwise Hashing, One
Permutation Hashing, etc. In this pager, we use the Bag-of-Visual-Words (BoVW)
model based on the Scale Invariant Feature Transform (SIFT) to represent the
image features. We have proved that the filter is correct and effective through
the experiment on real image datasets.
