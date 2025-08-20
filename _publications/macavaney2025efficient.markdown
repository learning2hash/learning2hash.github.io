---
layout: publication
title: Efficient Constant-space Multi-vector Retrieval
authors: Sean MacAvaney, Antonio Mallia, Nicola Tonellotto
conference: Lecture Notes in Computer Science
year: 2025
bibkey: macavaney2025efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.01818'}]
tags: [Memory Efficiency]
short_authors: Sean MacAvaney, Antonio Mallia, Nicola Tonellotto
---
Multi-vector retrieval methods, exemplified by the ColBERT architecture, have
shown substantial promise for retrieval by providing strong trade-offs in terms
of retrieval latency and effectiveness. However, they come at a high cost in
terms of storage since a (potentially compressed) vector needs to be stored for
every token in the input collection. To overcome this issue, we propose
encoding documents to a fixed number of vectors, which are no longer
necessarily tied to the input tokens. Beyond reducing the storage costs, our
approach has the advantage that document representations become of a fixed size
on disk, allowing for better OS paging management. Through experiments using
the MSMARCO passage corpus and BEIR with the ColBERT-v2 architecture, a
representative multi-vector ranking model architecture, we find that passages
can be effectively encoded into a fixed number of vectors while retaining most
of the original effectiveness.