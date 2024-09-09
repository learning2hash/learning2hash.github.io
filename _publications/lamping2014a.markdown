---
layout: publication
title: A Fast, Minimal Memory, Consistent Hash Algorithm
authors: Lamping John, Veach Eric
conference: "Arxiv"
year: 2014
bibkey: lamping2014a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1406.2294"}
tags: ['ARXIV']
---
We present jump consistent hash, a fast, minimal memory, consistent hash algorithm that can be expressed in about 5 lines of code. In comparison to the algorithm of Karger et al., jump consistent hash requires no storage, is faster, and does a better job of evenly dividing the key space among the buckets and of evenly dividing the workload when the number of buckets changes. Its main limitation is that the buckets must be numbered sequentially, which makes it more suitable for data storage applications than for distributed web caching.
