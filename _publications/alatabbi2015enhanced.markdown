---
layout: publication
title: Enhanced Covers Of Regular & Indeterminate Strings Using Prefix Tables
authors: Ali Alatabbi, A. S. Sohidull Islam, M. Sohel Rahman, Jamie Simpson, W. F.
  Smyth
conference: Arxiv
year: 2015
bibkey: alatabbi2015enhanced
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.06793'}]
tags: []
short_authors: Alatabbi et al.
---
A \itbf\{cover\} of a string \(x = x[1..n]\) is a proper substring \(u\) of \(x\)
such that \(x\) can be constructed from possibly overlapping instances of \(u\). A
recent paper \cite\{FIKPPST13\} relaxes this definition --- an \itbf\{enhanced
cover\} \(u\) of \(x\) is a border of \(x\) (that is, a proper prefix that is also a
suffix) that covers a \{\it maximum\} number of positions in \(x\) (not necessarily
all) --- and proposes efficient algorithms for the computation of enhanced
covers. These algorithms depend on the prior computation of the \itbf\{border
array\} \(\beta[1..n]\), where \(\beta[i]\) is the length of the longest border of
\(x[1..i]\), \(1 \le i \le n\). In this paper, we first show how to compute
enhanced covers using instead the \itbf\{prefix table\}: an array \(\pi[1..n]\)
such that \(\pi[i]\) is the length of the longest substring of \(x\) beginning at
position \(i\) that matches a prefix of \(x\). Unlike the border array, the prefix
table is robust: its properties hold also for \itbf\{indeterminate strings\} ---
that is, strings defined on \{\it subsets\} of the alphabet \(\Sigma\) rather than
individual elements of \(\Sigma\). Thus, our algorithms, in addition to being
faster in practice and more space-efficient than those of \cite\{FIKPPST13\},
allow us to easily extend the computation of enhanced covers to indeterminate
strings. Both for regular and indeterminate strings, our algorithms execute in
expected linear time. Along the way we establish an important theoretical
result: that the expected maximum length of any border of any prefix of a
regular string \(x\) is approximately 1.64 for binary alphabets, less for larger
ones.