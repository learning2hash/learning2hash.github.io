---
layout: publication
title: Detecting \(k\)-(sub-)cadences And Equidistant Subsequence Occurrences
authors: Mitsuru Funakoshi, Yuto Nakashima, Shunsuke Inenaga, Hideo Bannai, Masayuki
  Takeda, Ayumi Shinohara
conference: Arxiv
year: 2020
bibkey: funakoshi2020detecting
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06796'}]
tags: []
short_authors: Funakoshi et al.
---
The equidistant subsequence pattern matching problem is considered. Given a
pattern string \(P\) and a text string \(T\), we say that \(P\) is an
*equidistant subsequence* of \(T\) if \(P\) is a subsequence of the text such
that consecutive symbols of \(P\) in the occurrence are equally spaced. We can
consider the problem of equidistant subsequences as generalizations of
(sub-)cadences. We give bit-parallel algorithms that yield \(o(n^2)\) time
algorithms for finding \(k\)-(sub-)cadences and equidistant subsequences.
Furthermore, \(O(nlog^2 n)\) and \(O(nlog n)\) time algorithms, respectively for
equidistant and Abelian equidistant matching for the case \(|P| = 3\), are shown.
The algorithms make use of a technique that was recently introduced which can
efficiently compute convolutions with linear constraints.