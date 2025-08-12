---
layout: publication
title: Logarithmically Larger Deletion Codes Of All Distances
authors: Noga Alon, Gabriela Bourla, Ben Graham, Xiaoyu He, Noah Kravitz
conference: IEEE Transactions on Information Theory
year: 2023
bibkey: alon2022logarithmically
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.11882'}]
tags: ["Compact Codes", "Efficiency", "Memory Efficiency", "Robustness", "Scalability"]
short_authors: Alon et al.
---
The deletion distance between two binary words \\(u,v \in \\{0,1\\}^n\\) is the
smallest \\(k\\) such that \\(u\\) and \\(v\\) share a common subsequence of length \\(n-k\\).
A set \\(C\\) of binary words of length \\(n\\) is called a \\(k\\)-deletion code if every
pair of distinct words in \\(C\\) has deletion distance greater than \\(k\\). In 1965,
Levenshtein initiated the study of deletion codes by showing that, for \\(k\ge 1\\)
fixed and \\(n\\) going to infinity, a \\(k\\)-deletion code \\(C\subseteq \\{0,1\\}^n\\) of
maximum size satisfies \\(Ω_k(2^n/n^\{2k\}) \leq |C| \leq O_k( 2^n/n^k)\\). We
make the first asymptotic improvement to these bounds by showing that there
exist \\(k\\)-deletion codes with size at least \\(Ω_k(2^n log n/n^\{2k\})\\). Our
proof is inspired by Jiang and Vardy's improvement to the classical
Gilbert--Varshamov bounds. We also establish several related results on the
number of longest common subsequences and shortest common supersequences of a
pair of words with given length and deletion distance.