---
layout: publication
title: Streaming Algorithms For Computing Edit Distance Without Exploiting Suffix
  Trees
authors: "Diptarka Chakraborty, Elazar Goldenberg, Michal Kouck\xFD"
conference: Arxiv
year: 2016
bibkey: chakraborty2016streaming
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.03718'}]
tags: ["Efficiency", "Scalability"]
short_authors: "Diptarka Chakraborty, Elazar Goldenberg, Michal Kouck\xFD"
---
The edit distance is a way of quantifying how similar two strings are to one
another by counting the minimum number of character insertions, deletions, and
substitutions required to transform one string into the other.
  In this paper we study the computational problem of computing the edit
distance between a pair of strings where their distance is bounded by a
parameter \(k\ll n\). We present two streaming algorithms for computing edit
distance: One runs in time \(O(n+k^2)\) and the other \(n+O(k^3)\). By writing
\(n+O(k^3)\) we want to emphasize that the number of operations per an input
symbol is a small constant. In particular, the running time does not depend on
the alphabet size, and the algorithm should be easy to implement.
  Previously a streaming algorithm with running time \(O(n+k^4)\) was given in
the paper by the current authors (STOC'16). The best off-line algorithm runs in
time \(O(n+k^2)\) (Landau et al., 1998) which is known to be optimal under the
Strong Exponential Time Hypothesis.