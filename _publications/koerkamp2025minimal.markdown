---
layout: publication
title: 'Ptrhash: Minimal Perfect Hashing At RAM Throughput'
authors: Ragnar Groot Koerkamp
conference: "Arxiv"
year: 2025
citations: 0
bibkey: koerkamp2025minimal
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2502.15539'}
tags: ['Hashing Fundamentals', 'Evaluation Metrics', 'Efficient Learning', 'Hashing Methods']
---
Given a set \\(K\\) of \\(n\\) keys, a minimal perfect hash function (MPHF) is a collision-free bijective map \\(\mathsf\{H_\{mphf\}\}\\) from \\(K\\) to \\(\\{0, \dots, n-1\\}\\). This work presents a (minimal) perfect hash function that first prioritizes query throughput, while also allowing efficient construction for \\(10^9\\) or more elements using 2.4 bits of memory per key.
  Both PTHash and PHOBIC first map all \\(n\\) keys to \\(n/\lambda < n\\) buckets. Then, each bucket stores a pilot that controls the final hash value of the keys mapping to it. PtrHash builds on this by using 1) fixed-width (uncompressed) 8-bit pilots, 2) a construction algorithm similar to cuckoo-hashing to find suitable pilot values. Further, it 3) uses the same number of buckets and slots for each part, with 4) a single remap table to map intermediate positions \\(\geq n\\) to \\(<n\\), 5) encoded using per-cacheline Elias-Fano coding. Lastly, 6) PtrHash support streaming queries, where we use prefetching to answer a stream of multiple queries more efficiently than one-by-one processing.
  With default parameters, PtrHash takes 2.0 bits per key. On 300 million string keys, PtrHash is as fast or faster to build than other MPHFs, and at least \\(2.1\times\\) faster to query. When streaming multiple queries, this improves to \\(3.3\times\\) speedup over the fastest alternative, while also being significantly faster to construct. When using \\(10^9\\) integer keys instead, query times are as low as 12 ns/key when iterating in a for loop, or even down to 8 ns/key when using the streaming approach, just short of the 7.4 ns inverse throughput of random memory accesses.
