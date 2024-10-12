---
layout: publication
title: Optimal Las Vegas Locality Sensitive Data Structures
authors: Ahle Thomas Dybdahl
conference: "Arxiv"
year: 2017
bibkey: ahle2017optimal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.02054"}
tags: ['ARXIV', 'LSH', 'Unsupervised']
---
We show that approximate similarity (near neighbour) search can be solved in high dimensions with performance matching state of the art (data independent) Locality Sensitive Hashing, but with a guarantee of no false negatives. Specifically, we give two data structures for common problems. For \(c\)-approximate near neighbour in Hamming space we get query time \(dn^\&amp;\#123;1/c+o(1)\&amp;\#125;\) and space \(dn^\&amp;\#123;1+1/c+o(1)\&amp;\#125;\) matching that of \cite&amp;\#123;indyk1998approximate&amp;\#125; and answering a long standing open question from~\cite&amp;\#123;indyk2000dimensionality&amp;\#125; and~\cite&amp;\#123;pagh2016locality&amp;\#125; in the affirmative. By means of a new deterministic reduction from \(\ell\_1\) to Hamming we also solve \(\ell\_1\) and \(\ell\_2\) with query time \(d^2n^\&amp;\#123;1/c+o(1)\&amp;\#125;\) and space $d^2 n^&amp;\#123;1+1/c+o(1)&amp;\#125;$. For \((s\_1,s\_2)\)-approximate Jaccard similarity we get query time \(dn^\&amp;\#123;\rho+o(1)\&amp;\#125;\) and space \(dn^\&amp;\#123;1+\rho+o(1)\&amp;\#125;\), \(\rho=\log\frac\&amp;\#123;1+s\_1\&amp;\#125;\&amp;\#123;2s\_1\&amp;\#125;\big/\log\frac\&amp;\#123;1+s\_2\&amp;\#125;\&amp;\#123;2s\_2\&amp;\#125;\), when sets have equal size, matching the performance of~\cite&amp;\#123;tobias2016&amp;\#125;. The algorithms are based on space partitions, as with classic LSH, but we construct these using a combination of brute force, tensoring, perfect hashing and splitter functions \a la~\cite&amp;\#123;naor1995splitters&amp;\#125;. We also show a new dimensionality reduction lemma with 1-sided error.
