---
layout: publication
title: Linear-space Substring Range Counting Over Polylogarithmic Alphabets
authors: "Travis Gagie, Pawe\u0142 Gawrychowski"
conference: Arxiv
year: 2012
bibkey: gagie2012linear
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1202.3208'}]
tags: []
short_authors: "Travis Gagie, Pawe\u0142 Gawrychowski"
---
Bille and G\{\o\}rtz (2011) recently introduced the problem of substring range
counting, for which we are asked to store compactly a string \(S\) of \(n\)
characters with integer labels in ([0, u]), such that later, given an interval
([a, b]) and a pattern \(P\) of length \(m\), we can quickly count the occurrences
of \(P\) whose first characters' labels are in ([a, b]). They showed how to store
\(S\) in \(\Oh\{n log n / log log n\}\) space and answer queries in \(\Oh\{m + log
log u\}\) time. We show that, if \(S\) is over an alphabet of size (\polylog (n)),
then we can achieve optimal linear space. Moreover, if (u = n \polylog (n)),
then we can also reduce the time to \(\Oh\{m\}\). Our results give linear space and
time bounds for position-restricted substring counting and the counting
versions of indexing substrings with intervals, indexing substrings with gaps
and aligned pattern matching.