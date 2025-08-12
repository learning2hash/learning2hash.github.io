---
layout: publication
title: Fast And Simple Jumbled Indexing For Binary RLE Strings
authors: "Lu\xEDs Cunha, Simone Dantas, Travis Gagie, Roland Wittler, Luis Kowada,\
  \ Jens Stoye"
conference: Arxiv
year: 2017
bibkey: cunha2017fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.01280'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Cunha et al.
---
Important papers have appeared recently on the problem of indexing binary
strings for jumbled pattern matching, and further lowering the time bounds in
terms of the input size would now be a breakthrough with broad implications. We
can still make progress on the problem, however, by considering other natural
parameters. Badkobeh et al.\ (IPL, 2013) and Amir et al.\ (TCS, 2016) gave
algorithms that index a binary string in \(O (n + \rho^2 log \rho)\) time, where
\(n\) is the length and \(\rho\) is the number of runs, and Giaquinta and Grabowski
(IPL, 2013) gave one that runs in \(O (n + \rho^2)\) time. In this paper we
propose a new and very simple algorithm that also runs in \(O(n + \rho^2)\) time
and can be extended either so that the index returns the position of a match
(if there is one), or so that the algorithm uses only \(O (n)\) bits of space.