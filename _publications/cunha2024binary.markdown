---
layout: publication
title: 'Binary Jumbled Indexing: Suffix Tree Histogram'
authors: "Lu\xEDs Cunha, M\xE1rio Medina"
conference: Arxiv
year: 2024
bibkey: cunha2024binary
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.00111'}]
tags: ["Hashing Methods", "Tree Based ANN", "Vector Indexing"]
short_authors: "Lu\xEDs Cunha, M\xE1rio Medina"
---
Given a binary string \(\omega\) over the alphabet \(\\{0, 1\\}\), a vector \((a,
b)\) is a Parikh vector if and only if a factor of \(\omega\) contains exactly \(a\)
occurrences of \(0\) and \(b\) occurrences of \(1\). Answering whether a vector is a
Parikh vector of \(\omega\) is known as the Binary Jumbled Indexing Problem
(BJPMP) or the Histogram Indexing Problem. Most solutions to this problem rely
on an \(O(n)\) word-space index to answer queries in constant time, encoding the
Parikh set of \(\omega\), i.e., all its Parikh vectors. Cunha et al.
(Combinatorial Pattern Matching, 2017) introduced an algorithm (JBM2017), which
computes the index table in \(O(n+\rho^2)\) time, where \(\rho\) is the number of
runs of identical digits in \(\omega\), leading to \(O(n^2)\) in the worst case. We
prove that the average number of runs \(\rho\) is \(n/4\), confirming the quadratic
behavior also in the average-case. We propose a new algorithm, SFTree, which
uses a suffix tree to remove duplicate substrings. Although SFTree also has an
average-case complexity of \(\Theta(n^2)\) due to the fundamental reliance on run
boundaries, it achieves practical improvements by minimizing memory access
overhead through vectorization. The suffix tree further allows distinct
substrings to be processed efficiently, reducing the effective cost of memory
access. As a result, while both algorithms exhibit similar theoretical growth,
SFTree significantly outperforms others in practice. Our analysis highlights
both the theoretical and practical benefits of the SFTree approach, with
potential extensions to other applications of suffix trees.