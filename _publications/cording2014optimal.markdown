---
layout: publication
title: Optimal Time Random Access To Grammar-compressed Strings In Small Space
authors: Patrick Hagge Cording
conference: Arxiv
year: 2014
bibkey: cording2014optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1410.4701'}]
tags: ["Efficiency"]
short_authors: Patrick Hagge Cording
---
The random access problem for compressed strings is to build a data structure
that efficiently supports accessing the character in position \(i\) of a string
given in compressed form. Given a grammar of size \(n\) compressing a string of
size \(N\), we present a data structure using \(O(n\Delta log_\Delta \frac N n
log N)\) bits of space that supports accessing position \(i\) in \(O(log_\Delta
N)\) time for \(\Delta \leq log^\{O(1)\} N\). The query time is optimal for
polynomially compressible strings, i.e., when \(n=O(N^\{1-\epsilon\})\).