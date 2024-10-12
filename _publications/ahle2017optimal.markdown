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
We show that approximate similarity (near neighbour) search can be solved in high dimensions with performance matching state of the art (data independent) Locality Sensitive Hashing, but with a guarantee of no false negatives. Specifically, we give two data structures for common problems. For \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}-approximate near neighbour in Hamming space we get query time \{&#37; raw &#37;\}\\(dn^\{1/c+o(1)\}\\)\{&#37; endraw &#37;\} and space \{&#37; raw &#37;\}\\(dn^\{1+1/c+o(1)\}\\)\{&#37; endraw &#37;\} matching that of \cite\{indyk1998approximate\} and answering a long standing open question from~\cite\{indyk2000dimensionality\} and~\cite\{pagh2016locality\} in the affirmative. By means of a new deterministic reduction from \{&#37; raw &#37;\}\\(\ell\_1\\)\{&#37; endraw &#37;\} to Hamming we also solve \{&#37; raw &#37;\}\\(\ell\_1\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(\ell\_2\\)\{&#37; endraw &#37;\} with query time \{&#37; raw &#37;\}\\(d^2n^\{1/c+o(1)\}\\)\{&#37; endraw &#37;\} and space $d^2 n^\{1+1/c+o(1)\}$. For \{&#37; raw &#37;\}\\((s\_1,s\_2)\\)\{&#37; endraw &#37;\}-approximate Jaccard similarity we get query time \{&#37; raw &#37;\}\\(dn^\{\rho+o(1)\}\\)\{&#37; endraw &#37;\} and space \{&#37; raw &#37;\}\\(dn^\{1+\rho+o(1)\}\\)\{&#37; endraw &#37;\}, \{&#37; raw &#37;\}\\(\rho=\log\frac\{1+s\_1\}\{2s\_1\}\big/\log\frac\{1+s\_2\}\{2s\_2\}\\)\{&#37; endraw &#37;\}, when sets have equal size, matching the performance of~\cite\{tobias2016\}. The algorithms are based on space partitions, as with classic LSH, but we construct these using a combination of brute force, tensoring, perfect hashing and splitter functions \a la~\cite\{naor1995splitters\}. We also show a new dimensionality reduction lemma with 1-sided error.
