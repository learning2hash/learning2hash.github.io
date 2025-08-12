---
layout: publication
title: High Performance Construction Of Recsplit Based Minimal Perfect Hash Functions
authors: Dominik Bez, Florian Kurpicz, Hans-Peter Lehmann, Peter Sanders
conference: Arxiv
year: 2022
bibkey: bez2022high
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.09562'}]
tags: ["Hashing Methods"]
short_authors: Bez et al.
---
A minimal perfect hash function (MPHF) bijectively maps a set S of objects to
the first |S| integers. It can be used as a building block in databases and
data compression. RecSplit [Esposito et al., ALENEX'20] is currently the most
space efficient practical minimal perfect hash function. It heavily relies on
trying out hash functions in a brute force way. We introduce rotation fitting,
a new technique that makes the search more efficient by drastically reducing
the number of tried hash functions. Additionally, we greatly improve the
construction time of RecSplit by harnessing parallelism on the level of bits,
vectors, cores, and GPUs. In combination, the resulting improvements yield
speedups up to 239 on an 8-core CPU and up to 5438 using a GPU. The original
single-threaded RecSplit implementation needs 1.5 hours to construct an MPHF
for 5 Million objects with 1.56 bits per object. On the GPU, we achieve the
same space usage in just 5 seconds. Given that the speedups are larger than the
increase in energy consumption, our implementation is more energy efficient
than the original implementation.