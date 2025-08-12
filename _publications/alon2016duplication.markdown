---
layout: publication
title: Duplication Distance To The Root For Binary Sequences
authors: Noga Alon, Jehoshua Bruck, Farzad Farnoud, Siddharth Jain
conference: IEEE Transactions on Information Theory
year: 2017
bibkey: alon2016duplication
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05537'}]
tags: ["Distance Metric Learning"]
short_authors: Alon et al.
---
We study the tandem duplication distance between binary sequences and their
roots. In other words, the quantity of interest is the number of tandem
duplication operations of the form \\(\seq x = \seq a \seq b \seq c \to \seq y =
\seq a \seq b \seq b \seq c\\), where \\(\seq x\\) and \\(\seq y\\) are sequences and
\\(\seq a\\), \\(\seq b\\), and \\(\seq c\\) are their substrings, needed to generate a
binary sequence of length \\(n\\) starting from a square-free sequence from the set
\\(\\{0,1,01,10,010,101\\}\\). This problem is a restricted case of finding the
duplication/deduplication distance between two sequences, defined as the
minimum number of duplication and deduplication operations required to
transform one sequence to the other. We consider both exact and approximate
tandem duplications. For exact duplication, denoting the maximum distance to
the root of a sequence of length \\(n\\) by \\(f(n)\\), we prove that \\(f(n)=\Theta(n)\\).
For the case of approximate duplication, where a \\(\beta\\)-fraction of symbols
may be duplicated incorrectly, we show that the maximum distance has a sharp
transition from linear in \\(n\\) to logarithmic at \\(\beta=1/2\\). We also study the
duplication distance to the root for sequences with a given root and for
special classes of sequences, namely, the de Bruijn sequences, the Thue-Morse
sequence, and the Fibbonaci words. The problem is motivated by genomic tandem
duplication mutations and the smallest number of tandem duplication events
required to generate a given biological sequence.