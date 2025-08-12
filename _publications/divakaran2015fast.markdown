---
layout: publication
title: Fast Algorithms For Exact String Matching
authors: Srikrishnan Divakaran
conference: Arxiv
year: 2015
bibkey: divakaran2015fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.09228'}]
tags: []
short_authors: Srikrishnan Divakaran
---
Given a pattern string \(P\) of length \(n\) and a query string \(T\) of length
\(m\), where the characters of \(P\) and \(T\) are drawn from an alphabet of size
\(\Delta\), the \{\em exact string matching\} problem consists of finding all
occurrences of \(P\) in \(T\). For this problem, we present algorithms that in
\(O(n\Delta^2)\) time pre-process \(P\) to essentially identify \(sparse(P)\), a
rarely occurring substring of \(P\), and then use it to find occurrences of \(P\)
in \(T\) efficiently. Our algorithms require a worst case search time of \(O(m)\),
and expected search time of \(O(m/min(|sparse(P)|, \Delta))\), where
\(|sparse(P)|\) is at least \(\delta\) (i.e. the number of distinct characters in
\(P\)), and for most pattern strings it is observed to be \(Ω(n^\{1/2\})\).