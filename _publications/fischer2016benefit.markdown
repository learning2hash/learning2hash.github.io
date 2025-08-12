---
layout: publication
title: On The Benefit Of Merging Suffix Array Intervals For Parallel Pattern Matching
authors: "Johannes Fischer, Dominik K\xF6ppl, Florian Kurpicz"
conference: Arxiv
year: 2016
bibkey: fischer2016benefit
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.02465'}]
tags: []
short_authors: "Johannes Fischer, Dominik K\xF6ppl, Florian Kurpicz"
---
We present parallel algorithms for exact and approximate pattern matching
with suffix arrays, using a CREW-PRAM with \(p\) processors. Given a static text
of length \(n\), we first show how to compute the suffix array interval of a
given pattern of length \(m\) in \(O(\frac\{m\}\{p\}+ \lg p + \lg\lg p\cdot\lg\lg n)\)
time for \(p \le m\). For approximate pattern matching with \(k\) differences or
mismatches, we show how to compute all occurrences of a given pattern in
\(O(\frac\{m^k\sigma^k\}\{p\}\max\left(k,\lg\lg n\right)\!+\!(1+\frac\{m\}\{p\}) \lg
p\cdot \lg\lg n + \text\{occ\})\) time, where \(\sigma\) is the size of the alphabet
and \(p \le \sigma^k m^k\). The workhorse of our algorithms is a data structure
for merging suffix array intervals quickly: Given the suffix array intervals
for two patterns \(P\) and \(P'\), we present a data structure for computing the
interval of \(PP'\) in \(O(\lg\lg n)\) sequential time, or in \(O(1+\lg_p\lg n)\)
parallel time. All our data structures are of size \(O(n)\) bits (in addition to
the suffix array).