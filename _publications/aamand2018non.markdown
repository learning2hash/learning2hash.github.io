---
layout: publication
title: Non-empty Bins With Simple Tabulation Hashing
authors: Anders Aamand, Mikkel Thorup
conference: Proceedings of the Thirtieth Annual ACM-SIAM Symposium on Discrete Algorithms
year: 2019
bibkey: aamand2018non
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.13187'}]
tags: ["Hashing Methods"]
short_authors: Anders Aamand, Mikkel Thorup
---
We consider the hashing of a set \(X\subseteq U\) with \(|X|=m\) using a simple
tabulation hash function \(h:U\to [n]=\\{0,\dots,n-1\\}\) and analyse the number of
non-empty bins, that is, the size of \(h(X)\). We show that the expected size of
\(h(X)\) matches that with fully random hashing to within low-order terms. We
also provide concentration bounds. The number of non-empty bins is a
fundamental measure in the balls and bins paradigm, and it is critical in
applications such as Bloom filters and Filter hashing. For example, normally
Bloom filters are proportioned for a desired low false-positive probability
assuming fully random hashing (see \url\{en.wikipedia.org/wiki/Bloom_filter\}).
Our results imply that if we implement the hashing with simple tabulation, we
obtain the same low false-positive probability for any possible input.