---
layout: publication
title: 'Faster Approximate Pattern Matching: A Unified Approach'
authors: Panagiotis Charalampopoulos, Tomasz Kociumaka, Philip Wellnitz
conference: 2020 IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS)
year: 2020
bibkey: charalampopoulos2020faster
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.08350'}]
tags: []
short_authors: Panagiotis Charalampopoulos, Tomasz Kociumaka, Philip Wellnitz
---
Approximate pattern matching is a natural and well-studied problem on
strings: Given a text \(T\), a pattern \(P\), and a threshold \(k\), find (the
starting positions of) all substrings of \(T\) that are at distance at most \(k\)
from \(P\). We consider the two most fundamental string metrics: the Hamming
distance and the edit distance. Under the Hamming distance, we search for
substrings of \(T\) that have at most \(k\) mismatches with \(P\), while under the
edit distance, we search for substrings of \(T\) that can be transformed to \(P\)
with at most \(k\) edits.
  Exact occurrences of \(P\) in \(T\) have a very simple structure: If we assume
for simplicity that \(|T| \le 3|P|/2\) and trim \(T\) so that \(P\) occurs both as a
prefix and as a suffix of \(T\), then both \(P\) and \(T\) are periodic with a common
period. However, an analogous characterization for the structure of occurrences
with up to \(k\) mismatches was proved only recently by Bringmann et al.
[SODA'19]: Either there are \(O(k^2)\) \(k\)-mismatch occurrences of \(P\) in \(T\), or
both \(P\) and \(T\) are at Hamming distance \(O(k)\) from strings with a common
period \(O(m/k)\). We tighten this characterization by showing that there are
\(O(k)\) \(k\)-mismatch occurrences in the case when the pattern is not
(approximately) periodic, and we lift it to the edit distance setting, where we
tightly bound the number of \(k\)-edit occurrences by \(O(k^2)\) in the
non-periodic case. Our proofs are constructive and let us obtain a unified
framework for approximate pattern matching for both considered distances. We
showcase the generality of our framework with results for the fully-compressed
setting (where \(T\) and \(P\) are given as a straight-line program) and for the
dynamic setting (where we extend a data structure of Gawrychowski et al.
[SODA'18]).