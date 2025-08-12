---
layout: publication
title: An Optimal-time RLBWT Construction In Bwt-runs Bounded Space
authors: Takaaki Nishimoto, Shunsuke Kanda, Yasuo Tabei
conference: Arxiv
year: 2022
bibkey: nishimoto2022optimal
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.07885'}]
tags: []
short_authors: Takaaki Nishimoto, Shunsuke Kanda, Yasuo Tabei
---
The compression of highly repetitive strings (i.e., strings with many
repetitions) has been a central research topic in string processing, and quite
a few compression methods for these strings have been proposed thus far. Among
them, an efficient compression format gathering increasing attention is the
run-length Burrows--Wheeler transform (RLBWT), which is a run-length encoded
BWT as a reversible permutation of an input string on the lexicographical order
of suffixes. State-of-the-art construction algorithms of RLBWT have a serious
issue with respect to (i) non-optimal computation time or (ii) a working space
that is linearly proportional to the length of an input string. In this paper,
we present *r-comp*, the first optimal-time construction algorithm of
RLBWT in BWT-runs bounded space. That is, the computational complexity of
r-comp is \(O(n + r log\{r\})\) time and \(O(rlog\{n\})\) bits of working space for
the length \(n\) of an input string and the number \(r\) of equal-letter runs in
BWT. The computation time is optimal (i.e., \(O(n)\)) for strings with the
property \(r=O(n/log\{n\})\), which holds for most highly repetitive strings.
Experiments using a real-world dataset of highly repetitive strings show the
effectiveness of r-comp with respect to computation time and space.