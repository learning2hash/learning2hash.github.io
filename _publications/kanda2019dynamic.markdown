---
layout: publication
title: Dynamic Path-decomposed Tries
authors: "Shunsuke Kanda, Dominik K\xF6ppl, Yasuo Tabei, Kazuhiro Morita, Masao Fuketa"
conference: ACM Journal of Experimental Algorithmics
year: 2020
bibkey: kanda2019dynamic
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.06015'}]
tags: []
short_authors: Kanda et al.
---
A keyword dictionary is an associative array whose keys are strings. Recent
applications handling massive keyword dictionaries in main memory have a need
for a space-efficient implementation. When limited to static applications,
there are a number of highly-compressed keyword dictionaries based on the
advancements of practical succinct data structures. However, as most succinct
data structures are only efficient in the static case, it is still difficult to
implement a keyword dictionary that is space efficient and dynamic. In this
article, we propose such a keyword dictionary. Our main idea is to embrace the
path decomposition technique, which was proposed for constructing
cache-friendly tries. To store the path-decomposed trie in small memory, we
design data structures based on recent compact hash trie representations.
Experiments on real-world datasets reveal that our dynamic keyword dictionary
needs up to 68% less space than the existing smallest ones, while achieving a
relevant space-time tradeoff.