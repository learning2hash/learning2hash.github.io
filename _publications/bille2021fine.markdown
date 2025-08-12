---
layout: publication
title: The Fine-grained Complexity Of Episode Matching
authors: "Philip Bille, Inge Li G\xF8rtz, Shay Mozes, Teresa Anna Steiner, Oren Weimann"
conference: Arxiv
year: 2022
bibkey: bille2021fine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08613'}]
tags: []
short_authors: Bille et al.
---
Given two strings \\(S\\) and \\(P\\), the Episode Matching problem is to find the
shortest substring of \\(S\\) that contains \\(P\\) as a subsequence. The best known
upper bound for this problem is \\(\tilde O(nm)\\) by Das et al. (1997) , where
\\(n,m\\) are the lengths of \\(S\\) and \\(P\\), respectively. Although the problem is
well studied and has many applications in data mining, this bound has never
been improved. In this paper we show why this is the case by proving that no
\\(O((nm)^\{1-\epsilon\})\\) algorithm (even for binary strings) exists, unless the
Strong Exponential Time Hypothesis (SETH) is false. We then consider the
indexing version of the problem, where \\(S\\) is preprocessed into a data
structure for answering episode matching queries \\(P\\). We show that for any
\\(\tau\\), there is a data structure using \\(O(n+\left(\frac\{n\}\{\tau\}\right)^k)\\)
space that answers episode matching queries for any \\(P\\) of length \\(k\\) in
\\(O(k\cdot \tau \cdot log log n )\\) time. We complement this upper bound with
an almost matching lower bound, showing that any data structure that answers
episode matching queries for patterns of length \\(k\\) in time \\(O(n^\delta)\\), must
use \\(Ω(n^\{k-k\delta-o(1)\})\\) space, unless the Strong \\(k\\)-Set Disjointness
Conjecture is false. Finally, for the special case of \\(k=2\\), we present a
faster construction of the data structure using fast min-plus multiplication of
bounded integer matrices.