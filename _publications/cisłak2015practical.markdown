---
layout: publication
title: A Practical Index For Approximate Dictionary Matching With Few Mismatches
authors: "Aleksander Cis\u0142ak, Szymon Grabowski"
conference: Computing and Informatics
year: 2017
bibkey: "cis\u0142ak2015practical"
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1501.04948'}]
tags: ["Efficiency"]
short_authors: "Aleksander Cis\u0142ak, Szymon Grabowski"
---
Approximate dictionary matching is a classic string matching problem
(checking if a query string occurs in a collection of strings) with
applications in, e.g., spellchecking, online catalogs, geolocation, and web
searchers. We present a surprisingly simple solution called a split index,
which is based on the Dirichlet principle, for matching a keyword with few
mismatches, and experimentally show that it offers competitive space-time
tradeoffs. Our implementation in the C++ language is focused mostly on data
compaction, which is beneficial for the search speed (e.g., by being cache
friendly). We compare our solution with other algorithms and we show that it
performs better for the Hamming distance. Query times in the order of 1
microsecond were reported for one mismatch for the dictionary size of a few
megabytes on a medium-end PC. We also demonstrate that a basic compression
technique consisting in \\(q\\)-gram substitution can significantly reduce the
index size (up to 50% of the input text size for the DNA), while still keeping
the query time relatively low.