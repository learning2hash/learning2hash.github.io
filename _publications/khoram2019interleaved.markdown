---
layout: publication
title: Interleaved Composite Quantization For High-dimensional Similarity Search
authors: Khoram Soroosh, Wright Stephen J, Li Jing
conference: Arxiv
year: 2019
bibkey: khoram2019interleaved
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08756'}]
tags: ["Efficiency", "Memory Efficiency", "Quantization", "Scalability", "Similarity Search"]
short_authors: Khoram Soroosh, Wright Stephen J, Li Jing
---
Similarity search retrieves the nearest neighbors of a query vector from a
dataset of high-dimensional vectors. As the size of the dataset grows, the cost
of performing the distance computations needed to implement a query can become
prohibitive. A method often used to reduce this computational cost is
quantization of the vector space and location-based encoding of the dataset
vectors. These encodings can be used during query processing to find
approximate nearest neighbors of the query point quickly. Search speed can be
improved by using shorter codes, but shorter codes have higher quantization
error, leading to degraded precision. In this work, we propose the Interleaved
Composite Quantization (ICQ) which achieves fast similarity search without
using shorter codes. In ICQ, a small subset of the code is used to approximate
the distances, with complete codes being used only when necessary. Our method
effectively reduces both code length and quantization error. Furthermore, ICQ
is compatible with several recently proposed techniques for reducing
quantization error and can be used in conjunction with these other techniques
to improve results. We confirm these claims and show strong empirical
performance of ICQ using several synthetic and real-word datasets.