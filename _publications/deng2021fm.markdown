---
layout: publication
title: Fm-indexing Grammars Induced By Suffix Sorting For Long Patterns
authors: "Jin Jie Deng, Wing-kai Hon, Dominik K\xF6ppl, Kunihiko Sadakane"
conference: 2022 Data Compression Conference (DCC)
year: 2022
bibkey: deng2021fm
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.01181'}]
tags: ["Efficiency"]
short_authors: Deng et al.
---
The run-length compressed Burrows-Wheeler transform (RLBWT) used in
conjunction with the backward search introduced in the FM index is the
centerpiece of most compressed indexes working on highly-repetitive data sets
like biological sequences. Compared to grammar indexes, the size of the RLBWT
is often much bigger, but queries like counting the occurrences of long
patterns can be done much faster than on any existing grammar index so far. In
this paper, we combine the virtues of a grammar with the RLBWT by building the
RLBWT on top of a special grammar based on induced suffix sorting. Our
experiments reveal that our hybrid approach outperforms the classic RLBWT with
respect to the index sizes, and with respect to query times on biological data
sets for sufficiently long patterns.