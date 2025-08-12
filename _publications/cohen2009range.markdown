---
layout: publication
title: Range Non-overlapping Indexing
authors: Hagai Cohen, Ely Porat
conference: Lecture Notes in Computer Science
year: 2009
bibkey: cohen2009range
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0909.4893'}]
tags: ["Efficiency"]
short_authors: Hagai Cohen, Ely Porat
---
We study the non-overlapping indexing problem: Given a text T, preprocess it
so that you can answer queries of the form: given a pattern P, report the
maximal set of non-overlapping occurrences of P in T. A generalization of this
problem is the range non-overlapping indexing where in addition we are given
two indexes i,j to report the maximal set of non-overlapping occurrences
between these two indexes. We suggest new solutions for these problems. For the
non-overlapping problem our solution uses O(n) space with query time of O(m +
occ_\{NO\}). For the range non-overlapping problem we propose a solution with
O(nlog^\epsilon n) space for some 0<\epsilon<1 and O(m + loglog n +
occ_\{ij,NO\}) query time.