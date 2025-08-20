---
layout: publication
title: Low-complexity Data-parallel Earth Mover's Distance Approximations
authors: Kubilay Atasu, Thomas Mittelholzer
conference: Arxiv
year: 2018
bibkey: atasu2018low
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.02091'}]
tags: [Scalability, Datasets]
short_authors: Kubilay Atasu, Thomas Mittelholzer
---
The Earth Mover's Distance (EMD) is a state-of-the art metric for comparing
discrete probability distributions, but its high distinguishability comes at a
high cost in computational complexity. Even though linear-complexity
approximation algorithms have been proposed to improve its scalability, these
algorithms are either limited to vector spaces with only a few dimensions or
they become ineffective when the degree of overlap between the probability
distributions is high. We propose novel approximation algorithms that overcome
both of these limitations, yet still achieve linear time complexity. All our
algorithms are data parallel, and thus, we take advantage of massively parallel
computing engines, such as Graphics Processing Units (GPUs). On the popular
text-based 20 Newsgroups dataset, the new algorithms are four orders of
magnitude faster than a multi-threaded CPU implementation of Word Mover's
Distance and match its nearest-neighbors-search accuracy. On MNIST images, the
new algorithms are four orders of magnitude faster than a GPU implementation of
the Sinkhorn's algorithm while offering a slightly higher
nearest-neighbors-search accuracy.