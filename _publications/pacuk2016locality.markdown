---
layout: publication
title: Locality-sensitive Hashing Without False Negatives For L_p
authors: Pacuk Andrzej, Sankowski Piotr, Wegrzycki Karol, Wygocki Piotr
conference: "Computing and Combinatorics -"
year: 2016
bibkey: pacuk2016locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.09317"}
tags: ['Independent']
---
In this paper we show a construction of locality-sensitive hash functions without false negatives i.e. which ensure collision for every pair of points within a given radius R in d dimensional space equipped with l_p norm when p (in) 1(infty). Furthermore we show how to use these hash functions to solve the c-approximate nearest neighbor search problem without false negatives. Namely if there is a point at distance R we will certainly report it and points at distance greater than cR will not be reported for c=(Omega)((sqrtd)d^1-(frac1)p). The constructed algorithms work - with preprocessing time (mathcalO)(n (log)(n)) and sublinear expected query time - with preprocessing time (mathcalO)((mathrmpoly)(n)) and expected query time (mathcalO)((log)(n)). Our paper reports progress on answering the open problem presented by Pagh 8 who considered the nearest neighbor search without false negatives for the Hamming distance.
