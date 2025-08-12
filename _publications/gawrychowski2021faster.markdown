---
layout: publication
title: Faster Exponential Algorithm For Permutation Pattern Matching
authors: Pawel Gawrychowski, Mateusz Rzepecki
conference: Symposium on Simplicity in Algorithms (SOSA)
year: 2022
bibkey: gawrychowski2021faster
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.11475'}]
tags: ["Efficiency"]
short_authors: Pawel Gawrychowski, Mateusz Rzepecki
---
The Permutation Pattern Matching problem asks, given two permutations
\\(\sigma\\) on \\(n\\) elements and \\(\pi\\), whether \\(\sigma\\) admits a subsequence with
the same relative order as \\(\pi\\) (or, in the counting version, how many such
subsequences are there). This natural problem was shown by Bose, Buss and Lubiw
[IPL 1998] to be NP-complete, and hence we should seek exact exponential time
solutions. The asymptotically fastest such solution up to date, by Berendsohn,
Kozma and Marx [IPEC 2019], works in \\(\mathcal\{O\}(1.6181^n)\\) time. We design a
simple and faster \\(\mathcal\{O\}(1.415^\{n\})\\) time algorithm for both the
detection and the counting version. We also prove that this is optimal among a
certain natural class of algorithms.