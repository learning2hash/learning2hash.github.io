---
layout: publication
title: Efficient Multi-vector Dense Retrieval Using Bit Vectors
authors: Nardini Franco Maria, Rulli Cosimo, Venturini Rossano
conference: Lecture Notes in Computer Science
year: 2024
bibkey: nardini2024efficient
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.02805'}]
---
Dense retrieval techniques employ pre-trained large language models to build
a high-dimensional representation of queries and passages. These
representations compute the relevance of a passage w.r.t. to a query using
efficient similarity measures. In this line, multi-vector representations show
improved effectiveness at the expense of a one-order-of-magnitude increase in
memory footprint and query latency by encoding queries and documents on a
per-token level. Recently, PLAID has tackled these problems by introducing a
centroid-based term representation to reduce the memory impact of multi-vector
systems. By exploiting a centroid interaction mechanism, PLAID filters out
non-relevant documents, thus reducing the cost of the successive ranking
stages. This paper proposes ``Efficient Multi-Vector dense retrieval with Bit
vectors'' (EMVB), a novel framework for efficient query processing in
multi-vector dense retrieval. First, EMVB employs a highly efficient
pre-filtering step of passages using optimized bit vectors. Second, the
computation of the centroid interaction happens column-wise, exploiting SIMD
instructions, thus reducing its latency. Third, EMVB leverages Product
Quantization (PQ) to reduce the memory footprint of storing vector
representations while jointly allowing for fast late interaction. Fourth, we
introduce a per-document term filtering method that further improves the
efficiency of the last step. Experiments on MS MARCO and LoTTE show that EMVB
is up to 2.8x faster while reducing the memory footprint by 1.8x with no loss
in retrieval accuracy compared to PLAID.