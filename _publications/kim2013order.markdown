---
layout: publication
title: Order Preserving Matching
authors: Jinil Kim, Peter Eades, Rudolf Fleischer, Seok-Hee Hong, Costas S. Iliopoulos,
  Kunsoo Park, Simon J. Puglisi, Takeshi Tokuyama
conference: Theoretical Computer Science
year: 2013
bibkey: kim2013order
citations: 86
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1302.4064'}]
tags: []
short_authors: Kim et al.
---
We introduce a new string matching problem called order-preserving matching
on numeric strings where a pattern matches a text if the text contains a
substring whose relative orders coincide with those of the pattern.
Order-preserving matching is applicable to many scenarios such as stock price
analysis and musical melody matching in which the order relations should be
matched instead of the strings themselves. Solving order-preserving matching
has to do with representations of order relations of a numeric string. We
define prefix representation and nearest neighbor representation, which lead to
efficient algorithms for order-preserving matching. We present efficient
algorithms for single and multiple pattern cases. For the single pattern case,
we give an O(n log m) time algorithm and optimize it further to obtain O(n + m
log m) time. For the multiple pattern case, we give an O(n log m) time
algorithm.