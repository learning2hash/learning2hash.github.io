---
layout: publication
title: Analysing The Performance Of GPU Hash Tables For State Space Exploration
authors: Nathan Eindhoven University Of Technology et al.
conference: EPTCS 263 2017 pp. 1-15
year: 2017
citations: 5
bibkey: cassee2017analysing
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.09494'}]
tags: [Applications, Hashing Methods]
---
In the past few years, General Purpose Graphics Processors (GPUs) have been
used to significantly speed up numerous applications. One of the areas in which
GPUs have recently led to a significant speed-up is model checking. In model
checking, state spaces, i.e., large directed graphs, are explored to verify
whether models satisfy desirable properties. GPUexplore is a GPU-based model
checker that uses a hash table to efficiently keep track of already explored
states. As a large number of states is discovered and stored during such an
exploration, the hash table should be able to quickly handle many inserts and
queries concurrently. In this paper, we experimentally compare two different
hash tables optimised for the GPU, one being the GPUexplore hash table, and the
other using Cuckoo hashing. We compare the performance of both hash tables
using random and non-random data obtained from model checking experiments, to
analyse the applicability of the two hash tables for state space exploration.
We conclude that Cuckoo hashing is three times faster than GPUexplore hashing
for random data, and that Cuckoo hashing is five to nine times faster for
non-random data. This suggests great potential to further speed up GPUexplore
in the near future.