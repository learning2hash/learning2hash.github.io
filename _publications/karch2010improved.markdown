---
layout: publication
title: Improved Fast Similarity Search In Dictionaries
authors: Karch Daniel, Luxen Dennis, Sanders Peter
conference: "Arxiv"
year: 2010
bibkey: karch2010improved
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1008.1191"}
tags: ['ARXIV']
---
We engineer an algorithm to solve the approximate dictionary matching problem. Given a list of words \{\{ '\{\{' \}\}\mathcal\{W\}\{\{ '\}\}' \}\}, maximum distance \{\{ '\{\{' \}\}d\{\{ '\}\}' \}\} fixed at preprocessing time and a query word \{\{ '\{\{' \}\}q\{\{ '\}\}' \}\}, we would like to retrieve all words from \{\{ '\{\{' \}\}\mathcal\{W\}\{\{ '\}\}' \}\} that can be transformed into \{\{ '\{\{' \}\}q\{\{ '\}\}' \}\} with \{\{ '\{\{' \}\}d\{\{ '\}\}' \}\} or less edit operations. We present data structures that support fault tolerant queries by generating an index. On top of that, we present a generalization of the method that eases memory consumption and preprocessing time significantly. At the same time, running times of queries are virtually unaffected. We are able to match in lists of hundreds of thousands of words and beyond within microseconds for reasonable distances.
