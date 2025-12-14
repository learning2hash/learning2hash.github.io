---
layout: publication
title: Streaming Similarity Search Over One Billion Tweets Using Parallel Locality-sensitive
  Hashing
authors: Narayanan Sundaram, Turmukhametova, Satish, Mostak, Indyk, Dubey
conference: Proceedings of the VLDB Endowment
year: 2025
bibkey: sundaram2025streaming
citations: 109
additional_links: [{name: Paper, url: 'http://www.vldb.org/pvldb/vol6/p1930-sundaram.pdf'}]
tags: [Evaluation, Similarity Search, Efficiency, Datasets, Hashing Methods, Text
    Retrieval, Locality Sensitive Hashing]
short_authors: Sundaram et al.
---
Finding nearest neighbors has become an important operation on databases, with applications to text search, multimedia indexing,
and many other areas. One popular algorithm for similarity search, especially for high dimensional data (where spatial indexes like kdtrees do not perform well) is Locality Sensitive Hashing (LSH), an
approximation algorithm for finding similar objects. In this paper, we describe a new variant of LSH, called Parallel
LSH (PLSH) designed to be extremely efficient, capable of scaling out on multiple nodes and multiple cores, and which supports highthroughput streaming of new data. Our approach employs several
novel ideas, including: cache-conscious hash table layout, using a 2-level merge algorithm for hash table construction; an efficient
algorithm for duplicate elimination during hash-table querying; an insert-optimized hash table structure and efficient data expiration
algorithm for streaming data; and a performance model that accurately estimates performance of the algorithm and can be used to
optimize parameter settings. We show that on a workload where we perform similarity search on a dataset of > 1 Billion tweets, with
hundreds of millions of new tweets per day, we can achieve query times of 1–2.5 ms. We show that this is an order of magnitude faster
than existing indexing schemes, such as inverted indexes. To the best of our knowledge, this is the fastest implementation of LSH,
with table construction times up to 3.7x faster and query times that are 8.3x faster than a basic implementation.