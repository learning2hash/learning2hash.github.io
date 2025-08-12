---
layout: publication
title: A Compressed-gap Data-aware Measure
authors: Nicola Prezza
conference: Arxiv
year: 2015
bibkey: prezza2015compressed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.03288'}]
tags: ["Compact Codes"]
short_authors: Nicola Prezza
---
In this paper, we consider the problem of efficiently representing a set \(S\)
of \(n\) items out of a universe \(U=\\{0,...,u-1\\}\) while supporting a number of
operations on it. Let \(G=g_1...g_n\) be the gap stream associated with \(S\),
\(gap\) its bit-size when encoded with *gap-encoding*, and \(H_0(G)\) its
empirical zero-order entropy. We prove that (1) \(nH_0(G)\in o(gap)\) if \(G\) is
highly compressible, and (2) \(nH_0(G) \leq nlog(u/n) + n \leq uH_0(S)\). Let
\(d\) be the number of *distinct* gap lengths between elements in \(S\). We
firstly propose a new space-efficient zero-order compressed representation of
\(S\) taking \(n(H_0(G)+1)+\mathcal O(dlog u)\) bits of space. Then, we describe a
fully-indexable dictionary that supports *rank* and *select* queries
in \(\mathcal O(log(u/n)+loglog u)\) time while requiring asymptotically the
same space as the proposed compressed representation of \(S\).