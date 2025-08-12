---
layout: publication
title: Sparse Suffix Tree Construction With Small Space
authors: "Philip Bille, Inge Li G\xF8rtz, Tsvi Kopelowitz, Benjamin Sach, Hjalte Wedel\
  \ Vildh\xF8j"
conference: Lecture Notes in Computer Science
year: 2013
bibkey: bille2012sparse
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1207.1135'}]
tags: ["Memory Efficiency", "Tree Based ANN"]
short_authors: Bille et al.
---
We consider the problem of constructing a sparse suffix tree (or suffix
array) for \\(b\\) suffixes of a given text \\(T\\) of size \\(n\\), using only \\(O(b)\\)
words of space during construction time. Breaking the naive bound of
\\(Ω(nb)\\) time for this problem has occupied many algorithmic researchers
since a different structure, the (evenly spaced) sparse suffix tree, was
introduced by K\{\"a\}rkk\{\"a\}inen and Ukkonen in 1996. While in the evenly
spaced sparse suffix tree the suffixes considered must be evenly spaced in \\(T\\),
here there is no constraint on the locations of the suffixes.
  We show that the sparse suffix tree can be constructed in \\(O(nlog^2b)\\) time.
To achieve this we develop a technique, which may be of independent interest,
that allows to efficiently answer \\(b\\) longest common prefix queries on suffixes
of \\(T\\), using only \\(O(b)\\) space. We expect that this technique will prove
useful in many other applications in which space usage is a concern.
Furthermore, additional tradeoffs between the space usage and the construction
time are given.