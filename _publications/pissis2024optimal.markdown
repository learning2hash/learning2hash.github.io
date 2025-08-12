---
layout: publication
title: Optimal Prefix-suffix Queries With Applications
authors: Solon P. Pissis
conference: 2025 Symposium on Simplicity in Algorithms (SOSA)
year: 2025
bibkey: pissis2024optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.03784'}]
tags: ["Efficiency"]
short_authors: Solon P. Pissis
---
We revisit the classic border tree data structure [Gu, Farach, Beigel, SODA
1994] that answers the following prefix-suffix queries on a string \\(T\\) of
length \\(n\\) over an integer alphabet \\(\Sigma=[0,\sigma)\\): for any \\(i,j \in
[0,n)\\) return all occurrences of \\(T\\) in \\(T[0\mathinner\{.\,.\}
i]T[j\mathinner\{.\,.\} n-1]\\). The border tree of \\(T\\) can be constructed in
\\(\mathcal\{O\}(n)\\) time and answers prefix-suffix queries in \\(\mathcal\{O\}(log n
+ \textsf\{Occ\})\\) time, where \\(\textsf\{Occ\}\\) is the number of occurrences of \\(T\\)
in \\(T[0\mathinner\{.\,.\} i]T[j\mathinner\{.\,.\} n-1]\\). Our contribution here is
the following. We present a completely different and remarkably simple data
structure that can be constructed in the optimal \\(\mathcal\{O\}(n/log_\sigma n)\\)
time and supports queries in the optimal \\(\mathcal\{O\}(1)\\) time. Our result is
based on a new structural lemma that lets us encode the output of any query in
constant time and space. We also show a new direct application of our result in
pattern matching on node-labeled graphs.