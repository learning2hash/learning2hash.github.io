---
layout: publication
title: Improved Approximation Guarantees For Shortest Superstrings Using Cycle Classification
  By Overlap To Length Ratios
authors: "Matthias Englert, Nicolaos Matsakis, Pavel Vesel\xFD"
conference: Proceedings of the 54th Annual ACM SIGACT Symposium on Theory of Computing
year: 2022
bibkey: englert2021improved
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.03968'}]
tags: []
short_authors: "Matthias Englert, Nicolaos Matsakis, Pavel Vesel\xFD"
---
In the Shortest Superstring problem, we are given a set of strings and we are
asking for a common superstring, which has the minimum number of characters.
The Shortest Superstring problem is NP-hard and several constant-factor
approximation algorithms are known for it. Of particular interest is the GREEDY
algorithm, which repeatedly merges two strings of maximum overlap until a
single string remains. The GREEDY algorithm, being simpler than other
well-performing approximation algorithms for this problem, has attracted
attention since the 1980s and is commonly used in practical applications.
  Tarhio and Ukkonen (TCS 1988) conjectured that GREEDY gives a
2-approximation. In a seminal work, Blum, Jiang, Li, Tromp, and Yannakakis
(STOC 1991) proved that the superstring computed by GREEDY is a
4-approximation, and this upper bound was improved to 3.5 by Kaplan and Shafrir
(IPL 2005).
  We show that the approximation guarantee of GREEDY is at most
\\((13+\sqrt\{57\})/6 \approx 3.425\\), making the first progress on this question
since 2005. Furthermore, we prove that the Shortest Superstring can be
approximated within a factor of \\((37+\sqrt\{57\})/18\approx 2.475\\), improving
slightly upon the currently best \\(2\frac\{11\}\{23\}\\)-approximation algorithm by
Mucha (SODA 2013).