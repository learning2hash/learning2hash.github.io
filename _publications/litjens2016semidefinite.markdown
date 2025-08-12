---
layout: publication
title: Semidefinite Bounds For Nonbinary Codes Based On Quadruples
authors: Bart Litjens, Sven Polak, Alexander Schrijver
conference: Designs, Codes and Cryptography
year: 2016
bibkey: litjens2016semidefinite
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.02531'}]
tags: ["Compact Codes"]
short_authors: Bart Litjens, Sven Polak, Alexander Schrijver
---
For nonnegative integers \(q,n,d\), let \(A_q(n,d)\) denote the maximum
cardinality of a code of length \(n\) over an alphabet \([q]\) with \(q\) letters and
with minimum distance at least \(d\). We consider the following upper bound on
\(A_q(n,d)\). For any \(k\), let \(\CC_k\) be the collection of codes of cardinality
at most \(k\). Then \(A_q(n,d)\) is at most the maximum value of
\(\sum_\{v\in[q]^n\}x(\\{v\\})\), where \(x\) is a function \(\CC_4\to R_+\) such that
\(x(\emptyset)=1\) and \(x(C)=0\) if \(C\) has minimum distance less than \(d\), and
such that the \(\CC_2\times\CC_2\) matrix \((x(C\cup C'))_\{C,C'\in\CC_2\}\) is
positive semidefinite. By the symmetry of the problem, we can apply
representation theory to reduce the problem to a semidefinite programming
problem with order bounded by a polynomial in \(n\). It yields the new upper
bounds \(A_4(6,3)\leq 176\), \(A_4(7,4)\leq 155\), \(A_5(7,4)\leq 489\), and
\(A_5(7,5)\leq 87\).