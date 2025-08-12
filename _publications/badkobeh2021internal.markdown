---
layout: publication
title: Internal Shortest Absent Word Queries In Constant Time And Linear Space
authors: Golnaz Badkobeh, Panagiotis Charalampopoulos, Dmitry Kosolobov, Solon P.
  Pissis
conference: Theoretical Computer Science
year: 2022
bibkey: badkobeh2021internal
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.01763'}]
tags: []
short_authors: Badkobeh et al.
---
Given a string \\(T\\) of length \\(n\\) over an alphabet \\(\Sigma\subset
\\{1,2,\ldots,n^\{O(1)\}\\}\\) of size \\(\sigma\\), we are to preprocess \\(T\\) so that
given a range \\([i,j]\\), we can return a representation of a shortest string over
\\(\Sigma\\) that is absent in the fragment \\(T[i]\cdots T[j]\\) of \\(T\\). We present an
\\(O(n)\\)-space data structure that answers such queries in constant time and can
be constructed in \\(O(nlog_\sigma n)\\) time.