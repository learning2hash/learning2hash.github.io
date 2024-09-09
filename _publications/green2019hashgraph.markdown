---
layout: publication
title: "HashGraph -- Scalable Hash Tables Using A Sparse Graph Data Structure"
authors: Green Oded
conference: Arxiv
year: 2019
bibkey: green2019hashgraph
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1907.02900"}
tags: ['ARXIV', 'Graph']
---
Hash tables are ubiquitous and used in a wide range of applications for efficient probing of large and unsorted data. If designed properly, hash-tables can enable efficients look ups in a constant number of operations or commonly referred to as O(1) operations. As data sizes continue to grow and data becomes less structured (as is common for big-data applications), the need for efficient and scalable hash table also grows. In this paper we introduce HashGraph, a new scalable approach for building hash tables that uses concepts taken from sparse graph representations--hence the name HashGraph. We show two different variants of HashGraph, a simple algorithm that outlines the method to create the hash-table and an advanced method that creates the hash table in a more efficient manner (with an improved memory access pattern). HashGraph shows a new way to deal with hash-collisions that does not use "open-addressing" or "chaining", yet has all the benefits of both these approaches. HashGraph currently works for static inputs, though recent progress with dynamic graph data structures suggest that HashGraph might be extended to dynamic inputs as well. We show that HashGraph can deal with a large number of hash-values per entry without loss of performance as most open-addressing and chaining approaches have. Further, we show that HashGraph is indifferent to the load-factor. Lastly, we show a new probing algorithm for the second phase of value lookups. Given the above, HashGraph is extremely fast and outperforms several state of the art hash-table implementations. The implementation of HashGraph in this paper is for NVIDIA GPUs, though HashGraph is not architecture dependent. Using a NVIDIA GV100 GPU, HashGraph is anywhere from 2X-8X faster than cuDPP, WarpDrive, and cuDF. HashGraph is able to build a hash-table at a rate of 2.5 billion keys per second and can probe at nearly the same rate.