---
layout: publication
title: Locality-sensitive Hashing Without False Negatives For L_p
authors: Andrzej Pacuk, Piotr Sankowski, Karol Wegrzycki, Piotr Wygocki
conference: Lecture Notes in Computer Science
year: 2016
bibkey: pacuk2016locality
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.09317'}]
tags: [Hashing Methods, Efficiency]
short_authors: Pacuk et al.
---
In this paper, we show a construction of locality-sensitive hash functions
without false negatives, i.e., which ensure collision for every pair of points
within a given radius \(R\) in \(d\) dimensional space equipped with \(l_p\) norm
when \(p \in [1,\infty]\). Furthermore, we show how to use these hash functions
to solve the \(c\)-approximate nearest neighbor search problem without false
negatives. Namely, if there is a point at distance \(R\), we will certainly
report it and points at distance greater than \(cR\) will not be reported for
\(c=Ω(\sqrt\{d\},d^\{1-\frac\{1\}\{p\}\})\). The constructed algorithms work: - with
preprocessing time \(\mathcal\{O\}(n log(n))\) and sublinear expected query time,
- with preprocessing time \(\mathcal\{O\}(\mathrm\{poly\}(n))\) and expected query
time \(\mathcal\{O\}(log(n))\). Our paper reports progress on answering the open
problem presented by Pagh [8] who considered the nearest neighbor search
without false negatives for the Hamming distance.