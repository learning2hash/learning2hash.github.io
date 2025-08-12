---
layout: publication
title: Ultra-fast Multiple Genome Sequence Matching Using GPU
authors: Gang Liao, Qi Sun, Longfei Ma, Sha Ding, Wen Xie
conference: Arxiv
year: 2013
bibkey: liao2013ultra
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1303.3692'}]
tags: ["Efficiency"]
short_authors: Liao et al.
---
In this paper, a contrastive evaluation of massively parallel implementations
of suffix tree and suffix array to accelerate genome sequence matching are
proposed based on Intel Core i7 3770K quad-core and NVIDIA GeForce GTX680 GPU.
Besides suffix array only held approximately 20%~30% of the space relative to
suffix tree, the coalesced binary search and tile optimization make suffix
array clearly outperform suffix tree using GPU. Consequently, the experimental
results show that multiple genome sequence matching based on suffix array is
more than 99 times speedup than that of CPU serial implementation. There is no
doubt that massively parallel matching algorithm based on suffix array is an
efficient approach to high-performance bioinformatics applications.