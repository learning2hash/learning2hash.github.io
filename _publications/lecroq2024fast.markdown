---
layout: publication
title: A Fast Implementation Of The Good-suffix Array For The Boyer-moore String Matching
  Algorithm
authors: Thierry Lecroq
conference: Arxiv
year: 2024
bibkey: lecroq2024fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16469'}]
tags: ["Efficiency", "Tools & Libraries"]
short_authors: Thierry Lecroq
---
String matching is the problem of finding all the occurrences of a pattern in
a text. It has been intensively studied and the Boyer-Moore string matching
algorithm is probably one of the most famous solution to this problem. This
algorithm uses two precomputed shift tables called the good-suffix table and
the bad-character table. The good-suffix table is tricky to compute in linear
time. Text book solutions perform redundant operations. Here we present a fast
implementation for this good-suffix table based on a tight analysis of the
pattern. Experimental results show two versions of this new implementation are
the fastest in almost all tested situations.