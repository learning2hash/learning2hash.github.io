---
layout: publication
title: Faster Compact Top-k Document Retrieval
authors: Roberto Konow, Gonzalo Navarro
conference: 2013 Data Compression Conference
year: 2013
bibkey: konow2012faster
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1211.5353'}]
tags: ["Text Retrieval"]
short_authors: Roberto Konow, Gonzalo Navarro
---
An optimal index solving top-k document retrieval [Navarro and Nekrich,
SODA12] takes O(m + k) time for a pattern of length m, but its space is at
least 80n bytes for a collection of n symbols. We reduce it to 1.5n to 3n
bytes, with O(m+(k+log log n) log log n) time, on typical texts. The index is
up to 25 times faster than the best previous compressed solutions, and requires
at most 5% more space in practice (and in some cases as little as one half).
Apart from replacing classical by compressed data structures, our main idea is
to replace suffix tree sampling by frequency thresholding to achieve
compression.