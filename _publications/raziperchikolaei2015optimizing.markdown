---
layout: publication
title: Optimizing Affinity-based Binary Hashing Using Auxiliary Coordinates
authors: "Ramin Raziperchikolaei, Miguel \xC1. Carreira-perpi\xF1\xE1n"
conference: Arxiv
year: 2015
citations: 11
bibkey: raziperchikolaei2015optimizing
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1501.05352'}]
tags: [Applications, Tools and Libraries, Evaluation Metrics, Loss Functions, Supervised,
  Hashing Methods]
---
In supervised binary hashing, one wants to learn a function that maps a
high-dimensional feature vector to a vector of binary codes, for application to
fast image retrieval. This typically results in a difficult optimization
problem, nonconvex and nonsmooth, because of the discrete variables involved.
Much work has simply relaxed the problem during training, solving a continuous
optimization, and truncating the codes a posteriori. This gives reasonable
results but is quite suboptimal. Recent work has tried to optimize the
objective directly over the binary codes and achieved better results, but the
hash function was still learned a posteriori, which remains suboptimal. We
propose a general framework for learning hash functions using affinity-based
loss functions that uses auxiliary coordinates. This closes the loop and
optimizes jointly over the hash functions and the binary codes so that they
gradually match each other. The resulting algorithm can be seen as a corrected,
iterated version of the procedure of optimizing first over the codes and then
learning the hash function. Compared to this, our optimization is guaranteed to
obtain better hash functions while being not much slower, as demonstrated
experimentally in various supervised datasets. In addition, our framework
facilitates the design of optimization algorithms for arbitrary types of loss
and hash functions.