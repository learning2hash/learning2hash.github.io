---
layout: publication
title: Efficiently Testing Simon's Congruence
authors: Pawel Gawrychowski, Maria Kosche, Tore Koss, Florin Manea, Stefan Siemer
conference: Arxiv
year: 2020
bibkey: gawrychowski2020efficiently
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.01112'}]
tags: ["Efficiency"]
short_authors: Gawrychowski et al.
---
Simon's congruence \(\sim_k\) is defined as follows: two words are
\(\sim_k\)-equivalent if they have the same set of subsequences of length at most
\(k\). We propose an algorithm which computes, given two words \(s\) and \(t\), the
largest \(k\) for which \(s\sim_k t\). Our algorithm runs in linear time
\(O(|s|+|t|)\) when the input words are over the integer alphabet
\(\\{1,\ldots,|s|+|t|\\}\) (or other alphabets which can be sorted in linear time).
This approach leads to an optimal algorithm in the case of general alphabets as
well. Our results are based on a novel combinatorial approach and a series of
efficient data structures.