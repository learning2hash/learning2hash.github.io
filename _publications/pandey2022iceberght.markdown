---
layout: publication
title: 'Iceberght: High Performance PMEM Hash Tables Through Stability And Low Associativity'
authors: "Prashant Pandey, Michael A. Bender, Alex Conway, Mart\xEDn Farach-Colton,\
  \ William Kuszmaul, Guido Tagliavini, Rob Johnson"
conference: Arxiv
year: 2022
bibkey: pandey2022iceberght
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.04068'}]
tags: ["Hashing Methods"]
short_authors: Pandey et al.
---
Modern hash table designs strive to minimize space while maximizing speed.
The most important factor in speed is the number of cache lines accessed during
updates and queries. This is especially important on PMEM, which is slower than
DRAM and in which writes are more expensive than reads.
  This paper proposes two stronger design objectives: stability and
low-associativity. A stable hash table doesn't move items around, and a hash
table has low associativity if there are only a few locations where an item can
be stored. Low associativity ensures that queries need to examine only a few
memory locations, and stability ensures that insertions write to very few cache
lines. Stability also simplifies scaling and crash safety.
  We present IcebergHT, a fast, crash-safe, concurrent, and space-efficient
hash table for PMEM based on the design principles of stability and low
associativity. IcebergHT combines in-memory metadata with a new hashing
technique, iceberg hashing, that is (1) space efficient, (2) stable, and (3)
supports low associativity. In contrast, existing hash-tables either modify
numerous cache lines during insertions (e.g. cuckoo hashing), access numerous
cache lines during queries (e.g. linear probing), or waste space (e.g.
chaining). Moreover, the combination of (1)-(3) yields several emergent
benefits: IcebergHT scales better than other hash tables, supports
crash-safety, and has excellent performance on PMEM (where writes are
particularly expensive).