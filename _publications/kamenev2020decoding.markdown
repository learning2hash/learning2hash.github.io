---
layout: publication
title: On Decoding Of Reed-muller Codes Using A Local Graph Search
authors: Mikhail Kamenev
conference: 2020 IEEE Information Theory Workshop (ITW)
year: 2021
bibkey: kamenev2020decoding
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.04338'}]
tags: []
short_authors: Mikhail Kamenev
---
We present a novel iterative decoding algorithm for Reed-Muller (RM) codes,
which takes advantage of a graph representation of the code. Vertices of the
considered graph correspond to codewords, with two vertices being connected by
an edge if and only if the Hamming distance between the corresponding codewords
equals the minimum distance of the code. The algorithm uses a greedy local
search to find a node optimizing a metric, e.g. the correlation between the
received vector and the corresponding codeword. In addition, the cyclic
redundancy check can be used to terminate the search as soon as a valid
codeword is found, leading to an improvement in the average computational
complexity of the algorithm. Simulation results for both binary symmetric
channel and additive white Gaussian noise channel show that the presented
decoder approaches the performance of maximum likelihood decoding for RM codes
of length less than 1024 and for the second-order RM codes of length less than
4096. Moreover, it is demonstrated that the considered decoding approach
outperforms state-of-the-art decoding algorithms of RM codes with similar
computational complexity for a wide range of block lengths and rates.