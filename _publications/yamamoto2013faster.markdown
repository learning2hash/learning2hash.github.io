---
layout: publication
title: Faster Compact On-line Lempel-ziv Factorization
authors: Jun'ichi Yamamoto, Tomohiro I, Hideo Bannai, Shunsuke Inenaga, Masayuki Takeda
conference: Arxiv
year: 2014
bibkey: yamamoto2013faster
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1305.6095'}]
tags: []
short_authors: Yamamoto et al.
---
We present a new on-line algorithm for computing the Lempel-Ziv factorization
of a string that runs in \\(O(Nlog N)\\) time and uses only \\(O(Nlog\sigma)\\) bits
of working space, where \\(N\\) is the length of the string and \\(\sigma\\) is the
size of the alphabet. This is a notable improvement compared to the performance
of previous on-line algorithms using the same order of working space but
running in either \\(O(Nlog^3N)\\) time (Okanohara & Sadakane 2009) or
\\(O(Nlog^2N)\\) time (Starikovskaya 2012). The key to our new algorithm is in the
utilization of an elegant but less popular index structure called Directed
Acyclic Word Graphs, or DAWGs (Blumer et al. 1985). We also present an
opportunistic variant of our algorithm, which, given the run length encoding of
size \\(m\\) of a string of length \\(N\\), computes the Lempel-Ziv factorization
on-line, in \\(O\left(m \cdot \min \left\\{\frac\{(loglog m)(log log
N)\}\{logloglog N\}, \sqrt\{\frac\{log m\}\{log log m\}\} \right\\}\right)\\) time
and \\(O(mlog N)\\) bits of space, which is faster and more space efficient when
the string is run-length compressible.