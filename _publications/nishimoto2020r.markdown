---
layout: publication
title: 'R-enum: Enumeration Of Characteristic Substrings In Bwt-runs Bounded Space'
authors: Takaaki Nishimoto, Yasuo Tabei
conference: Arxiv
year: 2020
bibkey: nishimoto2020r
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.01493'}]
tags: []
short_authors: Takaaki Nishimoto, Yasuo Tabei
---
Enumerating characteristic substrings (e.g., maximal repeats, minimal unique
substrings, and minimal absent words) in a given string has been an important
research topic because there are a wide variety of applications in various
areas such as string processing and computational biology. Although several
enumeration algorithms for characteristic substrings have been proposed, they
are not space-efficient in that their space-usage is proportional to the length
of an input string. Recently, the run-length encoded Burrows-Wheeler transform
(RLBWT) has attracted increased attention in string processing, and various
algorithms for the RLBWT have been developed. Developing enumeration algorithms
for characteristic substrings with the RLBWT, however, remains a challenge. In
this paper, we present r-enum (RLBWT-based enumeration), the first enumeration
algorithm for characteristic substrings based on RLBWT. R-enum runs in \(O(n
log log (n/r))\) time and with \(O(r log n)\) bits of working space for string
length \(n\) and number \(r\) of runs in RLBWT, where \(r\) is expected to be
significantly smaller than \(n\) for highly repetitive strings (i.e., strings
with many repetitions). Experiments using a benchmark dataset of highly
repetitive strings show that the results of r-enum are more space-efficient
than the previous results. In addition, we demonstrate the applicability of
r-enum to a huge string by performing experiments on a 300-gigabyte string of
100 human genomes.