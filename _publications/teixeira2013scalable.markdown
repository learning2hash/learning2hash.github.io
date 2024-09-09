---
layout: publication
title: "Scalable Locality-Sensitive Hashing for Similarity Search in High-Dimensional, Large-Scale Multimedia Datasets"
authors: Teixeira Thiago S. F. X., Teodoro George, Valle Eduardo, Saltz Joel H.
conference: Arxiv
year: 2013
bibkey: teixeira2013scalable
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1310.4136"}
tags: ['ARXIV', 'LSH']
---
Similarity search is critical for many database applications, including the increasingly popular online services for Content-Based Multimedia Retrieval (CBMR). These services, which include image search engines, must handle an overwhelming volume of data, while keeping low response times. Thus, scalability is imperative for similarity search in Web-scale applications, but most existing methods are sequential and target shared-memory machines. Here we address these issues with a distributed, efficient, and scalable index based on Locality-Sensitive Hashing (LSH). LSH is one of the most efficient and popular techniques for similarity search, but its poor referential locality properties has made its implementation a challenging problem. Our solution is based on a widely asynchronous dataflow parallelization with a number of optimizations that include a hierarchical parallelization to decouple indexing and data storage, locality-aware data partition strategies to reduce message passing, and multi-probing to limit memory usage. The proposed parallelization attained an efficiency of 90% in a distributed system with about 800 CPU cores. In particular, the original locality-aware data partition reduced the number of messages exchanged in 30%. Our parallel LSH was evaluated using the largest public dataset for similarity search (to the best of our knowledge) with $10^9$ 128-d SIFT descriptors extracted from Web images. This is two orders of magnitude larger than datasets that previous LSH parallelizations could handle.