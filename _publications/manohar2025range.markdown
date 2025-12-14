---
layout: publication
title: Range Retrieval With Graph-based Indices
authors: Magdalen Dobson Manohar, Taekseung Kim, Guy E. Blelloch
conference: Arxiv
year: 2025
bibkey: manohar2025range
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.13245'}]
tags: [Evaluation, Graph-based ANN, Datasets]
short_authors: Magdalen Dobson Manohar, Taekseung Kim, Guy E. Blelloch
---
Retrieving points based on proximity in a high-dimensional vector space is a
crucial step in information retrieval applications. The approximate nearest
neighbor search (ANNS) problem, which identifies the \(k\) nearest neighbors for
a query (approximately, since exactly is hard), has been extensively studied in
recent years. However, comparatively little attention has been paid to the
related problem of finding all points within a given distance of a query, the
range retrieval problem, despite its applications in areas such as duplicate
detection, plagiarism checking, and facial recognition. In this paper, we
present a set of algorithms for range retrieval on graph-based vector indices,
which are known to achieve excellent performance on ANNS queries. Since a range
query may have anywhere from no matching results to thousands of matching
results in the database, we introduce a set of range retrieval algorithms based
on modifications of the standard graph search that adapt to terminate quickly
on queries in the former group, and to put more resources into finding results
for the latter group. Due to the lack of existing benchmarks for range
retrieval, we also undertake a comprehensive study of range characteristics of
existing embedding datasets, and select a suitable range retrieval radius for
eight existing datasets with up to 100 million points in addition to the one
existing benchmark. We test our algorithms on these datasets, and find up to
100x improvement in query throughput over a naive baseline approach, with 5-10x
improvement on average, and strong performance up to 100 million data points.