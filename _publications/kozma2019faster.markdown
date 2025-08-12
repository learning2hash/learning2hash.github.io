---
layout: publication
title: Faster And Simpler Algorithms For Finding Large Patterns In Permutations
authors: "L\xE1szl\xF3 Kozma"
conference: Arxiv
year: 2019
bibkey: kozma2019faster
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.08809'}]
tags: ["Efficiency", "Scalability"]
short_authors: "L\xE1szl\xF3 Kozma"
---
Permutation patterns and pattern avoidance have been intensively studied in
combinatorics and computer science, going back at least to the seminal work of
Knuth on stack-sorting (1968). Perhaps the most natural algorithmic question in
this area is deciding whether a given permutation of length \(n\) contains a
given pattern of length \(k\).
  In this work we give two new algorithms for this well-studied problem, one
whose running time is \(n^\{0.44k+o(k)\}\), and one whose running time is the
better of \(O(1.6181^n)\) and \(n^\{k/2+o(k)\}\). These results improve the earlier
best bounds of Ahal and Rabinovich (2000), and Bruner and Lackner (2012), and
are the fastest algorithms for the problem when \(k = Ω(log n)\). When \(k =
o(log n)\), the parameterized algorithm of Guillemot and Marx (2013) dominates.
  Our second algorithm uses polynomial space and is significantly simpler than
all previous approaches with comparable running times, including an
\(n^\{k/2+o(k)\}\) algorithm proposed by Guillemot and Marx. Our approach can be
summarized as follows: "for every matching of the even-valued entries of the
pattern, try to match all odd-valued entries left-to-right". For the special
case of patterns that are Jordan-permutations, we show an improved,
subexponential running time.