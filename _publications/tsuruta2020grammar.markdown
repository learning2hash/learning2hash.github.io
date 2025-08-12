---
layout: publication
title: Grammar-compressed Self-index With Lyndon Words
authors: "Kazuya Tsuruta, Dominik K\xF6ppl, Yuto Nakashima, Shunsuke Inenaga, Hideo\
  \ Bannai, Masayuki Takeda"
conference: Arxiv
year: 2020
bibkey: tsuruta2020grammar
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.05309'}]
tags: []
short_authors: Tsuruta et al.
---
We introduce a new class of straight-line programs (SLPs), named the Lyndon
SLP, inspired by the Lyndon trees (Barcelo, 1990). Based on this SLP, we
propose a self-index data structure of \(O(g)\) words of space that can be built
from a string \(T\) in \(O(n \lg n)\) expected time, retrieving the starting
positions of all occurrences of a pattern \(P\) of length \(m\) in \(O(m + \lg m \lg
n + occ \lg g)\) time, where \(n\) is the length of \(T\), \(g\) is the size of the
Lyndon SLP for \(T\), and \(occ\) is the number of occurrences of \(P\) in \(T\).