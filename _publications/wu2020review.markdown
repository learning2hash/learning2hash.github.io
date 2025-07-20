---
layout: publication
title: A Review for Weighted MinHash Algorithms
authors: Wu et al.
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: wu2020review
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.04633'}]
tags: [Survey Paper, Locality Sensitive Hashing]
---
Data similarity (or distance) computation is a fundamental research topic
which underpins many high-level applications based on similarity measures in
machine learning and data mining. However, in large-scale real-world scenarios,
the exact similarity computation has become daunting due to "3V" nature
(volume, velocity and variety) of big data. In such cases, the hashing
techniques have been verified to efficiently conduct similarity estimation in
terms of both theory and practice. Currently, MinHash is a popular technique
for efficiently estimating the Jaccard similarity of binary sets and
furthermore, weighted MinHash is generalized to estimate the generalized
Jaccard similarity of weighted sets. This review focuses on categorizing and
discussing the existing works of weighted MinHash algorithms. In this review,
we mainly categorize the Weighted MinHash algorithms into quantization-based
approaches, "active index"-based ones and others, and show the evolution and
inherent connection of the weighted MinHash algorithms, from the integer
weighted MinHash algorithms to real-valued weighted MinHash ones (particularly
the Consistent Weighted Sampling scheme). Also, we have developed a python
toolbox for the algorithms, and released it in our github. Based on the
toolbox, we experimentally conduct a comprehensive comparative study of the
standard MinHash algorithm and the weighted MinHash ones.