---
layout: publication
title: Optimal-time Queries On Bwt-runs Compressed Indexes
authors: Takaaki Nishimoto, Yasuo Tabei
conference: Arxiv
year: 2021
bibkey: nishimoto2020optimal
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.05104'}]
tags: ["Efficiency"]
short_authors: Takaaki Nishimoto, Yasuo Tabei
---
Indexing highly repetitive strings (i.e., strings with many repetitions) for
fast queries has become a central research topic in string processing, because
it has a wide variety of applications in bioinformatics and natural language
processing. Although a substantial number of indexes for highly repetitive
strings have been proposed thus far, developing compressed indexes that support
various queries remains a challenge. The run-length Burrows-Wheeler transform
(RLBWT) is a lossless data compression by a reversible permutation of an input
string and run-length encoding, and it has received interest for indexing
highly repetitive strings. LF and \\(\phi^\{-1\}\\) are two key functions for
building indexes on RLBWT, and the best previous result computes LF and
\\(\phi^\{-1\}\\) in \\(O(log log n)\\) time with \\(O(r)\\) words of space for the string
length \\(n\\) and the number \\(r\\) of runs in RLBWT. In this paper, we improve LF
and \\(\phi^\{-1\}\\) so that they can be computed in a constant time with \\(O(r)\\)
words of space. Subsequently, we present OptBWTR (optimal-time queries on
BWT-runs compressed indexes), the first string index that supports various
queries including locate, count, extract queries in optimal time and \\(O(r)\\)
words of space.