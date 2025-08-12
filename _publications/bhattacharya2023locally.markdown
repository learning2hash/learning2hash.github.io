---
layout: publication
title: Locally Consistent Decomposition Of Strings With Applications To Edit Distance
  Sketching
authors: "Sudatta Bhattacharya, Michal Kouck\xFD"
conference: Proceedings of the 55th Annual ACM Symposium on Theory of Computing
year: 2023
bibkey: bhattacharya2023locally
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.04475'}]
tags: ["Distance Metric Learning"]
short_authors: "Sudatta Bhattacharya, Michal Kouck\xFD"
---
In this paper we provide a new locally consistent decomposition of strings.
Each string \(x\) is decomposed into blocks that can be described by grammars of
size \(\widetilde\{O\}(k)\) (using some amount of randomness). If we take two
strings \(x\) and \(y\) of edit distance at most \(k\) then their block decomposition
uses the same number of grammars and the \(i\)-th grammar of \(x\) is the same as
the \(i\)-th grammar of \(y\) except for at most \(k\) indexes \(i\). The edit distance
of \(x\) and \(y\) equals to the sum of edit distances of pairs of blocks where \(x\)
and \(y\) differ. Our decomposition can be used to design a sketch of size
\(\widetilde\{O\}(k^2)\) for edit distance, and also a rolling sketch for edit
distance of size \(\widetilde\{O\}(k^2)\). The rolling sketch allows to update the
sketched string by appending a symbol or removing a symbol from the beginning
of the string.