---
layout: publication
title: PHOBIC Perfect Hashing With Optimized Bucket Sizes And Interleaved Coding
authors: Hermann Stefan, Lehmann Hans-peter, Pibiri Giulio Ermanno, Sanders Peter, Walzer Stefan
conference: "Arxiv"
year: 2024
bibkey: hermann2024phobic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2404.18497"}
tags: ['ARXIV', 'Independent']
---
A minimal perfect hash function (MPHF) maps a set of n keys to &amp;\#123;1, ..., n&amp;\#125; without collisions. Such functions find widespread application e.g. in bioinformatics and databases. In this paper we revisit PTHash - a construction technique particularly designed for fast queries. PTHash distributes the input keys into small buckets and, for each bucket, it searches for a hash function seed that places its keys in the output domain without collisions. The collection of all seeds is then stored in a compressed way. Since the first buckets are easier to place, buckets are considered in non-increasing order of size. Additionally, PTHash heuristically produces an imbalanced distribution of bucket sizes by distributing 60&#37; of the keys into 30&#37; of the buckets. Our main contribution is to characterize, up to lower order terms, an optimal distribution of expected bucket sizes. We arrive at a simple, closed form solution which improves construction throughput for space efficient configurations in practice. Our second contribution is a novel encoding scheme for the seeds. We split the keys into partitions. Within each partition, we run the bucket distribution and search step. We then store the seeds in an interleaved way by consecutively placing the seeds for the i-th buckets from all partitions. The seeds for the i-th bucket of each partition follow the same statistical distribution. This allows us to tune a compressor for each bucket. Hence, we call our technique PHOBIC - Perfect Hashing with Optimized Bucket sizes and Interleaved Coding. Compared to PTHash, PHOBIC is 0.17 bits/key more space efficient for same query time and construction throughput. We also contribute a GPU implementation to further accelerate MPHF construction. For a configuration with fast queries, PHOBIC-GPU can construct a perfect hash function at 2.17 bits/key in 28 ns per key, which can be queried in 37 ns on the CPU.
