---
layout: publication
title: Reducing Approximate Longest Common Subsequence To Approximate Edit Distance
authors: Aviad Rubinstein, Zhao Song
conference: Proceedings of the Fourteenth Annual ACM-SIAM Symposium on Discrete Algorithms
year: 2019
bibkey: rubinstein2019reducing
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.05451'}]
tags: []
short_authors: Aviad Rubinstein, Zhao Song
---
Given a pair of strings, the problems of computing their Longest Common
Subsequence and Edit Distance have been extensively studied for decades. For
exact algorithms, LCS and Edit Distance (with character insertions and
deletions) are equivalent; the state of the art running time is (almost)
quadratic and this is tight under plausible fine-grained complexity
assumptions. But for approximation algorithms the picture is different: there
is a long line of works with improved approximation factors for Edit Distance,
but for LCS (with binary strings) only a trivial \(1/2\)-approximation was known.
In this work we give a reduction from approximate LCS to approximate Edit
Distance, yielding the first efficient \((1/2+\epsilon)\)-approximation algorithm
for LCS for some constant \(\epsilon>0\).