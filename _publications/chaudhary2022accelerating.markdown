---
layout: publication
title: Accelerating Barnes-hut T-sne Algorithm By Efficient Parallelization On Multi-core
  Cpus
authors: Narendra Chaudhary, Alexander Pivovar, Pavel Yakovlev, Andrey Gorshkov, Sanchit
  Misra
conference: Arxiv
year: 2022
bibkey: chaudhary2022accelerating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.11506'}]
tags: []
short_authors: Chaudhary et al.
---
t-SNE remains one of the most popular embedding techniques for visualizing
high-dimensional data. Most standard packages of t-SNE, such as scikit-learn,
use the Barnes-Hut t-SNE (BH t-SNE) algorithm for large datasets. However,
existing CPU implementations of this algorithm are inefficient. In this work,
we accelerate the BH t-SNE on CPUs via cache optimizations, SIMD, parallelizing
sequential steps, and improving parallelization of multithreaded steps. Our
implementation (Acc-t-SNE) is up to 261x and 4x faster than scikit-learn and
the state-of-the-art BH t-SNE implementation from daal4py, respectively, on a
32-core Intel(R) Icelake cloud instance.