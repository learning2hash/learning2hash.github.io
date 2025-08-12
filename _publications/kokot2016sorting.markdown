---
layout: publication
title: Sorting Data On Ultra-large Scale With RADULS. New Incarnation Of Radix Sort
authors: Marek Kokot, Sebastian Deorowicz, Agnieszka Debudaj-Grabysz
conference: Arxiv
year: 2016
bibkey: kokot2016sorting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.02557'}]
tags: []
short_authors: Marek Kokot, Sebastian Deorowicz, Agnieszka Debudaj-Grabysz
---
The paper introduces RADULS, a new parallel sorter based on radix sort
algorithm, intended to organize ultra-large data sets efficiently. For example
4G 16-byte records can be sorted with 16 threads in less than 15 seconds on
Intel Xeon-based workstation. The implementation of RADULS is not only highly
optimized to gain such an excellent performance, but also parallelized in a
cache friendly manner to make the most of modern multicore architectures.
Besides, our parallel scheduler launches a few different procedures at runtime,
according to the current parameters of the execution, for proper workload
management. All experiments show RADULS to be superior to competing algorithms.