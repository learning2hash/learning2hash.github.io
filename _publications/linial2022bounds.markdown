---
layout: publication
title: Bounds On Unique-neighbor Codes
authors: Nati Linial, Edan Orzech
conference: Arxiv
year: 2022
bibkey: linial2022bounds
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.10330'}]
tags: []
short_authors: Nati Linial, Edan Orzech
---
Recall that a binary linear code of length \(n\) is a linear subspace
\(\mathcal\{C\} = \\{x\in\mathbb\{F\}_2^n\mid Ax=0\\}\). Here the parity check matrix
\(A\) is a binary \(m\times n\) matrix of rank \(m\). We say that \(\mathcal\{C\}\) has
rate \(R=1-\frac mn\). Its distance, denoted \(\delta n\) is the smallest Hamming
weight of a non-zero vector in \(\mathcal\{C\}\). The rate vs.\ distance problem
for binary linear codes is a fundamental open problem in coding theory, and a
fascinating question in discrete mathematics. It concerns the function
\(R_L(\delta)\), the largest possible rate \(R\) for given \(0\le\delta\le1\) and
arbitrarily large length \(n\). Here we investigate a variation of this
fundamental question that we describe next.
  Clearly, \(\mathcal\{C\}\) has distance \(\delta n\), if and only if for every
\(0<n'<\delta n\), every \(m\times n'\) submatrix of \(A\) has a row of odd weight.
Motivated by several problems from coding theory, we say that \(A\) has the
unique-neighbor property with parameter \(\delta n\), if every such submatrix has
a row of weight \(1\). Let \(R_U(\delta)\) be the largest possible asymptotic rate
of linear codes with a parity check matrix that has this stronger property.
Clearly, \(R_U(\cdot),R_L(\cdot)\) are non-increasing functions, and
\(R_U(\delta)\le R_L(\delta)\) for all \(\delta\). Also, \(R_U(0)=R_L(0)=1\), and
\(R_U(1)=R_L(1)=0\), so let \(0\le\delta_U \le\delta_L\le1\) be the smallest values
of \(\delta\) at which \(R_U\) resp.\ \(R_L\) vanish. It is well known that
\(\delta_L=\frac12\) and we conjecture that \(\delta_U\) is strictly smaller than
\(\frac12\), i.e., the rate of linear codes with the unique-neighbor property is
more strictly bounded. While the conjecture remains open, we prove here several
results supporting it.
  The reader is not assumed to have any specific background in coding theory,
but we occasionally point out some relevant facts from that area.