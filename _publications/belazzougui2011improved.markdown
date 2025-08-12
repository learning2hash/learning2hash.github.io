---
layout: publication
title: Improved Space-time Tradeoffs For Approximate Full-text Indexing With One Edit
  Error
authors: Djamal Belazzougui
conference: Algorithmica
year: 2014
bibkey: belazzougui2011improved
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1103.2167'}]
tags: ["Efficiency", "Similarity Search", "Text Retrieval", "Vector Indexing"]
short_authors: Djamal Belazzougui
---
In this paper we are interested in indexing texts for substring matching
queries with one edit error. That is, given a text \\(T\\) of \\(n\\) characters over
an alphabet of size \\(\sigma\\), we are asked to build a data structure that
answers the following query: find all the \\(occ\\) substrings of the text that are
at edit distance at most \\(1\\) from a given string \\(q\\) of length \\(m\\). In this
paper we show two new results for this problem. The first result, suitable for
an unbounded alphabet, uses \\(O(nlog^\epsilon n)\\) (where \\(\epsilon\\) is any
constant such that \\(0<\epsilon<1\\)) words of space and answers to queries in
time \\(O(m+occ)\\). This improves simultaneously in space and time over the result
of Cole et al. The second result, suitable only for a constant alphabet, relies
on compressed text indices and comes in two variants: the first variant uses
\\(O(nlog^\{\epsilon\} n)\\) bits of space and answers to queries in time
\\(O(m+occ)\\), while the second variant uses \\(O(nloglog n)\\) bits of space and
answers to queries in time \\(O((m+occ)loglog n)\\). This second result improves
on the previously best results for constant alphabets achieved in Lam et al.
(Algorithmica 2008) and Chan et al. (Algorithmica 2010).