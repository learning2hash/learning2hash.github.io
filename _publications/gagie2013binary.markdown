---
layout: publication
title: Binary Jumbled Pattern Matching On Trees And Tree-like Structures
authors: Travis Gagie, Danny Hermelin, Gad M. Landau, Oren Weimann
conference: Algorithmica
year: 2014
bibkey: gagie2013binary
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1301.6127'}]
tags: []
short_authors: Gagie et al.
---
Binary jumbled pattern matching asks to preprocess a binary string \\(S\\) in
order to answer queries \\((i,j)\\) which ask for a substring of \\(S\\) that is of
length \\(i\\) and has exactly \\(j\\) 1-bits. This problem naturally generalizes to
vertex-labeled trees and graphs by replacing "substring" with "connected
subgraph". In this paper, we give an \\(O(n^2 / log^2 n)\\)-time solution for
trees, matching the currently best bound for (the simpler problem of) strings.
We also give an \\(\Oh\{g^\{2 / 3\} n^\{4 / 3\}/(log n)^\{4/3\}\}\\)-time solution for
strings that are compressed by a grammar of size \\(g\\). This solution improves
the known bounds when the string is compressible under many popular compression
schemes. Finally, we prove that the problem is fixed-parameter tractable with
respect to the treewidth \\(w\\) of the graph, thus improving the previous best
\\(n^\{O(w)\}\\) algorithm [ICALP'07].