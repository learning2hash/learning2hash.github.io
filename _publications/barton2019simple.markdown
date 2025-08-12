---
layout: publication
title: A Simple Reduction For Full-permuted Pattern Matching Problems On Multi-track
  Strings
authors: Carl Barton, Ewan Birney, Tomas Fitzgerald
conference: Arxiv
year: 2019
bibkey: barton2019simple
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.02364'}]
tags: []
short_authors: Carl Barton, Ewan Birney, Tomas Fitzgerald
---
In this paper we study a variant of string pattern matching which deals with
tuples of strings known as \textit\{multi-track strings\}. Multi-track strings
are a generalisation of strings (or \textit\{single-track strings\}) that have
primarily found uses in problems related to searching multiple genomes and
music information retrieval. A multi-track string \(\mathcal\{T\} = (t_1, t_2,
t_3, \ldots , t_N)\) of length \(n\) and track count \(N\) is a multi-set of \(N\)
strings of length \(n\) with characters drawn from a common alphabet of size
\(\sigma_U\). Given two multi-track strings \(\mathcal\{T\} = (t_1, t_2, t_3, \ldots
, t_N)\) and \( \mathcal\{P\} = (p_1, p_2, p_3, \ldots , p_N)\) of length \(n\) and
track count \(N\), there is a \textit\{full-permuted-match\} between \(\mathcal\{P\}\)
and \(\mathcal\{T\}\) if \(t_\{r_i\} = p_i\) for all \(i \in \\{1,2,3,\ldots N \\}\) and
some permutation \((r_1, r_2, r_3\ldots,r_N)\) of \((1, 2, 3,\ldots,N)\), we denote
this \(\mathcal\{P\}\asymp\mathcal\{T\}\).
  Efficient algorithms for some full-permuted-match problems on multi-track
strings have recently been presented. In this paper we show a reduction from a
multi-track string of length \(n\) and track count \(N\) with alphabet size
\(\sigma_U\), to a single-track string of length \(2n-1\) with alphabet size
\(\sigma_U^N\). Through this reduction we allow any string algorithm to be used
on multi-track string problems using \(\asymp\) as the match relation. For
polynomial time algorithms on single-track strings of length \(n\) there is a
multiplicative penalty of not more than \(\mathcal\{O\}(N)\)-time for the same
algorithm on mt-strings of length \(n\) and track count \(N\).