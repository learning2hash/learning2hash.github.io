---
layout: publication
title: Hamming Distance Oracle
authors: Itai Boneh, Dvir Fried, Shay Golan, Matan Kraus
conference: Arxiv
year: 2024
bibkey: boneh2024hamming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.05430'}]
tags: ["Efficiency"]
short_authors: Boneh et al.
---
In this paper, we present and study the *Hamming distance oracle
problem*. In this problem, the task is to preprocess two strings \(S\) and \(T\) of
lengths \(n\) and \(m\), respectively, to obtain a data-structure that is able to
answer queries regarding the Hamming distance between a substring of \(S\) and a
substring of \(T\).
  For a constant size alphabet strings, we show that for every \(x\le nm\) there
is a data structure with \(\tilde\{O\}(nm/x)\) preprocess time and \(O(x)\) query
time. We also provide a combinatorial conditional lower bound, showing that for
every \(\epsilon > 0\) and \(x \le nm\) there is no data structure with query
time \(O(x)\) and preprocess time \(O((\frac\{nm\}\{x\})^\{1-\epsilon\})\) unless
combinatorial fast matrix multiplication is possible.
  For strings over general alphabet, we present a data structure with
\(\tilde\{O\}(nm/\sqrt\{x\})\) preprocess time and \(O(x)\) query time for every \(x \le
nm\).