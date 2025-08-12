---
layout: publication
title: 'Hashmem: Pim-based Hashmap Accelerator'
authors: Akhil Shekar, Morteza Baradaran, Sabiha Tajdari, Kevin Skadron
conference: Arxiv
year: 2023
bibkey: shekar2023hashmem
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.17721'}]
tags: ["Efficiency"]
short_authors: Shekar et al.
---
Hashmaps are widely utilized data structures in many applications to perform
a probe on key-value pairs. However, their performance tends to degrade with
the increase in the dataset size, which leads to expensive off-chip memory
accesses to perform bucket traversals associated with hash collision. In this
work, we propose HashMem, a processing-in-memory (PIM) architecture designed to
perform bucket traversals along the row buffers at the subarray level. Due to
the inherent parallelism achieved with many concurrent subarray accesses and
the massive bandwidth available within DRAM, the execution time related to
bucket traversals is significantly reduced. We have evaluated two versions of
HashMem, performance-optimized and area-optimized, which have a speedup of
49.1x/17.1x and 9.2x/3.2x over standard C++ map and hyper-optimized hopscotch
map implementations, respectively.