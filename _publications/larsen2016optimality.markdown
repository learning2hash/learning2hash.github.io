---
layout: publication
title: Optimality Of The Johnson-lindenstrauss Lemma
authors: Kasper Green Larsen, Jelani Nelson
conference: 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2017
bibkey: larsen2016optimality
citations: 83
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.02094'}]
tags: []
short_authors: Kasper Green Larsen, Jelani Nelson
---
For any integers \\(d, n \geq 2\\) and \\(1/(\{\min\\{n,d\\}\})^\{0.4999\} <
\epsilon<1\\), we show the existence of a set of \\(n\\) vectors \\(X\subset
\mathbb\{R\}^d\\) such that any embedding \\(f:X\rightarrow \mathbb\{R\}^m\\) satisfying
$\\( \forall x,y\in X,\ (1-\epsilon)\|x-y\|_2^2\le \|f(x)-f(y)\|_2^2 \le
(1+\epsilon)\|x-y\|_2^2 \\)\\( must have \\)\\( m = Ω(\epsilon^\{-2\} \lg n).
\\)\\( This lower bound matches the upper bound given by the Johnson-Lindenstrauss
lemma [JL84]. Furthermore, our lower bound holds for nearly the full range of
\\)\epsilon\\( of interest, since there is always an isometric embedding into
dimension \\)\min\\{d, n\\}\\( (either the identity map, or projection onto
\\)\mathop\{span\}(X)\\().
  Previously such a lower bound was only known to hold against linear maps \\)f\\(,
and not for such a wide range of parameters \\)\epsilon, n, d\\( [LN16]. The
best previously known lower bound for general \\)f\\( was \\)m =
Ω(\epsilon^\{-2\}\lg n/\lg(1/\epsilon))\\( [Wel74, Lev83, Alo03], which
is suboptimal for any \\)\epsilon = o(1)$.