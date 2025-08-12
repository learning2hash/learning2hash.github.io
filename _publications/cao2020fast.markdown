---
layout: publication
title: A Fast Randomized Algorithm For Finding The Maximal Common Subsequences
authors: Jin Cao, Dewei Zhong
conference: Arxiv
year: 2020
bibkey: cao2020fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.03352'}]
tags: []
short_authors: Jin Cao, Dewei Zhong
---
Finding the common subsequences of \(L\) multiple strings has many applications
in the area of bioinformatics, computational linguistics, and information
retrieval. A well-known result states that finding a Longest Common Subsequence
(LCS) for \(L\) strings is NP-hard, e.g., the computational complexity is
exponential in \(L\). In this paper, we develop a randomized algorithm, referred
to as \{\em Random-MCS\}, for finding a random instance of Maximal Common
Subsequence (\(MCS\)) of multiple strings. A common subsequence is \{\em maximal\}
if inserting any character into the subsequence no longer yields a common
subsequence. A special case of MCS is LCS where the length is the longest. We
show the complexity of our algorithm is linear in \(L\), and therefore is
suitable for large \(L\). Furthermore, we study the occurrence probability for a
single instance of MCS and demonstrate via both theoretical and experimental
studies that the longest subsequence from multiple runs of \{\em Random-MCS\}
often yields a solution to \(LCS\).