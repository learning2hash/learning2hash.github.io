---
layout: publication
title: Clustering Images By Unmasking - A New Baseline
authors: Mariana-Iuliana Georgescu, Radu Tudor Ionescu
conference: 2019 IEEE International Conference on Image Processing (ICIP)
year: 2019
bibkey: georgescu2019clustering
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.00773'}]
tags: []
short_authors: Mariana-Iuliana Georgescu, Radu Tudor Ionescu
---
We propose a novel agglomerative clustering method based on unmasking, a
technique that was previously used for authorship verification of text
documents and for abnormal event detection in videos. In order to join two
clusters, we alternate between (i) training a binary classifier to distinguish
between the samples from one cluster and the samples from the other cluster,
and (ii) removing at each step the most discriminant features. The
faster-decreasing accuracy rates of the intermediately-obtained classifiers
indicate that the two clusters should be joined. To the best of our knowledge,
this is the first work to apply unmasking in order to cluster images. We
compare our method with k-means as well as a recent state-of-the-art clustering
method. The empirical results indicate that our approach is able to improve
performance for various (deep and shallow) feature representations and
different tasks, such as handwritten digit recognition, texture classification
and fine-grained object recognition.