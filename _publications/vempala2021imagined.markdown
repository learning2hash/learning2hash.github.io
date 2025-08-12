---
layout: publication
title: Imagined-trailing-whitespace-agnostic Levenshtein Distance For Plaintext Table
  Detection
authors: Kartik Vempala
conference: Arxiv
year: 2021
bibkey: vempala2021imagined
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.06942'}]
tags: []
short_authors: Kartik Vempala
---
The standard algorithm for Levenshtein distance, treats trailing whitespace
the same as any other letter or symbol. However, when humans compare 2 strings,
we implicitly assume that both strings are padded by infinite trailing
whitespace. This informs our expectations for what the costs for insertion,
deletion and replacement, should be. This violation of our expectations results
in non-intuitive edit distance values. To account for this specific human
intuition, a naive approach which considers "all possible" substrings of
trailing whitespace would yield an \(O(n^3)\) algorithm. In this work, we provide
an efficient \(O(n^2)\) algorithm to compute the same. Keywords: Imagined
Infinite Trailing Whitespace, Human Friendly, Intuitive Edit Distance, Table
Detection, Table Alignment