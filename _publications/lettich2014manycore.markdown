---
layout: publication
title: Manycore Processing Of Repeated K-nn Queries Over Massive Moving Objects Observations
authors: Francesco Lettich, Salvatore Orlando, Claudio Silvestri
conference: Arxiv
year: 2014
bibkey: lettich2014manycore
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.6170'}]
tags: [Evaluation, Datasets]
short_authors: Francesco Lettich, Salvatore Orlando, Claudio Silvestri
---
The ability to timely process significant amounts of continuously updated
spatial data is mandatory for an increasing number of applications. In this
paper we focus on a specific data-intensive problem concerning the repeated
processing of huge amounts of k nearest neighbours (k-NN) queries over massive
sets of moving objects, where the spatial extents of queries and the position
of objects are continuously modified over time. In particular, we propose a
novel hybrid CPU/GPU pipeline that significantly accelerate query processing
thanks to a combination of ad-hoc data structures and non-trivial memory access
patterns. To the best of our knowledge this is the first work that exploits
GPUs to efficiently solve repeated k-NN queries over massive sets of
continuously moving objects, even characterized by highly skewed spatial
distributions. In comparison with state-of-the-art sequential CPU-based
implementations, our method highlights significant speedups in the order of
10x-20x, depending on the datasets, even when considering cheap GPUs.