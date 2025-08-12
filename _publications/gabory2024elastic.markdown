---
layout: publication
title: Elastic-degenerate String Comparison
authors: Esteban Gabory, Moses Njagi Mwaniki, Nadia Pisanti, Solon P. Pissis, Jakub
  Radoszewski, Michelle Sweering, Wiktor Zuba
conference: Information and Computation
year: 2025
bibkey: gabory2024elastic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.07782'}]
tags: ["Evaluation"]
short_authors: Gabory et al.
---
An elastic-degenerate (ED) string \\(T\\) is a sequence of \\(n\\) sets
\\(T[1],\ldots,T[n]\\) containing \\(m\\) strings in total whose cumulative length is
\\(N\\). We call \\(n\\), \\(m\\), and \\(N\\) the length, the cardinality and the size of \\(T\\),
respectively. The language of \\(T\\) is defined as \\(L(T)=\\{S_1 \cdots S_n\,:\,S_i
\in T[i]\\) for all \\(i\in[1,n]\\}\\). ED strings have been introduced to represent a
set of closely-related DNA sequences, also known as a pangenome. The basic
question we investigate here is: Given two ED strings, how fast can we check
whether the two languages they represent have a nonempty intersection? We call
the underlying problem the ED String Intersection (EDSI) problem.For two ED
strings \\(T_1\\) and \\(T_2\\) of lengths \\(n_1\\) and \\(n_2\\), cardinalities \\(m_1\\) and
\\(m_2\\), and sizes \\(N_1\\) and \\(N_2\\), respectively, we show the following:
  - There is no \\(O((N_1N_2)^\{1-\epsilon\})\\)-time algorithm, for any constant
\\(\epsilon>0\\), for EDSI even when \\(T_1\\) and \\(T_2\\) are over a binary alphabet,
unless the Strong Exponential-Time Hypothesis is false.
  - There is no combinatorial \\(O((N_1+N_2)^\{1.2-\epsilon\}f(n_1,n_2))\\)-time
algorithm, for any constant \\(\epsilon>0\\) and any function \\(f\\), for EDSI even
when \\(T_1\\) and \\(T_2\\) are over a binary alphabet, unless the Boolean Matrix
Multiplication conjecture is false.
  - An \\(O(N_1log N_1log n_1+N_2log N_2log n_2)\\)-time algorithm for
outputting a compact (RLE) representation of the intersection language of two
unary ED strings. In the case when \\(T_1\\) and \\(T_2\\) are given in a compact
representation, we show that the problem is NP-complete.
  - An \\(O(N_1m_2+N_2m_1)\\)-time algorithm for EDSI.
  - An \\(\tilde\{O\}(N_1^\{\omega-1\}n_2+N_2^\{\omega-1\}n_1)\\)-time algorithm for
EDSI, where \\(\omega\\) is the exponent of matrix multiplication; the \\(\tilde\{O\}\\)
notation suppresses factors that are polylogarithmic in the input size.