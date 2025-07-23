---
layout: publication
title: 'Fishing In The Stream: Similarity Search Over Endless Data'
authors: Kraus Naama, Carmel David, Keidar Idit
conference: 2017 IEEE International Conference on Big Data (Big Data)
year: 2017
bibkey: kraus2017fishing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.02062'}]
tags: ["Datasets", "Large-Scale Search", "Locality Sensitive Hashing", "Similarity Search"]
short_authors: Kraus Naama, Carmel David, Keidar Idit
---
Similarity search is the task of retrieving data items that are similar to a
given query. In this paper, we introduce the time-sensitive notion of
similarity search over endless data-streams (SSDS), which takes into account
data quality and temporal characteristics in addition to similarity. SSDS is
challenging as it needs to process unbounded data, while computation resources
are bounded. We propose Stream-LSH, a randomized SSDS algorithm that bounds the
index size by retaining items according to their freshness, quality, and
dynamic popularity attributes. We analytically show that Stream-LSH increases
the probability to find similar items compared to alternative approaches using
the same space capacity. We further conduct an empirical study using real world
stream datasets, which confirms our theoretical results.