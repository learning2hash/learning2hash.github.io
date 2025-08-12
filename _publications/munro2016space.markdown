---
layout: publication
title: Space-efficient Construction Of Compressed Indexes In Deterministic Linear
  Time
authors: J. Ian Munro, Gonzalo Navarro, Yakov Nekrich
conference: Proceedings of the Twenty-Eighth Annual ACM-SIAM Symposium on Discrete
  Algorithms
year: 2017
bibkey: munro2016space
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.04346'}]
tags: ["Efficiency", "Memory Efficiency"]
short_authors: J. Ian Munro, Gonzalo Navarro, Yakov Nekrich
---
We show that the compressed suffix array and the compressed suffix tree of a
string \\(T\\) can be built in \\(O(n)\\) deterministic time using \\(O(nlog\sigma)\\)
bits of space, where \\(n\\) is the string length and \\(\sigma\\) is the alphabet
size. Previously described deterministic algorithms either run in time that
depends on the alphabet size or need \\(\omega(nlog \sigma)\\) bits of working
space. Our result has immediate applications to other problems, such as
yielding the first linear-time LZ77 and LZ78 parsing algorithms that use \\(O(n
log\sigma)\\) bits.