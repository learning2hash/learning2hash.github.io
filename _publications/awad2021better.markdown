---
layout: publication
title: Better GPU Hash Tables
authors: Awad Muhammad A., Ashkiani Saman, Porumbescu Serban D., Farach-colton Martín, Owens John D.
conference: "Arxiv"
year: 2021
bibkey: awad2021better
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2108.07232"}
tags: ['ARXIV', 'Independent']
---
We revisit the problem of building static hash tables on the GPU and design and build three bucketed hash tables that use different probing schemes. Our implementations are lock-free and offer efficient memory access patterns; thus only the probing scheme is the factor affecting the performance of the hash tables different operations. Our results show that a bucketed cuckoo hash table that uses three hash functions (BCHT) outperforms alternative methods that use power-of-two choices iceberg hashing and a cuckoo hash table that uses a bucket size one. At high load factors as high as 0.99 BCHT enjoys an average probe count of 1.43 during insertion. Using three hash functions only positive and negative queries require at most 1.39 and 2.8 average probes per key respectively.
