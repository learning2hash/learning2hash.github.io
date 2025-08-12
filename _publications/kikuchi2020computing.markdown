---
layout: publication
title: Computing Covers Under Substring Consistent Equivalence Relations
authors: Natsumi Kikuchi, Diptarama Hendrian, Ryo Yoshinaka, Ayumi Shinohara
conference: Lecture Notes in Computer Science
year: 2020
bibkey: kikuchi2020computing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06764'}]
tags: []
short_authors: Kikuchi et al.
---
Covers are a kind of quasiperiodicity in strings. A string \(C\) is a cover of
another string \(T\) if any position of \(T\) is inside some occurrence of \(C\) in
\(T\). The shortest and longest cover arrays of \(T\) have the lengths of the
shortest and longest covers of each prefix of \(T\), respectively. The literature
has proposed linear-time algorithms computing longest and shortest cover arrays
taking border arrays as input. An equivalence relation \(\approx\) over strings
is called a substring consistent equivalence relation (SCER) iff \(X \approx Y\)
implies (1) \(|X| = |Y|\) and (2) \(X[i:j] \approx Y[i:j]\) for all \(1 \le i \le j
\le |X|\). In this paper, we generalize the notion of covers for SCERs and prove
that existing algorithms to compute the shortest cover array and the longest
cover array of a string \(T\) under the identity relation will work for any SCERs
taking the accordingly generalized border arrays.