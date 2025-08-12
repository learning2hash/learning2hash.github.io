---
layout: publication
title: Cache-oblivious Parallel Convex Hull In The Binary Forking Model
authors: Reilly Browne, Rezaul Chowdhury, Shih-Yu Tsai, Yimin Zhu
conference: Arxiv
year: 2023
bibkey: browne2023cache
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.10389'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Browne et al.
---
We present two cache-oblivious sorting-based convex hull algorithms in the
Binary Forking Model. The first is an algorithm for a presorted set of points
which achieves \(O(n)\) work, \(O(log n)\) span, and \(O(n/B)\) serial cache
complexity, where \(B\) is the cache line size. These are all optimal worst-case
bounds for cache-oblivious algorithms in the Binary Forking Model. The second
adapts Cole and Ramachandran's cache-oblivious sorting algorithm, matching its
properties including achieving \(O(n log n)\) work, \(O(log n log log n)\)
span, and \(O(n/B log_M n)\) serial cache complexity. Here \(M\) is the size of
the private cache.