---
layout: publication
title: Identifying Duplicate And Contradictory Information In Wikipedia
authors: Sarah Weissman, Samet Ayhan, Joshua Bradley, Jimmy Lin
conference: 'JCDL ''15: 15th ACM/IEEE-CS Joint Conference on Digital Libraries'
year: 2014
bibkey: weissman2014identifying
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1406.1143'}]
tags: ["Locality-Sensitive-Hashing"]
short_authors: Weissman et al.
---
Our study identifies sentences in Wikipedia articles that are either
identical or highly similar by applying techniques for near-duplicate detection
of web pages. This is accomplished with a MapReduce implementation of minhash
to identify clusters of sentences with high Jaccard similarity. We show that
these clusters can be categorized into six different types, two of which are
particularly interesting: identical sentences quantify the extent to which
content in Wikipedia is copied and pasted, and near-duplicate sentences that
state contradictory facts point to quality issues in Wikipedia.