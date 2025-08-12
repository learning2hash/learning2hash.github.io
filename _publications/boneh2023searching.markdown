---
layout: publication
title: Searching 2d-strings For Matching Frames
authors: Itai Boneh, Dvir Fried, Shay Golan, Matan Kraus, Adrian Miclaus, Arseny Shur
conference: Arxiv
year: 2023
bibkey: boneh2023searching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.02670'}]
tags: []
short_authors: Boneh et al.
---
We introduce the natural notion of a matching frame in a \(2\)-dimensional
string. A matching frame in a \(2\)-dimensional \(n\times m\) string \(M\), is a
rectangle such that the strings written on the horizontal sides of the
rectangle are identical, and so are the strings written on the vertical sides
of the rectangle. Formally, a matching frame in \(M\) is a tuple \((u,d,\ell,r)\)
such that \(M[u][\ell ..r] = M[d][\ell ..r]\) and \(M[u..d][\ell] = M[u..d][r]\).
  In this paper, we present an algorithm for finding the maximum perimeter
matching frame in a matrix \(M\) in \(\tilde\{O\}(n^\{2.5\})\) time (assuming \(n \ge
m)\). Additionally, for every constant \(\epsilon> 0\) we present a near-linear
\((1-\epsilon)\)-approximation algorithm for the maximum perimeter of a matching
frame.
  In the development of the aforementioned algorithms, we introduce inventive
technical elements and uncover distinctive structural properties that we
believe will captivate the curiosity of the community.