---
layout: publication
title: Exact Clustering In Linear Time
authors: Marshall Jonathan A., Rafsky Lawrence C.
conference: "Arxiv"
year: 2017
bibkey: marshall2017exact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1702.05425"}
tags: ['ARXIV', 'Unsupervised']
---
The time complexity of data clustering has been viewed as fundamentally
quadratic, slowing with the number of data items, as each item is compared for
similarity to preceding items. Clustering of large data sets has been
infeasible without resorting to probabilistic methods or to capping the number
of clusters. Here we introduce MIMOSA, a novel class of algorithms which
achieve linear time computational complexity on clustering tasks. MIMOSA
algorithms mark and match partial-signature keys in a hash table to obtain
exact, error-free cluster retrieval. Benchmark measurements, on clustering a
data set of 10,000,000 news articles by news topic, found that a MIMOSA
implementation finished more than four orders of magnitude faster than a
standard centroid implementation.
