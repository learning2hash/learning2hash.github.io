---
layout: publication
title: "Optimal Las Vegas Locality Sensitive Data Structures"
authors: Ahle Thomas Dybdahl
conference: Arxiv
year: 2017
bibkey: ahle2017optimal
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1704.02054"}
tags: ['ARXIV', 'LSH']
---
We show that approximate similarity (near neighbour) search can be solved in high dimensions with performance matching state of the art (data independent) Locality Sensitive Hashing, but with a guarantee of no false negatives. Specifically, we give two data structures for common problems. For $c$-approximate near neighbour in Hamming space we get query time $dn^\{1/c+o(1)\}$ and space $dn^\{1+1/c+o(1)\}$ matching that of \cite{indyk1998approximate} and answering a long standing open question from~\cite{indyk2000dimensionality} and~\cite{pagh2016locality} in the affirmative. By means of a new deterministic reduction from $\ell_1$ to Hamming we also solve $\ell_1$ and $\ell_2$ with query time $d^2n^\{1/c+o(1)\}$ and space $d^2 n^\{1+1/c+o(1)\}$. For $(s_1,s_2)$-approximate Jaccard similarity we get query time $dn^\{\rho+o(1)\}$ and space $dn^\{1+\rho+o(1)\}$, $\rho=\log\frac\{1+s_1\}\{2s_1\}\big/\log\frac\{1+s_2\}\{2s_2\}$, when sets have equal size, matching the performance of~\cite{tobias2016}. The algorithms are based on space partitions, as with classic LSH, but we construct these using a combination of brute force, tensoring, perfect hashing and splitter functions \`a la~\cite{naor1995splitters}. We also show a new dimensionality reduction lemma with 1-sided error.