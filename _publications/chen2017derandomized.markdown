---
layout: publication
title: Derandomized Balanced Allocation
authors: Chen Xue
conference: "Arxiv"
year: 2017
bibkey: chen2017derandomized
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1702.03375"}
tags: ['ARXIV', 'Independent']
---
In this paper, we study the maximum loads of explicit hash families in the
\\(d\\)-choice schemes when allocating sequentially \\(n\\) balls into \\(n\\) bins. We
consider the *Uniform-Greedy* scheme, which provides \\(d\\) independent bins
for each ball and places the ball into the bin with the least load, and its
non-uniform variant --- the *Always-Go-Left* scheme introduced by
V\"ocking. We construct a hash family with \\(O(log n log log n)\\) random bits
based on the previous work of Celis et al. and show the following results.
  1. With high probability, this hash family has a maximum load of \\(\frac\{log
log n\}\{log d\} + O(1)\\) in the *Uniform-Greedy* scheme.
  2. With high probability, it has a maximum load of \\(\frac\{log log n\}\{d log
\phi_d\} + O(1)\\) in the *Always-Go-Left* scheme for a constant
\\(\phi_d>1.61\\).
  The maximum loads of our hash family match the maximum loads of a perfectly
random hash function in the *Uniform-Greedy* and *Always-Go-Left*
scheme separately, up to the low order term of constants. Previously, the best
known hash families matching the same maximum loads of a perfectly random hash
function in \\(d\\)-choice schemes were \\(O(log n)\\)-wise independent functions,
which needs \\(\Theta(log^2 n)\\) random bits.
