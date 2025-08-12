---
layout: publication
title: Quotient Hash Tables - Efficiently Detecting Duplicates In Streaming Data
authors: "R\xE9mi G\xE9raud, Marius Lombard-Platet, David Naccache"
conference: Arxiv
year: 2019
bibkey: "g\xE9raud2019quotient"
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.04358'}]
tags: []
short_authors: "R\xE9mi G\xE9raud, Marius Lombard-Platet, David Naccache"
---
This article presents the Quotient Hash Table (QHT) a new data structure for
duplicate detection in unbounded streams. QHTs stem from a corrected analysis
of streaming quotient filters (SQFs), resulting in a 33% reduction in memory
usage for equal performance. We provide a new and thorough analysis of both
algorithms, with results of interest to other existing constructions.
  We also introduce an optimised version of our new data structure dubbed
Queued QHT with Duplicates (QQHTD).
  Finally we discuss the effect of adversarial inputs for hash-based duplicate
filters similar to QHT.