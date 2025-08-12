---
layout: publication
title: Compressed Indexing For Consecutive Occurrences
authors: "Pawe\u0142 Gawrychowski, Garance Gourdel, Tatiana Starikovskaya, Teresa\
  \ Anna Steiner"
conference: Arxiv
year: 2023
bibkey: gawrychowski2023compressed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.00887'}]
tags: ["Vector Indexing"]
short_authors: Gawrychowski et al.
---
The fundamental question considered in algorithms on strings is that of
indexing, that is, preprocessing a given string for specific queries. By now we
have a number of efficient solutions for this problem when the queries ask for
an exact occurrence of a given pattern \(P\). However, practical applications
motivate the necessity of considering more complex queries, for example
concerning near occurrences of two patterns. Recently, Bille et al. [CPM 2021]
introduced a variant of such queries, called gapped consecutive occurrences, in
which a query consists of two patterns \(P_\{1\}\) and \(P_\{2\}\) and a range \([a,b]\),
and one must find all consecutive occurrences \((q_1,q_2)\) of \(P_\{1\}\) and
\(P_\{2\}\) such that \(q_2-q_1 \in [a,b]\). By their results, we cannot hope for a
very efficient indexing structure for such queries, even if \(a=0\) is fixed
(although at the same time they provided a non-trivial upper bound). Motivated
by this, we focus on a text given as a straight-line program (SLP) and design
an index taking space polynomial in the size of the grammar that answers such
queries in time optimal up to polylog factors.