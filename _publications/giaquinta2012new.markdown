---
layout: publication
title: New Algorithms For Binary Jumbled Pattern Matching
authors: Emanuele Giaquinta, Szymon Grabowski
conference: Information Processing Letters
year: 2013
bibkey: giaquinta2012new
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1210.6176'}]
tags: ["Efficiency"]
short_authors: Emanuele Giaquinta, Szymon Grabowski
---
Given a pattern \\(P\\) and a text \\(T\\), both strings over a binary alphabet, the
binary jumbled string matching problem consists in telling whether any
permutation of \\(P\\) occurs in \\(T\\). The indexed version of this problem, i.e.,
preprocessing a string to efficiently answer such permutation queries, is hard
and has been studied in the last few years. Currently the best bounds for this
problem are \\(O(n^2/log^2 n)\\) (with O(n) space and O(1) query time) and
\\(O(r^2log r)\\) (with O(|L|) space and \\(O(log|L|)\\) query time), where \\(r\\) is
the length of the run-length encoding of \\(T\\) and \\(|L| = O(n)\\) is the size of
the index. In this paper we present new results for this problem. Our first
result is an alternative construction of the index by Badkobeh et al. that
obtains a trade-off between the space and the time complexity. It has
\\(O(r^2log k + n/k)\\) complexity to build the index, \\(O(log k)\\) query time, and
uses \\(O(n/k + |L|)\\) space, where \\(k\\) is a parameter. The second result is an
\\(O(n^2 log^2 w / w)\\) algorithm (with O(n) space and O(1) query time), based on
word-level parallelism where \\(w\\) is the word size in bits.