---
layout: publication
title: Fast Indexes For Gapped Pattern Matching
authors: "Manuel C\xE1ceres, Simon J. Puglisi, Bella Zhukova"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: "c\xE1ceres2020fast"
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.12662'}]
tags: []
short_authors: "Manuel C\xE1ceres, Simon J. Puglisi, Bella Zhukova"
---
We describe indexes for searching large data sets for variable-length-gapped
(VLG) patterns. VLG patterns are composed of two or more subpatterns, between
each adjacent pair of which is a gap-constraint specifying upper and lower
bounds on the distance allowed between subpatterns. VLG patterns have numerous
applications in computational biology (motif search), information retrieval
(e.g., for language models, snippet generation, machine translation) and
capture a useful subclass of the regular expressions commonly used in practice
for searching source code. Our best approach provides search speeds several
times faster than prior art across a broad range of patterns and texts.