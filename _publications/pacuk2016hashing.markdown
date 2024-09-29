---
layout: publication
title: Locality45;sensitive Hashing Without False Negatives For L95;p
authors: Pacuk Andrzej, Sankowski Piotr, Wegrzycki Karol, Wygocki Piotr
conference: "Computing and Combinatorics -"
year: 2016
bibkey: pacuk2016hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.09317"}
tags: ['Independent']
---
In this paper we show a construction of locality45;sensitive hash functions without false negatives i.e. which ensure collision for every pair of points within a given radius R in d dimensional space equipped with l95;p norm when p in 1∞. Furthermore we show how to use these hash functions to solve the c45;approximate nearest neighbor search problem without false negatives. Namely if there is a point at distance R we will certainly report it and points at distance greater than cR will not be reported for c=Omega(sqrt123;d125;d^123;145;frac123;1125;123;p125;125;). The constructed algorithms work 45; with preprocessing time mathcal123;O125;(n log(n)) and sublinear expected query time 45; with preprocessing time mathcal123;O125;(mathrm123;poly125;(n)) and expected query time mathcal123;O125;(log(n)). Our paper reports progress on answering the open problem presented by Pagh 8 who considered the nearest neighbor search without false negatives for the Hamming distance.
