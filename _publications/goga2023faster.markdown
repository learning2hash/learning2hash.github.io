---
layout: publication
title: Faster Maximal Exact Matches With Lazy LCP Evaluation
authors: "Adri\xE1n Goga, Lore Depuydt, Nathaniel K. Brown, Jan Fostier, Travis Gagie,\
  \ Gonzalo Navarro"
conference: 2024 Data Compression Conference (DCC)
year: 2024
bibkey: goga2023faster
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.04538'}]
tags: []
short_authors: Goga et al.
---
MONI (Rossi et al., \{\it JCB\} 2022) is a BWT-based compressed index for
computing the matching statistics and maximal exact matches (MEMs) of a pattern
(usually a DNA read) with respect to a highly repetitive text (usually a
database of genomes) using two operations: LF-steps and longest common
extension (LCE) queries on a grammar-compressed representation of the text. In
practice, most of the operations are constant-time LF-steps but most of the
time is spent evaluating LCE queries. In this paper we show how (a variant of)
the latter can be evaluated lazily, so as to bound the total time MONI needs to
process the pattern in terms of the number of MEMs between the pattern and the
text, while maintaining logarithmic latency.