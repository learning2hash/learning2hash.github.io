---
layout: publication
title: 'POPE: Partial Order Preserving Encoding'
authors: Daniel S. Roche, Daniel Apon, Seung Geol Choi, Arkady Yerukhimovich
conference: Arxiv
year: 2015
bibkey: roche2015pope
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.04025'}]
tags: []
short_authors: Roche et al.
---
Recently there has been much interest in performing search queries over
encrypted data to enable functionality while protecting sensitive data. One
particularly efficient mechanism for executing such queries is order-preserving
encryption/encoding (OPE) which results in ciphertexts that preserve the
relative order of the underlying plaintexts thus allowing range and comparison
queries to be performed directly on ciphertexts. In this paper, we propose an
alternative approach to range queries over encrypted data that is optimized to
support insert-heavy workloads as are common in "big data" applications while
still maintaining search functionality and achieving stronger security.
Specifically, we propose a new primitive called partial order preserving
encoding (POPE) that achieves ideal OPE security with frequency hiding and also
leaves a sizable fraction of the data pairwise incomparable. Using only O(1)
persistent and \(O(n^\epsilon)\) non-persistent client storage for
\(0<\epsilon<1\), our POPE scheme provides extremely fast batch insertion
consisting of a single round, and efficient search with O(1) amortized cost for
up to \(O(n^\{1-\epsilon\})\) search queries. This improved security and
performance makes our scheme better suited for today's insert-heavy databases.