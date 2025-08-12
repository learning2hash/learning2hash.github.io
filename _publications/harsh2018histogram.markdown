---
layout: publication
title: Histogram Sort With Sampling
authors: Vipul Harsh, Laxmikant Kale, Edgar Solomonik
conference: The 31st ACM Symposium on Parallelism in Algorithms and Architectures
year: 2019
bibkey: harsh2018histogram
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.01237'}]
tags: []
short_authors: Vipul Harsh, Laxmikant Kale, Edgar Solomonik
---
To minimize data movement, state-of-the-art parallel sorting algorithms use
techniques based on sampling and histogramming to partition keys prior to
redistribution. Sampling enables partitioning to be done using a representative
subset of the keys, while histogramming enables evaluation and iterative
improvement of a given partition. We introduce Histogram sort with sampling
(HSS), which combines sampling and iterative histogramming to find high quality
partitions with minimal data movement and high practical performance. Compared
to the best known (recently introduced) algorithm for finding these partitions,
our algorithm requires a factor of \{\Theta\}(log(p)/ log log(p)) less
communication, and substantially less when compared to standard variants of
Sample sort and Histogram sort. We provide a distributed memory implementation
of the proposed algorithm, compare its performance to two existing
implementations, and provide a brief application study showing benefit of the
new algorithm.