---
layout: publication
title: 'Phast -- Perfect Hashing With Fast Evaluation'
authors: Piotr Beling, Peter Sanders
conference: "Arxiv"
year: 2025
citations: 0
bibkey: beling2025phast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2504.17918'}
tags: ['Cross-Modal', 'Independent', 'Evaluation', 'Shallow', 'Hashing', 'Applications']
---
Perfect hash functions give unique "names" to arbitrary keys requiring only a
few bits per key. This is an essential building block in applications like
static hash tables, databases, or bioinformatics. This paper introduces the
PHast approach that has the currently fastest query time with competitive
construction time and space consumption. PHast improves bucket-placement which
first hashes each key k to a bucket, and then looks for the bucket seed s such
that a secondary hash function maps pairs (s,k) in a collision-free way. PHast
can use small-range primary hash functions with linear mapping, fixed-width
encoding of seeds, and parallel construction. This is achieved using small
overlapping slices of allowed values and bumping to handle unsuccessful seed
assignment.
