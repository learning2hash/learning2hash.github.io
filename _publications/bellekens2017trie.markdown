---
layout: publication
title: Trie Compression For GPU Accelerated Multi-pattern Matching
authors: Xavier Bellekens, Amar Seeam, Christos Tachtatzis, Robert Atkinson
conference: Arxiv
year: 2017
bibkey: bellekens2017trie
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.03657'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Bellekens et al.
---
Graphics Processing Units allow for running massively parallel applications
offloading the CPU from computationally intensive resources, however GPUs have
a limited amount of memory. In this paper a trie compression algorithm for
massively parallel pattern matching is presented demonstrating 85% less space
requirements than the original highly efficient parallel failure-less
aho-corasick, whilst demonstrating over 22 Gbps throughput. The algorithm
presented takes advantage of compressed row storage matrices as well as shared
and texture memory on the GPU.