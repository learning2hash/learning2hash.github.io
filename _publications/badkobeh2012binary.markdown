---
layout: publication
title: Binary Jumbled String Matching For Highly Run-length Compressible Texts
authors: "Golnaz Badkobeh, Gabriele Fici, Steve Kroon, Zsuzsanna Lipt\xE1k"
conference: Information Processing Letters
year: 2013
bibkey: badkobeh2012binary
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1206.2523'}]
tags: []
short_authors: Badkobeh et al.
---
The Binary Jumbled String Matching problem is defined as: Given a string \\(s\\)
over \\(\\{a,b\\}\\) of length \\(n\\) and a query \\((x,y)\\), with \\(x,y\\) non-negative
integers, decide whether \\(s\\) has a substring \\(t\\) with exactly \\(x\\) \\(a\\)'s and \\(y\\)
\\(b\\)'s. Previous solutions created an index of size O(n) in a pre-processing
step, which was then used to answer queries in constant time. The fastest
algorithms for construction of this index have running time \\(O(n^2/log n)\\)
[Burcsi et al., FUN 2010; Moosa and Rahman, IPL 2010], or \\(O(n^2/log^2 n)\\) in
the word-RAM model [Moosa and Rahman, JDA 2012]. We propose an index
constructed directly from the run-length encoding of \\(s\\). The construction time
of our index is \\(O(n+\rho^2log \rho)\\), where O(n) is the time for computing
the run-length encoding of \\(s\\) and \\(\rho\\) is the length of this encoding---this
is no worse than previous solutions if \\(\rho = O(n/log n)\\) and better if \\(\rho
= o(n/log n)\\). Our index \\(L\\) can be queried in \\(O(log \rho)\\) time. While
\\(|L|= O(\min(n, \rho^\{2\}))\\) in the worst case, preliminary investigations have
indicated that \\(|L|\\) may often be close to \\(\rho\\). Furthermore, the algorithm
for constructing the index is conceptually simple and easy to implement. In an
attempt to shed light on the structure and size of our index, we characterize
it in terms of the prefix normal forms of \\(s\\) introduced in [Fici and Lipt\'ak,
DLT 2011].