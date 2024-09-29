---
layout: publication
title: Fast Exact Search In Hamming Space With Multi-index Hashing
authors: Norouzi Mohammad, Punjani Ali, Fleet David J.
conference: "Arxiv"
year: 2013
bibkey: norouzi2013fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1307.2982"}
tags: ['ARXIV']
---
There is growing interest in representing image data and feature descriptors using compact binary codes for fast near neighbor search. Although binary codes are motivated by their use as direct indices (addresses) into a hash table codes longer than 32 bits are not being used as such as it was thought to be ineffective. We introduce a rigorous way to build multiple hash tables on binary code substrings that enables exact k-nearest neighbor search in Hamming space. The approach is storage efficient and straightforward to implement. Theoretical analysis shows that the algorithm exhibits sub-linear run-time behavior for uniformly distributed codes. Empirical results show dramatic speedups over a linear scan baseline for datasets of up to one billion codes of 64 128 or 256 bits.
