---
layout: publication
title: Combined Data Structure For Previous- And Next-smaller-values
authors: Johannes Fischer
conference: Theoretical Computer Science
year: 2011
bibkey: fischer2011combined
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1102.0395'}]
tags: []
short_authors: Johannes Fischer
---
Let \(A\) be a static array storing \(n\) elements from a totally ordered set. We
present a data structure of optimal size at most \(nlog_2(3+2\sqrt\{2\})+o(n)\)
bits that allows us to answer the following queries on \(A\) in constant time,
without accessing \(A\): (1) previous smaller value queries, where given an index
\(i\), we wish to find the first index to the left of \(i\) where \(A\) is strictly
smaller than at \(i\), and (2) next smaller value queries, which search to the
right of \(i\). As an additional bonus, our data structure also allows to answer
a third kind of query: given indices \(i<j\), find the position of the minimum in
\(A[i..j]\). Our data structure has direct consequences for the space-efficient
storage of suffix trees.