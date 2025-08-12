---
layout: publication
title: Binary Pebbling Algorithms For In-place Reversal Of One-way Hash Chains
authors: Berry Schoenmakers
conference: Nieuw Archief voor Wiskunde series 5 volume 18 number 3 pages 199-204
  September 2017
year: 2018
bibkey: schoenmakers2018binary
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.03748'}]
tags: []
short_authors: Berry Schoenmakers
---
We present optimal binary pebbling algorithms for in-place reversal (backward
traversal) of one-way hash chains. For a hash chain of length \(2^k\), the number
of hashes performed in each output round does not exceed \(\lceil k/2 \rceil\),
whereas the number of hash values stored (pebbles) throughout is at most \(k\).
  We introduce a framework for rigorous comparison of explicit binary pebbling
algorithms, including simple speed-1 binary pebbling, Jakobsson's speed-2
binary pebbling, and our optimal binary pebbling algorithm. Explicit schedules
describe for each pebble exactly how many hashes need to be performed in each
round. The optimal schedule turns out to be essentially unique and exhibits a
nice recursive structure, which allows for fully optimized implementations that
can readily be deployed. In particular, we develop the first in-place
implementations with minimal storage overhead (essentially, storing only hash
values), and fast implementations with minimal computational overhead.