---
layout: publication
title: Streaming Dictionary Matching With Mismatches
authors: "Pawe\u0142 Gawrychowski, Tatiana Starikovskaya"
conference: Algorithmica
year: 2021
bibkey: gawrychowski2018streaming
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.02517'}]
tags: []
short_authors: "Pawe\u0142 Gawrychowski, Tatiana Starikovskaya"
---
In the \\(k\\)-mismatch problem we are given a pattern of length \\(n\\) and a text
and must find all locations where the Hamming distance between the pattern and
the text is at most \\(k\\). A series of recent breakthroughs have resulted in an
ultra-efficient streaming algorithm for this problem that requires only \\(O(k
log \frac\{n\}\{k\})\\) space and \\(O(log \frac\{n\}\{k\} (\sqrt\{k log k\} + log^3 n))\\)
time per letter [Clifford, Kociumaka, Porat, SODA 2019]. In this work, we
consider a strictly harder problem called dictionary matching with \\(k\\)
mismatches. In this problem, we are given a dictionary of \\(d\\) patterns, where
the length of each pattern is at most \\(n\\), and must find all substrings of the
text that are within Hamming distance \\(k\\) from one of the patterns. We develop
a streaming algorithm for this problem with \\(O(k d log^k d
\mathrm\{polylog\}(n))\\) space and \\(O(k log^\{k\} d \mathrm\{polylog\}(n) +
|\mathrm\{occ\}|)\\) time per position of the text. The algorithm is randomised and
outputs correct answers with high probability. On the lower bound side, we show
that any streaming algorithm for dictionary matching with \\(k\\) mismatches
requires \\(Ω(k d)\\) bits of space.