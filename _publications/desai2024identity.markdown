---
layout: publication
title: IDentity with Locality: An ideal hash for gene sequence search
authors: Desai Aditya, Gupta Gaurav, Zhang Tianyi, Shrivastava Anshumali
conference: Arxiv
year: 2024
bibkey: desai2024identity
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2406.14901"}
tags: ['Arxiv', 'LSH']
---
Gene sequence search is a fundamental operation in computational genomics. Due to the petabyte scale of genome archives, most gene search systems now use hashing-based data structures such as Bloom Filters (BF). The state-of-the-art systems such as Compact bit-slicing signature index (COBS) and Repeated And Merged Bloom filters (RAMBO) use BF with Random Hash (RH) functions for gene representation and identification. The standard recipe is to cast the gene search problem as a sequence of membership problems testing if each subsequent gene substring (called kmer) of Q is present in the set of kmers of the entire gene database D. We observe that RH functions, which are crucial to the memory and the computational advantage of BF, are also detrimental to the system performance of gene-search systems. While subsequent kmers being queried are likely very similar, RH, oblivious to any similarity, uniformly distributes the kmers to different parts of potentially large BF, thus triggering excessive cache misses and causing system slowdown. We propose a novel hash function called the Identity with Locality (IDL) hash family, which co-locates the keys close in input space without causing collisions. This approach ensures both cache locality and key preservation. IDL functions can be a drop-in replacement for RH functions and help improve the performance of information retrieval systems. We give a simple but practical construction of IDL function families and show that replacing the RH with IDL functions reduces cache misses by a factor of 5x, thus improving query and indexing times of SOTA methods such as COBS and RAMBO by factors up to 2x without compromising their quality. We also provide a theoretical analysis of the false positive rate of BF with IDL functions. Our hash function is the first study that bridges Locality Sensitive Hash (LSH) and RH to obtain cache efficiency.
