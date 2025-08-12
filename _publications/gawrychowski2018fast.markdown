---
layout: publication
title: Fast Entropy-bounded String Dictionary Look-up With Mismatches
authors: "Pawe\u0142 Gawrychowski, Gad M. Landau, Tatiana Starikovskaya"
conference: Arxiv
year: 2018
bibkey: gawrychowski2018fast
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.09646'}]
tags: ["Efficiency"]
short_authors: "Pawe\u0142 Gawrychowski, Gad M. Landau, Tatiana Starikovskaya"
---
We revisit the fundamental problem of dictionary look-up with mismatches.
Given a set (dictionary) of \(d\) strings of length \(m\) and an integer \(k\), we
must preprocess it into a data structure to answer the following queries: Given
a query string \(Q\) of length \(m\), find all strings in the dictionary that are
at Hamming distance at most \(k\) from \(Q\). Chan and Lewenstein (CPM 2015) showed
a data structure for \(k = 1\) with optimal query time \(O(m/w + occ)\), where \(w\)
is the size of a machine word and \(occ\) is the size of the output. The data
structure occupies \(O(w d log^\{1+\epsilon\} d)\) extra bits of space (beyond
the entropy-bounded space required to store the dictionary strings). In this
work we give a solution with similar bounds for a much wider range of values
\(k\). Namely, we give a data structure that has \(O(m/w + log^k d + occ)\) query
time and uses \(O(w d log^k d)\) extra bits of space.