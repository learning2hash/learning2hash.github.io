---
layout: publication
title: 'Compressed Spaced Suffix Arrays'
authors: Travis Gagie, Giovanni Manzini, Daniel Valenzuela
conference: "Arxiv"
year: 2013
citations: 2
bibkey: gagie2013compressed
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1312.3422'}
tags: ['Indexing and Efficiency', 'Approximate Nearest Neighbor Search']
---
Spaced seeds are important tools for similarity search in bioinformatics, and
using several seeds together often significantly improves their performance.
With existing approaches, however, for each seed we keep a separate linear-size
data structure, either a hash table or a spaced suffix array (SSA). In this
paper we show how to compress SSAs relative to normal suffix arrays (SAs) and
still support fast random access to them. We first prove a theoretical upper
bound on the space needed to store an SSA when we already have the SA. We then
present experiments indicating that our approach works even better in practice.
