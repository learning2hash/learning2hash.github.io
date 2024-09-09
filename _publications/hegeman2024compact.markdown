---
layout: publication
title: Compact Parallel Hash Tables on the GPU
authors: Hegeman Steef, Wöltgens Daan, Wijs Anton, Laarman Alfons
conference: "Arxiv"
year: 2024
bibkey: hegeman2024compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2406.09255"}
tags: ['ARXIV']
---
On the GPU, hash table operation speed is determined in large part by cache line efficiency, and state-of-the-art hashing schemes thus divide tables into cache line-sized buckets. This raises the question whether performance can be further improved by increasing the number of entries that fit in such buckets. Known compact hashing techniques have not yet been adapted to the massively parallel setting, nor have they been evaluated on the GPU. We consider a compact version of bucketed cuckoo hashing, and a version of compact iceberg hashing suitable for the GPU. We discuss the tables from a theoretical perspective, and provide an open source implementation of both schemes in CUDA for comparative benchmarking. In terms of performance, the state-of-the-art cuckoo hashing benefits from compactness on lookups and insertions (most experiments show at least 10-20% increase in throughput), and the iceberg table benefits significantly, to the point of being comparable to compact cuckoo hashing--while supporting performant dynamic operation.
