---
layout: publication
title: "Locality-Sensitive Hashing without False Negatives for l_p"
authors: Pacuk Andrzej, Sankowski Piotr, Wegrzycki Karol, Wygocki Piotr
conference: Computing and Combinatorics -
year: 2016
bibkey: pacuk2016locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.09317"}
tags: []
---
In this paper, we show a construction of locality-sensitive hash functions without false negatives, i.e., which ensure collision for every pair of points within a given radius $R$ in $d$ dimensional space equipped with $l_p$ norm when $p \in [1,\infty]$. Furthermore, we show how to use these hash functions to solve the $c$-approximate nearest neighbor search problem without false negatives. Namely, if there is a point at distance $R$, we will certainly report it and points at distance greater than $cR$ will not be reported for $c=\Omega(\sqrt\{d\},d^\{1-\frac\{1\}\{p\}\})$. The constructed algorithms work: - with preprocessing time $\mathcal\{O\}(n \log(n))$ and sublinear expected query time, - with preprocessing time $\mathcal\{O\}(\mathrm\{poly\}(n))$ and expected query time $\mathcal\{O\}(\log(n))$. Our paper reports progress on answering the open problem presented by Pagh [8] who considered the nearest neighbor search without false negatives for the Hamming distance.