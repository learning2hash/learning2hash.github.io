---
layout: publication
title: Longest Common Prefixes With \(k\)-errors And Applications
authors: Lorraine A. K. Ayad, Panagiotis Charalampopoulos, Costas S. Iliopoulos, Solon
  P. Pissis
conference: Lecture Notes in Computer Science
year: 2018
bibkey: ayad2018longest
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.04425'}]
tags: []
short_authors: Ayad et al.
---
Although real-world text datasets, such as DNA sequences, are far from being
uniformly random, average-case string searching algorithms perform
significantly better than worst-case ones in most applications of interest. In
this paper, we study the problem of computing the longest prefix of each suffix
of a given string of length \(n\) over a constant-sized alphabet that occurs
elsewhere in the string with \(k\)-errors. This problem has already been studied
under the Hamming distance model. Our first result is an improvement upon the
state-of-the-art average-case time complexity for non-constant \(k\) and using
only linear space under the Hamming distance model. Notably, we show that our
technique can be extended to the edit distance model with the same time and
space complexities. Specifically, our algorithms run in \(\mathcal\{O\}(n log^k n
log log n)\) time on average using \(\mathcal\{O\}(n)\) space. We show that our
technique is applicable to several algorithmic problems in computational
biology and elsewhere.