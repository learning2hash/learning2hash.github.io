---
layout: publication
title: Approximately Minwise Independence with Twisted Tabulation
authors: Dahlgaard Søren, Thorup Mikkel
conference: "Arxiv"
year: 2014
bibkey: dahlgaard2014approximately
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1404.6724"}
tags: ['ARXIV', 'FOCS']
---
A random hash function h is \varepsilon-minwise if for any set S S=n and element x\in S \Prh(x)=\min h(S)=(1\pm\varepsilon)/n. Minwise hash functions with low bias \varepsilon have widespread applications within similarity estimation. Hashing from a universe u the twisted tabulation hashing of Ptracu and Thorup SODA13 makes c=O(1) lookups in tables of size u^1/c. Twisted tabulation was invented to get good concentration for hashing based sampling. Here we show that twisted tabulation yields \tilde O(1/u^1/c)-minwise hashing. In the classic independence paradigm of Wegman and Carter FOCS79 \tilde O(1/u^1/c)-minwise hashing requires \Omega(\log u)-independence Indyk SODA99. Ptracu and Thorup STOC11 had shown that simple tabulation using same space and lookups yields \tilde O(1/n^1/c)-minwise independence which is good for large sets but useless for small sets. Our analysis uses some of the same methods but is much cleaner bypassing a complicated induction argument.
