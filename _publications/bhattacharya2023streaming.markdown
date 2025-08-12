---
layout: publication
title: Streaming \(k\)-edit Approximate Pattern Matching Via String Decomposition
authors: "Sudatta Bhattacharya, Michal Kouck\xFD"
conference: Arxiv
year: 2023
bibkey: bhattacharya2023streaming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.00615'}]
tags: []
short_authors: "Sudatta Bhattacharya, Michal Kouck\xFD"
---
In this paper we give an algorithm for streaming \(k\)-edit approximate pattern
matching which uses space \(\widetilde\{O\}(k^2)\) and time \(\widetilde\{O\}(k^2)\)
per arriving symbol. This improves substantially on the recent algorithm of
Kociumaka, Porat and Starikovskaya (2022) which uses space \(\widetilde\{O\}(k^5)\)
and time \(\widetilde\{O\}(k^8)\) per arriving symbol. In the \(k\)-edit approximate
pattern matching problem we get a pattern \(P\) and text \(T\) and we want to
identify all substrings of the text \(T\) that are at edit distance at most \(k\)
from \(P\). In the streaming version of this problem both the pattern and the
text arrive in a streaming fashion symbol by symbol and after each symbol of
the text we need to report whether there is a current suffix of the text with
edit distance at most \(k\) from \(P\). We measure the total space needed by the
algorithm and time needed per arriving symbol.