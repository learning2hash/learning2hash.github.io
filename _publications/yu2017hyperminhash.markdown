---
layout: publication
title: 'Hyperminhash: Minhash In Loglog Space'
authors: Yu Yun William, Weber Griffin M.
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: yu2017hyperminhash
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.08436'}]
tags: ["Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Scalability"]
short_authors: Yu Yun William, Weber Griffin M.
---
In this extended abstract, we describe and analyze a lossy compression of
MinHash from buckets of size \\(O(log n)\\) to buckets of size \\(O(loglog n)\\) by
encoding using floating-point notation. This new compressed sketch, which we
call HyperMinHash, as we build off a HyperLogLog scaffold, can be used as a
drop-in replacement of MinHash. Unlike comparable Jaccard index fingerprinting
algorithms in sub-logarithmic space (such as b-bit MinHash), HyperMinHash
retains MinHash's features of streaming updates, unions, and cardinality
estimation. For a multiplicative approximation error \\(1+ \epsilon\\) on a Jaccard
index \\( t \\), given a random oracle, HyperMinHash needs \\(O\left(\epsilon^\{-2\}
\left( loglog n + log \frac\{1\}\{ t \epsilon\} \right)\right)\\) space.
HyperMinHash allows estimating Jaccard indices of 0.01 for set cardinalities on
the order of \\(10^\{19\}\\) with relative error of around 10% using 64KiB of
memory; MinHash can only estimate Jaccard indices for cardinalities of
\\(10^\{10\}\\) with the same memory consumption.